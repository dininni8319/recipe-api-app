from django.test import TestCase, Client
from django.contrib.auth import get_user_model #we are importing the user model
from django.urls import reverse  #helper function that allow us to generete urls 
# from django.test import Client  #will allow us to make test request to our application

class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@londonappdev.com',
            password='password123'
        )

        self.client.force_login(self.admin_user) #Uses the Client helper function that allows the user to login, make are life easyer to test the application, we dont have to login. 
        self.user = get_user_model().objects.create_user(
            email="test@londonappdev.com",
            password='password123',
            name='Test user full name'
        )

    def test_users_listed(self): #we are going to test if the user are listed in are django admin, we are going to make some few changes to are custom user model 
        """Test that users are listed on user page"""
        url = reverse('admin:core_user_changelist') #this url are defined in the django documentation, what it does this it will generate the url for our list user page.
         #this will perform an http get on are url that we find above
        res = self.client.get(url) # --> this is an object
        #assertContains will check that will contain 
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    #Here we are going to update are django admin to support the user model, to make sure that the changed page renders correctly 
    def test_user_change_page(self):
        """Test that the user edit page works"""
        url = reverse("admin:core_user_change", args=[self.user.id]) #we are genereting the url with reverse
        res = self.client.get(url)  #http get on the url
        self.assertEqual(res.status_code, 200) # assert that the page renders correctly

    def test_create_user_page(self): 
        """Test that the create user page works"""

        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)