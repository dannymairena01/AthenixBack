from rest_framework import serializers
from .models import Athlete

class AthleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Athlete
        fields = '__all__'  # Incluye todos los campos del modelo