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
        is_admin_role = getattr(user, 'role', '').lower() == 'admin'
        
        if user.is_superuser or is_admin_role:
            # Superuser or role=admin gets full access
            return User.objects.filter(is_deleted=False)

        # Other users can only see themselves
        return User.objects.filter(id=user.id, is_deleted=False)

