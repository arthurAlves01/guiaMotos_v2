# Generated by Django 2.2.6 on 2019-11-30 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('motos', '0002_delete_buscafavorita'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favoritos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idUsuario', models.IntegerField()),
                ('fabricante', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('anoModelo', models.CharField(max_length=50)),
            ],
        ),
    ]
