from django.http import Http404
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
