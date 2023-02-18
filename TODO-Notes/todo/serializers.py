from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Project, ToDo
from users.serializers import UserModelSerializer
from users.models import User
from drf_writable_nested import WritableNestedModelSerializer


class ProjectModelSerializer(HyperlinkedModelSerializer, 
                                WritableNestedModelSerializer):
    user = UserModelSerializer(many=True)

    class Meta:
        model = Project
        fields = '__all__'


class ProjectForToDoModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'link_to_repo']


class UserForToDoModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class ToDoModelSerializer(HyperlinkedModelSerializer,
                            WritableNestedModelSerializer):
    user = UserForToDoModelSerializer()
    project = ProjectForToDoModelSerializer()
    
    class Meta:
        model = ToDo
        fields = '__all__'
