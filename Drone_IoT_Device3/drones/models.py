from django.db import models
from django.contrib.auth.models import User
import datetime

class DroneCategory(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
    
class Drone(models.Model):
    drone_category = models.ForeignKey(
        DroneCategory, 
        on_delete=models.CASCADE, 
        related_name= 'drone_cat')
    name = models.CharField(max_length=50)
    manfacturing_date = models.DateField(default=datetime.datetime.now())
    participated_in_race_s = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
    
class Pilot(models.Model):
    class Gender(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'

    # user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    
    name = models.CharField(max_length=100)
    gender = models.CharField(
        max_length=1,
        choices=Gender.choices,
        default= Gender.MALE,
    )
    num_of_races = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

class Competition(models.Model):
    pilot = models.ForeignKey(
        Pilot,
        on_delete=models.CASCADE,
        related_name='competitions')
    drone = models.ForeignKey(
        Drone,
        on_delete=models.CASCADE,
        related_name='competitions'
    )
    distance_in_feet = models.FloatField(default=0)
    date_of_competition = models.DateField()

    def __str__(self) -> str:
        return f"{self.pilot} - {self.drone} - {self.distance_in_feet}"
