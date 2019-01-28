from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
# Create your views here.
from .models import Post, Sezione
from .mixins import StaffMixing
from .forms import DiscussioneModelForm
from django.http import HttpResponseRedirect

class CreaSezione(StaffMixing, CreateView):
    model = Sezione
    fields = "__all__"
    template_name = "forum/crea_sezione.html"
    success_url = "/"


def visualizzaSezione(request, pk):
    sezione = get_object_or_404(Sezione, pk=pk)
    context = {"sezione": sezione}
    return render(request, "forum/simula_sezione.html", context)

@login_required
def creaDiscussione(request, pk):
    sezione = get_object_or_404(Sezione, pk=pk)
    if request.method == "POST":
        form = DiscussioneModelForm(request.POST)
        if form.is_valid():
            discussione = form.save(commit=False)
            discussione.sezione_appartenenza = sezione
            discussione.autore_discussione = request.user
            discussione.save()
            primo_post = Post.objects.create(
                discussione=discussione, 
                autore_post=request.user, 
                contenuto=form.cleaned_data["contenuto"])
            return HttpResponseRedirect("/admin/")
    else:
        form = DiscussioneModelForm()
    context = {"form": form, "sezione": sezione}
    return render(request, "forum/crea_discussione.html", context)
