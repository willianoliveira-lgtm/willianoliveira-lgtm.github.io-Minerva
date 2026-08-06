from django.conf import settings
from django.db import models
from django.urls import reverse


class Cotacao(models.Model):
    """Equivalente aos objetos 'quotations' mockados em
    app/restrito/cotacao/aprovacao/page.tsx"""

    STATUS_CHOICES = [
        ("pendente", "Pendente"),
        ("aprovado", "Aprovado"),
        ("reprovado", "Reprovado"),
        ("ressalva", "Aprovado com Ressalva"),
    ]

    MOEDA_CHOICES = [("USD", "USD"), ("EUR", "EUR"), ("BRL", "BRL")]

    # Dados do produto
    produto = models.CharField("Produto", max_length=200)
    tipo = models.CharField("Tipo", max_length=100, blank=True)
    quantidade = models.PositiveIntegerField("Quantidade", default=1)
    link = models.URLField("Link da especificação", blank=True)

    # Dados financeiros
    valor_unitario = models.DecimalField("Valor unitário", max_digits=14, decimal_places=2)
    moeda = models.CharField("Moeda", max_length=3, choices=MOEDA_CHOICES, default="USD")
    frete = models.DecimalField("Frete", max_digits=14, decimal_places=2, default=0)
    alfandega = models.DecimalField("Alfândega", max_digits=14, decimal_places=2, default=0)
    desconto = models.DecimalField("Desconto (%)", max_digits=5, decimal_places=2, default=0)
    total = models.DecimalField("Total", max_digits=14, decimal_places=2)

    # Fornecedor e projeto
    fornecedor = models.CharField("Fornecedor", max_length=150)
    numero_interno = models.CharField("Número interno", max_length=50, blank=True)
    projeto = models.CharField("Projeto", max_length=150, blank=True)

    # Prazos e condições
    prazo = models.CharField("Prazo de entrega", max_length=50, blank=True)
    condicoes_pagamento = models.CharField("Condições de pagamento", max_length=100, blank=True)
    data_recebimento = models.DateField("Data de recebimento", null=True, blank=True)
    validade_cotacao = models.DateField("Validade da cotação", null=True, blank=True)

    # Aprovação
    status = models.CharField("Status", max_length=20, choices=STATUS_CHOICES, default="pendente")
    justificativa = models.TextField("Justificativa da decisão", blank=True)
    observacoes = models.TextField("Observações", blank=True)
    data_aprovacao = models.DateField("Data da aprovação", null=True, blank=True)
    aprovado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name="Aprovado por",
        null=True, blank=True, on_delete=models.SET_NULL, related_name="cotacoes_aprovadas",
    )

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Cotação"
        verbose_name_plural = "Cotações"
        ordering = ["-criado_em"]

    def __str__(self):
        return f"{self.produto} — {self.fornecedor}"

    def get_absolute_url(self):
        return reverse("cotacoes:aprovacao")


class Compra(models.Model):
    """Equivalente aos objetos 'purchases' mockados em
    app/restrito/cotacao/compras/page.tsx. Nasce, opcionalmente, de uma
    Cotação aprovada."""

    STATUS_CHOICES = [
        ("comprado", "Comprado"),
        ("aguardando_nf", "Aguardando Nota Fiscal"),
        ("cancelado", "Cancelado"),
    ]

    cotacao = models.ForeignKey(
        Cotacao, verbose_name="Cotação de origem",
        null=True, blank=True, on_delete=models.SET_NULL, related_name="compras",
    )

    produto = models.CharField("Produto", max_length=200)
    quantidade = models.PositiveIntegerField("Quantidade", default=1)
    fornecedor_escolhido = models.CharField("Fornecedor escolhido", max_length=150)
    justificativa = models.TextField("Justificativa da escolha", blank=True)

    valor_final_pago = models.DecimalField("Valor final pago", max_digits=14, decimal_places=2)
    moeda = models.CharField("Moeda", max_length=3, choices=Cotacao.MOEDA_CHOICES, default="USD")
    condicoes_pagamento = models.CharField("Condições de pagamento", max_length=100, blank=True)

    numero_compra = models.CharField("Número da compra", max_length=50, blank=True)
    nota_fiscal = models.CharField("Nota fiscal", max_length=100, blank=True)
    data_compra = models.DateField("Data da compra")
    projeto = models.CharField("Projeto", max_length=150, blank=True)

    status = models.CharField("Status", max_length=20, choices=STATUS_CHOICES, default="aguardando_nf")
    observacoes = models.TextField("Observações", blank=True)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Compra"
        verbose_name_plural = "Compras"
        ordering = ["-data_compra"]

    def __str__(self):
        return f"{self.numero_compra or 'Compra'} — {self.produto}"

    def get_absolute_url(self):
        return reverse("cotacoes:compras")


class Comprovante(models.Model):
    """Equivalente ao array 'comprovantes' de cada compra — arquivos de
    verdade agora, gravados em disco/S3 pelo FileField do Django (a versão
    React só simulava o upload, sem realmente guardar o arquivo)."""

    TIPO_CHOICES = [
        ("pagamento", "Comprovante de pagamento"),
        ("certificado", "Certificado"),
        ("nota_fiscal", "Nota fiscal"),
        ("ordem", "Ordem de compra"),
        ("outro", "Outro documento"),
    ]

    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name="comprovantes")
    arquivo = models.FileField("Arquivo", upload_to="comprovantes/%Y/%m/")
    tipo = models.CharField("Tipo", max_length=20, choices=TIPO_CHOICES, default="outro")
    enviado_em = models.DateTimeField(auto_now_add=True)
    enviado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL,
    )

    class Meta:
        verbose_name = "Comprovante"
        verbose_name_plural = "Comprovantes"
        ordering = ["-enviado_em"]

    def __str__(self):
        return self.arquivo.name.rsplit("/", 1)[-1]


class HistoricoEvento(models.Model):
    """Equivalente ao array 'historicoNegociacao' de cada compra."""

    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name="historico")
    acao = models.CharField("Ação", max_length=150)
    observacao = models.TextField("Observação", blank=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    data = models.DateTimeField("Data", auto_now_add=True)

    class Meta:
        verbose_name = "Evento do histórico"
        verbose_name_plural = "Histórico de negociação"
        ordering = ["data"]

    def __str__(self):
        return f"{self.acao} ({self.compra})"
