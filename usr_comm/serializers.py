from rest_framework import serializers
from .models import UserComment


class UserCommentSerializer(serializers.ModelSerializer):
    """
    unused feature
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    # from account_id to art_acc_id
    art_acc_id = serializers.ReadOnlyField(source='owner.profile.id')
    # from account_img to art_acc_img
    art_acc_img = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    
    class Meta:
        model = UserComment
        fields = [
            'id', 'owner', 'is_owner', 'art_acc_id', 'art_acc_img',
            'project', 'created_at', 'updated_at', 'comment',
        ]


class UserCommentDetailSerializer(UserCommentSerializer):
    """
    Obligatory docstring
    """
    post = serializers.ReadOnlyField(source='post.id')