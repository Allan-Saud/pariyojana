from rest_framework.permissions import BasePermission

class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj == request.user
# permissions.py
# from rest_framework.permissions import BasePermission

# class IsAdminOrSuperUser(BasePermission):
#     """
#     Allows access only to admin users (is_staff=True) or superusers (is_superuser=True)
#     """
#     def has_permission(self, request, view):
#         return request.user.is_authenticated and (request.user.is_staff or request.user.is_superuser)

#     def has_object_permission(self, request, view, obj):
#         return self.has_permission(request, view)