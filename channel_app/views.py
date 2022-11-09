import json

from django.http import JsonResponse

from channel_app.models import Channel


def get_all_channels_json(request, since=-15, to=6):

    unload_data = {}
    all_channels = Channel.objects.all()

    for _ in all_channels:
        channels = [
            {"id": str(channel.id), "title": channel.title, "icon": str(channel.icon)}
            for channel in all_channels
        ]
        unload_data["channels"] = channels

    with open("channels.json", "w") as file:
        json.dump(unload_data, file, indent=2, ensure_ascii=False)

    return JsonResponse(unload_data, safe=False)
