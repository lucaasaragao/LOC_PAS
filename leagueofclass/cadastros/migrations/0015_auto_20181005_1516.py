# Generated by Django 2.1.1 on 2018-10-05 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0014_auto_20181004_0244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='frequencia',
            name='aluno',
        ),
        migrations.AddField(
            model_name='frequencia',
            name='aluno',
            field=models.ManyToManyField(to='cadastros.Aluno'),
        ),
        migrations.RemoveField(
            model_name='frequencia',
            name='disciplina',
        ),
        migrations.AddField(
            model_name='frequencia',
            name='disciplina',
            field=models.ManyToManyField(to='cadastros.Disciplinas'),
        ),
    ]