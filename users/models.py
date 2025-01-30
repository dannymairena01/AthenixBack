from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLES = (
        ('doctor', 'Médico del Deporte'),
        ('athlete', 'Atleta'),
        ('trainer', 'Entrenador'),
        ('nutritionist', 'Nutriólogo'),
    )
    role = models.CharField(max_length=20, choices=ROLES)
    institution = models.CharField(max_length=100, blank=True, null=True)