from rest_framework import permissions

class IsAdminOrTeacher(permissions.BasePermission):
    """
    فقط ادمین یا معلم می‌تونن لیست کاربران رو ببینن.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            request.user.role in ['admin', 'teacher'] or request.user.is_superuser
        )
