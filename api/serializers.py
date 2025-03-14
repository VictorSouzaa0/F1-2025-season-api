from rest_framework import serializers
from .models import Driver,Legend

class DriverSerliaziers(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = [
                'name', 
                'birth_date',
                'team', 
                'country'       
                ]

class LegendsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Legend
        fields = [   
                'name',
                'birth_date',
                'country',
                'championships',
                'teams'
                ]