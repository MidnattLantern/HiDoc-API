# Generated by Django 3.2.23 on 2024-02-10 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documentation', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documentation',
            name='paragraph',
        ),
    ]
