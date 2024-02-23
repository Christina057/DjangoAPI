from django.urls import path
from .views import InvoiceViewSet

urlpatterns = [
    path('invoices/', InvoiceViewSet.as_view({'get': 'list', 'post': 'create'}), name='invoice-list'),
    path('invoices/<int:pk>/', InvoiceViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='invoice-detail'),
]
