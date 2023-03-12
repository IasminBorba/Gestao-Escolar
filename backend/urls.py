from rest_framework import routers
from .views import *

routerBackend = routers.DefaultRouter()

routerBackend.register('alunos', AlunosViewSet)
routerBackend.register('professores', ProfessoresViewSet)
routerBackend.register('disciplinas', DisciplinasViewSet)
routerBackend.register('plano_de_aula', PlanoAulaViewSet)
routerBackend.register('atividades', AtividadesViewSet)
routerBackend.register('atividade_aluno', AtividadeAlunoViewSet)
routerBackend.register('disciplina_aluno', DisciplinaAlunoViewSet)
routerBackend.register('frequencia', FrequenciaViewSet)
routerBackend.register('frequencia_aluno', FrequenciaAlunoViewSet)