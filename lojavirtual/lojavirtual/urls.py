from django.contrib import admin
from django.urls import path, include
from loja.views import RoupasViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('roupas', RoupasViewSet, basename='Roupas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
