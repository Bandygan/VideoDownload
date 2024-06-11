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
