from rest_framework import viewsets, permissions
# from .permissions import IsAdminOrSuperUser
from .models import User
from .serializers import UserSerializer
from .permissions import IsAdminOrSuperUserOrIsSelf

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_deleted=False)
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrSuperUserOrIsSelf]

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.is_active = False
        instance.save()
        
        
    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.is_superuser:
            # Admin/superuser sees all users
            return User.objects.filter(is_deleted=False)
        # Normal users see only their own user record
        return User.objects.filter(id=user.id, is_deleted=False)
