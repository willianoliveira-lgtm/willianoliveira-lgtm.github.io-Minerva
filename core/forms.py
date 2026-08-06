from django import forms

from .models import MensagemContato


class ContatoForm(forms.ModelForm):
    class Meta:
        model = MensagemContato
        fields = ["nome", "email", "assunto", "mensagem"]
        widgets = {
            "nome": forms.TextInput(attrs={
                "class": "flex h-10 w-full rounded-md border border-gray-300 px-3 py-2 text-sm "
                         "focus:outline-none focus:ring-2 focus:ring-blue-500",
                "placeholder": "Seu nome",
            }),
            "email": forms.EmailInput(attrs={
                "class": "flex h-10 w-full rounded-md border border-gray-300 px-3 py-2 text-sm "
                         "focus:outline-none focus:ring-2 focus:ring-blue-500",
                "placeholder": "seu@email.com",
            }),
            "assunto": forms.TextInput(attrs={
                "class": "flex h-10 w-full rounded-md border border-gray-300 px-3 py-2 text-sm "
                         "focus:outline-none focus:ring-2 focus:ring-blue-500",
                "placeholder": "Assunto da mensagem",
            }),
            "mensagem": forms.Textarea(attrs={
                "class": "flex w-full rounded-md border border-gray-300 px-3 py-2 text-sm "
                         "focus:outline-none focus:ring-2 focus:ring-blue-500",
                "placeholder": "Digite sua mensagem aqui...",
                "rows": 6,
            }),
        }
        labels = {
            "nome": "Nome completo",
            "email": "E-mail",
            "assunto": "Assunto",
            "mensagem": "Mensagem",
        }
