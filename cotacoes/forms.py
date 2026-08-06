from django import forms

from .models import Comprovante, Cotacao


INPUT_CLS = ("flex h-10 w-full rounded-md border border-gray-300 px-3 py-2 text-sm "
             "focus:outline-none focus:ring-2 focus:ring-blue-500")
SELECT_CLS = INPUT_CLS
TEXTAREA_CLS = ("flex w-full rounded-md border border-gray-300 px-3 py-2 text-sm "
                "focus:outline-none focus:ring-2 focus:ring-blue-500")


class AprovacaoFiltroForm(forms.Form):
    """Equivalente ao useState 'filters' de app/restrito/cotacao/aprovacao/page.tsx"""
    data_inicio = forms.DateField(required=False, widget=forms.DateInput(
        attrs={"type": "date", "class": INPUT_CLS}))
    data_fim = forms.DateField(required=False, widget=forms.DateInput(
        attrs={"type": "date", "class": INPUT_CLS}))
    projeto = forms.CharField(required=False, widget=forms.TextInput(
        attrs={"class": INPUT_CLS, "placeholder": "Filtrar por projeto"}))
    status = forms.ChoiceField(
        required=False,
        choices=[("", "Todos")] + Cotacao.STATUS_CHOICES,
        widget=forms.Select(attrs={"class": SELECT_CLS}),
    )
    fornecedor = forms.CharField(required=False, widget=forms.TextInput(
        attrs={"class": INPUT_CLS, "placeholder": "Filtrar por fornecedor"}))
    numero_interno = forms.CharField(required=False, widget=forms.TextInput(
        attrs={"class": INPUT_CLS, "placeholder": "Número interno"}))


class DecisaoAprovacaoForm(forms.ModelForm):
    """Equivalente ao useState 'approvalData' — o formulário dentro do
    Dialog de análise de cotação."""

    class Meta:
        model = Cotacao
        fields = ["status", "justificativa", "observacoes"]
        widgets = {
            "status": forms.Select(attrs={"class": SELECT_CLS}),
            "justificativa": forms.Textarea(attrs={
                "class": TEXTAREA_CLS, "rows": 3,
                "placeholder": "Digite a justificativa da decisão...",
            }),
            "observacoes": forms.Textarea(attrs={
                "class": TEXTAREA_CLS, "rows": 2,
                "placeholder": "Observações técnicas ou comerciais...",
            }),
        }

    def clean_status(self):
        status = self.cleaned_data["status"]
        if status == "pendente":
            raise forms.ValidationError("Selecione uma decisão (Aprovar, Reprovar ou Ressalva).")
        return status


class ComprasFiltroForm(forms.Form):
    """Equivalente ao useState 'filters' de app/restrito/cotacao/compras/page.tsx"""
    from .models import Compra
    projeto = forms.CharField(required=False, widget=forms.TextInput(
        attrs={"class": INPUT_CLS, "placeholder": "Filtrar por projeto"}))
    status = forms.ChoiceField(
        required=False,
        choices=[("", "Todos")] + Compra.STATUS_CHOICES,
        widget=forms.Select(attrs={"class": SELECT_CLS}),
    )
    fornecedor = forms.CharField(required=False, widget=forms.TextInput(
        attrs={"class": INPUT_CLS, "placeholder": "Filtrar por fornecedor"}))
    data_inicio = forms.DateField(required=False, widget=forms.DateInput(
        attrs={"type": "date", "class": INPUT_CLS}))
    data_fim = forms.DateField(required=False, widget=forms.DateInput(
        attrs={"type": "date", "class": INPUT_CLS}))


class ComprovanteUploadForm(forms.ModelForm):
    """Equivalente ao handleFileUpload() de components/file-upload.tsx,
    mas com upload real (o React só simulava)."""

    class Meta:
        model = Comprovante
        fields = ["arquivo", "tipo"]
        widgets = {
            "tipo": forms.Select(attrs={"class": SELECT_CLS}),
        }
