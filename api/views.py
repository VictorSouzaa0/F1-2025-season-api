from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Legend,Driver
from .serializers import LegendsSerializers,DriverSerliaziers


@api_view(['GET'])

def get_drivers(request):

    if request.method == 'GET':
        drivers = Driver.objects.all()
        serializer = DriverSerliaziers(drivers, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])

def get_legends(request):

    if request.method == 'GET':
        legends = Legend.objects.all()
        serializer = LegendsSerializers(legends, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)