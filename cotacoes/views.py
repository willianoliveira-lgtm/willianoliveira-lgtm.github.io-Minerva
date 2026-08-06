from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from core.decorators import area_restrita_required

from .forms import (AprovacaoFiltroForm, ComprasFiltroForm,
                     ComprovanteUploadForm, DecisaoAprovacaoForm)
from .models import Compra, Cotacao, HistoricoEvento


@area_restrita_required
def cotacao_index(request):
    """Equivalente a app/restrito/cotacao/page.tsx: redireciona direto para a aprovação."""
    return redirect("cotacoes:aprovacao")


# ---------------------------------------------------------------------------
# Aprovação de cotações (equivalente a app/restrito/cotacao/aprovacao/page.tsx)
# ---------------------------------------------------------------------------
@area_restrita_required
def aprovacao(request):
    filtro = AprovacaoFiltroForm(request.GET or None)
    cotacoes = Cotacao.objects.all()

    if filtro.is_valid():
        dados = filtro.cleaned_data
        if dados.get("data_inicio"):
            cotacoes = cotacoes.filter(data_recebimento__gte=dados["data_inicio"])
        if dados.get("data_fim"):
            cotacoes = cotacoes.filter(data_recebimento__lte=dados["data_fim"])
        if dados.get("projeto"):
            cotacoes = cotacoes.filter(projeto__icontains=dados["projeto"])
        if dados.get("status"):
            cotacoes = cotacoes.filter(status=dados["status"])
        if dados.get("fornecedor"):
            cotacoes = cotacoes.filter(fornecedor__icontains=dados["fornecedor"])
        if dados.get("numero_interno"):
            cotacoes = cotacoes.filter(numero_interno__icontains=dados["numero_interno"])

    stats = {
        "total": Cotacao.objects.count(),
        "aprovadas": Cotacao.objects.filter(status="aprovado").count(),
        "ressalva": Cotacao.objects.filter(status="ressalva").count(),
        "pendentes": Cotacao.objects.filter(status="pendente").count(),
    }

    return render(request, "cotacoes/aprovacao.html", {
        "quotations": cotacoes,
        "filtro": filtro,
        "stats": stats,
        "decisao_form": DecisaoAprovacaoForm(),
    })


@area_restrita_required
def aprovar_cotacao(request, pk):
    """Recebe o POST do formulário de decisão dentro do modal de análise
    (equivalente à função handleApproval() do React)."""
    cotacao = get_object_or_404(Cotacao, pk=pk)

    if request.method == "POST":
        form = DecisaoAprovacaoForm(request.POST, instance=cotacao)
        if form.is_valid():
            decisao = form.save(commit=False)
            decisao.data_aprovacao = timezone.now().date()
            decisao.aprovado_por = request.user
            decisao.save()
            messages.success(request, f"Decisão registrada para “{cotacao.produto}”.")
        else:
            messages.error(request, "Selecione uma decisão antes de confirmar.")

    return redirect("cotacoes:aprovacao")


# ---------------------------------------------------------------------------
# Compras (equivalente a app/restrito/cotacao/compras/page.tsx)
# ---------------------------------------------------------------------------
@area_restrita_required
def compras(request):
    filtro = ComprasFiltroForm(request.GET or None)
    lista = Compra.objects.prefetch_related("comprovantes", "historico").all()

    if filtro.is_valid():
        dados = filtro.cleaned_data
        if dados.get("projeto"):
            lista = lista.filter(projeto__icontains=dados["projeto"])
        if dados.get("status"):
            lista = lista.filter(status=dados["status"])
        if dados.get("fornecedor"):
            lista = lista.filter(fornecedor_escolhido__icontains=dados["fornecedor"])
        if dados.get("data_inicio"):
            lista = lista.filter(data_compra__gte=dados["data_inicio"])
        if dados.get("data_fim"):
            lista = lista.filter(data_compra__lte=dados["data_fim"])

    stats = {
        "total": Compra.objects.count(),
        "comprado": Compra.objects.filter(status="comprado").count(),
        "aguardando_nf": Compra.objects.filter(status="aguardando_nf").count(),
    }

    return render(request, "cotacoes/compras.html", {
        "purchases": lista,
        "filtro": filtro,
        "stats": stats,
        "upload_form": ComprovanteUploadForm(),
    })


@area_restrita_required
def upload_comprovante(request, pk):
    """Equivalente ao handleFileUpload() de components/file-upload.tsx —
    agora com upload de verdade, gravado em MEDIA_ROOT/comprovantes/."""
    compra = get_object_or_404(Compra, pk=pk)

    if request.method == "POST":
        form = ComprovanteUploadForm(request.POST, request.FILES)
        if form.is_valid():
            comprovante = form.save(commit=False)
            comprovante.compra = compra
            comprovante.enviado_por = request.user
            comprovante.save()
            HistoricoEvento.objects.create(
                compra=compra, usuario=request.user,
                acao="Documento anexado",
                observacao=f"Arquivo “{comprovante.arquivo.name.rsplit('/', 1)[-1]}” enviado.",
            )
            messages.success(request, "Documento enviado com sucesso.")
        else:
            messages.error(request, "Não foi possível enviar o arquivo. Verifique o formato/tamanho.")

    return redirect("cotacoes:compras")
