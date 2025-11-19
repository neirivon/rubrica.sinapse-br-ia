# Caminho completo: /home/neirivon/SINAPSE2.0/sinapsebr_rubrica/scripts/pages/05_Meta_Rubrica_3D.py
# Arquivo: 05_Meta_Rubrica_3D.py
# Página Streamlit – Meta-Rubrica SINAPSE-BR IA em visão 3D interativa

import streamlit as st
from textwrap import dedent

st.set_page_config(
    page_title="Meta-Rubrica SINAPSE-BR IA – Visão 3D",
    layout="wide",
)

# ==================================================================
#  CSS — ESTILO JEDI + TOOLTIP PARA REFERÊNCIAS
# ==================================================================

st.markdown(
    """
    <style>
        .titulo-jedi {
            font-size: 2.8rem !important;
            font-weight: 900;
            color: #0f172a;  /* título bem legível no fundo claro */
            text-align: center;
            margin-bottom: 1.4rem;
        }
        .texto-jedi {
            font-size: 1.26rem !important;
            line-height: 1.75;
            text-align: justify;
            color: #111827;  /* texto escuro, sem aspecto esmaecido */
            margin-bottom: 2.4rem;
        }
        /* O estilo da dica 3D será injetado diretamente como H4 na seção principal */
        
        /* Tooltip para referências ABNT */
        .tt {
            position: relative;
            color: #0ea5e9;
            cursor: pointer;
            font-weight: 700;
        }
        .tt .tt-text {
            visibility: hidden;
            width: 420px;
            background: rgba(15, 23, 42, 0.97);
            color: #f8fafc;
            text-align: left;
            padding: 14px;
            border-radius: 10px;
            border: 1px solid #38bdf8;
            position: absolute;
            z-index: 9999;
            top: 110%;
            left: 0;
            font-size: 0.86rem;
            line-height: 1.4;
            box-shadow: 0 10px 26px rgba(0,0,0,0.7);
        }
        .tt:hover .tt-text {
            visibility: visible;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ==================================================================
#  TEXTO PRINCIPAL (H1 E PARÁGRAFOS)
# ==================================================================

st.markdown(
    """
    <h1 class="titulo-jedi">🌌 Meta-Rubrica SINAPSE-BR IA — Visão Teórica e Interativa</h1>

    <p class="texto-jedi">
        A <strong>Meta-Rubrica SINAPSE-BR IA</strong> é o instrumento responsável por avaliar a 
        <strong>qualidade das rubricas</strong> utilizadas no sistema SINAPSE-BR — Discente, Docente e Autoavaliativa.
        Sua construção se fundamenta em referenciais clássicos e contemporâneos da avaliação educacional, como 
        <span class="tt">Brookhart (2013)
            <span class="tt-text">BROOKHART, Susan M. <em>How to Create and Use Rubrics for Formative Assessment and Grading.</em> Alexandria, VA: ASCD, 2013.</span>
        </span>,
        <span class="tt">Moskal (2000)
            <span class="tt-text">MOSKAL, Barbara M. <em>Scoring rubrics: What, when and how?</em> Practical Assessment, Research, and Evaluation, v.7, n.3, 2000.</span>
        </span>,
        <span class="tt">Andrade (2000)
            <span class="tt-text">ANDRADE, Heidi Goodrich. <em>Understanding rubrics.</em> Educational Leadership, 57(5), 14–17, 2000.</span>
        </span>,
        <span class="tt">Mertler (2001)
            <span class="tt-text">MERTLER, Craig. <em>Designing scoring rubrics for your classroom.</em> PARE, 7(25), 2001.</span>
        </span> 
        e 
        <span class="tt">Jonsson &amp; Svingby (2007)
            <span class="tt-text">JONSSON, A.; SVINGBY, G. The use of scoring rubrics: Reliability, validity and educational consequences. <em>Educational Research Review</em>, 2(2), 130–144, 2007.</span>
        </span>.
    </p>

    <p class="texto-jedi">
        A Meta-Rubrica responde à pergunta-chave da avaliação formativa:
        <br><strong>🔍 “Uma rubrica é realmente uma boa rubrica?”</strong>
        <br><br>
        Para isso, ela verifica se cada rubrica do SINAPSE-BR apresenta:
        <br>🧩 critérios bem definidos;
        <br>🔎 distinção real entre os níveis de desempenho;
        <br>📘 alinhamento com BNCC, Bloom, DUA e Neuropsicopedagogia;
        <br>🎓 confiabilidade entre avaliadores;
        <br>🧠 promoção da metacognição;
        <br>🌍 sensibilidade territorial (CTC/EJI/ESCS);
        <br>⚙️ aplicabilidade real na prática docente.
    </p>

    <p class="texto-jedi">
        A dimensão da <strong>Avaliação Formativa</strong>, como discutem Black &amp; Wiliam e
        <span class="tt">Brookhart (2013)
            <span class="tt-text">BROOKHART, Susan M. <em>How to Create and Use Rubrics for Formative Assessment.</em></span>
        </span>, reforça que rubricas de qualidade orientam o aprendizado, fornecem devolutivas ricas e promovem autonomia.
        Já a dimensão da <strong>metacognição</strong> dialoga com
        <span class="tt">Flavell (1987)
            <span class="tt-text">FLAVELL, John. <em>Cognitive Development.</em> Prentice Hall, 1987.</span>
        </span> 
        e 
        <span class="tt">Pintrich (2002)
            <span class="tt-text">PINTRICH, Paul R. <em>The Role of Metacognitive Knowledge in Learning.</em> 2002.</span>
        </span>.
    </p>

    <p class="texto-jedi">
        Já os aspectos de <strong>equidade, território e identidade</strong> dialogam com
        <span class="tt">Frigotto (1999)</span>,
        <span class="tt">Ciavatta (2009)</span> e
        <span class="tt">Ramos (2010)</span>,
        reforçando que aprender é um processo situado, atravessado por cultura, território e condições socioeconômicas.
    </p>

    <p class="texto-jedi">
        A seguir estão as <strong>9 dimensões oficiais da Meta-Rubrica</strong>, apresentadas em um painel 3D interativo:
        <br><br>
        • <strong>CC</strong> – Clareza dos Critérios<br>
        • <strong>DN</strong> – Distinção dos Níveis<br>
        • <strong>CF</strong> – Confiabilidade<br>
        • <strong>RR</strong> – Redação da Rubrica<br>
        • <strong>CE</strong> – Comunicação de Expectativas<br>
        • <strong>PD</strong> – Participação Discente<br>
        • <strong>MC</strong> – Metacognição<br>
        • <strong>AT</strong> – Aderência Teórica<br>
        • <strong>AU</strong> – Aplicabilidade<br>
    </p>
    """,
    unsafe_allow_html=True,
)

# ==================================================================
#  TÍTULO EXTRA (REPOSICIONADO AQUI)
# ==================================================================

st.markdown(
    "<h3 style='text-align: center; color: #4b5563; font-weight: 700; margin-top: 1.5rem; margin-bottom: 0.5rem;'>RUBRICA AVALIATIVA DE RUBRICAS</h3>", 
    unsafe_allow_html=True
)

# ==================================================================
#  DICA 3D
# ==================================================================

st.markdown(
    """
    <h4 style='text-align: center; margin-top: 1rem; color: #111827;'>
        Passe o mouse sobre os blocos para ver o efeito 3D. Clique para abrir a explicação completa de cada dimensão.
    </h4>
    """,
    unsafe_allow_html=True,
)

# ==================================================================
#  PAINEL 3D – HTML + CSS + JS
# ==================================================================

html = dedent("""
<div class="mr-container">
  <div class="mr-grid"></div>

  <div class="mr-panel">
    <h2 id="mr-dim-title">Selecione uma dimensão da Meta-Rubrica</h2>

    <p id="mr-dim-desc">
      Clique em qualquer bloco à esquerda para visualizar a descrição completa da dimensão,
      entendendo seu papel na validação das rubricas do sistema SINAPSE-BR IA.
    </p>

    <h3>Níveis da Meta-Rubrica (1–4)</h3>
    <ul id="mr-levels">
      <li><strong>1 – Inaceitável:</strong> A rubrica é inadequada, confusa ou desalinhada com o objetivo avaliativo.</li>
      <li><strong>2 – Aceitável:</strong> Há alguma estrutura, mas com ambiguidades e fragilidades importantes.</li>
      <li><strong>3 – Bom/Sólido:</strong> Rubrica clara, coerente e funcional para avaliação formativa.</li>
      <li><strong>4 – Exemplar:</strong> Modelo de referência: rigorosa, bem fundamentada e altamente operacional.</li>
    </ul>

    <h3>Uso na pesquisa</h3>
    <ul class="mr-usage">
      <li>Validar as rubricas Discente, Docente e Autoavaliativa do SINAPSE-BR IA;</li>
      <li>Guiar revisões até que todas as dimensões atinjam nível Bom/Sólido (3) ou superior;</li>
      <li>Garantir rigor teórico, equidade e aplicabilidade na EPT.</li>
    </ul>
  </div>
</div>

<style>
  body {
    background: radial-gradient(circle at top, #020617, #020617);
  }

  .mr-container {
    display: grid;
    grid-template-columns: 1.5fr 2fr;
    gap: 2rem;
    padding: 1.2rem 1.6rem 2rem 2.6rem;
    font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  }

  .mr-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1.4rem;
    perspective: 1100px;
    margin-top: 2.0rem;
    justify-content: flex-start;
  }

  .mr-block {
    width: 135px;
    height: 135px;
    padding: 0.4rem;
    border-radius: 1.1rem;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    cursor: pointer;
    color: white;
    transform-style: preserve-3d;
    transition:
      transform 0.28s ease,
      box-shadow 0.28s ease,
      filter 0.28s ease;
    box-shadow: 0 12px 24px rgba(0,0,0,0.55);
  }

  .mr-block:hover {
    transform: translateY(-14px) scale(1.12) rotateX(9deg);
    box-shadow: 0 22px 40px rgba(0,0,0,0.85);
    filter: brightness(1.14);
  }

  .mr-block.mr-selected {
    transform: translateY(-18px) scale(1.18) rotateX(11deg);
    box-shadow: 0 28px 55px rgba(0,0,0,0.9);
    outline: 3px solid rgba(248, 250, 252, 0.95);
    outline-offset: 3px;
  }

  .mr-sigla {
    font-size: 2.1rem;
    font-weight: 900;
    text-shadow: 0 2px 6px rgba(0,0,0,0.7);
  }

  .mr-title {
    margin-top: 0.3rem;
    font-size: 0.83rem;
    font-weight: 600;
    line-height: 1.15;
    text-shadow: 0 1px 4px rgba(0,0,0,0.5);
  }

  .mr-panel {
    background: rgba(5, 10, 25, 0.94);
    border-radius: 1.2rem;
    padding: 1.8rem;
    border: 1px solid rgba(56, 189, 248, 0.7);
    box-shadow: 0 18px 48px rgba(0,0,0,0.8);
    color: #e5e7eb;
  }

  .mr-panel h2 {
    color: #67e8f9;
    font-size: 1.5rem;
    margin-bottom: 0.6rem;
  }

  .mr-panel h3 {
    color: #5eead4;
    font-size: 1.15rem;
    margin-top: 1.2rem;
  }

  .mr-panel p {
    font-size: 0.98rem;
    line-height: 1.6;
  }

  .mr-panel ul {
    font-size: 0.98rem;
    line-height: 1.55;
    padding-left: 1.2rem;
  }

  .mr-panel li + li {
    margin-top: 0.25rem;
  }

  .mr-usage {
    margin-top: 0.35rem;
  }

  @media (max-width: 900px) {
    .mr-container {
      grid-template-columns: 1fr;
    }
    .mr-panel {
      margin-top: 1.5rem;
    }
  }
</style>

<script>
  const dimensoes = [
    {
      id: 0,
      sigla: "CC",
      titulo: "Clareza dos Critérios",
      desc: "Avalia se os critérios da rubrica são claros, específicos, não ambíguos e adequados ao produto/tarefa."
    },
    {
      id: 1,
      sigla: "DN",
      titulo: "Distinção dos Níveis",
      desc: "Examina se os níveis são nitidamente distintos, progressivos e coerentes, permitindo diferenciar desempenhos."
    },
    {
      id: 2,
      sigla: "CF",
      titulo: "Confiabilidade",
      desc: "Verifica se diferentes avaliadores, usando a mesma rubrica, chegam a resultados semelhantes."
    },
    {
      id: 3,
      sigla: "RR",
      titulo: "Redação da Rubrica",
      desc: "Considera se a rubrica é bem escrita, objetiva, tecnicamente correta e compreensível."
    },
    {
      id: 4,
      sigla: "CE",
      titulo: "Comunicação de Expectativas",
      desc: "Analisa se a rubrica comunica de forma transparente o que se espera do trabalho antes e durante o processo."
    },
    {
      id: 5,
      sigla: "PD",
      titulo: "Participação Discente",
      desc: "Examina em que medida estudantes participam da construção, revisão ou uso ativo da rubrica."
    },
    {
      id: 6,
      sigla: "MC",
      titulo: "Metacognição",
      desc: "Verifica se a rubrica estimula a reflexão do estudante sobre o próprio processo de aprendizagem."
    },
    {
      id: 7,
      sigla: "AT",
      titulo: "Aderência Teórica",
      desc: "Avalia o alinhamento da rubrica com BNCC, Taxonomia de Bloom, DUA, Neuropsicopedagogia e dimensões territoriais (CTC/EJI/ESCS)."
    },
    {
      id: 8,
      sigla: "AU",
      titulo: "Aplicabilidade",
      desc: "Verifica se a rubrica é viável na prática: tempo de aplicação, número de critérios, clareza operacional e adequação ao contexto da EPT."
    }
  ];

  const cores = [
    "linear-gradient(135deg, #f97373, #ec4899)",  // CC
    "linear-gradient(135deg, #fb923c, #facc15)",  // DN
    "linear-gradient(135deg, #fde047, #22c55e)",  // CF
    "linear-gradient(135deg, #22c55e, #14b8a6)",  // RR
    "linear-gradient(135deg, #14b8a6, #3b82f6)",  // CE
    "linear-gradient(135deg, #38bdf8, #6366f1)",  // PD
    "linear-gradient(135deg, #6366f1, #a855f7)",  // MC
    "linear-gradient(135deg, #a855f7, #e879f9)",  // AT
    "linear-gradient(135deg, #64748b, #475569)"    // AU
  ];

  const grid = document.querySelector(".mr-grid");

  if (grid) {
    dimensoes.forEach((dim, idx) => {
      const div = document.createElement("div");
      div.className = "mr-block";
      div.style.backgroundImage = cores[idx];
      div.dataset.id = dim.id;

      const sigla = document.createElement("span");
      sigla.className = "mr-sigla";
      sigla.textContent = dim.sigla;

      const titulo = document.createElement("span");
      titulo.className = "mr-title";
      titulo.textContent = dim.titulo;

      div.appendChild(sigla);
      div.appendChild(titulo);

      div.addEventListener("click", () => {
        document.querySelectorAll(".mr-block").forEach(b =>
          b.classList.remove("mr-selected")
        );
        div.classList.add("mr-selected");

        const titleEl = document.getElementById("mr-dim-title");
        const descEl = document.getElementById("mr-dim-desc");

        if (titleEl && descEl) {
          titleEl.textContent = dim.sigla + " – " + dim.titulo;
          descEl.textContent = dim.desc;
        }
      });

      grid.appendChild(div);
    });
  }
</script>
""")

st.components.v1.html(html, height=720, scrolling=False)

# ==================================================================
#  VÍDEO NO YOUTUBE – LOGO ABAIXO DO PAINEL 3D
# ==================================================================

st.markdown("---")

st.markdown(
    """
    <h2 style="text-align:center; margin-top:1.5rem; margin-bottom:1rem;
               font-size:2rem; font-weight:800; color:#0f172a;">
        📘 Meta-Rubrica SINAPSE-BR IA — O Instrumento de Validação e Qualidade das Rubricas na EPT
    </h2>

    <div style="display:flex; justify-content:center; margin-bottom:2.5rem;">
        <iframe width="900" height="505"
            src="https://www.youtube.com/embed/L6egxk67Iuw?si=0t2N25BApftovxBP"
            title="Rubrica Avaliativa de Rubricas – O Instrumento que Garante Qualidade, Equidade e Rigor na EPT"
            frameborder="0"
            style="border-radius:14px; max-width:100%;"
            allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
            referrerpolicy="strict-origin-when-cross-origin"
            allowfullscreen
            loading="lazy">
        </iframe>
    </div>
    """,
    unsafe_allow_html=True,
)

