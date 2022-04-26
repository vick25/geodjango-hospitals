import imp
from django.shortcuts import render
from rest_framework import viewsets
from .models import Boundary
from .serializers import BoundarySerializer

from django.contrib.gis.db.models.functions import Area

# Create your views here.
class BoundaryViewset(viewsets.ModelViewSet):
    queryset = Boundary.objects.all()
    serializer_class = BoundarySerializer

    def get_queryset(self):
        boundary_area = Boundary.objects.annotate(area=Area("mpoly")).order_by("area")
        return boundary_area
