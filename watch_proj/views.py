from django.http import Http404
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from watch_proj.models import WatchProject
from watch_proj.serializers import WatchProjectSerializer
from drf_api.permissions import IsOwnerOrReadOnly


#plural watch projects
class WatchProjectList(APIView):
    serializer_class = WatchProjectSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = WatchProject.objects.all()

    def get(self, request):
        watchproject = WatchProject.objects.all()
        serializer = WatchProjectSerializer(
            watchproject, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchProjectSerializer(
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
    

# singular watch projects
class WatchProjectDetail(APIView):
    serializer_classes = WatchProjectSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = WatchProject.objects.all()

    def get_object(self, pk):
        try:
            watchproject = WatchProject.objects.get(pk=pk)
            self.check_object_permissions(self.request, watchproject)
            return watchproject
        except WatchProject.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        watchproject = self.get_object(pk)
        serializer = WatchProjectSerializer(
            watchproject, context={'request': request}
        )
        return Response(serializer.data)

    def delete(self, request, pk):
        watchproject = self.get_object(pk)
        watchproject.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
