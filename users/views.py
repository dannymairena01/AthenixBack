from django.shortcuts import render
from rest_framework import generics
from .models import User  # Importa el modelo User desde users.models
from .serializers import UserSerializer

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer