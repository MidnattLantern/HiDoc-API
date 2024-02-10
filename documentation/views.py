from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Documentation
from .serializers import DocumentationSerializer
from .serializers import DocumentationDetailSerializer


class DocumentationList(generics.ListCreateAPIView):
    """
    plural documentation objects
    """
    serializer_class = DocumentationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Documentation.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DocumentationDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    singular documentation object
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = DocumentationDetailSerializer
    queryset = Documentation.objects.all()
