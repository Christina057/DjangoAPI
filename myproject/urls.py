from django.contrib import admin
from django.urls import path, include
from appname.views import InvoiceListRedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('appname.urls')),
    path('', InvoiceListRedirectView.as_view(), name='root-redirect'),
]
