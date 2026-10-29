/* =========================================================
   MINERVA — layout compartilhado e páginas
   Para mudar contatos, equipe, projetos ou sistemas, edite
   os blocos de dados logo abaixo. Os artigos ficam em posts.js
   ========================================================= */
const SITE = {
  sigla: "M",
  nome: "Minerva",
  descricao: "Desenvolvemos soluções tecnológicas inovadoras através de pesquisa aplicada, conectando academia e indústria para transformar conhecimento em impacto social.",
  email: "contato@minerva.org.br",
  telefone: "(11) 1234-5678",
  endereco: ["Rua da Universidade, 123", "São Paulo, SP - 01234-567"],
  horario: ["Segunda a sexta: 8h às 18h", "Sábado: 8h às 12h"],
  redes: { facebook: "#", twitter: "#", linkedin: "#" },
};

const EQUIPE = [
  { nome: "Dr. João Silva", cargo: "Coordenador Geral", desc: "Doutor em Ciência da Computação com especialização em Sistemas Distribuídos.", skills: ["Sistemas Distribuídos", "Arquitetura de Software", "Gestão de Projetos"], email: "joao.silva@minerva.org.br" },
  { nome: "Dra. Maria Santos", cargo: "Pesquisadora Sênior", desc: "Doutora em Engenharia de Software com foco em Inteligência Artificial.", skills: ["Inteligência Artificial", "Machine Learning", "Análise de Dados"], email: "maria.santos@minerva.org.br" },
  { nome: "Prof. Carlos Oliveira", cargo: "Desenvolvedor Full-Stack", desc: "Especialista em desenvolvimento web e mobile com mais de 10 anos de experiência.", skills: ["React", "Node.js", "Python", "Mobile"], email: "carlos.oliveira@minerva.org.br" },
  { nome: "Ana Costa", cargo: "Designer UX/UI", desc: "Especialista em experiência do usuário e design de interfaces.", skills: ["UX Design", "UI Design", "Prototipagem"], email: "ana.costa@minerva.org.br" },
  { nome: "Willian Oliveira", cargo: "Editor do Portal", desc: "Responsável pela curadoria de conteúdo e pela publicação de notícias e artigos.", skills: ["Conteúdo", "Finanças", "Comunicação"], email: "willian.oliveira@minerva.org.br" },
  { nome: "Equipe de Bolsistas", cargo: "Iniciação Científica", desc: "Estudantes de graduação que participam ativamente dos projetos de pesquisa.", skills: ["Pesquisa", "Desenvolvimento", "Testes"], email: "bolsistas@minerva.org.br" },
];

const PROJETOS = [
  { titulo: "Sistema de Gestão Acadêmica", desc: "Plataforma integrada para gestão de atividades acadêmicas, incluindo matrículas, notas, frequência e relatórios administrativos.", status: "Em Desenvolvimento", inicio: "Janeiro 2024", equipe: ["Dr. João Silva", "Prof. Carlos Oliveira", "Ana Costa"], tech: ["React", "Node.js", "PostgreSQL", "Docker"], progresso: 75, icone: "database", cor: "#2563eb" },
  { titulo: "IA para Análise de Dados Educacionais", desc: "Sistema de inteligência artificial para análise preditiva de desempenho estudantil e identificação de padrões de aprendizagem.", status: "Concluído", inicio: "Março 2023", equipe: ["Dra. Maria Santos", "Dr. João Silva"], tech: ["Python", "TensorFlow", "Pandas", "Jupyter"], progresso: 100, icone: "cpu", cor: "#16a34a" },
  { titulo: "Portal de Pesquisa Colaborativa", desc: "Plataforma para facilitar a colaboração entre pesquisadores, compartilhamento de recursos e gestão de projetos de pesquisa.", status: "Planejamento", inicio: "Abril 2024", equipe: ["Prof. Carlos Oliveira", "Ana Costa"], tech: ["Next.js", "Supabase", "TypeScript"], progresso: 25, icone: "users", cor: "#9333ea" },
];

