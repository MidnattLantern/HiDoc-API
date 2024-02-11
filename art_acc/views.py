from django.db.models import Count
from django.http import Http404
from rest_framework import status, generics, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ArtAccount
from .serializers import ArtAccountSerializer
from drf_api.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


class ArtAccountList(generics.ListAPIView):
    """
    Plural Accounts
    """
    queryset = ArtAccount.objects.annotate(
        projects_count=Count(
            'owner__project', disctinct=True
        ),
        watchers_art_count=Count(
            'owner__account_watched', disctinct=True
        ),
        watching_art_count=Count(
            'owner__watching_artist', disctinct=True
        ),
    ).order_by('-created_at')
    serializer_class = ArtAccountSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    ordering_fields = [
            'projects_count',
    ]


class ArtAccountDetail(generics.RetrieveAPIView):
    """
    Singular art account
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = ArtAccount.objects.annotate(
        projects_count=Count(
            'owner__project', disctinct=True
        ),
        watchers_art_count=Count(
            'owner__account_watched', disctinct=True
        ),
        watching_art_count=Count(
            'owner__watching_artist', disctinct=True
        ),
    ).order_by('-created_at')
    serializer_class = ArtAccountSerializer
