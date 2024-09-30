from rest_framework import serializers
from django.contrib.auth.models import User
from .models import client
from .models import Project


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password', 'first_name', 'last_name']
        extra_kwargs={
            'password':{'write_only':True}
        }

        def create(self, validate_data):
            return User.objects.create(**validate_data)


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)
    class Meta:
        model = User
        fields = ['email', 'password']

class clientserializer(serializers.Serializer):
    client_name = serializers.CharField(max_length=100)
    created_at = serializers.DateTimeField()
    created_by = serializers.CharField(max_length=100)

    def create(self,validate_data):
        return client.objects.create(**validate_data)

class ProjectSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'users', 'created_at', 'created_by']



#add update method in studentserializer class

def update(self, instance, validated_data):
    instance.client_name = validated_data.get('client_name', instance.client_name)
    instance.created_by = validated_data.get('created_by', instance.created_by)
    instance.save()
    return instance
