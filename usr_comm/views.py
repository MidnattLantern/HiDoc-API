from django.http import Http404
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserComment
from .serializers import UserCommentSerializer
from drf_api.permissions import IsOwnerOrReadOnly


#plural user comments
class UserCommentList(APIView):
    serializer_class = UserCommentSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = UserComment.objects.all()

    def get(self, request):
        usercomments = UserComment.objects.all()
        serializer = UserCommentSerializer(
            usercomments, many=True, context={'request': request}
        )
        return Response(serializer.data)
    

    def post(self, request):
        serializer = UserCommentSerializer(
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


#singular user comments
class UserCommentDetail(APIView):
    serializer_class = UserCommentSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = UserComment.objects.all()

    def get_object(self, pk):
        try:
            usercomment = UserComment.objects.get(pk=pk)
            self.check_object_permissions(self.request, usercomment)
            return usercomment
        except UserComment.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        usercomment = self.get_object(pk)
        serializer = UserCommentSerializer(
            usercomment, context={'request': request}
        )
        return Response(serializer.data)
    
    def put(self, request, pk):
        usercomment = self.get_object(pk)
        serializer = UserCommentSerializer(
            usercomment, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        usercomment = self.get_object(pk)
        usercomment.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
