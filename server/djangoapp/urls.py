from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import index, about, contact, login_view, logout_view, signup # Import the new logout view
from . import views

app_name = 'djangoapp'

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),  # Add this line for the logout page
    path('', views.get_dealerships, name='index'),
    path('signup/', signup, name='signup'),
    # Add more URL patterns as needed
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
