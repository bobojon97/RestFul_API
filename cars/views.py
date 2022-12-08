from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from cars.serializers import CarDetailSerializer, CarListSerializer
from cars.models import Car
from cars.permissions import IsOwnerOrReadOnly

class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializer

class CarListView(generics.ListAPIView):
    serializer_class = CarDetailSerializer
    queryset = Car.objects.all()
    permission_classes = [IsAdminUser]

class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarDetailSerializer
    queryset = Car.objects.all()
    permission_classes = [IsOwnerOrReadOnly]