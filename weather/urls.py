from django.urls import path

from .views import WeatherList,DataAnalysisList

urlpatterns = [
     path("api/", WeatherList.as_view()),
     path("api/stats", DataAnalysisList.as_view()),
]
