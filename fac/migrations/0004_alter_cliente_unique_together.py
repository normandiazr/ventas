# Generated by Django 3.2.5 on 2021-07-29 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fac', '0003_auto_20190831_2250'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cliente',
            unique_together={('nombres', 'apellidos')},
        ),
    ]
