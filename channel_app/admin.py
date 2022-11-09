from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from channel_app.models import Customer, Channel, Program


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ["title", "start", "end", "description"]
    search_fields = ["title"]


@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "programs"]
    search_fields = ["id", "title"]


@admin.register(Customer)
class CustomerAdmin(UserAdmin):
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("first_name", "last_name", "username")}),
    )