const SISTEMAS = [
  { nome: "SIGAA - Sistema Integrado de Gestão", desc: "Sistema completo para gestão acadêmica e administrativa da instituição.", icone: "database", status: "Ativo", usuarios: "2.500+", categoria: "Gestão Acadêmica", recursos: ["Matrículas", "Notas", "Frequência", "Relatórios"] },
  { nome: "Portal do Pesquisador", desc: "Plataforma para submissão e acompanhamento de projetos de pesquisa.", icone: "file", status: "Ativo", usuarios: "450+", categoria: "Pesquisa", recursos: ["Submissão de projetos", "Acompanhamento", "Relatórios", "Colaboração"] },
  { nome: "Sistema de Autenticação Única", desc: "Gerenciamento centralizado de usuários e permissões.", icone: "shield", status: "Ativo", usuarios: "3.000+", categoria: "Segurança", recursos: ["SSO", "Controle de acesso", "Auditoria", "Integração"] },
  { nome: "Agenda Institucional", desc: "Sistema para agendamento de salas e recursos institucionais.", icone: "calendar", status: "Beta", usuarios: "200+", categoria: "Recursos", recursos: ["Reserva de salas", "Calendário", "Notificações", "Relatórios"] },
  { nome: "Portal de Recursos Humanos", desc: "Gestão de funcionários, folha de pagamento e benefícios.", icone: "users", status: "Desenvolvimento", usuarios: "Em breve", categoria: "RH", recursos: ["Cadastro", "Folha de pagamento", "Benefícios", "Avaliações"] },
  { nome: "Painel de Configurações", desc: "Interface administrativa para configuração dos sistemas.", icone: "settings", status: "Ativo", usuarios: "50+", categoria: "Administração", recursos: ["Configurações", "Monitoramento", "Logs", "Backup"] },
];

