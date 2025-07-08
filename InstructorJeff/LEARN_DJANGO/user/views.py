from django.shortcuts import render

# Create your views here.


def home(request):
    """
    Render the home page.
    """
    return render(request, 'home.html')


def login_views(request):
    """
    Render the login page.
    """
    return render(request, 'login.html')


def signup_views(request):
    """
    Render the signup page.
    """
    return render(request, 'signup.html')
