from django.db import models


class Noticia(models.Model):
    """Equivalente aos itens mockados em components/news-section.tsx"""

    CATEGORIA_CHOICES = [
        ("Pesquisa", "Pesquisa"),
        ("Publicação", "Publicação"),
        ("Evento", "Evento"),
    ]

    titulo = models.CharField("Título", max_length=200)
    descricao = models.TextField("Descrição")
    data = models.DateField("Data")
    categoria = models.CharField("Categoria", max_length=30, choices=CATEGORIA_CHOICES)
    imagem = models.ImageField("Imagem", upload_to="noticias/", blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Notícia"
        verbose_name_plural = "Notícias"
        ordering = ["-data"]

    def __str__(self):
        return self.titulo


class MensagemContato(models.Model):
    """Equivalente ao formulário em app/contato/page.tsx"""

    nome = models.CharField("Nome completo", max_length=150)
    email = models.EmailField("E-mail")
    assunto = models.CharField("Assunto", max_length=200)
    mensagem = models.TextField("Mensagem")
    enviado_em = models.DateTimeField(auto_now_add=True)
    lida = models.BooleanField("Lida", default=False)

    class Meta:
        verbose_name = "Mensagem de contato"
        verbose_name_plural = "Mensagens de contato"
        ordering = ["-enviado_em"]

    def __str__(self):
        return f"{self.nome} - {self.assunto}"
