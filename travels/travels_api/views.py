from functools import partial
from tkinter.messagebox import NO
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from rest_framework import permissions
from .models import Passenger
from .serializers import PassengerSerializer

class PassengerListApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the passenger items
        '''
        passengers = Passenger.objects.all().values()
        serializer = PassengerSerializer(passengers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'identification': request.data.get('identification'),
            'name': request.data.get('name'),
        }
        serializer = PassengerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PassengerDetailApiView(APIView):

    def get_object(self, passenger_id):
        try:
            return Passenger.objects.get(id=passenger_id)
        except Passenger.DoesNotExist:
            return None
    
    def get(self, request, passenger_id, *args, **kwargs):
        passenger = self.get_object(passenger_id)
        if not passenger:
            return Response({'res': 'No se encontró el pasajero indicado'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = PassengerSerializer(passenger)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, passenger_id, *args, **kwargs):
        passenger = self.get_object(passenger_id)
        if not passenger:
            return Response({'res': 'No se encontró el pasajero indicado'}, status=status.HTTP_400_BAD_REQUEST)
        data = {
            'identification': request.data.get('identification'),
            'name': request.data.get('name'),
        }
        serializer = PassengerSerializer(instance=passenger, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, passenger_id, *args, **kwargs):
        passenger = self.get_object(passenger_id)
        if not passenger:
            return Response({'res': 'No se encontró el pasajero indicado'}, status=status.HTTP_400_BAD_REQUEST)
        passenger.delete()
        return Response({'res': 'Pasajero borrado exitosamente!'}, status=status.HTTP_200_OK)