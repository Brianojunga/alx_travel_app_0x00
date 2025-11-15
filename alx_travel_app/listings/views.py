from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Listing
from .serializers import ListingSerializer

class ListingAPIView(APIView):
    def get(self, request):
        listings = Listing.objects.all()
        serializer = ListingSerializer(listings, many=True)
        return Response(serializer.data)
