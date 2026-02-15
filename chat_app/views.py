import json
from django.http import JsonResponse
from django.views import View
from chat_app.models import Chat


class Chat_View(View):

    def get(self, request):
        ChatDB = list(Chat.objects.values())
        return JsonResponse(ChatDB, safe=False)

    def post(self, request, *args, **kwargs):
        try:
            data = json.load(request.body)
            name = data.get('name')
            message = data.get('message')
            Chat.objects.create(name='name', message='message')
        except:
            print("Error")