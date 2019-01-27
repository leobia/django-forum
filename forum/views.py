from django.shortcuts import render
from django.views.generic.edit import CreateView
# Create your views here.
from .models import Sezione
from .mixins import StaffMixing

class CreaSezione(StaffMixing, CreateView):
    model = Sezione
    fields = "__all__"
    template_name = "forum/crea_sezione.html"
    success_url = "/"
