# Generated by Django 4.1.7 on 2023-03-11 01:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alunos',
            fields=[
                ('id_aluno', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('rg', models.CharField(max_length=8, unique=True)),
                ('matricula', models.CharField(max_length=8, unique=True)),
                ('telefone', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Alunos',
                'db_table': 'Alunos',
            },
        ),
        migrations.CreateModel(
            name='Disciplinas',
            fields=[
                ('id_disciplina', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('codigo', models.CharField(max_length=7, unique=True)),
                ('carga_horaria', models.IntegerField()),
                ('ementa', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Disciplinas',
                'db_table': 'Disciplinas',
            },
        ),
        migrations.CreateModel(
            name='Frequencia',
            fields=[
                ('id_frequencia', models.AutoField(primary_key=True, serialize=False)),
                ('dia', models.DateField()),
                ('id_materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.disciplinas')),
            ],
            options={
                'verbose_name_plural': 'Frequencias',
                'db_table': 'Frequencia',
            },
        ),
        migrations.CreateModel(
            name='Professores',
            fields=[
                ('id_professor', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('rg', models.CharField(max_length=8, unique=True)),
                ('codigo', models.CharField(max_length=8, unique=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('telefone', models.CharField(max_length=11)),
            ],
            options={
                'verbose_name_plural': 'Professores',
                'db_table': 'Professores',
            },
        ),
        migrations.CreateModel(
            name='PlanoAula',
            fields=[
                ('id_plano_aula', models.AutoField(primary_key=True, serialize=False)),
                ('tema_aula', models.CharField(max_length=255)),
                ('conteudo', models.TextField()),
                ('metodo', models.CharField(choices=[('T', 'Teorica'), ('P', 'Pratica')], max_length=1)),
                ('dia', models.DateField()),
                ('id_disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.disciplinas')),
            ],
            options={
                'verbose_name_plural': 'PlanoAulas',
                'db_table': 'PlanoAula',
            },
        ),
        migrations.CreateModel(
            name='FrequenciaAluno',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('presenca', models.BooleanField(default=True)),
                ('id_aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.alunos')),
                ('id_frequencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.frequencia')),
            ],
            options={
                'verbose_name_plural': 'FrequenciaAlunos',
                'db_table': 'FrequenciaAluno',
            },
        ),
        migrations.AddField(
            model_name='disciplinas',
            name='id_professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.professores'),
        ),
        migrations.CreateModel(
            name='DisciplinaAluno',
            fields=[
                ('id_matricula', models.AutoField(primary_key=True, serialize=False)),
                ('nota', models.FloatField()),
                ('id_aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.alunos')),
                ('id_disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.disciplinas')),
            ],
            options={
                'verbose_name_plural': 'DisciplinaAlunos',
                'db_table': 'DisciplinaAluno',
            },
        ),
        migrations.CreateModel(
            name='Atividades',
            fields=[
                ('id_atividade', models.AutoField(primary_key=True, serialize=False)),
                ('atividade', models.TextField()),
                ('tipo', models.CharField(choices=[('AS', 'Atividade de Sala'), ('AC', 'Atividade de Casa'), ('P', 'Prova')], max_length=2)),
                ('data_postagem', models.DateField(auto_now=True)),
                ('data_entrega', models.DateField(blank=True, null=True)),
                ('id_disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.disciplinas')),
                ('id_plano_aula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.planoaula')),
            ],
            options={
                'verbose_name_plural': 'Atividades',
                'db_table': 'Atividades',
            },
        ),
        migrations.CreateModel(
            name='AtividadeAluno',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nota', models.FloatField()),
                ('id_aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.alunos')),
                ('id_atividade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.atividades')),
            ],
            options={
                'verbose_name_plural': 'AtividadeAlunos',
                'db_table': 'AtividadeAluno',
            },
        ),
    ]
