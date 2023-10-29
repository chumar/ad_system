from rest_framework import serializers
from .models import  Ad,Location,CreateUser

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class AdSerializer(serializers.ModelSerializer):
    locations = serializers.ListField(child=serializers.CharField(), write_only=True)

    class Meta:
        model = Ad
        fields = '__all__'

class UserCreationSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username')
    location_name = serializers.CharField(source='location.name')

    class Meta:
        model = CreateUser
        fields = ['id', 'user_name', 'location_name']