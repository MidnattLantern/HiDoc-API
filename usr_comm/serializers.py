from rest_framework import serializers
from .models import UserComment


class UserCommentSerializer(serializers.ModelSerializer):
    """
    Obligatory docstring
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    account_id = serializers.ReadOnlyField(source='owner.profile.id')
    account_img = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    
    class Meta:
        model = UserComment
        fields = [
            'id', 'owner', 'is_owner', 'account_id', 'account_img',
            'project', 'created_at', 'updated_at', 'comment',
        ]


class UserCommentDetailSerializer(UserCommentSerializer):
    """
    Obligatory docstring
    """
    post = serializers.ReadOnlyField(source='post.id')