from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrSuperUserOrIsSelf(BasePermission):
    """
    Permissions:
    - Users with is_superuser=True or role="admin" can do anything.
    - Normal users can view all, but only edit their own data.
    """

    def has_permission(self, request, view):
        if view.action == 'create':
            # Only superuser or role=admin can create
            return request.user.is_authenticated and (
                request.user.is_superuser or 
                getattr(request.user, 'role', '').lower() == 'admin'
            )

        # For list/retrieve/update/delete actions, allow if authenticated;
        # fine-grained per-object check done in has_object_permission
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if not request.user or not request.user.is_authenticated:
            return False

        # Admins and superusers can do anything
        if request.user.is_superuser or getattr(request.user, 'role', '').lower() == 'admin':
            return True

        if request.method in SAFE_METHODS:
            # Anyone authenticated can read any user
            return True

        # Only allow unsafe methods (PUT, PATCH, DELETE) if it's the same user
        return obj == request.user


    


class IsAdminOrReadOnly(BasePermission):
    """
    Allow read-only access to any authenticated user,
    but only allow write access to users with role 'admin' or superuser.
    """

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False

        # Read-only methods (GET, HEAD, OPTIONS) are allowed to all authenticated users
        if request.method in SAFE_METHODS:
            return True

        # For write requests, allow only if superuser or role is 'admin'
        return request.user.is_superuser or getattr(request.user, 'role', '').lower() == 'admin'
