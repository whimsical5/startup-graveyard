# Generated by Django 5.2 on 2025-05-07 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startups', '0003_startup_lessons_learned'),
    ]

    operations = [
        migrations.AddField(
            model_name='startup',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]
