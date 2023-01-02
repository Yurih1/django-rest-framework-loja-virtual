from django.contrib import admin
from loja.models import Roupa

class Roupas(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao', 'modelo', 'tamanho')
    list_display_links = ('id', 'nome')
    list_per_page = 50
    search_fields = ('nome', 'modelo',)

admin.site.register(Roupa, Roupas)