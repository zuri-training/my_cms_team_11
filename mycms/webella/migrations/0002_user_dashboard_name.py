# Generated by Django 4.1 on 2022-08-12 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webella', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_dashboard',
            name='name',
            field=models.CharField(default='hey', max_length=50, verbose_name=''),
        ),
    ]
