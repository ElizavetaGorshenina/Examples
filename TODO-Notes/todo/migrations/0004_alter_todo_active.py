# Generated by Django 4.1.4 on 2023-02-09 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_alter_project_link_to_repo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]