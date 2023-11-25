from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('demographics/', views.demographics, name='demographics'),
    path('questions/', views.questions, name='questions'),
    path('submitDemographics', views.submitDemographics, name='submitDemographics')
]
