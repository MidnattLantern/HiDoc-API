from django.http import Http404
from rest_framework import status, permissions, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from watch_proj.models import WatchProject
from watch_proj.serializers import WatchProjectSerializer
from drf_api.permissions import IsOwnerOrReadOnly


class WatchProjectList(generics.ListCreateAPIView):
    """
    plural watch projects
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = WatchProjectSerializer
    queryset = WatchProject.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    

class WatchProjectDetail(generics.RetrieveDestroyAPIView):
    """
    singular watch project
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = WatchProjectSerializer
    queryset = WatchProject.objects.all()