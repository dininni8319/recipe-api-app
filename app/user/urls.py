from django.urls import path 

from user import views 

app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'), # we are giving the name to intify are reverse lookup function
    path('token/', views.CreateTokenView.as_view(), name='token')

]