from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ArtAccount
from .serializers import ArtAccountSerializer


# plural account
class ArtAccountList(APIView):
    def get(self, request):
        artaccounts = ArtAccount.objects.all()
        serializer = ArtAccountSerializer(artaccounts, many=True)
        return Response(serializer.data)


# singular account
class ArtAccountDetail(APIView):
    serializer_class = ArtAccountSerializer
    def get_object(self, pk):
        try:
            artaccount = ArtAccount.objects.get(pk=pk)
            return artaccount
        except ArtAccount.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        artaccount = self.get_object(pk)
        serializer = ArtAccountSerializer(artaccount)
        return Response(serializer.data)

    def put(self, request, pk):
        artaccount = self.get_object(pk)
        serializer = ArtAccountSerializer(artaccount, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)