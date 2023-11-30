from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('demographics/', views.demographics, name='demographics'),
    path('questions/', views.questions, name='questions'),
    path('submitDemographics/', views.submitDemographics, name='submitDemographics'),
    path('save-response/', views.save_response, name='save_response'),
    path('compile-postgresqlToCSV/', views.compile_postgresqlToCSV, name='compile_postgresqlToCSV')

]
