# views.py
import string
import random

from django.contrib.auth.decorators import login_required
from rest_framework import generics, permissions
from .models import Link
from .serializers import LinkSerializer
import logging
import json
import requests
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from jwt_project.credentials import TELEGRAM_API_URL
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import UserProfile
from rest_framework import status
from django.shortcuts import render

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


def index(request):
    return render(request, 'index.html')


@login_required
def generate_telegram_setup_code(request):
    profile = UserProfile.objects.get_or_create(user=request.user)[0]
    if profile.telegram_id != "":
        return HttpResponse("", status=status.HTTP_200_OK)
    code = ''.join(random.choices(string.ascii_lowercase + string.digits, k=16))
    profile.telegram_setup_code = code
    profile.save()
    return HttpResponse(code, status=status.HTTP_200_OK)
