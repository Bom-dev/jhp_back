from email.mime import application
from django.http import QueryDict
from rest_framework import serializers
from .models import User, Application, Interview, Event, Study, History

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'password', 'goal', 'start_date', 'end_date', 'applications', 'interviews', 'events', 'studies', 'histories')


class ApplicationSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    user_id = serializers.PrimaryKeyRelatedField(
        queryset = User.objects.all(),
        source = 'user'
    )
    class Meta:
        depth = 1
        model = Application
        fields = ('id', 'title', 'date', 'comment', 'user', 'user_id')
       
        
class InterviewSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    user_id = serializers.PrimaryKeyRelatedField(
        queryset = User.objects.all(),
        source = 'user'
    )
    class Meta:
        depth = 1
        model = Interview
        fields = ('id', 'title', 'date', 'comment', 'user', 'user_id')
        
        
class EventSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    user_id = serializers.PrimaryKeyRelatedField(
        queryset = User.objects.all(),
        source = 'user'
    )
    class Meta:
        depth = 1
        model = Event
        fields = ('id', 'title', 'date', 'comment', 'user', 'user_id')


class StudySerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    user_id = serializers.PrimaryKeyRelatedField(
        queryset = User.objects.all(),
        source = 'user'
    )
    class Meta:
        depth = 1
        model = Study
        fields = ('id', 'title', 'date', 'comment', 'user', 'user_id')
        

class HistorySerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    user_id = serializers.PrimaryKeyRelatedField(
        queryset = User.objects.all(),
        source = 'user'
    )
    class Meta:
        depth = 1
        model = History
        fields = ('id', 'start_date', 'end_date', 'applications', 'applications_number', 'interviews', 'events', 'studies', 'user_id')