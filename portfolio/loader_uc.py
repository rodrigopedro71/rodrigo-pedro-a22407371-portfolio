import json
from portfolio.models import *

# Limpar dados existentes
Licenciatura.objects.all().delete()
Docente.objects.all().delete()
UC.objects.all().delete()

f = open("portfolio/data/ULHT260-PT.json")
json_info = json.load(f)
f.close()

detalhes = json_info["courseDetail"]
plano = json_info["courseFlatPlan"]
docentes = json_info["teachers"]

for d in docentes:
    novo_docente = Docente.objects.create(
        card_code=d.get("cardCode"),
        employee_code=d.get("employeeCode"),
        nome=d.get("fullName"),
        degree=d.get("degree"),
        regime=d.get("regimen"),
        email=d.get("email"),
    )

for unidade in plano:
    codigo = unidade["curricularIUnitReadableCode"]
    ficheiro = f"portfolio/data/ucs/{codigo}-PT.json"

    g = open(ficheiro)
    dados_uc = json.load(g)
    g.close()

    UC.objects.create(
        nome=unidade["curricularUnitName"],
        ects=unidade["ects"],
        ano=unidade["curricularYear"],
        semestre=unidade["semester"],
        objetivo=dados_uc["objectives"],
        descricao=dados_uc["presentation"],
        programa=dados_uc["programme"],
    )

Licenciatura.objects.create(
    curso_codigo=detalhes["courseCode"],
    nome=detalhes["courseName"],
    curso_ects=detalhes["courseECTS"],
    semestres=detalhes["semesters"],
    objetivos=detalhes["objectives"],
    descricao=detalhes["presentation"],
)