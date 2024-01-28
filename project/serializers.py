from rest_framework import serializers
from project.models import Project
from watch_proj.models import WatchProject


class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    art_acc_id = serializers.ReadOnlyField(source='owner.profile.id')
    art_acc_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    watch_proj_id = serializers.SerializerMethodField()

    # limit to image size
    def validate_image(self, value):
        if value.size > 1024 * 1024:
            raise serializers.ValidationError(
                'Image size larger than 1MB'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_watch_proj_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            watchproj = WatchProject.objects.filter(
                owner=user, project=obj
            ).first()
            return watchproj.id if watchproj else None
        return None
    
    class Meta:
        model = Project
        fields = [
            # id is created automatically
            'id', 'owner', 'created_at', 'updated_at',
            'project_title', 'project_description',
            'feature_poster', 'art_acc_id', 'art_acc_image',
            'is_owner', 'watch_proj_id'
        ]
