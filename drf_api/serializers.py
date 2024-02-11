from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


class CurrentUserSerializer(UserDetailsSerializer):
    artaccount_id = serializers.ReadOnlyField(source='artaccount.id')
    artaccount_image = serializers.ReadOnlyField(source='artaccount.image.url')

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            'artaccount_id', 'artaccount_image'
        )
