# Generated by Django 3.2.7 on 2021-10-20 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Curriculum', '0003_rename_conocimientos_ingles_cv_conocimientos_de_inglés'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cv',
            old_name='Apellido',
            new_name='apellido',
        ),
        migrations.RenameField(
            model_name='cv',
            old_name='Conocimientos_de_Inglés',
            new_name='conocimientos_de_ingles',
        ),
        migrations.RenameField(
            model_name='cv',
            old_name='Conocimientos_Laborales_Previos',
            new_name='conocimientos_laborales_previos',
        ),
        migrations.RenameField(
            model_name='cv',
            old_name='Domicilio',
            new_name='domicilio',
        ),
        migrations.RenameField(
            model_name='cv',
            old_name='Edad',
            new_name='edad',
        ),
        migrations.RenameField(
            model_name='cv',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='cv',
            old_name='Estudios_o_Títulos',
            new_name='estudios_o_titulos',
        ),
        migrations.RenameField(
            model_name='cv',
            old_name='Nombre',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='cv',
            old_name='Perfil',
            new_name='perfil',
        ),
        migrations.RemoveField(
            model_name='cv',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='cv',
            name='published_date',
        ),
        migrations.AlterField(
            model_name='cv',
            name='Telefono',
            field=models.CharField(max_length=20),
        ),
    ]
