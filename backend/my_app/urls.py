from django.urls import path
from . import views 
urlpatterns=[
    path('profile/<input>/',views.profile, name='profile')]