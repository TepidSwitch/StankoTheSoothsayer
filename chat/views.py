from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from .models import ChatMessage, Conversation
from .serializers import GroupSerializer, UserSerializer, ChatMessageSerializer, ConversationSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ConversationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows conversations to be viewed or edited.
    """
    queryset = Conversation.objects.all().order_by('id')
    serializer_class = ConversationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class ChatMessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows chat messages to be viewed.
    """
    queryset = ChatMessage.objects.all().order_by('id')
    serializer_class = ChatMessageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]