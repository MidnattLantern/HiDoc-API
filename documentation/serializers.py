from rest_framework import serializers
from .models import Documentation


class DocumentationSerializer(serializers.ModelSerializer):
    """
    serializer for documentaiton
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    art_acc_id = serializers.ReadOnlyField(source='owner.profile.id')

    def validate_image(self, value):
        if value.size > 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 1 MB')
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

    class Meta:
        model = Documentation
        fields = [
            'id', 'owner', 'is_owner', 'art_acc_id',
            'project', 'created_at', 'updated_at',
            'documentation_title', 'documentation_paragraph',
            'documentation_image',
        ]


class DocumentationDetailSerializer(DocumentationSerializer):
    """
    serializer for documentation detail view
    """
#    project = serializers.ReadOnlyField(source="project.id")
    project = serializers.ReadOnlyField(source="project.id")