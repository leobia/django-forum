from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
# Create your views here.

def homepage(request):
    return render(request, 'core/homepage.html')

def userProfileView(request, username):
    user = get_object_or_404(User, username=username)
    context = {"user": user}
    return render(request, 'core/user_profile.html', context)

class UserList(ListView):
    model = User
    template_name = "core/users.html"