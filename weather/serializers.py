from rest_framework import serializers
from django import forms
from .models import Weather, DataAnalysis


class WeatherDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Weather
        fields = ["id","station_id","date","max_temp","min_temp","precipitation"]


class DataAnalysisSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DataAnalysis
        fields = ["id","station_id","year","max_temp_avg","min_temp_avg","total_precipitation"]