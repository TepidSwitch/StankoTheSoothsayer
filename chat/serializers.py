from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Conversation, ChatMessage

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
        
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class ChatMessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ChatMessage
        fields = '__all__'

class ConversationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Conversation
        fields= '__all__'