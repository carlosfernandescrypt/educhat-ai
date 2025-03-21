# accounts/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    nivel_educacao = forms.ChoiceField(
        choices=[
            ('', 'Selecione seu nível educacional'),
            ('fundamental', 'Ensino Fundamental'),
            ('medio', 'Ensino Médio'),
            ('superior', 'Ensino Superior'),
            ('pos', 'Pós-graduação'),
        ],
        required=False
    )
    area_interesse = forms.ChoiceField(
        choices=[
            ('', 'Selecione sua área de interesse'),
            ('exatas', 'Ciências Exatas'),
            ('humanas', 'Ciências Humanas'),
            ('biologicas', 'Ciências Biológicas'),
            ('tecnologia', 'Tecnologia'),
            ('linguagens', 'Linguagens'),
            ('outros', 'Outros'),
        ],
        required=False
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        
        if commit:
            user.save()
            user_profile = UserProfile.objects.create(
                user=user,
                nivel_educacao=self.cleaned_data.get('nivel_educacao', ''),
                area_interesse=self.cleaned_data.get('area_interesse', '')
            )
            
        return user