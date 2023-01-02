from django.contrib import admin
from django.urls import path
from loja.views import itens_loja

urlpatterns = [
    path('admin/', admin.site.urls),
    path('loja/', itens_loja),
]
