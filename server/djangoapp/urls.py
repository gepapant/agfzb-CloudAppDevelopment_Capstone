from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # route is a string contains a URL pattern
    # view refers to the view function
   # ./server/djangoapp/urls.py

from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index'),
    # Add more URL patterns as needed
]


   # ./server/djangoapp/urls.py

from django.urls import path
from .views import index, about

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),  # Add this line for the About Us page
    # Add more URL patterns as needed
]

from django.urls import path
from .views import index, about, contact

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),  # Add this line for the Contact Us page
    # Add more URL patterns as needed
]


    # path for registration

    # path for login

    # path for logout

    path(route='', view=views.get_dealerships, name='index'),

    # path for dealer reviews view

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)