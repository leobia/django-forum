from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
# Create your views here.
from .models import Discussione, Post, Sezione
from .mixins import StaffMixing
from .forms import DiscussioneModelForm, PostModelForm
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.urls import reverse

class CreaSezione(StaffMixing, CreateView):
    model = Sezione
    fields = "__all__"
    template_name = "forum/crea_sezione.html"
    success_url = "/"


def visualizzaSezione(request, pk):
    sezione = get_object_or_404(Sezione, pk=pk)
    discussioni_sezione = Discussione.objects.filter(sezione_appartenenza=sezione).order_by("-data_creazione")
    context = {"sezione": sezione, "discussioni": discussioni_sezione}
    return render(request, "forum/singola_sezione.html", context)


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
            return HttpResponseRedirect(discussione.get_absolute_url())
    else:
        form = DiscussioneModelForm()
    context = {"form": form, "sezione": sezione}
    return render(request, "forum/crea_discussione.html", context)


def visualizzaDiscussione(request, pk):
    discussione = get_object_or_404(Discussione, pk=pk)
    posts_discussione = Post.objects.filter(discussione=discussione)
    form_risposta = PostModelForm()
    context = {"discussione": discussione, 
                "posts_discussione": posts_discussione,
                "form_risposta":form_risposta}
    return render(request, "forum/singola_discussione.html", context)


def aggiungiRisposta(request, pk):
    discussione = get_object_or_404(Discussione, pk=pk)
    if request.method == "POST":
        form = PostModelForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.discussione = discussione
            form.instance.autore_post = request.user
            form.save()
            url_discussione = reverse("visualizza_discussione_view", kwargs={"pk": pk})
            return HttpResponseRedirect(url_discussione)
    else:
        return HttpResponseBadRequest()
