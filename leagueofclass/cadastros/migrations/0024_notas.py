# Generated by Django 2.1.1 on 2018-10-05 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0023_remove_frequencia_disciplina'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aluno', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cadastros.Aluno')),
            ],
            options={
                'verbose_name_plural': 'Notas',
            },
        ),
    ]
