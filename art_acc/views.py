from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ArtAccount
from .serializers import ArtAccountSerializer


class ArtAccountList(APIView):
    def get(self, request):
        artaccount = ArtAccount.objects.all()
        serializer = ArtAccountSerializer(artaccount, many=True)
        return Response(serializer.data)
