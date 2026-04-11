import json
from portfolio.models import *

Tfc.objects.all().delete()

f = open("portfolio/data/tfc.json")
dados = json.load(f)
f.close()

for entrada in dados["TFCs_2025"]:
    Tfc.objects.create(
        titulo=entrada["titulo"],
        aluno=entrada["autores"],
        orientador=entrada["orientadores"],
        licenciatura=entrada["licenciatura"],
        pdf=entrada["pdf"],
        email=entrada["email"],
        resumo=entrada["sumario"],
        palavras_chave=", ".join(entrada["palavras_chave"]),
        area=", ".join(entrada["areas"]),
        tecnologias=", ".join(entrada["tecnologias"]),
        rating=entrada["rating"],
    )