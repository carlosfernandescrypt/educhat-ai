# backend/accounts/views.py

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer, RegisterSerializer, LoginSerializer
from .models import UserProfile

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        # Autenticar e fazer login do usuário após registro
        auth_user = authenticate(
            username=request.data['username'],
            password=request.data['password']
        )
        if auth_user:
            login(request, auth_user)
        
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "Usuário cadastrado com sucesso!"
        }, status=status.HTTP_201_CREATED)

class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = authenticate(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )
        
        if user is not None:
            login(request, user)
            return Response({
                "user": UserSerializer(user).data,
                "message": "Login realizado com sucesso"
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                "error": "Credenciais inválidas"
            }, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({
            "message": "Logout realizado com sucesso"
        }, status=status.HTTP_200_OK)

class UserProfileView(APIView):
    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request):
        profile = request.user.profile
        profile_data = request.data.get('profile', {})
        
        # Atualizar campos do perfil
        if 'nivel_educacao' in profile_data:
            profile.nivel_educacao = profile_data['nivel_educacao']
        if 'area_interesse' in profile_data:
            profile.area_interesse = profile_data['area_interesse']
            
        profile.save()
        
        serializer = UserSerializer(request.user)
        return Response(serializer.data)