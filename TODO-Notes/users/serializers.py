from rest_framework.serializers import HyperlinkedModelSerializer
from .models import User


class UserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'firstname', 'lastname', 'email']


class UserModelSerializerV2(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'firstname', 'lastname', 'email', 'is_superuser', 'is_staff']
