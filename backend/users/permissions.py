from rest_framework import permissions

class IsLibrarian(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_librarian

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)