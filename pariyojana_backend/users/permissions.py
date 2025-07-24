from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrSuperUserOrIsSelf(BasePermission):
    """
    Permissions:
    - Admin/superuser can do anything (add/edit/change password for any user).
    - Regular users can only edit/read themselves.
    """

    def has_permission(self, request, view):
        if view.action == 'create':
            # Only admin/superuser can create users
            return request.user.is_authenticated and (request.user.is_staff or request.user.is_superuser)
        # For list/retrieve/update/delete actions, allow if authenticated;
        # detailed per-object permission checked in has_object_permission
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if not request.user or not request.user.is_authenticated:
            return False
        if request.user.is_staff or request.user.is_superuser:
            # Admin or superuser can do anything on any object
            return True
        if request.method in SAFE_METHODS:
            # Normal users can view only their own user object
            return obj == request.user
        # For unsafe methods (PUT, PATCH, DELETE), only allow users to modify their own object
        return obj == request.user

    
    
class IsAdminOrReadOnly(BasePermission):
    """
    Allow read-only access to any authenticated user,
    but only allow write access to admin or superuser.
    """

    def has_permission(self, request, view):
        # Allow read-only access to any authenticated user
        if request.method in SAFE_METHODS:
            return request.user.is_authenticated
        
        # For write requests (POST, PUT, PATCH, DELETE), allow only admin or superuser
        return request.user.is_authenticated and (request.user.is_staff or request.user.is_superuser)
