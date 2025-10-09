from rest_framework import routers
from .views import *

app_name = 'api-v1'

router = routers.DefaultRouter()
router.register('list-course', CoursesViewSetList)
urlpatterns = router.urls