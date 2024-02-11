from django.db import IntegrityError
from rest_framework import serializers
from .models import WatchProject


class WatchProjectSerializer(serializers.ModelSerializer):
    """
    serializer for watch project
    referenced from Code Institute Moments project
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = WatchProject
        fields = ['id', 'created_at', 'owner', 'project']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': "risk of project 'double-watching'"
            })
