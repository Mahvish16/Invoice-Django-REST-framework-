from django.db import models

# Create your models here.
class Invoice(models.Model):
    Date = models.DateField(auto_now=True)
    Invoice = models.TextField(max_length=50,null=True)
    CustomerName = models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.Invoice
    

class InvoiceDetail(models.Model):
    invoice= models.ForeignKey(Invoice, on_delete=models.CASCADE)
    description=  models.CharField(max_length=50)
    quantity = models.IntegerField(null=True)
    unit_price = models.DecimalField(max_digits=19, decimal_places=10, blank=False)
    price= models.IntegerField(null=True)
    def __str__(self):
        return self.invoice
