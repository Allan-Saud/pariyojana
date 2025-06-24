from rest_framework.permissions import BasePermission

class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow if user is staff (admin) OR the object belongs to the user
        return request.user.is_staff or obj == request.user
