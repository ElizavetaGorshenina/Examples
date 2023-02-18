import graphene
from graphene_django import DjangoObjectType
from users.models import User
from todo.models import Project, ToDo


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'

 
class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'       


class ToDoType(DjangoObjectType):
    class Meta:
        model = ToDo
        fields = '__all__'


class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)
    all_projects = graphene.List(ProjectType)
    all_todoes = graphene.List(ToDoType)
    users_by_project = graphene.List(UserType, name=graphene.String(required=False))

    def resolve_all_users(root, info):
        return User.objects.all()
    
    def resolve_all_projects(root, info):
        return Project.objects.all()

    def resolve_all_todoes(root, info):
        return ToDo.objects.all()

    def resolve_users_by_project(root, info, name=None):
        users = User.objects.all()
        if name:
            try:
                project = Project.objects.get(name=name)
                users = project.user.all()                
            except Project.DoesNotExist:
                return None
        return users


schema = graphene.Schema(query=Query)
