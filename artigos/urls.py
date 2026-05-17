from django.urls import path
from . import views

urlpatterns = [
    path("", views.artigos_view, name="artigos"),
    path("novo/", views.novo_artigo_view, name="novo_artigo"),
    path("detalhe/<int:artigo_id>/", views.detalhe_artigo_view, name="detalhe_artigo"),
    path("edita/<int:artigo_id>/", views.edita_artigo_view, name="edita_artigo"),
    path("apaga/<int:artigo_id>/", views.apaga_artigo_view, name="apaga_artigo"),
    path("like/<int:artigo_id>/", views.like_view, name="like"),
    path("edita/comentario/<int:comentario_id>/", views.edita_comentario_view, name="edita_comentario"),
    path("apaga/comentario/<int:comentario_id>/", views.apaga_comentario_view, name="apaga_comentario"),
]