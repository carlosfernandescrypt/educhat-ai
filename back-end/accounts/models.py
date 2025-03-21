# backend/accounts/models.py

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    EDUCATION_CHOICES = (
        ('fundamental', 'Ensino Fundamental'),
        ('medio', 'Ensino Médio'),
        ('superior', 'Ensino Superior'),
        ('pos', 'Pós-graduação'),
    )
    
    INTEREST_CHOICES = (
        ('exatas', 'Ciências Exatas'),
        ('humanas', 'Ciências Humanas'),
        ('biologicas', 'Ciências Biológicas'),
        ('tecnologia', 'Tecnologia'),
        ('linguagens', 'Linguagens'),
        ('outros', 'Outros'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    nivel_educacao = models.CharField(max_length=20, choices=EDUCATION_CHOICES, blank=True, null=True)
    area_interesse = models.CharField(max_length=20, choices=INTEREST_CHOICES, blank=True, null=True)
    
    def __str__(self):
        return f"Perfil de {self.user.username}"