# Generated by Django 4.0.5 on 2022-06-10 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sheets', '0005_gametemplate_generator_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='charactersheet',
            name='player',
        ),
    ]
