# Generated by Django 2.2.1 on 2019-06-06 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devlocl', '0003_auto_20190604_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disponibilidad',
            name='horas_disponer',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='peticion',
            name='horas_adicion',
            field=models.FloatField(null=True),
        ),
    ]
