from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LocationViewSet,AdViewSet,UserCreationViewSet,ViewAdByName
router = DefaultRouter()
router.register(r'locations', LocationViewSet)
router.register(r'ads', AdViewSet)
router.register(r'user-locations', UserCreationViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('view-ad-by-name/', ViewAdByName.as_view(), name='view-ad-by-name'),
]
