# views.py

from rest_framework import generics, permissions
from .models import Link
from .serializers import LinkSerializer
import logging

logger = logging.getLogger(__name__)

class LinkListCreateView(generics.ListCreateAPIView):
    serializer_class = LinkSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        try:
            return Link.objects.filter(user=self.request.user)
        except Exception as e:
            logger.error(f"Error fetching queryset: {e}")
            raise

    def perform_create(self, serializer):
        try:
            serializer.save(user=self.request.user)
        except Exception as e:
            logger.error(f"Error saving link: {e}")
            raise

class LinkDestroyView(generics.DestroyAPIView):
    serializer_class = LinkSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        try:
            return Link.objects.filter(user=self.request.user)
        except Exception as e:
            logger.error(f"Error fetching queryset: {e}")
            raise



import json
import requests
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from jwt_project.credentials import TELEGRAM_API_URL

@csrf_exempt
def telegram_bot(request):
  if request.method == 'POST':
    message = json.loads(request.body.decode('utf-8'))
    chat_id = message['message']['chat']['id']
    text = message['message']['text']
    send_message("sendMessage", {
      'chat_id': f'your message {text}'
    })
  return HttpResponse('ok')

def send_message(method, data):
  return requests.post(TELEGRAM_API_URL + method, data)




from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import UserProfile
from rest_framework import status


from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


class BindTelegramView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        user_profile, created = UserProfile.objects.get_or_create(user=user)
        user_profile.telegram_chat_id = None  # Reset chat ID
        user_profile.save()
        # Send a message to the user to start the bot and get the chat ID
        message = "Please start the Telegram bot and use /start command to complete the binding process."
        return Response({'message': message}, status=status.HTTP_200_OK)
