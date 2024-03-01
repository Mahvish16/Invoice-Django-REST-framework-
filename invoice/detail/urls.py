from django.contrib import admin
from django.urls import path,include
from .views import InvoiceViewset,detailViewset
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'invoices', InvoiceViewset)
router.register(r'read',detailViewset)

urlpatterns = [
    path('',include(router.urls))
    
  
   
]
