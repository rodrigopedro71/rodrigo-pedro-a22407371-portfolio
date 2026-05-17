from django.contrib import admin
from .models import *


class ArtigoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "data_criacao")
    ordering = ("autor", "data_criacao")
    search_fields = ("titulo", "autor__username")


class ComentarioAdmin(admin.ModelAdmin):
    list_display = ("artigo", "autor", "data_criacao")
    ordering = ("artigo", "autor")
    search_fields = ("artigo__titulo", "autor__username")


admin.site.register(Artigo, ArtigoAdmin)
admin.site.register(Comentario, ComentarioAdmin)