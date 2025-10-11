from rest_framework import permissions


class IsTeacherOrAdmin(permissions.BasePermission):
    
    def has_permission(self, request, view):
        # اگر فقط بخواد دیتا ببینه (GET)، مجازه
        if request.method in permissions.SAFE_METHODS:
            return True

        # اگر بخواد ایجاد یا ویرایش کنه، باید نقش خاص داشته باشه
        user = request.user
        return user.is_authenticated and (user.role in ['teacher', 'admin'])
    
class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # دیدن همه مجازه
        if request.method in permissions.SAFE_METHODS:
            return True
        # فقط سازنده یا ادمین
        return obj.teacher == request.user or request.user.role == 'admin'
    
class IsStudentOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role != 'teacher'