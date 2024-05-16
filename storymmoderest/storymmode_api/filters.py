import django_filters
from .models import Location, Character, Item, OpenAiUser

class LocationFilter(django_filters.FilterSet):
    class Meta:
        model = Location
        fields = {
            'name': ['exact', 'contains', 'icontains', 'iexact'],
            'description': ['exact', 'contains', 'icontains', 'iexact'],
            'meta_description': ['exact', 'contains', 'icontains', 'iexact'],
            'tags': ['exact', 'contains', 'icontains', 'iexact']
        }

class CharacterFilter(django_filters.FilterSet):
    class Meta:
        model = Character
        fields = {
            'name': ['exact', 'contains', 'icontains', 'iexact'],
            'description': ['exact', 'contains', 'icontains', 'iexact'],
            'meta_description': ['exact', 'contains', 'icontains', 'iexact'],
            'tags': ['exact', 'contains', 'icontains', 'iexact']
        }

class ItemFilter(django_filters.FilterSet):
    class Meta:
        model = Item
        fields = {
            'name': ['exact', 'contains', 'icontains', 'iexact'],
            'description': ['exact', 'contains', 'icontains', 'iexact'],
            'meta_description': ['exact', 'contains', 'icontains', 'iexact'],
            'tags': ['exact', 'contains', 'icontains', 'iexact']
        }

class OpenAiUserFilter(django_filters.FilterSet):
    class Meta:
        model = OpenAiUser
        fields = {
            'related_user_ids': ['exact', 'contains', 'icontains', 'iexact'],
            'related_conversation_ids': ['exact', 'contains', 'icontains', 'iexact'],
            'inventory': ['exact', 'contains', 'icontains', 'iexact'],
            'info': ['exact', 'contains', 'icontains', 'iexact']
        }