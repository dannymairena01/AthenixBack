from django.db import models

# Create your models here.
from users.models import User

class Athlete(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='athlete_profile')
    date_of_birth = models.DateField()
    category = models.CharField(max_length=50)
    medical_history = models.TextField(blank=True, null=True)
    injuries = models.TextField(blank=True, null=True)
    medications = models.TextField(blank=True, null=True)
    allergies = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.category}"