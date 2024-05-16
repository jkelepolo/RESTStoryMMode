from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Default custom user model for StoryMModeREST.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    name = models.CharField(_("Nickname"), blank=True, max_length=255)
    first_name = None  # type: ignore[assignment]
    last_name = None  # type: ignore[assignment]

    theme = models.ForeignKey(
        'Theme',
        on_delete=models.SET_NULL,
        null=True,
    )

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})

class Theme(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default="")

    primary_color = models.CharField(max_length=255, default="#4d6fa9")
    secondary_color = models.CharField(max_length=255, default="#253447")
    accent_color = models.CharField(max_length=255, default="#76a8d4")
    success_color = models.CharField(max_length=255, default="#00a896")
    info_color = models.CharField(max_length=255, default="#118ab2")
    warning_color = models.CharField(max_length=255, default="#ff8c00")
    danger_color = models.CharField(max_length=255, default="#e71d36")
    background_color = models.CharField(max_length=255, default="#f4f7fc")
    text_color = models.CharField(max_length=255, default="#333333")
    primary_hover_color = models.CharField(max_length=255, default="#3c5984")
    secondary_hover_color = models.CharField(max_length=255, default="#1e293d")
    accent_hover_color = models.CharField(max_length=255, default="#648fb8")
    success_hover_color = models.CharField(max_length=255, default="#009980")
    info_hover_color = models.CharField(max_length=255, default="#0e708b")
    warning_hover_color = models.CharField(max_length=255, default="#e67600")
    danger_hover_color = models.CharField(max_length=255, default="#c61a2b")

    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    default = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
