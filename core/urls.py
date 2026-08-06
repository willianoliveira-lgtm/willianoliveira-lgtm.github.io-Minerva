from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("equipe/", views.equipe, name="equipe"),
    path("projetos/", views.projetos, name="projetos"),
    path("sistemas/", views.sistemas, name="sistemas"),
    path("publicacoes/", views.publicacoes, name="publicacoes"),
    path("contato/", views.contato, name="contato"),
    path("login/", views.login_view, name="login"),
    path("admin-login/", views.admin_login_view, name="admin_login"),
    path("admin-dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("logout/", views.logout_view, name="logout"),
]
