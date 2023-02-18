from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from .models import Project, ToDo
from .serializers import ProjectModelSerializer, ToDoModelSerializer
from .filters import ProjectFilter


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = ProjectLimitOffsetPagination
    filterset_class = ProjectFilter


class ToDoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class ToDoModelViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer
    filterset_fields = ['project']
    pagination_class = ToDoLimitOffsetPagination

    def destroy(self, request, *args, **kwargs):
        todo_note = self.get_object()
        todo_note.active = False
        todo_note.save()
        serializer_context = {
            'request': request,
        }
        serializer = ToDoModelSerializer(todo_note, context=serializer_context)
        return Response(serializer.data)
