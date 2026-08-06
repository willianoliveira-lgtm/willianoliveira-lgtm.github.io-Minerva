from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import redirect, render

from .decorators import GRUPO_COTACAO, pode_acessar_area_restrita, area_admin_required
from .forms import ContatoForm
from .models import Noticia


# ---------------------------------------------------------------------------
# Home  (equivalente a app/page.tsx: Hero + QuickLinks + NewsSection)
# ---------------------------------------------------------------------------
def home(request):
    quick_links = [
        {"title": "Nossa Equipe", "description": "Conheça os pesquisadores e colaboradores",
         "url_name": "core:equipe", "icon": "users", "color": "bg-blue-50 text-blue-600"},
        {"title": "Projetos", "description": "Explore nossos projetos de pesquisa",
         "url_name": "core:projetos", "icon": "folder-open", "color": "bg-green-50 text-green-600"},
        {"title": "Sistemas", "description": "Ferramentas e sistemas desenvolvidos",
         "url_name": "core:sistemas", "icon": "settings", "color": "bg-purple-50 text-purple-600"},
        {"title": "Publicações", "description": "Artigos, notícias e publicações",
         "url_name": "core:publicacoes", "icon": "file-text", "color": "bg-orange-50 text-orange-600"},
        {"title": "Contato", "description": "Entre em contato conosco",
         "url_name": "core:contato", "icon": "phone", "color": "bg-red-50 text-red-600"},
    ]

    # Se ainda não houver notícias cadastradas no banco, usamos os dados de
    # exemplo originais do projeto React (assim a página nunca fica vazia).
    noticias = Noticia.objects.all()[:3]
    if not noticias:
        noticias = [
            {"titulo": "Novo Projeto de Pesquisa em IA Aprovado",
             "descricao": "Projeto interdisciplinar focado em aplicações de inteligência artificial para sustentabilidade ambiental recebe financiamento.",
             "data": "15 de janeiro de 2024", "categoria": "Pesquisa"},
            {"titulo": "Publicação em Revista Internacional",
             "descricao": "Artigo sobre otimização de algoritmos publicado na IEEE Transactions on Computing.",
             "data": "10 de janeiro de 2024", "categoria": "Publicação"},
            {"titulo": "Workshop de Tecnologias Emergentes",
             "descricao": "Evento aberto ao público sobre as últimas tendências em tecnologia e inovação.",
             "data": "5 de janeiro de 2024", "categoria": "Evento"},
        ]

    return render(request, "core/home.html", {
        "quick_links": quick_links,
        "noticias": noticias,
    })


# ---------------------------------------------------------------------------
# Equipe  (equivalente a app/equipe/page.tsx)
# ---------------------------------------------------------------------------
def equipe(request):
    team = [
        {"name": "Dr. João Silva", "role": "Coordenador Geral",
         "description": "Doutor em Ciência da Computação com especialização em Sistemas Distribuídos",
         "skills": ["Sistemas Distribuídos", "Arquitetura de Software", "Gestão de Projetos"],
         "email": "joao.silva@instituto.edu.br"},
        {"name": "Dra. Maria Santos", "role": "Pesquisadora Sênior",
         "description": "Doutora em Engenharia de Software com foco em Inteligência Artificial",
         "skills": ["Inteligência Artificial", "Machine Learning", "Análise de Dados"],
         "email": "maria.santos@instituto.edu.br"},
        {"name": "Prof. Carlos Oliveira", "role": "Desenvolvedor Full-Stack",
         "description": "Especialista em desenvolvimento web e mobile com mais de 10 anos de experiência",
         "skills": ["React", "Node.js", "Python", "Mobile Development"],
         "email": "carlos.oliveira@instituto.edu.br"},
        {"name": "Ana Costa", "role": "Designer UX/UI",
         "description": "Especialista em experiência do usuário e design de interfaces",
         "skills": ["UX Design", "UI Design", "Prototipagem", "Pesquisa de Usuário"],
         "email": "ana.costa@instituto.edu.br"},
    ]
    return render(request, "core/equipe.html", {"team": team})


