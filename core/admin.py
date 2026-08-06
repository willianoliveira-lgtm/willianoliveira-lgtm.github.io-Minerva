from django.contrib import admin

from .models import MensagemContato, Noticia


@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "categoria", "data")
    list_filter = ("categoria",)
    search_fields = ("titulo", "descricao")


@admin.register(MensagemContato)
class MensagemContatoAdmin(admin.ModelAdmin):
    list_display = ("nome", "email", "assunto", "enviado_em", "lida")
    list_filter = ("lida",)
    readonly_fields = ("nome", "email", "assunto", "mensagem", "enviado_em")
