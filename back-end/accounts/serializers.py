# backend/accounts/serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('nivel_educacao', 'area_interesse')

class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(required=False)
    
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'profile')
        read_only_fields = ('id',)

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    nivel_educacao = serializers.CharField(required=False, allow_blank=True)
    area_interesse = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2', 'nivel_educacao', 'area_interesse')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "As senhas não conferem"})
        
        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError({"email": "Este email já está sendo usado"})
            
        return attrs

    def create(self, validated_data):
        nivel_educacao = validated_data.pop('nivel_educacao', '')
        area_interesse = validated_data.pop('area_interesse', '')
        validated_data.pop('password2', None)
        
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        
        user.set_password(validated_data['password'])
        user.save()
        
        UserProfile.objects.create(
            user=user,
            nivel_educacao=nivel_educacao,
            area_interesse=area_interesse
        )
        
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)