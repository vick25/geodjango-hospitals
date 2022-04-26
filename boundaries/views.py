import imp
from django.shortcuts import render
from rest_framework import viewsets
from .models import Boundary
from .serializers import BoundarySerializer

# Create your views here.
class BoundaryViewset(viewsets.ModelViewSet):
    queryset = Boundary.objects.all()
    serializer_class = BoundarySerializer
