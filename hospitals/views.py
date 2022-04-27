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

    @action(detail=False, methods=["get"])
    def province_beds_capacity(self, request):
        province_bed_capacity = Hospital.objects.values("province_name").annotate(
            bed_capacity=Sum("beds")
        )
        return Response(province_bed_capacity)
