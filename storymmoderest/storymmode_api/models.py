from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    meta_description = models.TextField()
    tags = models.TextField(default="")

    def __str__(self):
        return self.name

class Character(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    meta_description = models.TextField()
    tags = models.TextField(default="")

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    meta_description = models.TextField()
    tags = models.TextField(default="")

    def __str__(self):
        return self.name

class OpenAiUser(models.Model):
    related_user_ids = models.TextField(default="")
    related_conversation_ids = models.TextField(default="")
    inventory = models.TextField(default="", blank=True)
    info = models.TextField(default="", blank=True)

    def __str__(self):
        return "OpenAiUser"
