# Generated by Django 3.2.7 on 2021-09-20 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20210904_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='question',
            field=models.CharField(max_length=150),
        ),
    ]