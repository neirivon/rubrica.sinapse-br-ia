# Caminho completo: /home/neirivon/SINAPSE2.0/sinapsebr_rubrica/scripts/pages/06_Rubrica_Docente_3D.py
# Arquivo: 06_Rubrica_Docente_3D.py
# Página Streamlit – Rubrica Docente SINAPSE-BR IA em visão 3D interativa

import streamlit as st
from textwrap import dedent

st.set_page_config(
    page_title="Rubrica Docente SINAPSE-BR IA – Visão 3D",
    layout="wide",
)

# ==================================================================
#  CSS — ESTILO JEDI + TOOLTIP PARA REFERÊNCIAS (MESMO PADRÃO)
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
#  TEXTO PRINCIPAL – RUBRICA DOCENTE (BASE DO TCC, ESTILIZADA)
# ==================================================================

st.markdown(
    """
    <h1 class="titulo-jedi">👩🏽‍🏫 Rubrica Docente SINAPSE-BR IA — Visão Teórica e Interativa</h1>

    <p class="texto-jedi">
        A <strong>Rubrica Docente SINAPSE-BR IA</strong> é o instrumento que organiza, de forma criteriosa, 
        as evidências do trabalho pedagógico realizado pelos professores no contexto da Educação Profissional 
        e Tecnológica (EPT). Enquanto a rubrica discente foca o <em>produto</em> e o <em>processo de aprendizagem</em> 
        dos estudantes, a rubrica docente destaca a <strong>mediação pedagógica</strong>, o <strong>planejamento</strong>,
        as <strong>devolutivas formativas</strong> e o compromisso com a <strong>equidade</strong>.
    </p>

    <p class="texto-jedi">
        Sua concepção dialoga com autores que defendem uma avaliação voltada para a aprendizagem, como 
        <span class="tt">Brookhart (2013)
            <span class="tt-text">
                BROOKHART, Susan M. <em>How to Create and Use Rubrics for Formative Assessment and Grading.</em> Alexandria, VA: ASCD, 2013.
            </span>
        </span>,
        <span class="tt">Perrenoud (1999)
            <span class="tt-text">
                PERRENOUD, Philippe. <em>A avaliação: da excelência à regulação das aprendizagens.</em> Porto Alegre: Artes Médicas, 1999.
            </span>
        </span>
        e
        <span class="tt">Hadji (2001)
            <span class="tt-text">
                HADJI, Charles. <em>A avaliação: regras do jogo.</em> Porto Alegre: Artmed, 2001.
            </span>
        </span>,
        que compreendem a avaliação como parte constitutiva do ensino e não apenas como verificação de resultados.
        A rubrica docente também incorpora contribuições de
        <span class="tt">Luckesi (2011)
            <span class="tt-text">
                LUCKESI, Cipriano C. <em>Avaliação da aprendizagem escolar.</em> São Paulo: Cortez, 2011.
            </span>
        </span>, ao destacar o caráter ético, dialógico e emancipador da avaliação.
    </p>

    <p class="texto-jedi">
        No SINAPSE-BR IA, esta rubrica organiza as práticas docentes em <strong>oito dimensões</strong>, que observam:
        planejamento intencional, clareza de objetivos, uso de metodologias ativas, devolutivas formativas,
        atenção à diversidade, uso pedagógico de tecnologias, articulação com a EPT integrada e processos de
        reflexão sobre a própria prática.
        Em conjunto, essas dimensões permitem responder à questão:
        <br><br>
        <strong>🧭 “O trabalho docente, tal como se materializa no curso, favorece aprendizagens profundas, equitativas e significativas?”</strong>
    </p>

    <p class="texto-jedi">
        A seguir, apresentamos as <strong>8 dimensões da Rubrica Docente SINAPSE-BR IA</strong> em um painel 3D interativo.
        Cada bloco colorido reúne uma sigla e um título curto que sintetizam aspectos centrais da ação docente:
        <br><br>
        • <strong>PP</strong> – Planejamento e Propósito Avaliativo<br>
        • <strong>FA</strong> – Foco na Aprendizagem e Feedback<br>
        • <strong>EQ</strong> – Equidade e Cuidado com a Turma<br>
        • <strong>DI</strong> – Diversificação de Instrumentos e Estratégias<br>
        • <strong>IN</strong> – Integração Curricular e BNCC/EPT<br>
        • <strong>TE</strong> – Tecnologias Educacionais e Recursos Digitais<br>
        • <strong>DV</strong> – Devolutivas e Registro Pedagógico<br>
        • <strong>RF</strong> – Reflexão Docente e Desenvolvimento Profissional<br><br>

        Passe o mouse sobre os blocos para sentir o efeito 3D e clique em cada dimensão
        para ler a descrição completa e compreender como ela contribui para uma docência 
        mais formativa, justa e alinhada ao projeto de EPT integrada.
    </p>
    """,
    unsafe_allow_html=True,
)

