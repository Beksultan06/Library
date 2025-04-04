from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'full_name', 'gender', 'birth_date', 'category', 'email', 'phone')


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('full_name', 'gender', 'birth_date', 'category', 'email','image', 'phone', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': 'Пароли не совпадают.'})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create(
            full_name=validated_data['full_name'],
            gender=validated_data['gender'],
            birth_date=validated_data['birth_date'],
            category=validated_data['category'],
            email=validated_data['email'],
            phone=validated_data['phone'],
            image=validated_data['image'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class ReatingsSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'full_name', 'reitforusers', 'image')