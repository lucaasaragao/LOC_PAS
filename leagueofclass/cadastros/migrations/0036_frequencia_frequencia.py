# Generated by Django 2.1.1 on 2018-10-06 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0035_auto_20181006_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='frequencia',
            name='frequencia',
            field=models.CharField(choices=[('P', 'Presente'), ('F', 'Faltou')], default=10, max_length=1),
            preserve_default=False,
        ),
    ]
