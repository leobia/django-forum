from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView
# Create your views here.
from .models import Sezione
from .mixins import StaffMixing

class CreaSezione(StaffMixing, CreateView):
    model = Sezione
    fields = "__all__"
    template_name = "forum/crea_sezione.html"
    success_url = "/"

def visualizzaSezione(request, pk):
    sezione = get_object_or_404(Sezione, pk=pk)
    context = {"sezione": sezione}
    return render(request, "forum/simula_sezione.html", context)