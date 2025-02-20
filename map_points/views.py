from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import MapPointSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import MapPoints


class MapPointViewSet(viewsets.ModelViewSet):
    queryset = MapPoints.objects.all()
    serializer_class = MapPointSerializer
    permission_classes = [IsAuthenticated]  # Use session authentication


def map_view(request):
    return render(request, 'map.html')


@api_view(['GET'])
@permission_classes([AllowAny])
def search_points(request):
    query = request.GET.get('search', '')
    if query:
        results = MapPoints.objects.filter(
            title__icontains=query
        ) | MapPoints.objects.filter(
            address__icontains=query
        ) | MapPoints.objects.filter(
            city__icontains=query
        )

        return Response([
            {
                "title": p.title, 
                "category": p.category, 
                "address": p.address, 
                "location": {"type": "Point", "coordinates": [p.location.x, p.location.y]}
            } 
            for p in results
        ])
    return Response([])