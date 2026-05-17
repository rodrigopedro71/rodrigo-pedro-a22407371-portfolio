from django.db import models


class Licenciatura(models.Model):
    curso_codigo = models.IntegerField()
    nome = models.CharField(max_length=100)
    semestres = models.IntegerField()
    curso_ects = models.IntegerField()
    descricao = models.TextField(blank=True)
    objetivos = models.TextField(blank=True)
    uc = models.ManyToManyField('UC', related_name="licenciaturas", blank=True)

    def __str__(self):
        return self.nome


class Formacao(models.Model):
    # tipo pode ser ex: curso, workshop, certificação
    tipo = models.CharField(max_length=100)
    data = models.DateField()
    descricao = models.TextField()

    def __str__(self):
        return f"{self.tipo} feito em {self.data}"


class Tecnologia(models.Model):
    nome = models.CharField(max_length=100)
    classificacao = models.IntegerField()
    descricao = models.TextField()
    logo = models.ImageField(upload_to="fotos_tecnologia/", blank=True)
    formacao = models.ManyToManyField(Formacao, blank=True, related_name="tecnologias")

    def __str__(self):
        return f"Tecnologia: {self.nome} | Classificação: {self.classificacao}/5"


class Competencia(models.Model):
    tipo = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.tipo


class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    conceitos = models.CharField(max_length=500)
    descricao = models.TextField()
    repositorio = models.CharField(max_length=100, blank=True)
    tecnologia = models.ManyToManyField(Tecnologia, related_name="projetos", blank=True)
    competencia = models.ManyToManyField(Competencia, related_name="projetos", blank=True)

    def __str__(self):
        return self.nome


class Docente(models.Model):
    REGIME_CHOICES = [
        ('integral', 'Tempo Integral'),
        ('parcial', 'Tempo Parcial'),
    ]

    card_code = models.IntegerField()
    employee_code = models.IntegerField()
    nome = models.CharField(max_length=100)
    degree = models.CharField(max_length=25, blank=True, null=True)
    regime = models.CharField(max_length=25)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.nome


class UC(models.Model):
    nome = models.CharField(max_length=100)
    ano = models.IntegerField()
    semestre = models.CharField(max_length=20)
    ects = models.IntegerField()
    objetivo = models.TextField(blank=True)
    descricao = models.TextField(blank=True)
    programa = models.TextField(blank=True)
    imagem = models.ImageField(upload_to="fotos_uc/", blank=True)
    docente = models.ManyToManyField(Docente, blank=True, related_name="ucs")
    projeto = models.ForeignKey(
        Projeto,
        on_delete=models.CASCADE,
        related_name="ucs",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.nome


class Tfc(models.Model):
    titulo = models.TextField()
    licenciatura = models.TextField()
    aluno = models.TextField()
    orientador = models.TextField()
    area = models.TextField()
    tecnologias = models.TextField()
    palavras_chave = models.TextField()
    rating = models.IntegerField()
    email = models.TextField()
    pdf = models.TextField()
    resumo = models.TextField()

    def __str__(self):
        return self.titulo


class MakingOf(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    alteracao = models.TextField(blank=True)
    justificacao = models.TextField(blank=True)
    llm = models.CharField(max_length=500, blank=True)
    fotos = models.ImageField(upload_to="makingof_fotos/", blank=True)

    def __str__(self):
        return self.titulo