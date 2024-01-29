from django.db.models import Count
from django.http import Http404
from rest_framework import status, permissions, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project
from .serializers import ProjectSerializer
from drf_api.permissions import IsOwnerOrReadOnly


# plural projects
class ProjectList(APIView):
    serializer_class = ProjectSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
#        projects = Project.objects.all()
        projects = Project.objects.annotate(
            watch_proj_count=Count(
                'watching_project', distinct=True
            ),
        ).order_by('-created_at')
        # unsolved: filter options don't appear
        filter_backends = [
            filters.OrderingFilter
        ]
        ordering_fields = [
            'watch_project_count',
        ]
        serializer = ProjectSerializer(
            projects, many=True, context={'request': request}
        )
        return Response(serializer.data)
    

    def post(self, request):
        serializer = ProjectSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


# singular project
class ProjectDetail(APIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            project = Project.objects.get(pk=pk)
            self.check_object_permissions(self.request, project)
            return project
        except Project.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        # unsolved: cannot show watching counter
        project = self.get_object(pk)
        serializer = ProjectSerializer(
            project, context={'request': request}
        )
        return Response(serializer.data)
    
    def put(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectSerializer(
            project, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        project = self.get_object(pk)
        project.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )