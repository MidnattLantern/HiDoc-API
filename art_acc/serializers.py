from rest_framework import serializers
from .models import ArtAccount
from watch_art.models import WatchArtist


class ArtAccountSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    watching_art_id = serializers.SerializerMethodField()
    # test
    projects_count = serializers.ReadOnlyField()
    watchers_art_count = serializers.ReadOnlyField()
    watching_art_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_watching_art_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            watching_artist = WatchArtist.objects.filter(
                owner=user, watched=obj.owner
            ).first()
#            print("watching:", watching_artist)
            return watching_artist.id if watching_artist else None
        return None

    class Meta:
        model = ArtAccount
        fields = [
            # id is created automatically
            'id', 'owner', 'created_at', 'updated_at',
            'name', 'content', 'image', 'is_owner',
            'watching_art_id',
            'projects_count', 'watchers_art_count', 'watching_art_count',
        ]
