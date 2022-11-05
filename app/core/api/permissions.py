from rest_framework import permissions


SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')


class IsAdminUserOrReadOnly(permissions.IsAdminUser):

    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)
        return request.method in SAFE_METHODS or is_admin  # if user is not SAFE_METHODS, look if user is_admin


class IsCommenterOrReadOnly():
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.user == obj.user:
            return True
        else:
            False
