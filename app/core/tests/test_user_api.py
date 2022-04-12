from django.test import TestCase 
from django.contrib.auth import get_user_model #we are importing the user model for the testing
from django.urls import reverse #this is for genereting the api url

from rest_framework.test import APIClient #rest framework api tools, APIClient  test client to make request to are api
from rest_framework import status # module that contains some status code, that we can see human redable form

CREATE_USER_URL = reverse('user:create') #this should create the create
TOKEN_URL = reverse('user:token') #this is going to be the urls that we are going get our token

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
        payload = { 'email': 'test@londonappdev.com', 'password': 'testpass', 'name': 'Test'}
        create_user(**payload)

        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self):
        """Test that the password must be more than 5 characters"""
        payload = { 'email': 'test@londonappdev.com', 'password': 'pw', 'name': 'Test',}
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(
            email=payload['email']
        ).exists()

        self.assertFalse(user_exists)
    
    def test_create_token_for_user(self):
        """Test that a token is created for the user"""
        payload = { 'email': "test@londonappdev.com", 'password': 'testpass'} #payload to test the API
        create_user(**payload) #user helper function that we can match the authentication
        res = self.client.post(TOKEN_URL, payload) #the response should contain the token
        
        self.assertIn('token', res.data) #we are going to  trast that contains the token
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_token_invalid_credetianls(self):
        """Test that the token is not created if invalid credentials are given"""
        create_user(email='test@londondevapp.com', password='testpass')
        payload = { 'email': 'test@londondevapp.com', 'password': 'wrong'}
        res = self.client.post(TOKEN_URL, payload)
        
        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_no_user(self):
        """Test that token is not created if user doesn't exist"""
        payload = {'email': 'test@londondevapp.com', 'password': 'testpass'}
        res = self.client.post(TOKEN_URL, payload)

        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_missing_field(self):
        """Test that email and password are required"""
        res = self.client.post(TOKEN_URL, {'email': 'one', 'password': ''})
        self.assertNotIn('token', res.data) 
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)   