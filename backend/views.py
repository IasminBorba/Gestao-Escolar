from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action


class AlunosViewSet(viewsets.ModelViewSet):
    queryset = Alunos.objects.all()
    serializer_class = AlunosSerializer


class ProfessoresViewSet(viewsets.ModelViewSet):
    queryset = Professores.objects.all()
    serializer_class = ProfessoresSerializer
    

class DisciplinasViewSet(viewsets.ModelViewSet):
    queryset = Disciplinas.objects.all()
    serializer_class = DisciplinasSerializer


class PlanoAulaViewSet(viewsets.ModelViewSet):
    queryset = PlanoAula.objects.all()
    serializer_class = PlanoAulaSerializer


class AtividadesViewSet(viewsets.ModelViewSet):
    queryset = Atividades.objects.all()
    serializer_class = AtividadesSerializer


class AtividadeAlunoViewSet(viewsets.ModelViewSet):
    queryset = AtividadeAluno.objects.all()
    serializer_class = AtividadeAlunoSerializer


class DisciplinaAlunoViewSet(viewsets.ModelViewSet):
    queryset = DisciplinaAluno.objects.all()
    serializer_class = DisciplinaAlunoSerializer


class FrequenciaViewSet(viewsets.ModelViewSet):
    queryset = Frequencia.objects.all()
    serializer_class = FrequenciaSerializer


class FrequenciaAlunoViewSet(viewsets.ModelViewSet):
    queryset = FrequenciaAluno.objects.all()
    serializer_class = FrequenciaAlunoSerializer