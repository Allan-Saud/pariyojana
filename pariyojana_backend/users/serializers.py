from rest_framework import serializers
from .models import User
import random
import string
from .utils import send_password_email

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True, 'required': False},
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = User(**validated_data)

        if password:
            user.set_password(password)
        else:
            password = self.generate_random_password()
            user.set_password(password)
            send_password_email(user.email, password)

        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password:
            instance.set_password(password)

        instance.save()
        return instance

    def generate_random_password(self, length=10):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choices(characters, k=length))



