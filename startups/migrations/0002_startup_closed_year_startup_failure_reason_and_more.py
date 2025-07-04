# Generated by Django 5.2 on 2025-05-06 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='startup',
            name='closed_year',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='startup',
            name='failure_reason',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='startup',
            name='industry',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
