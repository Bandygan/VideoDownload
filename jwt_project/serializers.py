# serializers.py

from rest_framework import serializers
from .models import Link

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ['id', 'url', 'user', 'created_at', 'show_name']
        read_only_fields = ['user', 'created_at']
