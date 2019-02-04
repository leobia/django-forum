from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="homeapge"),
    path("users/", views.UserList.as_view(), name="user_list"),
    path("user/<username>/", views.userProfileView, name="user_profile"),
    path("cerca/", views.cerca, name="cerca")
]
