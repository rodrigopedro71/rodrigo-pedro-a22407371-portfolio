from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.conf import settings
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
import os


def is_gestor(user):
    return user.groups.filter(name="gestor-portfolio").exists()


# VIEWS

def licenciatura_view(request):
    licenciaturas = Licenciatura.objects.prefetch_related("uc").all()
    context = {
        "licenciaturas": licenciaturas
    }
    return render(request, "portfolio/licenciatura.html", context)


def uc_view(request, id):
    uc = UC.objects.get(id=id)
    context = {
        "uc": uc
    }
    return render(request, "portfolio/uc.html", context)


def projeto_view(request):
    projetos = Projeto.objects.prefetch_related("tecnologia")
    context = {
        "projetos": projetos,
        "gestor": is_gestor(request.user)
    }
    return render(request, "portfolio/projetos.html", context)


def tecnologias_view(request):
    tecnologias = Tecnologia.objects.prefetch_related("formacao")
    context = {
        "tecnologias": tecnologias,
        "gestor": is_gestor(request.user)
    }
    return render(request, "portfolio/tecnologias.html", context)


def docentes_view(request, id):
    licenciatura = Licenciatura.objects.get(id=id)
    ucs = licenciatura.uc.all()
    docentes = Docente.objects.filter(ucs__in=ucs)
    context = {
        "licenciatura": licenciatura,
        "ucs": ucs,
        "docentes": docentes
    }
    return render(request, "portfolio/docentes.html", context)


def competencias_view(request):
    competencias = Competencia.objects.all()
    context = {
        "competencias": competencias,
        "gestor": is_gestor(request.user)
    }
    return render(request, "portfolio/competencias.html", context)


def formacoes_view(request):
    formacoes = Formacao.objects.all()
    context = {
        "formacoes": formacoes,
        "gestor": is_gestor(request.user)
    }
    return render(request, "portfolio/formacoes.html", context)


def tfcs_view(request):
    tfcs = Tfc.objects.all()
    context = {
        "tfcs": tfcs
    }
    return render(request, "portfolio/tfcs.html", context)


def makingof_view(request):
    makingofs = MakingOf.objects.all()
    context = {
        "makingofs": makingofs
    }
    return render(request, "portfolio/makingof.html", context)


def about_view(request):
    tecnologias = Tecnologia.objects.all()
    makingofs = MakingOf.objects.all()
    context = {
        "tecnologias": tecnologias,
        "makingofs": makingofs
    }
    return render(request, "portfolio/about.html", context)


# CRUD

@login_required
def novo_projeto_view(request):
    if not is_gestor(request.user):
        return redirect("projetos")

    form = ProjetoForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect("projetos")

    context = {"form": form}
    return render(request, "portfolio/novo_projeto.html", context)


@login_required
def edita_projeto_view(request, projeto_id):
    if not is_gestor(request.user):
        return redirect("projetos")

    projeto = Projeto.objects.get(id=projeto_id)
    if request.POST:
        form = ProjetoForm(request.POST or None, request.FILES, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect("projetos")
    else:
        form = ProjetoForm(instance=projeto)

    context = {"form": form, "projeto": projeto}
    return render(request, "portfolio/edita_projeto.html", context)


@login_required
def apaga_projeto_view(request, projeto_id):
    if not is_gestor(request.user):
        return redirect("projetos")

    projeto = Projeto.objects.get(id=projeto_id)
    projeto.delete()
    return redirect("projetos")


@login_required
def novo_tecnologia_view(request):
    if not is_gestor(request.user):
        return redirect("tecnologias")

    form = TecnologiaForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect("tecnologias")

    context = {"form": form}
    return render(request, "portfolio/novo_tecnologia.html", context)


@login_required
def edita_tecnologia_view(request, tecnologia_id):
    if not is_gestor(request.user):
        return redirect("tecnologias")

    tecnologia = Tecnologia.objects.get(id=tecnologia_id)
    if request.POST:
        form = TecnologiaForm(request.POST or None, request.FILES, instance=tecnologia)
        if form.is_valid():
            form.save()
            return redirect("tecnologias")
    else:
        form = TecnologiaForm(instance=tecnologia)

    context = {"form": form, "tecnologia": tecnologia}
    return render(request, "portfolio/edita_tecnologia.html", context)


@login_required
def apaga_tecnologia_view(request, tecnologia_id):
    if not is_gestor(request.user):
        return redirect("tecnologias")

    tecnologia = Tecnologia.objects.get(id=tecnologia_id)
    tecnologia.delete()
    return redirect("tecnologias")


@login_required
def novo_competencia_view(request):
    if not is_gestor(request.user):
        return redirect("competencias")

    form = CompetenciaForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect("competencias")

    context = {"form": form}
    return render(request, "portfolio/novo_competencia.html", context)


@login_required
def edita_competencia_view(request, competencia_id):
    if not is_gestor(request.user):
        return redirect("competencias")

    competencia = Competencia.objects.get(id=competencia_id)
    if request.POST:
        form = CompetenciaForm(request.POST or None, request.FILES, instance=competencia)
        if form.is_valid():
            form.save()
            return redirect("competencias")
    else:
        form = CompetenciaForm(instance=competencia)

    context = {"form": form, "competencia": competencia}
    return render(request, "portfolio/edita_competencia.html", context)


@login_required
def apaga_competencia_view(request, competencia_id):
    if not is_gestor(request.user):
        return redirect("competencias")

    competencia = Competencia.objects.get(id=competencia_id)
    competencia.delete()
    return redirect("competencias")


@login_required
def novo_formacao_view(request):
    if not is_gestor(request.user):
        return redirect("formacoes")

    form = FormacaoForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect("formacoes")

    context = {"form": form}
    return render(request, "portfolio/novo_formacao.html", context)


@login_required
def edita_formacao_view(request, formacao_id):
    if not is_gestor(request.user):
        return redirect("formacoes")

    formacao = Formacao.objects.get(id=formacao_id)
    if request.POST:
        form = FormacaoForm(request.POST or None, request.FILES, instance=formacao)
        if form.is_valid():
            form.save()
            return redirect("formacoes")
    else:
        form = FormacaoForm(instance=formacao)

    context = {"form": form, "formacao": formacao}
    return render(request, "portfolio/edita_formacao.html", context)


@login_required
def apaga_formacao_view(request, formacao_id):
    if not is_gestor(request.user):
        return redirect("formacoes")

    formacao = Formacao.objects.get(id=formacao_id)
    formacao.delete()
    return redirect("formacoes")