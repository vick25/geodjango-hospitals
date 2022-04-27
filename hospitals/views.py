from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Hospital
from .serializers import HospitalSerializer

from django.db.models import Sum

# Create your views here.
class HospitalViewSet(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer

    @action(detail=False, methods=["get"])
    def total_bed_capacity(self, request):
        bed_capactiy = Hospital.objects.aggregate(bed_capactiy=Sum("beds"))
        return Response(bed_capactiy)
