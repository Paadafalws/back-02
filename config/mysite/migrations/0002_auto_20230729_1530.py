# Generated by Django 3.2.6 on 2023-07-29 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quadro',
            name='Quadrofoto',
            field=models.FileField(blank=True, default='', upload_to=''),
        ),
        migrations.AlterField(
            model_name='quadro',
            name='Quadro',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]