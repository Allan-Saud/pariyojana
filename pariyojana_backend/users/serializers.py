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
        password = validated_data.get('password')
        if not password:
            password = self.generate_random_password()
        validated_data['password'] = password

        user = User.objects.create_user(**validated_data)

        # Send password via email
        send_password_email(user.email, password)

        return user

    def generate_random_password(self, length=10):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choices(characters, k=length))