/* ---------- Ícones (estilo Lucide) ---------- */
const P = {
  home: '<path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><path d="M9 22V12h6v10"/>',
  users: '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',
  folder: '<path d="M6 14l1.5-2.9A2 2 0 0 1 9.24 10H20a2 2 0 0 1 1.94 2.5l-1.54 6a2 2 0 0 1-1.95 1.5H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h3.9a2 2 0 0 1 1.69.9l.81 1.2a2 2 0 0 0 1.67.9H18a2 2 0 0 1 2 2v2"/>',
  settings: '<path d="M12.22 2h-.44a2 2 0 0 0-2 2v.18a2 2 0 0 1-1 1.73l-.43.25a2 2 0 0 1-2 0l-.15-.08a2 2 0 0 0-2.73.73l-.22.38a2 2 0 0 0 .73 2.73l.15.1a2 2 0 0 1 1 1.72v.51a2 2 0 0 1-1 1.74l-.15.09a2 2 0 0 0-.73 2.73l.22.38a2 2 0 0 0 2.73.73l.15-.08a2 2 0 0 1 2 0l.43.25a2 2 0 0 1 1 1.73V20a2 2 0 0 0 2 2h.44a2 2 0 0 0 2-2v-.18a2 2 0 0 1 1-1.73l.43-.25a2 2 0 0 1 2 0l.15.08a2 2 0 0 0 2.73-.73l.22-.39a2 2 0 0 0-.73-2.73l-.15-.08a2 2 0 0 1-1-1.74v-.5a2 2 0 0 1 1-1.74l.15-.09a2 2 0 0 0 .73-2.73l-.22-.38a2 2 0 0 0-2.73-.73l-.15.08a2 2 0 0 1-2 0l-.43-.25a2 2 0 0 1-1-1.73V4a2 2 0 0 0-2-2z"/><circle cx="12" cy="12" r="3"/>',
  file: '<path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z"/><path d="M14 2v6h6"/><path d="M16 13H8"/><path d="M16 17H8"/><path d="M10 9H8"/>',
  phone: '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/>',
  rocket: '<path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09z"/><path d="M12 15l-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2z"/><path d="M9 12H4s.55-3.03 2-4c1.62-1.08 5 0 5 0"/><path d="M12 15v5s3.03-.55 4-2c1.08-1.62 0-5 0-5"/>',
  building: '<rect x="4" y="2" width="16" height="20" rx="2"/><path d="M9 22v-4h6v4"/><path d="M8 6h.01M16 6h.01M12 6h.01M12 10h.01M12 14h.01M16 10h.01M16 14h.01M8 10h.01M8 14h.01"/>',
  book: '<path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/>',
  arrow: '<path d="M5 12h14"/><path d="M12 5l7 7-7 7"/>',
  back: '<path d="M19 12H5"/><path d="M12 19l-7-7 7-7"/>',
  calendar: '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>',
  clock: '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
  user: '<path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>',
  mail: '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="M22 7l-10 6L2 7"/>',
  pin: '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/>',
  menu: '<path d="M4 6h16M4 12h16M4 18h16"/>',
  x: '<path d="M18 6L6 18M6 6l12 12"/>',
  search: '<circle cx="11" cy="11" r="8"/><path d="M21 21l-4.3-4.3"/>',
  database: '<ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M3 5v14a9 3 0 0 0 18 0V5"/><path d="M3 12a9 3 0 0 0 18 0"/>',
  shield: '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>',
  cpu: '<rect x="4" y="4" width="16" height="16" rx="2"/><rect x="9" y="9" width="6" height="6"/><path d="M15 2v2M15 20v2M2 15h2M2 9h2M20 15h2M20 9h2M9 2v2M9 20v2"/>',
  ext: '<path d="M15 3h6v6"/><path d="M10 14L21 3"/><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/>',
  facebook: '<path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/>',
  twitter: '<path d="M22 4s-.7 2.1-2 3.4c1.6 10-9.4 17.3-18 11.6 2.2.1 4.4-.6 6-2C3 15.5.5 9.6 3 5c2.2 2.6 5.6 4.1 9 4-.9-4.2 4-6.6 7-3.8 1.1 0 3-1.2 3-1.2z"/>',
  linkedin: '<path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/><rect x="2" y="9" width="4" height="12"/><circle cx="4" cy="4" r="2"/>',
  bulb: '<path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5"/><path d="M9 18h6M10 22h4"/>',
  mic: '<path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><path d="M12 19v3"/>',
  flask: '<path d="M10 2v7.31"/><path d="M14 9.3V1.99"/><path d="M8.5 2h7"/><path d="M14 9.3a6.5 6.5 0 1 1-4 0"/><path d="M5.52 16h12.96"/>',
};
const ic = (n, cls = "") => `<svg class="i ${cls}" viewBox="0 0 24 24" aria-hidden="true">${P[n] || P.file}</svg>`;

/* Aparência das categorias de posts */
const CATEGORIAS = {
  "Pesquisa": { icone: "flask", cor: "#2563eb" },
  "Publicação": { icone: "file", cor: "#ea580c" },
  "Evento": { icone: "mic", cor: "#9333ea" },
  "Tecnologia": { icone: "cpu", cor: "#1e40af" },
  "Aprendizagem": { icone: "book", cor: "#16a34a" },
  "Educação": { icone: "bulb", cor: "#4f46e5" },
};

const NAV = [
  ["index.html", "Início", "home"],
  ["equipe.html", "Equipe", "users"],
  ["projetos.html", "Projetos", "folder"],
  ["sistemas.html", "Sistemas/Ferramentas", "settings"],
  ["blog.html", "Publicações/Notícias", "file"],
  ["contato.html", "Contato", "phone"],
];

/* ---------- utilitários ---------- */
const esc = s => String(s ?? "").replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
const $ = id => document.getElementById(id);
function fmtData(iso) {
  const [a, m, d] = iso.split("-").map(Number);
  return new Date(a, m - 1, d).toLocaleDateString("pt-BR", { day: "numeric", month: "long", year: "numeric" });
}
const ordenados = () => [...POSTS].sort((a, b) => b.data.localeCompare(a.data));
const iniciais = n => { const w = n.replace(/^(Dr\.|Dra\.|Prof\.)\s*/, "").split(" "); return (w[0][0] + (w.length > 1 ? w[w.length - 1][0] : "")).toUpperCase(); };

