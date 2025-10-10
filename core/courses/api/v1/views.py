from rest_framework import generics,viewsets
from .permissions import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated,AllowAny
from ...models import *
from .serializers import *


class CoursesViewSetList(viewsets.ModelViewSet):

    queryset = Course.objects.all()  # Define the queryset
    serializer_class = CoursesSerializer  # Specify the serializer
    permission_classes = [IsAuthenticated , IsTeacherOrAdmin, IsOwnerOrAdmin]

class CommentViewSetList(viewsets.ModelViewSet):
    queryset = Comment.objects.all()  # Define the queryset
    serializer_class = CommentSerializer  # Specify the serializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class EnrollmentViewSet(viewsets.ModelViewSet):
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated, IsStudent]

    def get_queryset(self):
        # فقط ثبت‌نام‌های خود دانشجو نمایش داده میشه
        return Enrollment.objects.filter(student=self.request.user)
    
class CategoryViewSetList(viewsets.ModelViewSet):

    queryset = Category.objects.all()  # Define the queryset
    serializer_class = CategorySerializer  # Specify the serializer
    permissions_classes = [IsAuthenticatedOrReadOnly]