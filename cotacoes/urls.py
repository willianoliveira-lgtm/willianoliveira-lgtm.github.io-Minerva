from django.urls import path

from . import views

app_name = "cotacoes"

urlpatterns = [
    path("", views.cotacao_index, name="index"),
    path("aprovacao/", views.aprovacao, name="aprovacao"),
    path("aprovacao/<int:pk>/decidir/", views.aprovar_cotacao, name="aprovar_cotacao"),
    path("compras/", views.compras, name="compras"),
    path("compras/<int:pk>/upload/", views.upload_comprovante, name="upload_comprovante"),
]