# ---------------------------------------------------------------------------
# Projetos  (equivalente a app/projetos/page.tsx)
# ---------------------------------------------------------------------------
def projetos(request):
    status_color = {
        "Concluído": "bg-green-500",
        "Em Desenvolvimento": "bg-blue-500",
        "Planejamento": "bg-yellow-500",
    }
    projects = [
        {"title": "Sistema de Gestão Acadêmica",
         "description": "Plataforma integrada para gestão de atividades acadêmicas, incluindo matrículas, notas, frequência e relatórios administrativos.",
         "status": "Em Desenvolvimento", "start_date": "Janeiro 2024",
         "team": ["Dr. João Silva", "Prof. Carlos Oliveira", "Ana Costa"],
         "technologies": ["React", "Node.js", "PostgreSQL", "Docker"], "progress": 75},
        {"title": "IA para Análise de Dados Educacionais",
         "description": "Sistema de inteligência artificial para análise preditiva de desempenho estudantil e identificação de padrões de aprendizagem.",
         "status": "Concluído", "start_date": "Março 2023",
         "team": ["Dra. Maria Santos", "Dr. João Silva"],
         "technologies": ["Python", "TensorFlow", "Pandas", "Jupyter"], "progress": 100},
        {"title": "Portal de Pesquisa Colaborativa",
         "description": "Plataforma para facilitar a colaboração entre pesquisadores, compartilhamento de recursos e gestão de projetos de pesquisa.",
         "status": "Planejamento", "start_date": "Abril 2024",
         "team": ["Prof. Carlos Oliveira", "Ana Costa"],
         "technologies": ["Next.js", "Supabase", "TypeScript"], "progress": 25},
    ]
    for p in projects:
        p["status_color"] = status_color.get(p["status"], "bg-gray-500")
    return render(request, "core/projetos.html", {"projects": projects})


# ---------------------------------------------------------------------------
# Sistemas  (equivalente a app/sistemas/page.tsx)
# ---------------------------------------------------------------------------
def sistemas(request):
    status_color = {"Ativo": "bg-green-500", "Beta": "bg-yellow-500", "Desenvolvimento": "bg-blue-500"}
    systems = [
        {"name": "SIGAA - Sistema Integrado de Gestão",
         "description": "Sistema completo para gestão acadêmica e administrativa da instituição.",
         "icon": "database", "status": "Ativo", "users": "2.500+", "category": "Gestão Acadêmica",
         "features": ["Matrículas", "Notas", "Frequência", "Relatórios"]},
        {"name": "Portal do Pesquisador",
         "description": "Plataforma para submissão e acompanhamento de projetos de pesquisa.",
         "icon": "file-text", "status": "Ativo", "users": "450+", "category": "Pesquisa",
         "features": ["Submissão de projetos", "Acompanhamento", "Relatórios", "Colaboração"]},
        {"name": "Sistema de Autenticação Única",
         "description": "Gerenciamento centralizado de usuários e permissões.",
         "icon": "shield", "status": "Ativo", "users": "3.000+", "category": "Segurança",
         "features": ["SSO", "Controle de acesso", "Auditoria", "Integração"]},
        {"name": "Agenda Institucional",
         "description": "Sistema para agendamento de salas e recursos institucionais.",
         "icon": "calendar", "status": "Beta", "users": "200+", "category": "Recursos",
         "features": ["Reserva de salas", "Calendário", "Notificações", "Relatórios"]},
        {"name": "Portal de Recursos Humanos",
         "description": "Gestão de funcionários, folha de pagamento e benefícios.",
         "icon": "users", "status": "Desenvolvimento", "users": "Em breve", "category": "RH",
         "features": ["Cadastro de funcionários", "Folha de pagamento", "Benefícios", "Avaliações"]},
        {"name": "Painel de Configurações",
         "description": "Interface administrativa para configuração dos sistemas.",
         "icon": "settings", "status": "Ativo", "users": "50+", "category": "Administração",
         "features": ["Configurações", "Monitoramento", "Logs", "Backup"]},
    ]
    for s in systems:
        s["status_color"] = status_color.get(s["status"], "bg-gray-500")
    categories = sorted({s["category"] for s in systems})
    return render(request, "core/sistemas.html", {"systems": systems, "categories": categories})


