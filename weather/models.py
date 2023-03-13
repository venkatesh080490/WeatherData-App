from statistics import mode
from django.db import models
from bulk_update_or_create import BulkUpdateOrCreateQuerySet


# Create your models here.
class Weather(models.Model):
    station_id = models.CharField(max_length=30, help_text="Weather station identifier")
    date = models.DateField(help_text="Date measured")
    max_temp = models.FloatField(
        help_text="The maximum temperature for that day (in tenths of a degree Celsius)",
    )
    min_temp = models.FloatField(
        help_text="The minimum temperature for that day (in tenths of a degree Celsius)",
    )
    precipitation = models.FloatField(
        help_text="The amount of precipitation for that day (in tenths of a millimeter)",
    )
    created_timestamp = models.DateTimeField(auto_now_add=True, null=False)
    updated_timestamp = models.DateTimeField(auto_now=True, null=False)
    objects = BulkUpdateOrCreateQuerySet.as_manager()

    class Meta: 
        db_table = "Weather"
        ordering = ['station_id']
        constraints = [
            models.UniqueConstraint(fields=['station_id', 'date'], name='unique station data for particular day')
        ]
    


class DataAnalysis(models.Model):
    station_id = models.CharField(max_length=30, help_text="Weather station identifier")
    year = models.PositiveSmallIntegerField(
        help_text="statistics were calculated for this year"
    )
    max_temp_avg = models.FloatField(
        null=True,
        help_text="Average maximum temperature (in degrees Celsius)",
    )
    min_temp_avg = models.FloatField(
        null=True,
        help_text="Average minimum temperature (in degrees Celsius)",
    )
    total_precipitation = models.FloatField(
        null=True,
        help_text="Total accumulated precipitation (in centimeters",
    )

    created_timestamp = models.DateTimeField(auto_now_add=True, null=False)
    updated_timestamp = models.DateTimeField(auto_now=True, null=False)

    class Meta:
        ordering = ['station_id', 'year']
        constraints = [
            models.UniqueConstraint(fields=['station_id', 'year'], name='unique station data for particular year')
        ]


