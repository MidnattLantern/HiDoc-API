from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .models import Documentation
from .serializers import DocumentationSerializer
from .serializers import DocumentationDetailSerializer


class DocumentationList(generics.ListCreateAPIView):
    """
    plural documentation objects
    filterset backends to "project", without this, every documentation
    on HiDoc would appear on strangers projects
    """
    serializer_class = DocumentationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Documentation.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['project']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DocumentationDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    singular documentation object
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = DocumentationDetailSerializer
    queryset = Documentation.objects.all()
