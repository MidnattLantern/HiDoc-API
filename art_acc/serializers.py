from rest_framework import serializers
from .models import ArtAccount


class ArtAccountSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = ArtAccount
        fields = [
            # id is created automatically
            'id', 'owner', 'created_at', 'updated_at',
            'name', 'content', 'image', 'is_owner',
        ]
