from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime
import logging
import json

# Get an instance of a logger
logger = logging.getLogger(__name__)

# ./server/djangoapp/views.py

def index(request):
    return render(request, 'djangoapp/index.html')

# Create an `about` view to render a static about page
# def about(request):
# ...

# Create a `contact` view to return a static contact page
# def contact(request):
# ...

# Create a `login_request` view to handle sign-in request
def login_request(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully logged in.')
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')

    return render(request, 'djangoapp/index.html')

# Create a `logout_request` view to handle sign-out request
def logout_request(request):
    logout(request)
    messages.success(request, 'Successfully logged out.')
    return redirect('index')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'djangoapp/registration.html', {'form': form})

# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/index.html', context)

# Create a `get_dealer_details` view to render the reviews of a dealer
# def get_dealer_details(request, dealer_id):
# ...

# Create a `add_review` view to submit a review
# def add_review(request, dealer_id):
# ...

# Add more views as needed...


# ... (your existing imports)

def logout_view(request):
    logout(request)
    return render(request, 'djangoapp/logout.html')  # You need to create a logout.html template
