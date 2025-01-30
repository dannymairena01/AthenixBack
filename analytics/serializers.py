from rest_framework import serializers
from .models import Analytics

class AthleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analytics
        fields = '__all__'  # Incluye todos los campos del modelo