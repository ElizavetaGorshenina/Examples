# Generated by Django 4.1.4 on 2023-02-09 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_alter_todo_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='link_to_repo',
            field=models.CharField(max_length=256),
        ),
    ]