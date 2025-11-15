# Caminho completo: /home/neirivon/SINAPSE2.0/sinapsebr_rubrica/scripts/pages/07_Rubrica_Autoavaliativa_3D.py
# Arquivo: 07_Rubrica_Autoavaliativa_3D.py
# Página Streamlit – Rubrica Autoavaliativa SINAPSE-BR IA em visão 3D interativa

import streamlit as st
from textwrap import dedent

st.set_page_config(
    page_title="Rubrica Autoavaliativa SINAPSE-BR IA – Visão 3D",
    layout="wide",
)

# ==================================================================
#  CSS — ESTILO JEDI + TOOLTIP (REUSA O MESMO PADRÃO)
# ==================================================================

st.markdown(
    """
    <style>
        .titulo-jedi {
            font-size: 2.8rem !important;
            font-weight: 900;
            color: #67e8f9;
            text-align: center;
            margin-bottom: 1.4rem;
        }
        .texto-jedi {
            font-size: 1.26rem !important;
            line-height: 1.75;
            text-align: justify;
            color: #0f172a;
            margin-bottom: 2.4rem;
        }

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
#  TEXTO PRINCIPAL – RUBRICA AUTOAVALIATIVA
# ==================================================================

st.markdown(
    """
    <h1 class="titulo-jedi">🧠 Rubrica Autoavaliativa SINAPSE-BR IA — Visão Teórica e Interativa</h1>

    <p class="texto-jedi">
        A <strong>Rubrica Autoavaliativa SINAPSE-BR IA</strong> foi concebida para apoiar o estudante a assumir um 
        papel de <strong>protagonista</strong> no próprio processo de aprendizagem. Em vez de ser apenas objeto da avaliação,
        o discente passa a <em>avaliar-se</em>, identificar avanços, reconhecer fragilidades e planejar próximos passos,
        em diálogo com o professor e com a rubrica discente.
    </p>

    <p class="texto-jedi">
        Essa perspectiva dialoga com a literatura sobre <strong>metacognição</strong> e <strong>autorregulação</strong> da aprendizagem,
        como os trabalhos de
        <span class="tt">Flavell (1987)
            <span class="tt-text">
                FLAVELL, John. <em>Cognitive Development.</em> Englewood Cliffs: Prentice Hall, 1987.
            </span>
        </span>,
        <span class="tt">Pintrich (2002)
            <span class="tt-text">
                PINTRICH, Paul R. <em>The Role of Metacognitive Knowledge in Learning, Teaching, and Assessing.</em> Theory Into Practice, 41(4), 219–225, 2002.
            </span>
        </span>
        e
        <span class="tt">Zimmerman (2002)
            <span class="tt-text">
                ZIMMERMAN, Barry J. <em>Becoming a self-regulated learner.</em> Theory Into Practice, 41(2), 64–70, 2002.
            </span>
        </span>,
        que enfatizam a importância de o estudante monitorar, regular e refletir sobre suas próprias estratégias de estudo.
    </p>

    <p class="texto-jedi">
        No âmbito da EPT, essa rubrica também se articula com a ideia de <strong>avaliação formativa</strong> e 
        <strong>avaliação para aprender</strong>, como discutem 
        <span class="tt">Black & Wiliam (1998)
            <span class="tt-text">
                BLACK, Paul; WILIAM, Dylan. <em>Inside the black box: Raising standards through classroom assessment.</em> Phi Delta Kappan, 80(2), 139–148, 1998.
            </span>
        </span>
        e
        <span class="tt">Brookhart (2013)
            <span class="tt-text">
                BROOKHART, Susan M. <em>How to Create and Use Rubrics for Formative Assessment and Grading.</em> ASCD, 2013.
            </span>
        </span>,
        pois convida o estudante a compreender os critérios de qualidade e utilizá-los como mapa de navegação da própria aprendizagem.
    </p>

    <p class="texto-jedi">
        A Rubrica Autoavaliativa SINAPSE-BR IA organiza essa reflexão em <strong>oito dimensões</strong>, que abordam:
        motivação, esforço, estratégias de estudo, gestão do tempo, colaboração, ética, uso de tecnologias e planejamento de futuro.
        Elas ajudam a responder, do ponto de vista discente:
        <br><br>
        <strong>🧭 “Como estou aprendendo, o que já conquistei e o que preciso ajustar para continuar avançando?”</strong>
    </p>

    <p class="texto-jedi">
        Abaixo, apresentamos as <strong>8 dimensões da Rubrica Autoavaliativa</strong> em um painel 3D interativo:
        <br><br>
        • <strong>FO</strong> – Foco e Organização do Estudo<br>
        • <strong>EM</strong> – Engajamento e Motivação<br>
        • <strong>ET</strong> – Estratégias de Trabalho e Resolução de Problemas<br>
        • <strong>CO</strong> – Colaboração e Comunicação<br>
        • <strong>RF</strong> – Reflexão Crítica sobre o Desempenho<br>
        • <strong>PR</strong> – Protagonismo e Autorregulação<br>
        • <strong>EC</strong> – Ética, Cuidado e Responsabilidade<br>
        • <strong>PL</strong> – Planejamento de Longo Prazo e Projeto de Vida<br><br>

        Passe o mouse sobre os blocos para ver o efeito 3D e clique em cada dimensão
        para explorar a descrição. A proposta é que o estudante use esta rubrica
        como um espelho formativo, dialogando com o professor e com o SINAPSE-BR IA
        sobre sua trajetória de aprendizagem.
    </p>
    """,
    unsafe_allow_html=True,
)

# ==================================================================
#  PAINEL 3D – RUBRICA AUTOAVALIATIVA (CLASSES EXCLUSIVAS: ra-*)
# ==================================================================

html = dedent("""
<div class="ra-container">
  <div class="ra-grid"></div>

  <div class="ra-panel">
    <h2 id="ra-dim-title">Selecione uma dimensão da Rubrica Autoavaliativa</h2>

    <p id="ra-dim-desc">
      Clique em um bloco para ler a descrição completa da dimensão e refletir
      sobre como ela aparece na sua rotina de estudos e na sua participação
      nos componentes curriculares da EPT.
    </p>

    <h3>Níveis da Rubrica Autoavaliativa (1–5)</h3>
    <ul id="ra-levels">
      <li><strong>1 – Ainda não desenvolvo:</strong> O estudante raramente manifesta essa dimensão em sua prática.</li>
      <li><strong>2 – Em desenvolvimento inicial:</strong> Há sinais pontuais, mas sem constância ou intencionalidade clara.</li>
      <li><strong>3 – Presente com regularidade:</strong> A dimensão aparece na maior parte das situações de estudo.</li>
      <li><strong>4 – Bem consolidada:</strong> O estudante utiliza essa dimensão de forma consciente e estratégica.</li>
      <li><strong>5 – Referência:</strong> A dimensão torna-se marca pessoal e inspira colegas, contribuindo para o coletivo.</li>
    </ul>
  </div>
</div>

<style>
  .ra-container {
    display: grid;
    grid-template-columns: 1.6fr 2.2fr;
    gap: 2rem;
    padding-top: 0.5rem;
  }

  .ra-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1.4rem;
    perspective: 1100px;
  }

  .ra-block {
    width: 140px;
    height: 140px;
    padding: 0.4rem;
    border-radius: 1.1rem;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    cursor: pointer;
    color: white;
    transform-style: preserve-3d;
    transition: transform 0.28s ease, box-shadow 0.28s ease, filter 0.28s ease;
    box-shadow: 0 12px 24px rgba(0,0,0,0.55);
  }

  .ra-block:hover {
    transform: translateY(-14px) scale(1.12) rotateX(9deg);
    box-shadow: 0 22px 40px rgba(0,0,0,0.85);
    filter: brightness(1.14);
  }

  .ra-block.ra-selected {
    transform: translateY(-18px) scale(1.18) rotateX(11deg);
    box-shadow: 0 28px 55px rgba(0,0,0,0.9);
    outline: 3px solid rgba(248, 250, 252, 0.95);
    outline-offset: 3px;
  }

  .ra-sigla {
    font-size: 2.0rem;
    font-weight: 900;
    text-shadow: 0 2px 6px rgba(0,0,0,0.7);
  }

  .ra-title {
    margin-top: 0.3rem;
    font-size: 0.83rem;
    font-weight: 600;
    line-height: 1.15;
    text-shadow: 0 1px 4px rgba(0,0,0,0.5);
    text-align: center;
  }

  .ra-panel {
    background: rgba(5, 10, 25, 0.94);
    border-radius: 1.2rem;
    padding: 1.8rem;
    border: 1px solid rgba(56, 189, 248, 0.7);
    box-shadow: 0 18px 48px rgba(0,0,0,0.8);
    color: #e5e7eb;
  }

  .ra-panel h2 { color: #67e8f9; font-size: 1.5rem; margin-bottom: 0.6rem; }
  .ra-panel h3 { color: #5eead4; font-size: 1.15rem; margin-top: 1.2rem; }
  .ra-panel p  { font-size: 0.98rem; line-height: 1.55; margin-bottom: 0.4rem; }
  .ra-panel ul { font-size: 0.98rem; line-height: 1.55; padding-left: 1.2rem; }

  @media (max-width: 1100px) {
    .ra-container {
      grid-template-columns: 1fr;
    }
    .ra-grid {
      justify-items: center;
    }
  }
</style>

<script>
  const raDimensoes = [
    {
      id: 0,
      sigla: "FO",
      titulo: "Foco e Organização do Estudo",
      desc: "Reflete a capacidade de organizar materiais, ambiente, prioridades e rotinas de estudo de forma coerente com os objetivos de aprendizagem."
    },
    {
      id: 1,
      sigla: "EM",
      titulo: "Engajamento e Motivação",
      desc: "Observa o interesse, a persistência diante de dificuldades e a disposição para participar ativamente das atividades propostas."
    },
    {
      id: 2,
      sigla: "ET",
      titulo: "Estratégias de Trabalho",
      desc: "Analisa o uso de estratégias de leitura, resolução de problemas, elaboração de resumos, mapas conceituais e outras formas de estudo ativo."
    },
    {
      id: 3,
      sigla: "CO",
      titulo: "Colaboração e Comunicação",
      desc: "Verifica como o estudante atua em grupo, escuta colegas, contribui com ideias, pede ajuda e oferece apoio quando necessário."
    },
    {
      id: 4,
      sigla: "RF",
      titulo: "Reflexão Crítica",
      desc: "Avalia a capacidade de analisar o próprio desempenho, reconhecer erros, interpretar feedbacks e transformar isso em aprendizagem."
    },
    {
      id: 5,
      sigla: "PR",
      titulo: "Protagonismo e Autorregulação",
      desc: "Observa se o estudante assume a responsabilidade pela própria aprendizagem, estabelece metas e acompanha o próprio progresso."
    },
    {
      id: 6,
      sigla: "EC",
      titulo: "Ética e Cuidado",
      desc: "Analisa atitudes de respeito, responsabilidade com prazos, honestidade acadêmica e cuidado com o ambiente e com os colegas."
    },
    {
      id: 7,
      sigla: "PL",
      titulo: "Planejamento de Longo Prazo",
      desc: "Verifica se o estudante relaciona os estudos com seu projeto de vida, carreira na EPT e inserção no mundo do trabalho."
    }
  ];

  const raCores = [
    "linear-gradient(135deg, #22c55e, #16a34a)",  // FO
    "linear-gradient(135deg, #f97373, #ec4899)",  // EM
    "linear-gradient(135deg, #3b82f6, #6366f1)",  // ET
    "linear-gradient(135deg, #06b6d4, #0ea5e9)",  // CO
    "linear-gradient(135deg, #a855f7, #e879f9)",  // RF
    "linear-gradient(135deg, #fb923c, #facc15)",  // PR
    "linear-gradient(135deg, #0f766e, #22c55e)",  // EC
    "linear-gradient(135deg, #64748b, #475569)"   // PL
  ];

  const raGrid = document.querySelector(".ra-grid");

  if (raGrid) {
    raDimensoes.forEach((dim, idx) => {
      const div = document.createElement("div");
      div.className = "ra-block";
      div.style.backgroundImage = raCores[idx] || raCores[0];
      div.dataset.id = dim.id;

      const sigla = document.createElement("span");
      sigla.className = "ra-sigla";
      sigla.textContent = dim.sigla;

      const titulo = document.createElement("span");
      titulo.className = "ra-title";
      titulo.textContent = dim.titulo;

      div.appendChild(sigla);
      div.appendChild(titulo);

      div.addEventListener("click", () => {
        document.querySelectorAll(".ra-block").forEach(b =>
          b.classList.remove("ra-selected")
        );
        div.classList.add("ra-selected");

        const titleEl = document.getElementById("ra-dim-title");
        const descEl  = document.getElementById("ra-dim-desc");

        if (titleEl && descEl) {
          titleEl.textContent = dim.sigla + " – " + dim.titulo;
          descEl.textContent  = dim.desc;
        }
      });

      raGrid.appendChild(div);
    });
  }
</script>
""")

st.components.v1.html(html, height=720, scrolling=False)

