from django.urls import path
from . import views

urlpatterns =[
    path("nuova-sezione/", views.CreaSezione.as_view(), name="crea_sezione"),
    path("sezione/<int:pk>/", views.visualizzaSezione, name="sezione_view"),
    path("sezione/<int:pk>/crea-discussione/", views.creaDiscussione, name="crea_discussione"),
    path("discussione/<int:pk>/", views.visualizzaDiscussione, name="visualizza_discussione_view"),
    path("discussioni/<int:pk>/rispondi/", views.aggiungiRisposta, name="rispondi_a_discussione"),
    path("discussioni/<int:id>/elimina/<int:pk>", views.CancellaPost.as_view(), name="cancella_post")

]
