/* Layout compartilhado (cabeçalho e rodapé) + renderização dos posts */
const SITE = {
  nome: "Minerva",
  slogan: "Portal do Conhecimento",
  email: "contato@minerva.org.br",
};

const NAV = [
  ["index.html", "Início"],
  ["blog.html", "Artigos"],
  ["projetos.html", "Projetos"],
  ["equipe.html", "Equipe"],
  ["sobre.html", "Sobre"],
  ["contato.html", "Contato"],
];

const OWL = `<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#c9a227" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4l3 3M20 4l-3 3"/><circle cx="8.5" cy="11" r="3"/><circle cx="15.5" cy="11" r="3"/><path d="M12 14l-1 2h2z"/><path d="M5 11c0 6 3 9 7 9s7-3 7-9"/></svg>`;

function esc(s) {
  return String(s).replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
}

function fmtData(iso) {
  const [a, m, d] = iso.split("-").map(Number);
  return new Date(a, m - 1, d).toLocaleDateString("pt-BR", { day: "numeric", month: "long", year: "numeric" });
}

function capa(p, cls = "cover") {
  const isImg = /\.(jpe?g|png|webp|gif|svg)$/i.test(p.capa || "");
  const bg = isImg
    ? `background-image:url('${esc(p.capa)}')`
    : `background:linear-gradient(135deg, ${p.cor || "#14213d"}, #14213d)`;
  return `<div class="${cls}" style="${bg}">${isImg ? "" : esc(p.capa || "📘")}</div>`;
}

function cardPost(p) {
  return `<a class="card" href="post.html?p=${encodeURIComponent(p.slug)}">
    ${capa(p)}
    <div class="body">
      <span><span class="tag">${esc(p.categoria)}</span></span>
      <h3>${esc(p.titulo)}</h3>
      <p>${esc(p.resumo)}</p>
      <div class="meta"><span>${fmtData(p.data)}</span><span>· ${p.leitura} min de leitura</span></div>
    </div></a>`;
}

function postsOrdenados() {
  return [...POSTS].sort((a, b) => b.data.localeCompare(a.data));
}

function montarLayout() {
  const atual = location.pathname.split("/").pop() || "index.html";
  const links = NAV.map(([h, t]) => `<a href="${h}" class="${atual === h || (atual === "post.html" && h === "blog.html") ? "active" : ""}">${t}</a>`).join("");
  const header = document.getElementById("header");
  if (header) header.outerHTML = `
    <div class="topbar"><div class="wrap"><span>Conhecimento aberto para todos</span><span>${esc(SITE.email)}</span></div></div>
    <header class="site"><div class="wrap">
      <a class="brand" href="index.html"><span class="logo">${OWL}</span><span>${SITE.nome}<small>${SITE.slogan}</small></span></a>
      <button class="menu-btn" aria-label="Abrir menu" onclick="document.querySelector('nav.main').classList.toggle('open')">☰</button>
      <nav class="main">${links}</nav>
    </div></header>`;

  const footer = document.getElementById("footer");
  if (footer) {
    const cats = [...new Set(POSTS.map(p => p.categoria))];
    footer.outerHTML = `
    <footer class="site"><div class="wrap">
      <div class="cols">
        <div><h4>${SITE.nome}</h4><p>Um portal dedicado à educação, à pesquisa e ao compartilhamento do conhecimento. Inspirado em Minerva, a deusa romana da sabedoria.</p></div>
        <div><h4>Navegação</h4>${NAV.map(([h, t]) => `<a href="${h}">${t}</a>`).join("")}</div>
        <div><h4>Categorias</h4>${cats.map(c => `<a href="blog.html?cat=${encodeURIComponent(c)}">${esc(c)}</a>`).join("")}</div>
      </div>
      <div class="copy">© ${new Date().getFullYear()} ${SITE.nome} — ${SITE.slogan}. Todos os direitos reservados.</div>
    </div></footer>`;
  }
}

/* Página inicial */
function renderHome() {
  const lista = postsOrdenados();
  const dest = lista.find(p => p.destaque) || lista[0];
  const fEl = document.getElementById("featured");
  if (fEl && dest) fEl.innerHTML = `
    <a class="featured" href="post.html?p=${encodeURIComponent(dest.slug)}" style="color:inherit">
      ${capa(dest, "cover")}
      <div class="body">
        <span><span class="tag">Destaque · ${esc(dest.categoria)}</span></span>
        <h3>${esc(dest.titulo)}</h3>
        <p style="color:var(--muted)">${esc(dest.resumo)}</p>
        <div class="meta"><span>${esc(dest.autor)}</span><span>· ${fmtData(dest.data)}</span><span>· ${dest.leitura} min</span></div>
      </div></a>`;
  const rEl = document.getElementById("recent");
  if (rEl) rEl.innerHTML = lista.filter(p => p !== dest).slice(0, 6).map(cardPost).join("");
}

/* Lista de artigos com filtro e busca */
function renderBlog() {
  const params = new URLSearchParams(location.search);
  let cat = params.get("cat") || "Todas";
  let q = "";
  const cats = ["Todas", ...new Set(POSTS.map(p => p.categoria))];
  const chips = document.getElementById("chips");
  const grid = document.getElementById("posts");
  const busca = document.getElementById("busca");

  function draw() {
    chips.innerHTML = cats.map(c => `<button class="chip ${c === cat ? "on" : ""}" data-c="${esc(c)}">${esc(c)}</button>`).join("");
    const termo = q.trim().toLowerCase();
    const lista = postsOrdenados().filter(p =>
      (cat === "Todas" || p.categoria === cat) &&
      (!termo || (p.titulo + " " + p.resumo + " " + p.autor).toLowerCase().includes(termo)));
    grid.innerHTML = lista.length ? lista.map(cardPost).join("") : `<p class="empty" style="grid-column:1/-1">Nenhum artigo encontrado.</p>`;
  }
  chips.addEventListener("click", e => { const b = e.target.closest(".chip"); if (b) { cat = b.dataset.c; draw(); } });
  busca.addEventListener("input", e => { q = e.target.value; draw(); });
  draw();
}

/* Página de um artigo */
function renderPost() {
  const slug = new URLSearchParams(location.search).get("p");
  const p = POSTS.find(x => x.slug === slug);
  const head = document.getElementById("post-head");
  const body = document.getElementById("post-body");
  if (!p) {
    head.innerHTML = `<div class="wrap"><h1>Artigo não encontrado</h1><a class="back" href="blog.html">← Voltar aos artigos</a></div>`;
    return;
  }
  document.title = `${p.titulo} — ${SITE.nome}`;
  head.innerHTML = `<div class="wrap">
    <a class="back" href="blog.html">← Todos os artigos</a><br>
    <span class="tag">${esc(p.categoria)}</span>
    <h1>${esc(p.titulo)}</h1>
    <div class="meta"><span>Por ${esc(p.autor)}</span><span>· ${fmtData(p.data)}</span><span>· ${p.leitura} min de leitura</span></div>
  </div>`;
  const outros = postsOrdenados().filter(x => x.slug !== p.slug).slice(0, 3);
  body.innerHTML = `<article class="article">${p.conteudo}</article>
    <section class="block" style="padding-top:0"><div class="wrap">
      <div class="sec-head"><h2>Continue lendo</h2></div>
      <div class="grid">${outros.map(cardPost).join("")}</div>
    </div></section>`;
}

document.addEventListener("DOMContentLoaded", () => {
  montarLayout();
  const page = document.body.dataset.page;
  if (page === "home") renderHome();
  if (page === "blog") renderBlog();
  if (page === "post") renderPost();
});
