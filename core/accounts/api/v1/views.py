# accounts/views.py
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import IsAdminOrTeacher
from courses.models import Enrollment
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from django.contrib.auth import authenticate
from accounts.models import *


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }


class UserViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminOrTeacher]

    def get_queryset(self):
        user = self.request.user

        # ادمین‌ها همه کاربران رو می‌بینن
        if user.role == "admin" or user.is_superuser:
            return User.objects.all()

        # معلم فقط دانشجوهای ثبت‌نام‌شده در دوره‌هاش رو می‌بینه
        if user.role == "teacher":
            # دوره‌هایی که معلم تدریس می‌کنه
            teacher_courses = user.courses.all()
            # دانشجوهای ثبت‌نام‌شده در اون دوره‌ها
            enrolled_students = User.objects.filter(
                enrollments__course__in=teacher_courses, role="student"
            ).distinct()
            return enrolled_students

        # بقیه کاربران (مثلاً دانشجوها) چیزی نمی‌بینن
        return User.objects.none()


class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        tokens = get_tokens_for_user(user)
        return Response(
            {"user": UserSerializer(user).data, "tokens": tokens},
            status=status.HTTP_201_CREATED,
        )


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(request, username=email, password=password)

        if user is None:
            return Response(
                {"error": "Invalid credentials"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        if not user.is_active:
            return Response(
                {"error": "Invalid credentials"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        refresh = RefreshToken.for_user(user)
        return Response(
            {
                "user": {
                    "id": user.id,
                    "email": user.email,
                },
                "tokens": {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                },
            }
        )
