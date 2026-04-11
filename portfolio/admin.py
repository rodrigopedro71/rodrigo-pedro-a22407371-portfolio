from .models import *
from django.contrib import admin


class TfcsAdmin(admin.ModelAdmin):
    search_fields = ("titulo",)
    list_display = ("titulo", "aluno", "orientador")
    ordering = ("titulo",)


class DocenteAdmin(admin.ModelAdmin):
    list_display = ("nome", "email", "employee_code", "regime", "degree")
    search_fields = ("nome", "email", "employee_code")
    ordering = ("employee_code", "nome")


class LicenciaturaAdmin(admin.ModelAdmin):
    ordering = ("curso_codigo", "nome")
    list_display = ("nome", "curso_codigo", "curso_ects", "semestres")
    search_fields = ("nome", "curso_codigo")


class UCAdmin(admin.ModelAdmin):
    search_fields = ("nome",)
    list_display = ("nome", "semestre", "ano")
    ordering = ("nome",)


class FormacaoAdmin(admin.ModelAdmin):
    list_display = ("tipo", "data", "descricao")
    search_fields = ("tipo",)
    ordering = ("tipo",)


class TecnologiaAdmin(admin.ModelAdmin):
    ordering = ("nome",)
    search_fields = ("nome",)
    list_display = ("nome", "site_oficial")


class CompetenciaAdmin(admin.ModelAdmin):
    ordering = ("tipo",)
    list_display = ("tipo", "descricao")
    search_fields = ("tipo",)


class ProjetoAdmin(admin.ModelAdmin):
    list_display = ("nome", "repositorio", "descricao")
    ordering = ("nome",)
    search_fields = ("nome",)


class MakingOfAdmin(admin.ModelAdmin):
    search_fields = ("titulo", "id")
    ordering = ("id",)
    list_display = ("titulo",)


admin.site.register(Tfc, TfcsAdmin)
admin.site.register(Docente, DocenteAdmin)
admin.site.register(Licenciatura, LicenciaturaAdmin)
admin.site.register(UC, UCAdmin)
admin.site.register(Formacao, FormacaoAdmin)
admin.site.register(Tecnologia, TecnologiaAdmin)
admin.site.register(Competencia, CompetenciaAdmin)
admin.site.register(Projeto, ProjetoAdmin)
admin.site.register(MakingOf, MakingOfAdmin)