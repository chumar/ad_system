from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import Location, Ad,CreateUser,UserVisit
from .serializers import LocationSerializer, AdSerializer,UserCreationSerializer
import datetime
from django.db.models import Sum

class LocationViewSet(viewsets.ModelViewSet):
    """ API endpoint that allows viewing and editing locations."""
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class AdViewSet(viewsets.ModelViewSet):
    """API endpoint that allows CRUD operations on ads """
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

    def create(self, request, *args, **kwargs):
        location_names = request.data.get("locations", [])
        location_ids = []

        # Fetch location IDs based on names
        for name in location_names:
            try:
                location = Location.objects.get(name=name)
                location_ids.append(location.id)
            except Location.DoesNotExist:
                return Response(
                    {"locations": f"Location with name '{name}' does not exist."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        data = request.data.copy()
        data["locations"] = location_ids

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserCreationViewSet(viewsets.ModelViewSet):
    """API endpoint that allows viewing and editing user creations. """
    queryset = CreateUser.objects.all()
    serializer_class = UserCreationSerializer


class ViewAdByName(APIView):
    """ API endpoint for viewing an ad by name."""
    permission_classes = [IsAuthenticated]
    def get(self, request):
        ad_name = request.query_params.get('ad_name')

        if not ad_name:
            return Response({'error': 'Please provide an ad_name as a query parameter.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            ad = Ad.objects.get(ad_name=ad_name)

            today = datetime.date.today()
            user = request.user
            user_location = user.createuser.location if hasattr(user, 'createuser') else None

            # Check if the user's location is not in the ad's specified locations
            if user_location and user_location not in ad.locations.all():
                return Response({
                    'error': f'You are not allowed to see the ad "{ad_name}" in your location "{user_location.name}".'
                }, status=status.HTTP_400_BAD_REQUEST)

            # Check if the number of unique users for this location has exceeded the limit
            max_daily_visitors_location = user_location.max_daily_visitors if user_location else 0
            users_per_day_location = UserVisit.objects.filter(
                ad=ad, date=today, user=user
            ).count()

            if users_per_day_location > max_daily_visitors_location:
                return Response({
                    'error': f'Ad with ad_name "{ad_name}" is blocked for today in the region "{user_location.name}".'
                }, status=status.HTTP_403_FORBIDDEN)

            # Record the user's visit and update the view count
            user_visit, created = UserVisit.objects.get_or_create(user=user, ad=ad, date=today)
            if not created:
                user_visit.view_count += 1
                user_visit.save()

            total_user_visits = UserVisit.objects.filter(user=user, ad=ad).aggregate(Sum('view_count'))['view_count__sum']

            response_data = {
                'ad_name': ad_name,
                'user_location': user_location.name if user_location else None,
                'user_visit_count': total_user_visits,

            }

            return Response(response_data, status=status.HTTP_200_OK)
        except Ad.DoesNotExist:
            all_ads = Ad.objects.values_list('ad_name', flat=True)
            return Response({'error': f'This "{ad_name}" does not exist. Please select the relevant ads',
                             'available_ads': list(all_ads)}, status=status.HTTP_404_NOT_FOUND)

