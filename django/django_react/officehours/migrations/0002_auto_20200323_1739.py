# Generated by Django 3.0.3 on 2020-03-23 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officehours', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='allDay',
        ),
        migrations.AlterField(
            model_name='event',
            name='classNum',
            field=models.CharField(max_length=100, verbose_name='CSE 442'),
        ),
        migrations.AlterField(
            model_name='event',
            name='endTime',
            field=models.CharField(max_length=100, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='event',
            name='startTime',
            field=models.CharField(max_length=100, verbose_name=''),
        ),
    ]