function thumb(p) {
  if (p.imagem) return `<img src="${esc(p.imagem)}" alt="${esc(p.titulo)}" loading="lazy">`;
  const c = CATEGORIAS[p.categoria] || { icone: "file", cor: "#2563eb" };
  return `<div class="art" style="background:linear-gradient(135deg, ${c.cor}, #1e3a8a)">${ic(c.icone)}</div>`;
}

function cardNoticia(p) {
  const url = `post.html?p=${encodeURIComponent(p.slug)}`;
  return `<article class="card">
    <a class="thumb" href="${url}">${thumb(p)}</a>
    <div class="hd">
      <div class="row-meta"><span class="badge">${esc(p.categoria)}</span><span class="date">${ic("calendar")}${fmtData(p.data)}</span></div>
      <h3 class="clamp2"><a href="${url}">${esc(p.titulo)}</a></h3>
      <p class="desc clamp3">${esc(p.resumo)}</p>
    </div>
    <div class="ct"><a class="btn btn-ghost" href="${url}">Ler mais ${ic("arrow")}</a></div>
  </article>`;
}

/* ---------- cabeçalho e rodapé ---------- */
function layout() {
  const atual = location.pathname.split("/").pop() || "index.html";
  const ativo = h => atual === h || (atual === "post.html" && h === "blog.html");
  const links = cls => NAV.map(([h, t, i]) => `<a href="${h}" class="${ativo(h) ? "active" : ""}">${ic(i)}<span>${t}</span></a>`).join("");
  const logo = `<a href="index.html" class="logo"><span class="mark">${SITE.sigla}</span><span class="name">${SITE.nome}</span></a>`;

  const h = $("header");
  if (h) h.outerHTML = `<header class="site"><div class="container">
      <div class="bar">${logo}
        <nav class="main">${links()}</nav>
        <button class="menu-btn" aria-label="Abrir menu" id="menuBtn">${ic("menu")}</button>
      </div>
      <nav class="mobile-nav" id="mobileNav">${links()}</nav>
    </div></header>`;
  const mb = $("menuBtn");
  if (mb) mb.addEventListener("click", () => {
    const open = $("mobileNav").classList.toggle("open");
    mb.innerHTML = ic(open ? "x" : "menu");
  });

  const f = $("footer");
  if (f) f.outerHTML = `<footer class="site"><div class="container">
      <div class="cols">
        <div>
          <div class="logo" style="margin-bottom:16px"><span class="mark">${SITE.sigla}</span><span class="name">${SITE.nome}</span></div>
          <p>${SITE.descricao}</p>
          <div class="social">
            <a href="${SITE.redes.facebook}" aria-label="Facebook">${ic("facebook")}</a>
            <a href="${SITE.redes.twitter}" aria-label="Twitter">${ic("twitter")}</a>
            <a href="${SITE.redes.linkedin}" aria-label="LinkedIn">${ic("linkedin")}</a>
          </div>
        </div>
        <div><h3>Links Rápidos</h3><ul>${NAV.slice(1, 5).map(([h, t]) => `<li><a href="${h}">${t.split("/")[0]}</a></li>`).join("")}</ul></div>
        <div><h3>Contato</h3><ul>
          <li class="ci">${ic("mail")}<span>${SITE.email}</span></li>
          <li class="ci">${ic("phone")}<span>${SITE.telefone}</span></li>
          <li class="ci">${ic("pin")}<span>${SITE.endereco.join("<br>")}</span></li>
        </ul></div>
      </div>
      <div class="copy">© ${new Date().getFullYear()} ${SITE.nome}. Todos os direitos reservados.</div>
    </div></footer>`;
}

