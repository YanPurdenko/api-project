import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class Program(models.Model):
    title = models.CharField(max_length=255)
    start = models.TimeField(auto_now=False, auto_now_add=False)
    end = models.TimeField(auto_now=False, auto_now_add=False)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "programs"
        ordering = ["title"]
        verbose_name = "program"
        verbose_name_plural = "programs"

    def __str__(self):
        return f"{self.title} (start: {self.start}, end: {self.end}, description: {self.description})"


class Channel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    icon = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    programs = models.ForeignKey(Program, null=True, on_delete=models.SET_NULL, related_name="channels")

    def __str__(self):
        return f"{self.id} (title: {self.title}, icon: {self.icon})"

    class Meta:
        db_table = "channels"
        ordering = ["title"]
        verbose_name = "channel"
        verbose_name_plural = "channels"


class Customer(AbstractUser):

    class Meta:
        db_table = "users"
        ordering = ["username"]
