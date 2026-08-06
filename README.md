# Minerva Aeroespacial Institucional — versão Django

Esta é a conversão do projeto original (Next.js/React/TypeScript) para **Python + Django**.

## O que já foi migrado (Fases 1, 2, 3, 4, 5 e 6 — todas concluídas)

- Estrutura do projeto Django (`minerva_project`) com os apps `core` e `cotacoes`
- Layout base (header/footer), reaproveitado em todas as páginas
- Site institucional completo:
  - Início (`/`)
  - Equipe (`/equipe/`)
  - Projetos (`/projetos/`)
  - Sistemas (`/sistemas/`)
  - Publicações (`/publicacoes/`)
  - Contato (`/contato/`) — com formulário **real**, que grava no banco de dados
- **Autenticação e permissões reais** (`django.contrib.auth` + grupos):
  - Login da área restrita: `/login/` — só entra quem está no grupo **Cotacao** (ou é da equipe admin)
  - Login administrativo: `/admin-login/` — só entra quem tem `is_staff=True`
  - As duas áreas são de fato isoladas uma da outra (testado: um usuário do grupo Cotação não consegue
    acessar o dashboard admin, e vice-versa não é automático)
- Painel administrativo pronto do Django em `/admin/` (gerencie notícias, mensagens de contato, usuários e grupos)
- **Sistema de Cotação/Aprovação/Compras** (app `cotacoes`), com modelos reais no banco:
  - `Cotacao`, `Compra`, `Comprovante` (upload real de arquivo) e `HistoricoEvento`
  - Aprovação de cotações com filtros: `/restrito/cotacao/aprovacao/`
  - Gestão de compras com upload real de comprovantes: `/restrito/cotacao/compras/`
  - Ambas protegidas pelo grupo **Cotacao**
- **Dashboard administrativo** (`/admin-dashboard/`), com estatísticas reais vindas do banco
  (substituindo os números fixos que existiam no React)

## Como rodar o projeto

1. Crie e ative um ambiente virtual (recomendado):
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Rode as migrações (cria o banco de dados SQLite):
   ```bash
   python manage.py migrate
   ```

4. (Opcional) Popule o banco com cotações/compras de exemplo, equivalentes aos mocks do React:
   ```bash
   python manage.py seed_cotacoes
   ```

5. Configure os grupos e um usuário de teste da área restrita (Fase 3):
   ```bash
   python manage.py setup_permissoes
   ```
   Isso cria o grupo **Cotacao** e um usuário `cotador` / senha `cotador123` — que acessa
   `/restrito/cotacao/...` mas **não** consegue entrar em `/admin-dashboard/` nem em `/admin/`.

6. Crie um superusuário para testar o login administrativo:
   ```bash
   python manage.py createsuperuser
   ```
   > Já deixei um usuário de teste pronto no banco enviado: **usuário `admin`, senha `admin123`**
   > (superusuário, acessa tudo — troque a senha depois).

7. Rode o servidor:
   ```bash
   python manage.py runserver
   ```

8. Acesse no navegador:
   - Site: http://127.0.0.1:8000/
   - Login área restrita (cotação/compras): http://127.0.0.1:8000/login/ (`cotador` / `cotador123`)
   - Login administrativo (dashboard): http://127.0.0.1:8000/admin-login/ (`admin` / `admin123`)
   - Painel admin do Django: http://127.0.0.1:8000/admin/

## Estrutura de pastas

```
minerva_django/
├── manage.py
├── requirements.txt
├── db.sqlite3                # banco de dados (SQLite), já com dados de exemplo
├── minerva_project/           # configurações do projeto (settings.py, urls.py)
├── core/                      # app com o site institucional e autenticação
│   ├── models.py              # Noticia, MensagemContato
│   ├── forms.py                # ContatoForm
│   ├── views.py                # páginas institucionais, login, dashboard admin
│   ├── decorators.py           # Fase 3: area_restrita_required, area_admin_required
│   ├── management/commands/setup_permissoes.py   # cria grupo "Cotacao" + usuário de teste
│   ├── urls.py
│   └── admin.py
├── cotacoes/                   # app com o sistema de cotação/aprovação/compras
│   ├── models.py               # Cotacao, Compra, Comprovante, HistoricoEvento
│   ├── forms.py                 # filtros, decisão de aprovação, upload
│   ├── views.py                 # aprovacao, compras, upload_comprovante
│   ├── urls.py
│   ├── admin.py
│   └── management/commands/seed_cotacoes.py   # popula dados de exemplo
├── templates/
│   ├── base.html                # layout (equivalente ao layout.tsx)
│   ├── includes/
│   │   ├── header.html
│   │   └── footer.html
│   ├── core/
│   │   ├── home.html, equipe.html, projetos.html, sistemas.html,
│   │   │   publicacoes.html, contato.html
│   │   ├── login.html, admin_login.html
│   │   └── admin_dashboard.html
│   └── cotacoes/
│       ├── aprovacao.html
│       └── compras.html
├── static/                     # arquivos estáticos do projeto
└── media/                      # uploads reais (comprovantes, imagens de notícias)
```

