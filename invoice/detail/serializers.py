from rest_framework import serializers
from .models import Invoice,InvoiceDetail
class invoiceSerializer(serializers.HyperlinkedModelSerializer):
    Date = serializers.DateField(format="%d-%m-%Y", input_formats=['%d-%m-%Y', 'iso-8601'])

    class Meta:
        model=Invoice
        fields="__all__"

class invoicedetailSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model=InvoiceDetail
        fields="__all__"