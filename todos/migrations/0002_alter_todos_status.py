# Generated by Django 5.1.5 on 2025-02-22 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todos',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
