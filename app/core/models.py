from django.db import models
#This are all thing that we need to extand the django user model, 
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                       PermissionsMixin
#The manager class provide a helper function for creating the user/superuser
class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields): # what it does, the last field, basecly takes any extra function passed into the create_user and  add them into the **extra_fields
        """Create and save a new user"""
        user = self.model(email=email, **extra_fields) #is going to pass the email first and then the extra things that we add
        user.set_password(password) # what it does it encript the password
        user.save(using=self._db)

        return user 
#AbstractBaseUser, PermissionsMixin are features that come auto of the box with django usermodel and with can customize 
    # user bye default are active but not staff
class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True) 
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'