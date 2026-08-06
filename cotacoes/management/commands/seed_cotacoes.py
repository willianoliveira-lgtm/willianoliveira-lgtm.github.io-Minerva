from datetime import date

from django.core.management.base import BaseCommand

from cotacoes.models import Comprovante, Compra, Cotacao, HistoricoEvento


class Command(BaseCommand):
    help = "Popula o banco com dados de exemplo (equivalentes aos mocks do React) para testar as telas."

    def handle(self, *args, **options):
        if Cotacao.objects.exists() or Compra.objects.exists():
            self.stdout.write(self.style.WARNING(
                "Já existem cotações/compras no banco — nada foi criado (evitar duplicar)."
            ))
            return

        c1 = Cotacao.objects.create(
            produto="Turbina CFM56-7B", tipo="Engine Component", quantidade=1,
            link="https://example.com/cfm56-spec",
            valor_unitario=1250000, moeda="USD", frete=15000, alfandega=25000, desconto=5,
            total=2515000, fornecedor="Safran Aircraft Engines", numero_interno="INT-2024-001",
            projeto="Projeto Alpha", prazo="90 dias", condicoes_pagamento="30/60/90 dias",
            data_recebimento=date(2024, 1, 15), validade_cotacao=date(2024, 3, 15),
            status="pendente", observacoes="Cotação com certificação AS9100 incluída",
        )
        c2 = Cotacao.objects.create(
            produto="Trem de Pouso Principal", tipo="Landing Gear", quantidade=2,
            link="https://example.com/landing-gear-spec",
            valor_unitario=450000, moeda="EUR", frete=8000, alfandega=12000, desconto=2,
            total=458000, fornecedor="Liebherr Aerospace", numero_interno="INT-2024-002",
            projeto="Projeto Alpha", prazo="60 dias", condicoes_pagamento="À vista",
            data_recebimento=date(2024, 1, 10), validade_cotacao=date(2024, 2, 28),
            status="aprovado", data_aprovacao=date(2024, 1, 18),
            observacoes="Aprovado com desconto negociado",
        )
        Cotacao.objects.create(
            produto="Sistema Avionics Display", tipo="Avionics", quantidade=4,
            link="https://example.com/avionics-spec",
            valor_unitario=45000, moeda="USD", frete=3000, alfandega=5000, desconto=0,
            total=182000, fornecedor="Honeywell Aerospace", numero_interno="INT-2024-003",
            projeto="Projeto Beta", prazo="45 dias", condicoes_pagamento="60 dias",
            data_recebimento=date(2024, 1, 8), validade_cotacao=date(2024, 2, 15),
            status="reprovado", data_aprovacao=date(2024, 1, 20),
            observacoes="Reprovado por prazo inadequado",
        )
        c4 = Cotacao.objects.create(
            produto="Bomba Hidráulica", tipo="Hydraulic System", quantidade=3,
            link="https://example.com/hydraulic-spec",
            valor_unitario=25000, moeda="USD", frete=1500, alfandega=2000, desconto=3,
            total=76500, fornecedor="Parker Hannifin", numero_interno="INT-2024-004",
            projeto="Projeto Gamma", prazo="30 dias", condicoes_pagamento="45 dias",
            data_recebimento=date(2024, 1, 12), validade_cotacao=date(2024, 3, 1),
            status="ressalva", data_aprovacao=date(2024, 1, 22),
            observacoes="Aprovado com ressalva sobre certificação",
        )
        Cotacao.objects.create(
            produto="Válvula do Sistema de Oxigênio", tipo="Life Support", quantidade=6,
            link="https://example.com/oxygen-valve-spec",
            valor_unitario=8500, moeda="USD", frete=800, alfandega=1500, desconto=1,
            total=51800, fornecedor="Zodiac Aerospace", numero_interno="INT-2024-005",
            projeto="Projeto Delta", prazo="21 dias", condicoes_pagamento="30 dias",
            data_recebimento=date(2024, 1, 25), validade_cotacao=date(2024, 2, 25),
            status="pendente", observacoes="Aguardando análise técnica",
        )

        p1 = Compra.objects.create(
            cotacao=c2, produto=c2.produto, quantidade=c2.quantidade,
            fornecedor_escolhido="Liebherr Aerospace",
            justificativa="Melhor custo-benefício e prazo de entrega adequado",
            valor_final_pago=458000, moeda="EUR", condicoes_pagamento="À vista",
            numero_compra="PC-2024-002", nota_fiscal="NF-LIE-2024-002.pdf",
            data_compra=date(2024, 1, 25), projeto="Projeto Alpha", status="comprado",
            observacoes="Compra realizada com sucesso. Fornecedor ofereceu garantia estendida.",
        )
        for acao, obs, dias in [
            ("Cotação aprovada", "Aprovado com desconto negociado", 18),
            ("Negociação iniciada", "Solicitado desconto adicional", 20),
            ("Desconto aprovado", "Desconto de 2% aprovado pelo fornecedor", 22),
            ("Compra finalizada", "Pedido de compra emitido", 25),
        ]:
            HistoricoEvento.objects.create(compra=p1, acao=acao, observacao=obs)

        p2 = Compra.objects.create(
            cotacao=c4, produto=c4.produto, quantidade=c4.quantidade,
            fornecedor_escolhido="Parker Hannifin",
            justificativa="Aprovado com ressalva sobre certificação - certificação confirmada posteriormente",
            valor_final_pago=76500, moeda="USD", condicoes_pagamento="45 dias",
            numero_compra="PC-2024-004", nota_fiscal="",
            data_compra=date(2024, 1, 28), projeto="Projeto Gamma", status="aguardando_nf",
            observacoes="Aguardando emissão da nota fiscal pelo fornecedor.",
        )
        for acao, obs in [
            ("Aprovado com ressalva", "Necessária confirmação de certificação"),
            ("Certificação confirmada", "Fornecedor enviou certificados AS9100"),
            ("Compra autorizada", "Pedido de compra emitido"),
        ]:
            HistoricoEvento.objects.create(compra=p2, acao=acao, observacao=obs)

        self.stdout.write(self.style.SUCCESS(
            f"Criadas {Cotacao.objects.count()} cotações e {Compra.objects.count()} compras de exemplo."
        ))
