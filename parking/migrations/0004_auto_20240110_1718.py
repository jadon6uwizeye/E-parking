# Generated by Django 3.1.5 on 2024-01-10 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0003_auto_20240110_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='duration_in_minutes',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
