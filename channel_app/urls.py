from django.urls import path

from channel_app.views import get_all_channels_json

urlpatterns = [
    path("channels/", get_all_channels_json, name="get_all_channels_json")
]
