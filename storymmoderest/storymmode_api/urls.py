from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LocationViewSet, CharacterViewSet, OpenAiUserViewSet, ItemViewSet, get_openai_info

router = DefaultRouter()
router.register(r'locations', LocationViewSet)
router.register(r'characters', CharacterViewSet)
router.register(r'openaiusers', OpenAiUserViewSet)
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('openai/', get_openai_info)
]
