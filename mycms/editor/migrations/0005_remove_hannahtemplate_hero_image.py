# Generated by Django 4.1 on 2022-08-23 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0004_hannahtemplate_about_paragragh_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hannahtemplate',
            name='hero_image',
        ),
    ]
