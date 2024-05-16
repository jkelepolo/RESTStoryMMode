from rest_framework import serializers
from .models import Location, Character, Item, OpenAiUser

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name', 'description', 'meta_description', 'tags']

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['id', 'name', 'description', 'meta_description', 'tags']

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'meta_description', 'tags']

class OpenAiUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpenAiUser
        fields = ['id', 'related_user_ids', 'related_conversation_ids', 'inventory', 'info']