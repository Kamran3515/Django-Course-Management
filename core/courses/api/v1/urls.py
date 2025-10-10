from rest_framework import routers
from .views import *

app_name = 'api-v1'

router = routers.DefaultRouter()
router.register('course', CoursesViewSetList, basename='course')
router.register('comment', CommentViewSetList, basename='comment')
router.register('enrollments', EnrollmentViewSet, basename='enrollment')
router.register('category', CategoryViewSetList, basename='category')
urlpatterns = router.urls