/* ---------- páginas ---------- */
function home() {
  const q = $("quick");
  const quick = [
    ["Nossa Equipe", "Conheça os pesquisadores e colaboradores", "equipe.html", "users", "c-blue"],
    ["Projetos", "Explore nossos projetos de pesquisa", "projetos.html", "folder", "c-green"],
    ["Sistemas", "Ferramentas e sistemas desenvolvidos", "sistemas.html", "settings", "c-purple"],
    ["Publicações", "Artigos, notícias e publicações", "blog.html", "file", "c-orange"],
    ["Contato", "Entre em contato conosco", "contato.html", "phone", "c-red"],
    ["Biblioteca", "Recursos e materiais de estudo", "blog.html?cat=Aprendizagem", "book", "c-indigo"],
  ];
  q.innerHTML = quick.map(([t, d, h, i, c]) => `<div class="card">
      <div class="hd"><div class="ico ${c}">${ic(i)}</div><h3>${t}</h3><p class="desc">${d}</p></div>
      <div class="ct"><a class="btn btn-ghost" href="${h}">Acessar ${ic("arrow")}</a></div></div>`).join("");
  $("news").innerHTML = ordenados().slice(0, 3).map(cardNoticia).join("");
}

function blog() {
  const params = new URLSearchParams(location.search);
  let cat = params.get("cat") || "Todas", q = "";
  const cats = ["Todas", ...new Set(POSTS.map(p => p.categoria))];
  const draw = () => {
    $("chips").innerHTML = cats.map(c => `<button class="chip ${c === cat ? "on" : ""}" data-c="${esc(c)}">${esc(c)}</button>`).join("");
    const t = q.trim().toLowerCase();
    const lista = ordenados().filter(p => (cat === "Todas" || p.categoria === cat) &&
      (!t || `${p.titulo} ${p.resumo} ${p.autor}`.toLowerCase().includes(t)));
    $("posts").innerHTML = lista.length ? lista.map(cardNoticia).join("") : `<p class="empty">Nenhuma publicação encontrada.</p>`;
  };
  $("chips").addEventListener("click", e => { const b = e.target.closest(".chip"); if (b) { cat = b.dataset.c; draw(); } });
  $("busca").addEventListener("input", e => { q = e.target.value; draw(); });
  draw();
}

function post() {
  const p = POSTS.find(x => x.slug === new URLSearchParams(location.search).get("p"));
  if (!p) {
    $("post-head").innerHTML = `<div class="container"><a class="back" href="blog.html">${ic("back")} Voltar às publicações</a><h1>Publicação não encontrada</h1></div>`;
    return;
  }
  document.title = `${p.titulo} — ${SITE.nome}`;
  $("post-head").innerHTML = `<div class="container">
    <a class="back" href="blog.html">${ic("back")} Todas as publicações</a><br>
    <span class="badge blue">${esc(p.categoria)}</span>
    <h1>${esc(p.titulo)}</h1>
    <div class="meta"><span>${ic("user")}${esc(p.autor)}</span><span>${ic("calendar")}${fmtData(p.data)}</span><span>${ic("clock")}${p.leitura} min de leitura</span></div>
  </div>`;
  $("post-body").innerHTML = `<article class="article">${p.conteudo}</article>`;
  $("related").innerHTML = ordenados().filter(x => x.slug !== p.slug).slice(0, 3).map(cardNoticia).join("");
}

function equipe() {
  $("team").innerHTML = EQUIPE.map(m => `<div class="card center"><div class="hd">
      <div class="avatar">${iniciais(m.nome)}</div>
      <h3>${esc(m.nome)}</h3><div class="role">${esc(m.cargo)}</div></div>
      <div class="ct"><p class="desc" style="margin-bottom:16px">${esc(m.desc)}</p>
      <div class="tags c">${m.skills.map(s => `<span class="badge outline">${esc(s)}</span>`).join("")}</div>
      <div class="links"><a href="mailto:${esc(m.email)}" aria-label="E-mail">${ic("mail")}</a><a href="#" aria-label="LinkedIn">${ic("linkedin")}</a></div></div></div>`).join("");
}

const corStatus = s => ({ "Concluído": "green", "Ativo": "green", "Em Desenvolvimento": "blue", "Desenvolvimento": "blue", "Planejamento": "yellow", "Beta": "yellow" }[s] || "");

