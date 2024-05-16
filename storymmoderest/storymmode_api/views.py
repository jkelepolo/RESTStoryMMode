from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from .models import Location, Character, Item, OpenAiUser
from .serializers import LocationSerializer, CharacterSerializer, ItemSerializer, OpenAiUserSerializer
from .filters import LocationFilter, CharacterFilter, ItemFilter, OpenAiUserFilter

def get_openai_info(request):
    return JsonResponse({
        "Openai-Ephemeral-User-Id": request.headers.get("Openai-Ephemeral-User-Id"),
        "Openai-Conversation-Id": request.headers.get("Openai-Conversation-Id"),
        "Openai-Gpt-Id": request.headers.get("Openai-Gpt-Id")
    })

class LocationViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAdminUser]
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = LocationFilter

class CharacterViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAdminUser]
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CharacterFilter

class ItemViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAdminUser]
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ItemFilter

class OpenAiUserViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAdminUser]
    queryset = OpenAiUser.objects.all()
    serializer_class = OpenAiUserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = OpenAiUserFilter