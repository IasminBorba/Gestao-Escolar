from django.contrib import admin

from .models import *

class AlunosForm(admin.ModelAdmin):
    list_display = ['nome','matricula']
    ordering = ['nome']
    search_fields = ['nome']


class ProfessoresForm(admin.ModelAdmin):
    list_display = ['nome','codigo']
    ordering = ['nome']
    search_fields = ['nome']


class DisciplinasForm(admin.ModelAdmin):
    def estado(self, instance):
        return instance.id_professor.nome
    
    list_display = ['codigo','nome', 'id_professor']
    list_filter = ['id_professor']
    ordering = ['nome']
    search_fields = ['nome']


class PlanoAulaForm(admin.ModelAdmin):
    def estado(self, instance):
        return instance.id_disciplina.nome

    list_display = ['id_disciplina', 'tema_aula', 'metodo']
    list_filter = ['metodo']
    ordering = ['id_disciplina']
    search_fields = ['tema_aula']


class AtividadesForm(admin.ModelAdmin):
    def estado(self, instance):
        return instance.id_disciplina.nome

    list_display = ['id_disciplina', 'atividade', 'tipo']
    list_filter = ['tipo']
    ordering = ['id_disciplina']
    search_fields = ['atividade']


class AtividadeAlunoForm(admin.ModelAdmin):
    def estado(self, instance):
        return instance.id_aluno.nome

    def estado(self, instance):
        return instance.id_atividade.atividade

    list_display = ['id_aluno', 'id_atividade', 'nota']
    ordering = ['id_aluno']
    search_fields = ['id_atividade']


class DisciplinaAlunoForm (admin.ModelAdmin):
    def estado(self, instance):
        return instance.id_aluno.nome
    
    def estado(self, instance):
        return instance.id_disciplina.nome

    list_display = ['id_aluno', 'id_disciplina', 'nota']
    list_filter = ['id_disciplina']
    ordering = ['id_aluno']
    search_fields = ['id_aluno']


class FrequenciaForm(admin.ModelAdmin):
    def estado(self, instance):
        return instance.id_materia.nome

    list_display = ['id_materia','dia']
    list_filter = ['id_materia']
    ordering = ['dia']
    search_fields = ['id_materia']


class FrequenciaAlunoForm(admin.ModelAdmin):
    def estado(self, instance):
        return instance.id_aluno.nome
    
    def estado(self, instance):
        return instance.id_frequencia.dia

    list_display = ['id_aluno', 'id_frequencia', 'presenca']
    list_filter = ['id_frequencia']
    ordering = ['id_frequencia']
    search_fields = ['id_aluno']


admin.site.register(Alunos, AlunosForm)
admin.site.register(Professores, ProfessoresForm)
admin.site.register(Disciplinas, DisciplinasForm)
admin.site.register(PlanoAula, PlanoAulaForm)
admin.site.register(Atividades, AtividadesForm)
admin.site.register(AtividadeAluno, AtividadeAlunoForm)
admin.site.register(DisciplinaAluno, DisciplinaAlunoForm)
admin.site.register(Frequencia, FrequenciaForm)
admin.site.register(FrequenciaAluno, FrequenciaAlunoForm)