# Generated by Django 3.0.3 on 2020-04-06 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officehours', '0002_auto_20200323_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='instructor',
            field=models.CharField(default='Andyboi', max_length=100000000, verbose_name='Andyboi'),
        ),
        migrations.AddField(
            model_name='event',
            name='owner',
            field=models.EmailField(default='a@a.com', max_length=254, verbose_name='a@a.com'),
        ),
    ]
