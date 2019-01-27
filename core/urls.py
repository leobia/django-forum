from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.homepage, name="homeapge"),
    path("users/", views.UserList.as_view(), name="user_list"),
    path("user/<username>/", views.userProfileView, name="user_profile")
]