# Generated by Django 2.1.1 on 2018-10-05 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0019_remove_disciplinas_nomedisciplina'),
    ]

    operations = [
        migrations.AddField(
            model_name='disciplinas',
            name='nomeDisciplina',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
