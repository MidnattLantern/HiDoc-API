from django.db import IntegrityError
from rest_framework import serializers
from .models import WatchArtist


class WatchArtistSerializer(serializers.ModelSerializer):
    """
    A couple things were left out from the tutorial.
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = WatchArtist
        fields = ['id', 'created_at', 'owner', 'watched',]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': "risk of artist 'double-watching'"
            })