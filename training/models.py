from django.db import models

# Create your models here.
from athletes.models import Athlete

class TrainingSession(models.Model):
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, related_name='training_sessions')
    date = models.DateField()
    duration = models.DurationField()
    heart_rate_avg = models.FloatField()
    heart_rate_max = models.FloatField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.athlete.user.username} - {self.date}"

class PhysicalTest(models.Model):
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, related_name='physical_tests')
    test_type = models.CharField(max_length=100)
    date = models.DateField()
    result = models.JSONField()  # Para almacenar resultados flexibles

    def __str__(self):
        return f"{self.athlete.user.username} - {self.test_type}"