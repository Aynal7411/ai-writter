from django.urls import path
from .views import home_page, projects
urlpatterns = [
    path("", home_page, name="home"),
     path('projects/', projects, name='projects'),
]