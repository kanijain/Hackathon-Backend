  
from .views import profile,MedicalFormAPI,Dailydiet
from django.urls import path
urlpatterns = [
    path('profile/',profile.as_view(),name="profile"),
    path('Medicalform/',MedicalFormAPI.as_view(),name="daily food intake"),
    path('Dailydiet/',Dailydiet.as_view(),name="daily food")


]