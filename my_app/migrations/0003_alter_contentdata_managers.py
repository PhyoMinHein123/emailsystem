# Generated by Django 3.2 on 2024-02-13 16:25

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_contentdata'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='contentdata',
            managers=[
                ('people', django.db.models.manager.Manager()),
            ],
        ),
    ]
