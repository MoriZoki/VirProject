from rest_framework.permissions import BasePermission, SAFE_METHODS

# create ur permissions here

class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)
