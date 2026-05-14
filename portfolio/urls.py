from django.urls import path
from . import views


urlpatterns = [
    path('', views.about_view),
    path('licenciaturas/', views.licenciatura_view, name="licenciaturas"),
    path("uc/<int:id>", views.uc_view, name="uc"),
    path("projetos/", views.projeto_view, name="projetos"),
    path("tecnologias/", views.tecnologias_view, name="tecnologias"),
    path("docentes/<int:id>", views.docentes_view, name="docentes"),
    path("competencias/", views.competencias_view, name="competencias"),
    path("formacoes/", views.formacoes_view, name="formacoes"),
    path("tfcs/", views.tfcs_view, name="tfcs"),
    path("makingof/", views.makingof_view, name="makingof"),
    path("about", views.about_view, name="about"),

    #CRUD
    path("projeto/novo", views.novo_projeto_view, name="novo_projeto"),
    path("projeto/<int:projeto_id>/edita", views.edita_projeto_view, name="edita_projeto"),
    path("projeto/<int:projeto_id>/apaga", views.apaga_projeto_view, name="apaga_projeto"),

    path("tecnologia/novo", views.novo_tecnologia_view, name="novo_tecnologia"),
    path("tecnologia/<int:tecnologia_id>/edita", views.edita_tecnologia_view, name="edita_tecnologia"),
    path("tecnologia/<int:tecnologia_id>/apaga", views.apaga_tecnologia_view, name="apaga_tecnologia"),

    path("competencia/novo", views.novo_competencia_view, name="novo_competencia"),
    path("competencia/<int:competencia_id>/edita", views.edita_competencia_view, name="edita_competencia"),
    path("competencia/<int:competencia_id>/apaga", views.apaga_competencia_view, name="apaga_competencia"),

    path("formacao/novo", views.novo_formacao_view, name="novo_formacao"),
    path("formacao/<int:formacao_id>/edita", views.edita_formacao_view, name="edita_formacao"),
    path("formacao/<int:formacao_id>/apaga", views.apaga_formacao_view, name="apaga_formacao"),
]