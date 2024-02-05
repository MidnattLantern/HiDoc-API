from django.db.models import Count
from django.http import Http404
from rest_framework import status, permissions, filters, generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project
from .serializers import ProjectSerializer
from drf_api.permissions import IsOwnerOrReadOnly


# plural projects
class ProjectList(generics.ListCreateAPIView):
    """
    Obligatory Docstring
    """
    serializer_class = ProjectSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Project.objects.annotate(
        watch_proj_count=Count(
            'watching_project', distinct=True
        ),
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        # potential future feature: watching artists
#        'owner__watched__owner__artaccount',
        # projects appearing in watch project list
        'watching_project__owner__artaccount',
        # user projects
        'owner__artaccount',
    ]
    search_fields = [
        'owner__username',
        'project_title',
    ]
    ordering_fields = [
#        'watch_project_count',
        'created_at',
        'updated_at',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



# singular project
class ProjectDetail(generics.RetrieveAPIView):
    """
    Obligatory docstring
    """
    serializer_class = ProjectSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Project.objects.annotate(
        watch_proj_count=Count(
            'watching_project', distinct=True
        ),
    ).order_by('-created_at')
