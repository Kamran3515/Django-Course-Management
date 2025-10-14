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
    user = User.objects.create_user(email='test@gmail.com',password='12345/@a')
    return user

@pytest.mark.django_db
class TestAccountApi:

    def test_account_register_response_201(self,api_client):
        url = reverse("accounts:api-v1:register")
        data = {
            "email":"test@gmail.com",
            "password":"12345/@a",
            "password1":"12345/@a",
            "role":"student"
        }
        response = api_client.post(url,data,format="json")
        assert response.status_code == 201

    def test_account_login_response_200(self,api_client,common_user):
        url = reverse("accounts:api-v1:login")
        data = {
            "email":"test@gmail.com",
            "password":"12345/@a",
        }
        response = api_client.post(url,data,format="json")
        assert response.status_code == 200