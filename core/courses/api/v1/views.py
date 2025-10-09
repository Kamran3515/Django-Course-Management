from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAuthenticatedOrReadOnly
from ...models import *
from .serializers import *


class CoursesViewSetList(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Course.objects.all()  # Define the queryset
    serializer_class = CoursesSerializer  # Specify the serializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        if request.user == IsAuthenticated:
            return super().create(request, *args, **kwargs)
