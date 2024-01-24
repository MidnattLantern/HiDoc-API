from rest_framework import serializers
from .models import ArtAccount


class ArtAccountSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = ArtAccount
        fields = [
            # id is created automatically
            'id', 'owner', 'created_at', 'updated_at',
            'name', 'content', 'image',
        ]