from django.contrib import admin
from principal.models import *

# Register your models here.

class ProdutosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')


admin.site.register (Categoria)
admin.site.register (Produto, ProdutosAdmin)
admin.site.register (Cliente)
admin.site.register (Colaborador)
admin.site.register (CarrinhoCompras)