function projetos() {
  $("projects").innerHTML = PROJETOS.map(p => `<div class="card project">
      <div class="side" style="background:linear-gradient(135deg, ${p.cor}, #1e3a8a)">${ic(p.icone)}</div>
      <div class="body">
        <span class="badge ${corStatus(p.status)}">${p.status}</span>
        <h3>${esc(p.titulo)}</h3>
        <p class="desc" style="font-size:1rem">${esc(p.desc)}</p>
        <div class="kv"><div>${ic("calendar")}Início: ${p.inicio}</div><div>${ic("users")}${p.equipe.length} membros</div></div>
        <div class="prog-row"><span>Progresso</span><b>${p.progresso}%</b></div>
        <div class="progress"><div style="width:${p.progresso}%"></div></div>
        <p style="font-size:.88rem;font-weight:500;margin:18px 0 8px">Tecnologias</p>
        <div class="tags">${p.tech.map(t => `<span class="badge outline">${t}</span>`).join("")}</div>
        <p style="font-size:.88rem;font-weight:500;margin:16px 0 8px">Equipe</p>
        <div class="tags">${p.equipe.map(t => `<span class="badge">${t}</span>`).join("")}</div>
      </div></div>`).join("");
}

function sistemas() {
  let cat = "Todas";
  const cats = ["Todas", ...new Set(SISTEMAS.map(s => s.categoria))];
  const draw = () => {
    $("chips").innerHTML = cats.map(c => `<button class="chip ${c === cat ? "on" : ""}" data-c="${esc(c)}">${esc(c)}</button>`).join("");
    $("systems").innerHTML = SISTEMAS.filter(s => cat === "Todas" || s.categoria === cat).map(s => `<div class="card">
      <div class="hd">
        <div class="row-meta"><div class="ico c-blue" style="margin:0">${ic(s.icone)}</div><span class="badge ${corStatus(s.status)}">${s.status}</span></div>
        <h3 style="margin-top:12px">${esc(s.nome)}</h3><p class="desc">${esc(s.desc)}</p></div>
      <div class="ct">
        <div class="prog-row" style="color:var(--gray-600)"><span>Categoria</span><b style="color:var(--gray-900)">${s.categoria}</b></div>
        <div class="prog-row" style="color:var(--gray-600)"><span>Usuários</span><b style="color:var(--gray-900)">${s.usuarios}</b></div>
        <div class="tags" style="margin:14px 0 18px">${s.recursos.map(r => `<span class="badge outline">${r}</span>`).join("")}</div>
        <a class="btn btn-outline" style="width:100%" href="contato.html">Saiba mais ${ic("ext")}</a>
      </div></div>`).join("");
  };
  $("chips").addEventListener("click", e => { const b = e.target.closest(".chip"); if (b) { cat = b.dataset.c; draw(); } });
  draw();
  const ativos = SISTEMAS.filter(s => s.status === "Ativo").length;
  $("stats").innerHTML = [
    [SISTEMAS.length, "Sistemas", "#2563eb"], [ativos, "Ativos", "#16a34a"],
    ["6.000+", "Usuários", "#9333ea"], ["99,9%", "Disponibilidade", "#ea580c"],
  ].map(([n, t, c]) => `<div class="card stat"><b style="color:${c}">${n}</b><span>${t}</span></div>`).join("");
}

function contato() {
  $("info").innerHTML = [
    ["mail", "E-mail", SITE.email], ["phone", "Telefone", SITE.telefone],
    ["pin", "Endereço", SITE.endereco.join("<br>")], ["clock", "Horário", SITE.horario.join("<br>")],
  ].map(([i, t, v]) => `<div class="info"><div class="ico c-blue">${ic(i)}</div><div><h4>${t}</h4><p>${v}</p></div></div>`).join("");
  $("form").addEventListener("submit", e => {
    e.preventDefault();
    const f = e.target;
    const assunto = `[${f.assunto.value}] ${f.nome.value}`;
    const corpo = `${f.msg.value}\n\n— ${f.nome.value} (${f.email.value})`;
    location.href = `mailto:${SITE.email}?subject=${encodeURIComponent(assunto)}&body=${encodeURIComponent(corpo)}`;
    $("notice").style.display = "block";
  });
}

document.addEventListener("DOMContentLoaded", () => {
  layout();
  ({ home, blog, post, equipe, projetos, sistemas, contato })[document.body.dataset.page]?.();
});
