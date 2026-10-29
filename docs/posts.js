/* =========================================================
   POSTS DO PORTAL MINERVA
   Para publicar um novo artigo, copie um bloco { ... } abaixo,
   cole no topo da lista e altere os campos. Salve o arquivo e
   envie ao GitHub — o site atualiza sozinho.
   - slug: identificador único, sem espaços nem acentos
   - data: formato AAAA-MM-DD
   - capa: emoji ou caminho de imagem (ex.: "img/foto.jpg")
   ========================================================= */
const POSTS = [
  {
    slug: "ia-na-sala-de-aula",
    titulo: "Inteligência artificial na sala de aula: aliada ou ameaça?",
    resumo: "Como professores e estudantes podem usar ferramentas de IA de forma ética para aprender mais — e não menos.",
    categoria: "Tecnologia",
    autor: "Dra. Maria Santos",
    data: "2026-10-20",
    leitura: 6,
    capa: "🤖",
    cor: "#1f3160",
    destaque: true,
    conteudo: `
      <p class="lead">A chegada das ferramentas de inteligência artificial às escolas e universidades mudou a forma como estudamos. A pergunta já não é <em>se</em> vamos usá-las, mas <em>como</em>.</p>
      <h2>O que muda para o estudante</h2>
      <p>Assistentes de IA podem explicar um conceito de várias maneiras, gerar exercícios de revisão e dar feedback imediato. Usados como tutores, aceleram o aprendizado. Usados como atalho para entregar trabalhos prontos, fazem o contrário.</p>
      <h2>O papel do professor</h2>
      <p>O professor passa a ser curador e mediador: orienta quando a ferramenta ajuda, ensina a checar fontes e valoriza o raciocínio, não só a resposta final.</p>
      <blockquote>A tecnologia amplia o que já fazemos. Se a intenção é aprender, ela ajuda a aprender.</blockquote>
      <h2>Boas práticas</h2>
      <ul>
        <li>Peça explicações, não respostas prontas.</li>
        <li>Confira as informações em fontes confiáveis.</li>
        <li>Declare quando usou IA em um trabalho.</li>
        <li>Use a ferramenta para revisar, não para pensar por você.</li>
      </ul>`
  },
  {
    slug: "metodo-de-estudo-ativo",
    titulo: "5 técnicas de estudo ativo comprovadas pela ciência",
    resumo: "Releitura e grifos dão a sensação de aprendizado. Estas técnicas, porém, fazem você realmente lembrar.",
    categoria: "Aprendizagem",
    autor: "Equipe Minerva",
    data: "2026-10-12",
    leitura: 5,
    capa: "📚",
    cor: "#2d6a4f",
    conteudo: `
      <p class="lead">Pesquisas em psicologia cognitiva mostram que o cérebro guarda melhor aquilo que ele precisa <em>recuperar</em>, não apenas reler.</p>
      <h2>1. Autoteste</h2><p>Feche o livro e tente lembrar o que leu. Flashcards e questões de prova antigas são ótimos aliados.</p>
      <h2>2. Repetição espaçada</h2><p>Revise o conteúdo em intervalos crescentes: 1 dia, 3 dias, 1 semana, 1 mês.</p>
      <h2>3. Intercalação</h2><p>Misture tipos de exercício em vez de fazer vinte iguais em sequência.</p>
      <h2>4. Elaboração</h2><p>Pergunte-se “por quê?” e “como isso se conecta com o que já sei?”.</p>
      <h2>5. Ensinar alguém</h2><p>Explicar em voz alta revela rapidamente as lacunas do seu entendimento.</p>`
  },
  {
    slug: "workshop-tecnologias-emergentes",
    titulo: "Workshop de Tecnologias Emergentes abre inscrições",
    resumo: "Evento gratuito e aberto ao público reúne pesquisadores para discutir as últimas tendências em inovação.",
    categoria: "Eventos",
    autor: "Comunicação Minerva",
    data: "2026-10-05",
    leitura: 2,
    capa: "🎤",
    cor: "#9c6644",
    conteudo: `
      <p class="lead">O Instituto Minerva realiza mais uma edição do Workshop de Tecnologias Emergentes, com palestras, oficinas práticas e espaço para networking.</p>
      <h2>Programação</h2>
      <ul><li>Inteligência artificial aplicada à educação</li><li>Ciência de dados para iniciantes</li><li>Sustentabilidade e tecnologia</li></ul>
      <h2>Como participar</h2>
      <p>As vagas são limitadas. Entre em contato pela página <a href="contato.html">Contato</a> para garantir a sua inscrição.</p>`
  },
  {
    slug: "publicacao-revista-internacional",
    titulo: "Pesquisa do instituto é publicada em revista internacional",
    resumo: "Artigo sobre otimização de algoritmos ganha destaque e amplia a colaboração com grupos de pesquisa do exterior.",
    categoria: "Pesquisa",
    autor: "Dr. João Silva",
    data: "2026-09-28",
    leitura: 4,
    capa: "🔬",
    cor: "#5a189a",
    conteudo: `
      <p class="lead">O trabalho, desenvolvido ao longo de dois anos, propõe uma nova abordagem para reduzir o custo computacional de algoritmos de busca.</p>
      <h2>Por que isso importa</h2>
      <p>Algoritmos mais eficientes significam sistemas mais rápidos, mais baratos e com menor consumo de energia — um ganho direto para a sustentabilidade.</p>
      <h2>Próximos passos</h2>
      <p>O grupo agora testa a abordagem em aplicações reais de gestão acadêmica, em parceria com o projeto de Sistema de Gestão Acadêmica.</p>`
  },
  {
    slug: "educacao-financeira-jovens",
    titulo: "Educação financeira começa cedo: um guia para jovens",
    resumo: "Orçamento, reserva de emergência e consumo consciente explicados de forma simples para quem está começando.",
    categoria: "Aprendizagem",
    autor: "Willian Oliveira",
    data: "2026-09-18",
    leitura: 7,
    capa: "💡",
    cor: "#c9a227",
    conteudo: `
      <p class="lead">Saber lidar com dinheiro é uma habilidade que se aprende — e quanto antes, melhor.</p>
      <h2>Comece pelo orçamento</h2><p>Anote tudo o que entra e sai durante um mês. Só assim dá para ver para onde o dinheiro está indo.</p>
      <h2>Reserva de emergência</h2><p>Guarde um pouco todo mês até formar um valor que cubra alguns meses de despesas essenciais.</p>
      <h2>Consumo consciente</h2><p>Antes de comprar, pergunte: eu preciso disso ou só quero agora? Esperar 48 horas ajuda a decidir.</p>
      <blockquote>Conhecimento é o melhor investimento que existe.</blockquote>`
  },
  {
    slug: "projeto-ia-sustentabilidade",
    titulo: "Novo projeto de pesquisa em IA para sustentabilidade é aprovado",
    resumo: "Projeto interdisciplinar vai aplicar inteligência artificial ao monitoramento ambiental e recebe financiamento.",
    categoria: "Pesquisa",
    autor: "Comunicação Minerva",
    data: "2026-09-02",
    leitura: 3,
    capa: "🌱",
    cor: "#40916c",
    conteudo: `
      <p class="lead">A proposta reúne especialistas em computação, biologia e engenharia para criar modelos que antecipem riscos ambientais.</p>
      <h2>Objetivos</h2>
      <ul><li>Coletar e organizar dados ambientais abertos.</li><li>Treinar modelos preditivos.</li><li>Disponibilizar painéis públicos de acompanhamento.</li></ul>`
  }
];
