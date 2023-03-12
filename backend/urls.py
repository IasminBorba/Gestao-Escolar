from rest_framework import routers
from .views import *

routerBackend = routers.DefaultRouter()

routerBackend.register('alunos', AlunosViewSet)
routerBackend.register('professores', ProfessoresViewSet)
routerBackend.register('disciplinas', DisciplinasViewSet)
routerBackend.register('plano de aula', PlanoAulaViewSet)
routerBackend.register('atividades', AtividadesViewSet)
routerBackend.register('atividade aluno', AtividadeAlunoViewSet)
routerBackend.register('disciplina aluno', DisciplinaAlunoViewSet)
routerBackend.register('frequencia', FrequenciaViewSet)
routerBackend.register('frequencia aluno', FrequenciaAlunoViewSet)