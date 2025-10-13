from rest_framework.test import APIClient
from django.urls import reverse
from datetime import datetime
from accounts.models import User
from .models import *
import pytest

# Create your tests here.
@pytest.fixture
def api_client():
    client = APIClient()
    return client

@pytest.fixture
def common_user():
    user = User.objects.create_user(email='test@gmail.com',password='12345/@a',role='teacher')
    return user

@pytest.fixture
def category():
    return Category.objects.create(name="fun")

@pytest.mark.django_db
class TestCoursesApi:
    
    def test_get_courses_list_response_200(self,api_client):
        url = reverse("courses:api-v1:course-list")
        response = api_client.get(url)
        assert response.status_code == 200



    def test_create_course_response_201(self,api_client,common_user,category):
        url = reverse("courses:api-v1:course-list")
        data = {
            "title":"music",
            "body":"this is music",
            "category":[category.id],
            "published_at" :datetime.now()
        }
        api_client.force_authenticate(user=common_user)
        response = api_client.post(url,data,format="json")
        print(response.data)
        assert response.status_code == 201




    