from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

from user_app.api import serializers

from user_app import models

class UserRegisterView(generics.CreateAPIView):
    serializer_class = serializers.CustomUserSerializer

class UserLoginView(generics.GenericAPIView):
    serializer_class = serializers.UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        user = authenticate(request, username=email, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)

class UserLogoutView(generics.GenericAPIView):
    serializer_class = serializers.UserSerializer
    def post(self, request):
        try:
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "User successfully logged out."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)

class UserDetailView(generics.RetrieveUpdateAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    
    def get_view_name(self):
        return "Account Info"