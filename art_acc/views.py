from django.db.models import Count
from django.http import Http404
from rest_framework import status, generics, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ArtAccount
from .serializers import ArtAccountSerializer
from drf_api.permissions import IsOwnerOrReadOnly


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
        filters.OrderingFilter
    ]
    ordering_fields = [
            'projects_count',
            'watchers_art_count',
            'watching_art_count,',
            'owner__watching_artist__created_at',
            'owner__account_watched__created_at',
    ]

"""
    def get(self, request):
        art_account = ArtAccount.objects.all()
        serializer = ArtAccountSerializer(
            art_account, many=True, context={'request': request}
        )
        return Response(serializer.data)
"""


class ArtAccountDetail(generics.RetrieveAPIView):
    """
    Singular art account
    """
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


    def get_object(self, pk):
        try:
            art_account = ArtAccount.objects.get(pk=pk)
            self.check_object_permissions(self.request, art_account)
            return art_account
        except ArtAccount.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        art_account = self.get_object(pk)
        serializer = ArtAccountSerializer(
            art_account, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        art_account = self.get_object(pk)
        serializer = ArtAccountSerializer(
            art_account, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
