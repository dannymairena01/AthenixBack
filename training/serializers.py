from rest_framework import serializers
from .models import Training

class AthleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = '__all__'  # Incluye todos los campos del modelo