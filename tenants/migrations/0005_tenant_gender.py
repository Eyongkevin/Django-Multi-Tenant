# Generated by Django 3.2.7 on 2021-09-25 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenants', '0004_alter_tenant_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenant',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=50),
        ),
    ]