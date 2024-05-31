from rest_framework import serializers

from user_app import models

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ('email', 'first_name', 'last_name', 'affiliation', 'country', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def validate_email(self, value):
        if models.CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email address is already in use.")
        return value

    def create(self, validated_data):
        user = models.CustomUser.objects.create_user(**validated_data)
        return user

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

class UserSerializer(serializers.ModelSerializer):
    created_at = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = models.CustomUser
        exclude = ('password', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'groups', 'user_permissions')