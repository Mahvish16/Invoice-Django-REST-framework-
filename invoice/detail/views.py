from django.shortcuts import render
from rest_framework import viewsets
from .models import Invoice,InvoiceDetail
from .serializers import  invoiceSerializer,invoicedetailSerializer
# Create your views here.
class InvoiceViewset(viewsets.ModelViewSet):
    queryset= Invoice.objects.all()
    serializer_class = invoiceSerializer

class detailViewset(viewsets.ModelViewSet):
    queryset=InvoiceDetail.objects.all()
    serializer_class=invoicedetailSerializer