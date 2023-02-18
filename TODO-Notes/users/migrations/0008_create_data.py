from django.db import migrations, models
import uuid


def create_data(apps, schema_editor):
    User = apps.get_model('users', 'User')
    User(username='Max', firstname='Maxim', lastname='Antipov', email='max_antipov@gmail.com').save()
    User(username='Innes', firstname='Inna', lastname='Belskaya', email='innes@mail.ru').save()
    Project = apps.get_model('todo', 'Project')
    user1 = User.objects.get(email='max_antipov@gmail.com')
    user2 = User.objects.get(email='innes@mail.ru')
    project1 = Project.objects.create(name='Group Project', link_to_repo='link_to_group_project')
    project1.user.add(user1)
    project1.user.add(user2)
    project1.save()
    project2 = Project.objects.create(name='Home Study', link_to_repo='link_to_home_study_project')
    project2.user.add(user2)
    project2.save()
    ToDo = apps.get_model('todo', 'ToDo')
    todo1 = ToDo.objects.create(project=project1, text='To make presentation', user=user1)
    todo1.save()
    todo2 = ToDo.objects.create(project=project2, text='To watch the educational video', user=user2)
    todo2.save()


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_user_email'),
        ('todo', '0005_alter_todo_project'),
    ]

    operations = [
        migrations.RunPython(create_data),
    ]
