# Generated by Django 3.2.6 on 2023-07-30 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_auto_20230729_1702'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('feita', models.BooleanField(default=False)),
            ],
        ),
    ]
