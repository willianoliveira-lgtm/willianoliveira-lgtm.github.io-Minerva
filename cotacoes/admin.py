from django.contrib import admin

from .models import Comprovante, Compra, Cotacao, HistoricoEvento


class ComprovanteInline(admin.TabularInline):
    model = Comprovante
    extra = 0
    readonly_fields = ("enviado_em",)


class HistoricoInline(admin.TabularInline):
    model = HistoricoEvento
    extra = 0
    readonly_fields = ("data",)


@admin.register(Cotacao)
class CotacaoAdmin(admin.ModelAdmin):
    list_display = ("produto", "fornecedor", "projeto", "status", "total", "moeda", "criado_em")
    list_filter = ("status", "moeda")
    search_fields = ("produto", "fornecedor", "numero_interno", "projeto")


@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ("numero_compra", "produto", "fornecedor_escolhido", "status", "valor_final_pago", "data_compra")
    list_filter = ("status", "moeda")
    search_fields = ("produto", "fornecedor_escolhido", "numero_compra", "projeto")
    inlines = [ComprovanteInline, HistoricoInline]
