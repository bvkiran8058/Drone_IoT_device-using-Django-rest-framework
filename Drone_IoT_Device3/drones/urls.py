from django.urls import path
from .views import *

urlpatterns = [

    # path('register/', UserRegisterView.as_view(), name='user-register'),  
    #

     

    path('drone-categories/', DroneCategoryList.as_view(), name = 'categories-list' ),
    path('drone-categories/<int:pk>',DroneCategoryDetail.as_view(), name = 'category-detail'),

    path('drones/', DronesList.as_view(), name = 'drones-list'),
    path('drones/<int:pk>', DroneDetail.as_view(), name = 'drone-detail'),

    path('pilots/', PilotsList.as_view(), name = 'pilots-list'),
    path('pilots/<int:pk>', PilotDetail.as_view(), name = 'pilot-detail'),

    path('competitions/', CompetitionsList.as_view(), name = 'competitions-list'),
    path('competitions/<int:pk>', CompetitionDetail.as_view(), name = 'competition-detail'),
]