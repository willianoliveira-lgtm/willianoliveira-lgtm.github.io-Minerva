from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand

from core.decorators import GRUPO_COTACAO


class Command(BaseCommand):
    help = (
        "Fase 3: cria o grupo 'Cotacao' (área restrita) e um usuário de "
        "exemplo NÃO administrativo (cotador/cotador123), para provar que "
        "a separação de permissões funciona de verdade."
    )

    def handle(self, *args, **options):
        User = get_user_model()

        grupo, criado = Group.objects.get_or_create(name=GRUPO_COTACAO)
        if criado:
            self.stdout.write(self.style.SUCCESS(f"Grupo '{GRUPO_COTACAO}' criado."))
        else:
            self.stdout.write(f"Grupo '{GRUPO_COTACAO}' já existia.")

        usuario, criado = User.objects.get_or_create(
            username="cotador",
            defaults={"email": "cotador@instituto.edu.br", "is_staff": False},
        )
        if criado:
            usuario.set_password("cotador123")
            usuario.is_staff = False  # não deve acessar /admin-dashboard/ nem /admin/
            usuario.save()
            self.stdout.write(self.style.SUCCESS(
                "Usuário de teste 'cotador' criado (senha: cotador123) — "
                "acessa a área de cotações, mas NÃO o painel administrativo."
            ))
        else:
            self.stdout.write("Usuário 'cotador' já existia.")

        usuario.groups.add(grupo)
        self.stdout.write(self.style.SUCCESS(
            f"Usuário '{usuario.username}' associado ao grupo '{GRUPO_COTACAO}'."
        ))
