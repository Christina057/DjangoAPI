from rest_framework import viewsets
from .models import Invoice
from .serializers import InvoiceSerializer
from django.shortcuts import redirect
from django.views import View
from django.urls import reverse_lazy

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
class InvoiceListRedirectView(View):
    def get(self, request, *args, **kwargs):
        return redirect(reverse_lazy('invoice-list'))
