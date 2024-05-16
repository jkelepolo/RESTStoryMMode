from django.db import models
from django.conf import settings
from storymmoderest.users.models import User, Theme

def theme_colors(request):
    
    theme = None
    try:
        theme = Theme.objects.filter(default=True).first()
    except Theme.DoesNotExist:
        theme = Theme.objects.filter().first()


    if request.user.is_authenticated:
        current_user = User.objects.get(pk=request.user.pk)
        if current_user.theme:
            theme = current_user.theme
    
    color_context = {
        'primary_color': theme.primary_color,
        'secondary_color': theme.secondary_color,
        'accent_color': theme.accent_color,
        'success_color': theme.success_color,
        'info_color': theme.info_color,
        'warning_color': theme.warning_color,
        'danger_color': theme.danger_color,
        'background_color': theme.background_color,
        'text_color': theme.text_color,
        'primary_hover_color': theme.primary_hover_color,
        'secondary_hover_color': theme.secondary_hover_color,
        'accent_hover_color': theme.accent_hover_color,
        'success_hover_color': theme.success_hover_color,
        'info_hover_color': theme.info_hover_color,
        'warning_hover_color': theme.warning_hover_color,
        'danger_hover_color': theme.danger_hover_color
    }
    return color_context