from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import AtividadeAluno, DisciplinaAluno

@receiver(post_save, sender=AtividadeAluno)
def adiciona_atividade(sender, instance, **kwargs):
    aluno = instance.id_aluno
    disciplina = instance.id_atividade.id_disciplina
    relacao = DisciplinaAluno.objects.get(id_aluno=aluno, id_disciplina=disciplina)
    atividades = AtividadeAluno.objects.filter(id_aluno=aluno, id_atividade__id_disciplina=disciplina)
    
    nota = 0.0
    for atv in atividades:
        nota += atv.nota

    disciplina.nota = nota
    disciplina.save()


@receiver(post_delete, sender=AtividadeAluno)
def deleta_atividade(sender, instance, **kwargs):
    aluno = instance.id_aluno
    disciplina = instance.id_atividade.id_disciplina
    relacao = DisciplinaAluno.objects.get(id_aluno=aluno, id_disciplina=disciplina)
    atividades = AtividadeAluno.objects.filter(id_aluno=aluno, id_atividade__id_disciplina=disciplina)
    
    nota = 0.0
    for atv in atividades:
        nota += atv.nota

    disciplina.nota = nota
    disciplina.save()