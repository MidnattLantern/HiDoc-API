from django.http import Http404
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from watch_art.models import WatchArtist
from watch_art.serializers import WatchArtistSerializer
from drf_api.permissions import IsOwnerOrReadOnly


# plural watch artists
class WatchArtistList(APIView):
    serializer_class = WatchArtistSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = WatchArtist.objects.all()

    def get(self, request):
        watchartist = WatchArtist.objects.all()
        serializer = WatchArtistSerializer(
            watchartist, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchArtistSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


# singular watch artist
class WatchArtistDetail(APIView):
    serializer_classes = WatchArtistSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = WatchArtist.objects.all()

    def get_object(self, pk):
        try:
            watchartist = WatchArtist.objects.get(pk=pk)
            self.check_object_permissions(self.request, watchartist)
            return watchartist
        except WatchArtist.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        watchartist = self.get_object(pk)
        serializer = WatchArtistSerializer(
            watchartist, context={'request': request}
        )
        return Response(serializer.data)

    def delete(self, request, pk):
        watchartist = self.get_object(pk)
        watchartist.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
