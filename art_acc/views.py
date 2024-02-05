from django.db.models import Count
from django.http import Http404
from rest_framework import status, generics, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ArtAccount
from .serializers import ArtAccountSerializer
from drf_api.permissions import IsOwnerOrReadOnly


# plural accounts
class ArtAccountList(generics.ListAPIView):
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
        filters.OrderingFilter
    ]
    ordering_fields = [
            'projects_count',
            'watchers_art_count',
            'watching_art_count,',
            'owner__watching_artist__created_at',
            'owner__account_watched__created_at',
    ]


# singular account
class ArtAccountDetail(generics.RetrieveAPIView):
    #serializer_class = ArtAccountSerializer
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