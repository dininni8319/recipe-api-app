from django.test import TestCase 
from django.contrib.auth import get_user_model #we are importing the user model for the testing
from django.urls import reverse #this is for genereting the api url

from rest_framework.test import APIClient #rest framework api tools, APIClient  test client to make request to are api
from rest_framework import status # module that contains some status code, that we can see human redable form

CREATE_USER_URL = reverse('user:create') #this should create the create

#helper function 
# **dynamic list of arguments we can add many arguments
def create_user(**params):
    return get_user_model().objects.create_user(**params)

#public API
class PublicUserApiTests(TestCase):
    """Test the user API (public)"""

    def setUp(self):
        self.client = APIClient()

    def test_create_valid_user_success(self):
        """Test creating user with valid payload is successful"""

        #dectionary
        payload = {   
            'email': 'test@londonappdev.com',
            'password': 'testpass',
            'name': 'Test name'
        }
        #we are making our request
        res = self.client.post(CREATE_USER_URL, payload)
        #we are testing the status code
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        user = get_user_model().objects.get(**res.data) # we are testing that the object is created
        self.assertTrue(user.check_password(payload['password'])) #test are password is correct 
        #and finaly we don't the password returned in the request
        self.assertNotIn('password', res.data) 
    
    def test_user_exists(self):
        """Test creating  user that alrready exists fails"""
        payload = { 'email': 'test@londonappdev.com', 'password': 'testpass'}
        create_user(**payload)

        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self):
        """Test that the password must be more than 5 characters"""
        payload = { 'email': 'test@londonappdev.com', 'password': 'pw'}
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(
            email=payload['email']
        ).exists()

        self.assertFalse(user_exist)