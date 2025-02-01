from django.db import models

# Create your models here.
from athletes.models import Athlete

class AnalysisResult(models.Model):
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, related_name='analysis_results')
    date = models.DateField()
    risk_of_injury = models.FloatField()
    recommendations = models.TextField()

    def __str__(self):
        return f"{self.athlete.user.username} - {self.date}"