# ---------------------------------------------------------------------------
# Publicações  (equivalente a app/publicacoes/page.tsx)
# ---------------------------------------------------------------------------
def publicacoes(request):
    type_color = {
        "Artigo Científico": "bg-blue-500", "Tutorial Técnico": "bg-green-500",
        "Paper de Conferência": "bg-purple-500", "Artigo de Revista": "bg-orange-500",
        "Documentação Técnica": "bg-gray-500", "Estudo de Caso": "bg-red-500",
    }
    publications = [
        {"title": "Aplicação de Inteligência Artificial na Educação Superior",
         "description": "Estudo sobre o impacto da IA nos processos educacionais e sua implementação em instituições de ensino superior.",
         "type": "Artigo Científico", "date": "15 de Janeiro de 2024",
         "authors": ["Dra. Maria Santos", "Dr. João Silva"],
         "journal": "Revista Brasileira de Informática na Educação", "tags": ["IA", "Educação", "Tecnologia"]},
        {"title": "Desenvolvimento de Sistemas Web Responsivos com React",
         "description": "Guia completo para desenvolvimento de aplicações web modernas utilizando React e tecnologias relacionadas.",
         "type": "Tutorial Técnico", "date": "10 de Janeiro de 2024",
         "authors": ["Prof. Carlos Oliveira"], "journal": "Portal de Desenvolvimento",
         "tags": ["React", "Web Development", "Frontend"]},
        {"title": "Segurança em Sistemas de Informação Acadêmicos",
         "description": "Análise das principais vulnerabilidades e estratégias de proteção para sistemas acadêmicos.",
         "type": "Paper de Conferência", "date": "5 de Janeiro de 2024",
         "authors": ["Dr. João Silva", "Ana Costa"],
         "journal": "Conferência Brasileira de Segurança da Informação", "tags": ["Segurança", "Sistemas", "Proteção"]},
        {"title": "UX Design em Plataformas Educacionais",
         "description": "Princípios e práticas de design de experiência do usuário aplicados a sistemas educacionais.",
         "type": "Artigo de Revista", "date": "28 de Dezembro de 2023",
         "authors": ["Ana Costa", "Dra. Maria Santos"], "journal": "Design & Tecnologia",
         "tags": ["UX", "Design", "Educação"]},
        {"title": "Análise de Performance em Aplicações Node.js",
         "description": "Técnicas de otimização e monitoramento de performance para aplicações backend em Node.js.",
         "type": "Documentação Técnica", "date": "20 de Dezembro de 2023",
         "authors": ["Prof. Carlos Oliveira"], "journal": "Documentação Interna",
         "tags": ["Node.js", "Performance", "Backend"]},
        {"title": "Metodologias Ágeis no Desenvolvimento de Software Educacional",
         "description": "Aplicação de metodologias ágeis no contexto de desenvolvimento de software para instituições educacionais.",
         "type": "Estudo de Caso", "date": "15 de Dezembro de 2023",
         "authors": ["Dr. João Silva", "Prof. Carlos Oliveira"], "journal": "Revista de Engenharia de Software",
         "tags": ["Metodologias Ágeis", "Software", "Educação"]},
    ]
    for p in publications:
        p["type_color"] = type_color.get(p["type"], "bg-gray-500")
    types = sorted({p["type"] for p in publications})
    return render(request, "core/publicacoes.html", {"publications": publications, "types": types})


# ---------------------------------------------------------------------------
# Contato  (equivalente a app/contato/page.tsx)
# ---------------------------------------------------------------------------
def contato(request):
    if request.method == "POST":
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Mensagem enviada com sucesso! Entraremos em contato em breve.")
            return redirect("core:contato")
    else:
        form = ContatoForm()

    return render(request, "core/contato.html", {"form": form})


# ---------------------------------------------------------------------------
# Autenticação (substitui o localStorage fake de app/login e app/admin/login)
# ---------------------------------------------------------------------------
def login_view(request):
    """Login da área restrita (cotações), equivalente a app/login/page.tsx.

    Fase 3: não basta ter uma conta válida — o usuário precisa pertencer
    ao grupo "Cotacao" (ou ser da equipe administrativa)."""
    error = None
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None and pode_acessar_area_restrita(user):
            login(request, user)
            return redirect("cotacoes:aprovacao")
        elif user is not None:
            error = "Sua conta não tem permissão para acessar a área de cotações."
        else:
            error = "Credenciais inválidas."
    return render(request, "core/login.html", {"error": error})


def admin_login_view(request):
    """Login da área administrativa, equivalente a app/admin/login/page.tsx"""
    error = None
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect("core:admin_dashboard")
        error = "Credenciais inválidas."
    return render(request, "core/admin_login.html", {"error": error})


@area_admin_required
def admin_dashboard(request):
    """Equivalente a app/admin/dashboard/page.tsx — mas com números reais
    vindos do banco de dados, em vez dos valores fixos (12, 8, 5, R$ 2.5M)
    que estavam hardcoded no React."""
    from cotacoes.models import Compra, Cotacao

    stats = {
        "pendentes": Cotacao.objects.filter(status="pendente").count(),
        "aprovadas": Cotacao.objects.filter(status="aprovado").count(),
        "compras": Compra.objects.count(),
        "valor_total": Compra.objects.aggregate(total=Sum("valor_final_pago"))["total"] or 0,
    }
    return render(request, "core/admin_dashboard.html", {"stats": stats})


@login_required
def logout_view(request):
    logout(request)
    return redirect("core:home")
