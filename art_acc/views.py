from django.db.models import Count
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ArtAccount
from .serializers import ArtAccountSerializer
from drf_api.permissions import IsOwnerOrReadOnly


# plural accounts
class ArtAccountList(APIView):
    def get(self, request):
        artaccounts = ArtAccount.objects.annotate(
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
        serializer = ArtAccountSerializer(
            artaccounts, many=True, context={'request': request}
        )
        return Response(serializer.data)


# singular account
class ArtAccountDetail(APIView):
    serializer_class = ArtAccountSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            artaccount = ArtAccount.objects.get(pk=pk)
            self.check_object_permissions(self.request, artaccount)
            return artaccount
        except ArtAccount.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        artaccount = self.get_object(pk)
        serializer = ArtAccountSerializer(
            artaccount, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        artaccount = self.get_object(pk)
        serializer = ArtAccountSerializer(
            artaccount, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)