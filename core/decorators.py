"""
Fase 3: controle de acesso por grupo/permissão.

Duas áreas protegidas, cada uma com sua própria regra:

- Área restrita (/restrito/cotacao/...): usuário autenticado E membro do
  grupo "Cotacao" (ou membro da equipe administrativa, que tem acesso a
  tudo). Equivale a: "qualquer colaborador do setor de compras pode entrar
  aqui, mas nem todo mundo que tem conta no sistema".

- Área administrativa (/admin-dashboard/ e /admin/): usuário autenticado E
  com is_staff=True. Isso já é o conceito nativo do Django para "pode
  acessar telas administrativas" — não inventamos um campo novo pra isso.
"""
from functools import wraps

from django.contrib.auth.decorators import user_passes_test

GRUPO_COTACAO = "Cotacao"


def pode_acessar_area_restrita(user):
    if not user.is_authenticated:
        return False
    if user.is_staff or user.is_superuser:
        return True
    return user.groups.filter(name=GRUPO_COTACAO).exists()


def area_restrita_required(view_func):
    """Protege views da área de cotação/aprovação/compras."""
    decorated = user_passes_test(pode_acessar_area_restrita, login_url="core:login")
    return wraps(view_func)(decorated(view_func))


def area_admin_required(view_func):
    """Protege views do dashboard administrativo."""
    decorated = user_passes_test(
        lambda u: u.is_authenticated and u.is_staff, login_url="core:admin_login",
    )
    return wraps(view_func)(decorated(view_func))