## Decisões técnicas importantes

- **Estilo (CSS):** o projeto original usa Tailwind CSS com um processo de build via Node.js.
  Para reproduzir o mesmo visual **sem exigir Node.js**, os templates usam o **Tailwind via CDN**
  (`<script src="https://cdn.tailwindcss.com">` em `base.html`). Isso funciona bem para desenvolvimento
  e para você continuar aprendendo Django sem se preocupar com build de front-end. Se um dia quiser productionizar
  com Tailwind "de verdade" (compilado), dá pra migrar depois — não é urgente.
- **Ícones:** trocamos `lucide-react` pela versão web do Lucide via CDN (`<i data-lucide="...">`), que renderiza os
  mesmos ícones.
- **Menu mobile e modais:** no React eles abrem/fecham com `useState`; aqui usei a tag HTML `<details>/<summary>`,
  que faz o mesmo efeito sem precisar escrever JavaScript. Na tela de Aprovação, por exemplo, cada linha da tabela
  tem um `<details>` com o formulário de decisão dentro — clicar no ícone de "olho" abre, sem JS nenhum.
- **Abas do dashboard admin:** usamos o truque de CSS com `<input type="radio">` + seletor `:checked ~`, que
  também dispensa JavaScript.
- **Autenticação:** os logins fake (`admin/aerospace123` e `admin/admin123` fixos no código) foram substituídos
  pelo sistema de usuários real do Django. Crie os usuários que quiser com `createsuperuser` ou pelo `/admin/`.
  As páginas restritas (`/restrito/cotacao/...`) e o dashboard (`/admin-dashboard/`) usam `@login_required`
  de verdade — sem sessão, o Django redireciona sozinho para a tela de login correta.
- **Dados de cotação/compra:** antes eram arrays mockados dentro do `.tsx`; agora são tabelas reais no banco
  (`Cotacao`, `Compra`, `Comprovante`, `HistoricoEvento`), visíveis e editáveis também pelo `/admin/` do Django.
  Rode `python manage.py seed_cotacoes` para gerar os mesmos dados de exemplo do projeto original.
- **Upload de arquivos:** no React, o "upload" de comprovantes era só simulado (`Array.from(files)` na memória,
  nada era salvo de verdade). Aqui o upload é real — o Django grava o arquivo em `media/comprovantes/AAAA/MM/`
  e associa ao registro de compra no banco.
- **Duas versões duplicadas de Aprovação/Compras:** o projeto original tinha `app/restrito/aprovacao` e
  `app/restrito/cotacao/aprovacao` (e o mesmo para compras) — duas versões diferentes da mesma tela, uma mais
  simples e outra mais completa. Migrei apenas a versão **mais completa** (a de dentro de `restrito/cotacao/`),
  que tem mais campos e filtros. Se você precisar da outra versão, me avise.
- **Dados fixos (mock) restantes:** as listas de Equipe, Projetos, Sistemas e Publicações institucionais ainda
  estão escritas diretamente em `core/views.py` (assim como estavam em `.tsx`). Mover isso para o banco de dados
  (com telas de cadastro) é um bom próximo passo, se quiser.

- **Permissões (Fase 3):** criamos o grupo `Cotacao` no sistema de autenticação do Django. A view
  `core/decorators.py` define duas regras:
  - `area_restrita_required`: exige que o usuário esteja autenticado **e** pertença ao grupo `Cotacao`
    (ou seja da equipe `is_staff`, que tem acesso a tudo). Usada em todas as views do app `cotacoes`.
  - `area_admin_required`: exige `is_staff=True`. Usada no dashboard administrativo.

  Isso significa que hoje existem, de fato, **três perfis de acesso** diferentes, e testei os três:
  1. Visitante comum (sem conta): só vê o site institucional.
  2. Usuário do grupo `Cotacao` (ex.: `cotador` / `cotador123`): acessa `/restrito/cotacao/...`,
     mas é barrado em `/admin-dashboard/` e em `/admin/`.
  3. Usuário `is_staff` (ex.: `admin` / `admin123`): acessa tudo, incluindo `/admin/` do Django.

## Próximas fases (ainda não feitas)

- Mover Equipe/Projetos/Sistemas/Publicações para o banco de dados, com telas de cadastro
- Melhorar a experiência dos modais (`<details>`) com um pouco de JavaScript opcional, se desejar algo mais
  refinado visualmente
- Relatórios e exportação (PDF/Excel) da tela de compras
- Modal de pagamento e "plano PRO" — ainda não avaliamos se isso faz sentido manter no projeto

Quando quiser continuar, é só pedir a próxima etapa.

