<div align="center">

# 📚 Gestão Escolar 

</div>

<p align="center">
  <img alt="Last Commit" src="https://img.shields.io/github/last-commit/IasminBorba/Gestao-Escolar" />
  <img alt="License" src="https://img.shields.io/github/license/IasminBorba/Gestao-Escolar" />
  <a href="https://github.com/IasminBorba" target="_blank"><img alt="Follow Me" src="https://img.shields.io/github/followers/IasminBorba.svg?style=social&label=Follow&maxAge=2592000" /></a>
</p>

---

## ⚙️ Modo de uso
<br>

Antes de mais nada, para executar o projeto, é necessário que você crie seu ambiente virtual:

```sh
python -m venv env
```

Com o env definido, você precisa instalar as dependências (exemplo no ``dependencias.txt``):

```sh
source env/bin/activate
pip install -r dependencias.txt
```

Depois de instalar as dependências, basta executar ``python manage.py runserver``

(Embora você precise migrar usando: ``python manage.py migrate`` para ver o admin e criar um superusuário para entrar no admin: ``python manage.py createsuperuser``)

<br>

---

## 📑 Documentação da API
<br>

-   Admin: [/admin](http://localhost:8000/admin)
-   Alunos: [/api/alunos](http://localhost:8000/api/alunos/)
-   Professores: [/api/professores](http://localhost:8000/api/professores/)
-   Disciplinas: [/api/disciplinas](http://localhost:8000/api/disciplinas/)
-   Plano de aula: [/api/plano_de_aula](http://localhost:8000/api/plano_de_aula/)
-   Atividades: [/api/atividades](http://localhost:8000/api/atividades/)
-   Atividade Aluno: [/api/atividade_aluno](http://localhost:8000/api/atividade_aluno/)
-   Disciplina Aluno[/api/disciplina_aluno](http://localhost:8000/api/disciplina_aluno/)
-   Frequência: [/api/frequencia](http://localhost:8000/api/frequencia/)
-   Frequência Aluno: [/api/frequencia_aluno](http://localhost:8000/api/frequencia_aluno/)

---