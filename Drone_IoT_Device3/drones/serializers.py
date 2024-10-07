from rest_framework import serializers

from django.contrib.auth.models import User

from .models import (
    Drone,
    DroneCategory,
    Pilot,
    Competition,
)

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        
        
    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password']) 
        user.save()
        return user

class CompetitionSerializer(serializers.ModelSerializer):

    drone = serializers.StringRelatedField()
    pilot = serializers.StringRelatedField()
    class Meta:
        model = Competition
        fields = ['id', 'pilot', 'drone','distance_in_feet', 'date_of_competition']
        read_only_fields = ['id']

class PilotSerializer(serializers.ModelSerializer):
    
    competitions = CompetitionSerializer(many = True, read_only = True) # nested serializer with related name

    class Meta:
        model = Pilot
        fields = ['id', 'user', 'name', 'gender', 'num_of_races', 'competitions', 'timestamp']
        read_only_fields = ['id']

class DroneSerializer(serializers.ModelSerializer):

    competitions = CompetitionSerializer(many = True, read_only = True) # nested serializer with related name
    class Meta:
        model = Drone
        fields = ['id', 'name', 'manfacturing_date', 'competitions', 'participated_in_race_s', 'timestamp']
        read_only_fields = ['id']

class DroneCategorySerializer(serializers.ModelSerializer):

    drone_cat = DroneSerializer(many = True, read_only = True) # nested serializer with related name

    class Meta:
        model = DroneCategory
        fields = ['id', 'name', 'drone_cat',]
        read_only_fields = ['id']