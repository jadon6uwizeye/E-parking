# Generated by Django 3.1.5 on 2021-02-18 09:06

from django.db import migrations
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0002_auto_20210218_0442'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='location',
            field=location_field.models.plain.PlainLocationField(max_length=63, null=True),
        ),
    ]
