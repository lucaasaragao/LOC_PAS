# Generated by Django 2.1.1 on 2018-10-05 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0031_auto_20181005_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frequencia',
            name='data',
            field=models.DateField(),
        ),
    ]