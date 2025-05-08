from django.urls import path
from . import views
from .views import home_page 

urlpatterns = [
    path("", home_page, name="home"),
    path('contact/', views.contact, name='contact'),
]