from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models import User
from users.serializers import UserSerializer
from users.utils import send_password_email
import string, random
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.permissions import AllowAny


# Custom JWT Serializer
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data.update({
            'user_id': self.user.id,
            'full_name': self.user.full_name,
            'email': self.user.email,
            'role': self.user.role,
            'ward_no': self.user.ward_no
        })
        return data

# Custom JWT View
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

# Forgot Password View
class ForgotPasswordView(APIView):
    permission_classes = [AllowAny] 
    def post(self, request):
        email = request.data.get('email')
        if not email:
            return Response({'detail': 'Email is required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'detail': 'User with this email does not exist.'}, status=status.HTTP_404_NOT_FOUND)

        # Generate new password
        new_password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        user.set_password(new_password)
        user.save()

        # Send password to email
        send_password_email(email, new_password)

        return Response({'detail': 'A new password has been sent to your email.'}, status=status.HTTP_200_OK)

