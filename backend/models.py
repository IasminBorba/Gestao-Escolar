from django.db import models

class Alunos(models.Model):
    id_aluno = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11, unique=True)
    rg = models.CharField(max_length=8, unique=True)
    matricula = models.CharField(max_length=8, unique=True)
    telefone = models.CharField(max_length=11)
    email = models.EmailField(max_length=255, unique=True)

    class Meta:
        db_table = "Alunos"
        verbose_name_plural = "Alunos"

    def __str__(self):
        return self.nome


class Professores(models.Model):
    id_professor = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11, unique=True)
    rg = models.CharField(max_length=8, unique=True)
    codigo = models.CharField(max_length=8, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    telefone = models.CharField(max_length=11)

    class Meta:
        db_table = "Professores"
        verbose_name_plural = "Professores"

    def __str__(self):
        return self.nome
    

class Disciplinas(models.Model):
    id_disciplina = models.AutoField(primary_key=True)
    id_professor = models.ForeignKey("backend.Professores", on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    codigo = models.CharField(max_length=7, unique=True)
    carga_horaria = models.IntegerField()
    ementa = models.TextField(null=True, blank=True)

    class Meta:
        db_table = "Disciplinas"
        verbose_name_plural = "Disciplinas"

    def __str__(self):
        return self.codigo + "-" + self.nome
    

class PlanoAula(models.Model):
    metodo_choices = (
        ("T", "Teorica"),
        ("P", "Prática"),
    )

    id_plano_aula = models.AutoField(primary_key=True)
    id_disciplina = models.ForeignKey("backend.Disciplinas", on_delete=models.CASCADE)
    tema_aula = models.CharField(max_length=255)
    conteudo = models.TextField()
    metodo = models.CharField(max_length=1, choices=metodo_choices, blank=False, null=False)
    dia = models.DateField()

    class Meta:
        db_table = "PlanoAula"
        verbose_name_plural = "Plano de Aula"

    def __str__(self):
        return self.tema_aula + "(" + str(self.id_disciplina.nome) + ")"
    

class Atividades(models.Model):
    atividade_choices = (
        ("AS", "Atividade de Sala"),
        ("AC", "Atividade de Casa"),
        ("P","Prova")
    )

    id_atividade = models.AutoField(primary_key=True)
    atividade = models.TextField()
    tipo = models.CharField(max_length=2, choices=atividade_choices, blank=False, null=False)
    data_postagem = models.DateField(auto_now=True)
    data_entrega = models.DateField(null=True, blank=True)
    id_disciplina = models.ForeignKey("backend.Disciplinas", on_delete=models.CASCADE)
    id_plano_aula = models.ForeignKey("backend.PlanoAula", on_delete=models.CASCADE)

    class Meta:
        db_table = "Atividades"
        verbose_name_plural = "Atividades"

    def __str__(self):
        return self.atividade
    

class AtividadeAluno(models.Model):
    id = models.AutoField(primary_key=True)
    id_atividade = models.ForeignKey("backend.Atividades", on_delete=models.CASCADE)
    id_aluno = models.ForeignKey("backend.Alunos", on_delete=models.CASCADE)
    nota = models.FloatField(default=0.0, null=True, blank=True) 

    class Meta:
        db_table = "AtividadeAluno"
        verbose_name_plural = "Atividade Aluno"

    def __str__(self):
        return str(self.nota)
    

class DisciplinaAluno(models.Model):
    id_matricula = models.AutoField(primary_key=True)
    id_aluno = models.ForeignKey("backend.Alunos", on_delete=models.CASCADE)
    id_disciplina = models.ForeignKey("backend.Disciplinas", on_delete=models.CASCADE)
    nota = models.FloatField(default=0.0, null=True, blank=True) 

    class Meta:
        db_table = "DisciplinaAluno"
        verbose_name_plural = "Disciplina Aluno"

    def __str__(self):
        return str(self.nota)
    

class Frequencia(models.Model):
    id_frequencia = models.AutoField(primary_key=True)
    id_materia = models.ForeignKey("backend.Disciplinas", on_delete=models.CASCADE)
    dia = models.DateField()

    class Meta:
        db_table = "Frequencia"
        verbose_name_plural = "Frequência"

    def __str__(self):
        return str(self.dia)
    

class FrequenciaAluno(models.Model):
    id = models.AutoField(primary_key=True)
    id_aluno = models.ForeignKey("backend.Alunos", on_delete=models.CASCADE)
    id_frequencia = models.ForeignKey("backend.Frequencia", on_delete=models.CASCADE)
    presenca = models.BooleanField(default=True)

    class Meta:
        db_table = "FrequenciaAluno"
        verbose_name_plural = "Frequência do Aluno"

    def __str__(self):
        return str(self.id_frequencia) + "-" + str(self.presenca)