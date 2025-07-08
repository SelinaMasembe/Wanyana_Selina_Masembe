from django.urls import path
from . import views

# user/urls.py
urlpatterns = [
    # Define your URL patterns here
    path('',views.home, name='home'),
    path('login/', views.login_views, name='login'),
    path('signup/', views.signup_views, name='signup'),
]
