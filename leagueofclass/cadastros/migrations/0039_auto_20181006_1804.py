# Generated by Django 2.1.1 on 2018-10-06 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0038_auto_20181006_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='notas',
            name='disciplina',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='cadastros.Disciplinas'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notas',
            name='nota1',
            field=models.CharField(default='Nota não cadastrada', max_length=20),
        ),
        migrations.AddField(
            model_name='notas',
            name='nota2',
            field=models.CharField(default='Nota não cadastrada', max_length=20),
        ),
        migrations.AddField(
            model_name='notas',
            name='nota3',
            field=models.CharField(default='Nota não cadastrada', max_length=20),
        ),
        migrations.AlterField(
            model_name='notas',
            name='aluno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.Aluno'),
        ),
    ]
