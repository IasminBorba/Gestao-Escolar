from django.contrib import admin

from .models import *

class AlunosForm(admin.ModelAdmin):
    list_display = ['matricula','nome','email','telefone']
    ordering = ['nome']
    search_fields = ['nome','matricula']


class ProfessoresForm(admin.ModelAdmin):
    list_display = ['nome','email','telefone']
    ordering = ['nome']
    search_fields = ['nome']


class DisciplinasForm(admin.ModelAdmin):
    
    list_display = ['nome','id_professor','carga_horaria']
    list_filter = ['id_professor']
    ordering = ['nome']
    search_fields = ['nome','id_professor__nome']


class PlanoAulaForm(admin.ModelAdmin):
    def disciplina(self, instance):
        return instance.id_disciplina.nome

    list_display = ['disciplina','tema_aula','metodo']
    list_filter = ['metodo']
    ordering = ['id_disciplina__nome']
    search_fields = ['tema_aula']


class AtividadesForm(admin.ModelAdmin):
    def disciplina(self, instance):
        return instance.id_disciplina.nome

    list_display = ['disciplina','atividade','tipo']
    list_filter = ['tipo']
    ordering = ['id_disciplina__nome']
    search_fields = ['atividade']


class AtividadeAlunoForm(admin.ModelAdmin):
    def nome(self, instance):
        return instance.id_aluno.nome

    def atividade(self, instance):
        return instance.id_atividade.atividade

    list_display = ['nome','atividade','nota']
    ordering = ['id_aluno__nome']
    search_fields = ['id_atividade, id_aluno']


class DisciplinaAlunoForm (admin.ModelAdmin):
    def nome(self, instance):
        return instance.id_aluno.nome
    
    def disciplina(self, instance):
        return instance.id_disciplina.nome

    list_display = ['nome','disciplina','nota']
    list_filter = ['id_disciplina__nome']
    ordering = ['id_disciplina__nome']
    search_fields = ['nome']


class FrequenciaForm(admin.ModelAdmin):

    def materia(self, instance): 
        return instance.id_materia.nome

    list_display = ['materia','dia']
    list_filter = ['id_materia__nome']
    ordering = ['dia']
    search_fields = ['materia']


class FrequenciaAlunoForm(admin.ModelAdmin):
    def aluno(self, instance): 
        return instance.id_aluno.nome
    
    def data(self, instance):
        return instance.id_frequencia.dia

    list_display = ['aluno','data','presenca']
    list_filter = ['id_frequencia__id_materia__nome','id_aluno__nome']
    ordering = ['id_frequencia__dia']
    search_fields = ['aluno']


admin.site.register(Alunos, AlunosForm)
admin.site.register(Professores, ProfessoresForm)
admin.site.register(Disciplinas, DisciplinasForm)
admin.site.register(PlanoAula, PlanoAulaForm)
admin.site.register(Atividades, AtividadesForm)
admin.site.register(AtividadeAluno, AtividadeAlunoForm)
admin.site.register(DisciplinaAluno, DisciplinaAlunoForm)
admin.site.register(Frequencia, FrequenciaForm)
admin.site.register(FrequenciaAluno, FrequenciaAlunoForm)