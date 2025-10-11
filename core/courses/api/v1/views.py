from rest_framework import viewsets
from .permissions import *
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    IsAuthenticated,
)
from courses.models import *
from .serializers import *


class CoursesViewSetList(viewsets.ModelViewSet):

    queryset = Course.objects.all()  # Define the queryset
    serializer_class = CoursesSerializer  # Specify the serializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsTeacherOrAdmin,
        IsOwnerOrAdmin,
    ]

    def get_queryset(self):
        # همه‌ی دوره‌هایی که زمان انتشارشان رسیده
        ready_to_publish = Course.objects.filter(
            published_at__lte=timezone.now(), status=0
        )

        # وضعیت آن‌ها را به 1 تغییر بده
        ready_to_publish.update(status=1)

        # در نهایت فقط دوره‌های منتشرشده را برگردان
        return Course.objects.filter(status=1)


class CommentViewSetList(viewsets.ModelViewSet):
    queryset = Comment.objects.all()  # Define the queryset
    serializer_class = CommentSerializer  # Specify the serializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class EnrollmentViewSet(viewsets.ModelViewSet):
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated, IsStudentOrAdmin]

    def get_queryset(self):
        # فقط ثبت‌نام‌های خود دانشجو نمایش داده میشه
        return Enrollment.objects.filter(student=self.request.user)


class CategoryViewSetList(viewsets.ModelViewSet):

    queryset = Category.objects.all()  # Define the queryset
    serializer_class = CategorySerializer  # Specify the serializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class RateViewSetList(viewsets.ModelViewSet):

    queryset = Rate.objects.all()  # Define the queryset
    serializer_class = RateSerializer  # Specify the serializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class LessonViewSetList(viewsets.ModelViewSet):

    queryset = Lesson.objects.all()  # Define the queryset
    serializer_class = LessonSerializer  # Specify the serializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsTeacherOrAdmin,
    ]

    def get_queryset(self):
        # همه‌ی دوره‌هایی که زمان انتشارشان رسیده
        ready_to_publish = Lesson.objects.filter(
            published_at__lte=timezone.now(), status=0
        )

        # وضعیت آن‌ها را به 1 تغییر بده
        ready_to_publish.update(status=1)

        # در نهایت فقط دوره‌های منتشرشده را برگردان
        return Lesson.objects.filter(status=1)
