# Generated by Django 3.2.7 on 2021-10-20 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Curriculum', '0006_cv_localidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='edad',
            field=models.PositiveBigIntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cv',
            name='telefono',
            field=models.IntegerField(max_length=20),
        ),
    ]
