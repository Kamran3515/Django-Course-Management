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
def student_user():
    user = User.objects.create_user(
                        email='test2@gmail.com',
                        password='12345/@a',
                        role='student'
                    )
    return user

@pytest.fixture
def category():
    return Category.objects.create(name="fun")

@pytest.fixture
def sample_course(common_user,category):
    course = Course.objects.create(
        teacher=common_user,
        title="Music",
        body="This is a music course",
        published_at=timezone.now()
    )
    course.category.set([category.id])
    return course

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

    def test_create_lesson_response_201(self,api_client,common_user,sample_course):
        url = reverse("courses:api-v1:lesson-list")
        data = {
            "course":sample_course.id,
            "title":"music",
            "body":"this is music",
            "published_at" :datetime.now()
        }
        api_client.force_authenticate(user=common_user)
        response = api_client.post(url,data,format="json")
        print(response.data)
        assert response.status_code == 201

    def test_register_course_enrollment_response_201(self,student_user,sample_course,api_client):
        url = reverse("courses:api-v1:enrollment-list")
        data = {
            "course":sample_course.id
        }
        api_client.force_authenticate(user=student_user)
        response = api_client.post(url,data,format="json")
        print(response.data)
        assert response.status_code == 201

    def test_create_comment_response_201(self,student_user,sample_course,api_client):
        url = reverse("courses:api-v1:comment-list")
        data = {
            "course":sample_course.id,
            "comment":"this is very good coursess"
        }
        api_client.force_authenticate(user=student_user)
        response = api_client.post(url,data,format="json")
        print(response.data)
        assert response.status_code == 201

    def test_create_rate_response_201(self,student_user,sample_course,api_client):
        url = reverse("courses:api-v1:rate-list")
        data = {
            "course":sample_course.id,
            "score":7
        }
        api_client.force_authenticate(user=student_user)
        response = api_client.post(url,data,format="json")
        print(response.data)
        assert response.status_code == 201

    