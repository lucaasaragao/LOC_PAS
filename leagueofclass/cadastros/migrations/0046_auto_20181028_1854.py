# Generated by Django 2.1.2 on 2018-10-28 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0045_remove_perguntasx_matricula_professor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perguntasx',
            name='atividade',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]