# ==================================================================
#  PAINEL 3D – RUBRICA DOCENTE (CLASSES EXCLUSIVAS: rd-*)
# ==================================================================

html = dedent("""
<div class="rd-container">
  <div class="rd-grid"></div>

  <div class="rd-panel">
    <h2 id="rd-dim-title">Selecione uma dimensão da Rubrica Docente</h2>

    <p id="rd-dim-desc">
      Clique em qualquer bloco à esquerda para visualizar a descrição completa da dimensão,
      entendendo como ela qualifica o trabalho docente no contexto da Educação Profissional e Tecnológica.
    </p>

    <h3>Níveis da Rubrica Docente (1–5)</h3>
    <ul id="rd-levels">
      <li><strong>1 – Inicial:</strong> A prática docente revela ações pontuais, pouco articuladas e com frágil intencionalidade formativa.</li>
      <li><strong>2 – Básico:</strong> Há esforços de planejamento e acompanhamento, mas com lacunas na explicitação de critérios e devolutivas.</li>
      <li><strong>3 – Desenvolvido:</strong> A docência é consistente, com critérios claros, feedbacks regulares e uso adequado de metodologias.</li>
      <li><strong>4 – Avançado:</strong> O professor integra avaliação formativa, equidade e metodologias ativas de maneira sistemática.</li>
      <li><strong>5 – Referência:</strong> A prática docente torna-se modelo de excelência, inspirando pares e favorecendo aprendizagens profundas e equitativas.</li>
    </ul>
  </div>
</div>

<style>
  /* container geral */
  .rd-container {
    display: grid;
    grid-template-columns: 1.6fr 2.2fr;
    gap: 2rem;
    padding-top: 0.5rem;
  }

  /* grade 3D – 4 colunas x 2 linhas */
  .rd-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1.4rem;
    perspective: 1100px;
  }

  .rd-block {
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

  .rd-block:hover {
    transform: translateY(-14px) scale(1.12) rotateX(9deg);
    box-shadow: 0 22px 40px rgba(0,0,0,0.85);
    filter: brightness(1.14);
  }

  .rd-block.rd-selected {
    transform: translateY(-18px) scale(1.18) rotateX(11deg);
    box-shadow: 0 28px 55px rgba(0,0,0,0.9);
    outline: 3px solid rgba(248, 250, 252, 0.95);
    outline-offset: 3px;
  }

  .rd-sigla {
    font-size: 2.0rem;
    font-weight: 900;
    text-shadow: 0 2px 6px rgba(0,0,0,0.7);
  }

  .rd-title {
    margin-top: 0.3rem;
    font-size: 0.83rem;
    font-weight: 600;
    line-height: 1.15;
    text-shadow: 0 1px 4px rgba(0,0,0,0.5);
    text-align: center;
  }

  .rd-panel {
    background: rgba(5, 10, 25, 0.94);
    border-radius: 1.2rem;
    padding: 1.8rem;
    border: 1px solid rgba(56, 189, 248, 0.7);
    box-shadow: 0 18px 48px rgba(0,0,0,0.8);
    color: #e5e7eb;
  }

  .rd-panel h2 { color: #67e8f9; font-size: 1.5rem; margin-bottom: 0.6rem; }
  .rd-panel h3 { color: #5eead4; font-size: 1.15rem; margin-top: 1.2rem; }
  .rd-panel p  { font-size: 0.98rem; line-height: 1.55; margin-bottom: 0.4rem; }
  .rd-panel ul { font-size: 0.98rem; line-height: 1.55; padding-left: 1.2rem; }

  @media (max-width: 1100px) {
    .rd-container {
      grid-template-columns: 1fr;
    }
    .rd-grid {
      justify-items: center;
    }
  }
</style>

<script>
  const rdDimensoes = [
    {
      id: 0,
      sigla: "PP",
      titulo: "Planejamento e Propósito Avaliativo",
      desc: "Observa se o professor planeja de forma intencional, explicita objetivos, critérios e vínculos com o projeto pedagógico do curso."
    },
    {
      id: 1,
      sigla: "FA",
      titulo: "Foco na Aprendizagem e Feedback",
      desc: "Analisa se o docente utiliza a avaliação para apoiar a aprendizagem, oferecendo devolutivas claras, específicas e orientadas para a melhoria."
    },
    {
      id: 2,
      sigla: "EQ",
      titulo: "Equidade e Cuidado com a Turma",
      desc: "Verifica se há atenção à diversidade, adaptações razoáveis, escuta ativa e sensibilidade às diferentes condições de vida dos estudantes."
    },
    {
      id: 3,
      sigla: "DI",
      titulo: "Diversificação de Instrumentos",
      desc: "Avalia o uso de diferentes instrumentos e metodologias (projetos, problemas, portfólios, rubricas, auto e coavaliação) de modo coerente com os objetivos."
    },
    {
      id: 4,
      sigla: "IN",
      titulo: "Integração Curricular e BNCC/EPT",
      desc: "Examina se o professor articula os componentes curriculares com a BNCC, a EPT integrada, o mundo do trabalho e os projetos de vida dos estudantes."
    },
    {
      id: 5,
      sigla: "TE",
      titulo: "Tecnologias Educacionais",
      desc: "Verifica o uso pedagógico de tecnologias digitais (como o SINAPSE-BR IA), visando acessibilidade, engajamento e aprofundamento conceitual."
    },
    {
      id: 6,
      sigla: "DV",
      titulo: "Devolutivas e Registro",
      desc: "Analisa a qualidade dos registros avaliativos (rubricas, comentários, relatórios) e das devolutivas, bem como sua utilização para replanejar o ensino."
    },
    {
      id: 7,
      sigla: "RF",
      titulo: "Reflexão Docente",
      desc: "Observa se o professor analisa criticamente a própria prática, identifica pontos de melhoria e busca formação continuada."
    }
  ];

  const rdCores = [
    "linear-gradient(135deg, #f97373, #ec4899)",  // PP
    "linear-gradient(135deg, #fb923c, #facc15)",  // FA
    "linear-gradient(135deg, #22c55e, #16a34a)",  // EQ
    "linear-gradient(135deg, #06b6d4, #3b82f6)",  // DI
    "linear-gradient(135deg, #6366f1, #8b5cf6)",  // IN
    "linear-gradient(135deg, #0ea5e9, #22c55e)",  // TE
    "linear-gradient(135deg, #a855f7, #e879f9)",  // DV
    "linear-gradient(135deg, #64748b, #475569)"   // RF
  ];

  const rdGrid = document.querySelector(".rd-grid");

  if (rdGrid) {
    rdDimensoes.forEach((dim, idx) => {
      const div = document.createElement("div");
      div.className = "rd-block";
      div.style.backgroundImage = rdCores[idx] || rdCores[0];
      div.dataset.id = dim.id;

      const sigla = document.createElement("span");
      sigla.className = "rd-sigla";
      sigla.textContent = dim.sigla;

      const titulo = document.createElement("span");
      titulo.className = "rd-title";
      titulo.textContent = dim.titulo;

      div.appendChild(sigla);
      div.appendChild(titulo);

      div.addEventListener("click", () => {
        document.querySelectorAll(".rd-block").forEach(b =>
          b.classList.remove("rd-selected")
        );
        div.classList.add("rd-selected");

        const titleEl = document.getElementById("rd-dim-title");
        const descEl  = document.getElementById("rd-dim-desc");

        if (titleEl && descEl) {
          titleEl.textContent = dim.sigla + " – " + dim.titulo;
          descEl.textContent  = dim.desc;
        }
      });

      rdGrid.appendChild(div);
    });
  }
</script>
""")

st.components.v1.html(html, height=720, scrolling=False)

