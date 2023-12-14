# Generated by Django 4.0 on 2023-12-14 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome_cargo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('admissao', models.DateField()),
                ('id_cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.cargos')),
            ],
        ),
    ]