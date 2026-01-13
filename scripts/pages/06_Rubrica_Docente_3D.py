# /home/neirivon/SINAPSE2.0/sinapsebr_rubrica/scripts/pages/06_Rubrica_Docente_3D.py
# --------------------------------------------------------------------------------------
# NOME DO SCRIPT: 06_Rubrica_Docente_3D.py
# DESCRIÇÃO: Implementação da Rubrica Docente SINAPSE-BR IA com visualização 3D
#            interativa.
# FUNCIONALIDADES:
#   1. Cards didáticos explicativos sobre o foco e fundamentação da rubrica docente.
#   2. Painel 3D interativo com as 8 dimensões da prática pedagógica.
#   3. Exibição dinâmica de descritores ao clicar nos blocos 3D.
#   4. CSS aprimorado para estética visual profissional ("Jedi").
# AUTOR: Neirivon Elias Cardoso (Adaptado por Gemini)
# PROJETO: Rubrica SINAPSE-BR IA
# DATA: 04/01/2026
# --------------------------------------------------------------------------------------

import streamlit as st
import streamlit.components.v1 as components
from textwrap import dedent

st.set_page_config(
    page_title="Rubrica Docente SINAPSE-BR IA – Visão 3D",
    layout="wide",
)

# ==================================================================
#  CSS — ESTILO VISUAL APRIMORADO (CARDS ARREDONDADOS)
# ==================================================================

st.markdown(
    """
    <style>
        /* Título Principal */
        .titulo-jedi {
            font-size: 2.6rem !important;
            font-weight: 800;
            color: #1e40af; /* Cor Institucional */
            text-align: center;
            margin-bottom: 2rem;
            font-family: 'Segoe UI', sans-serif;
        }

        /* Cards Didáticos (Caixas Arredondadas) */
        .didactic-card {
            padding: 20px;
            border-radius: 15px;
            margin-bottom: 20px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
            font-family: 'Segoe UI', sans-serif;
            line-height: 1.6;
            border-left: 6px solid; 
            transition: transform 0.2s;
        }
        .didactic-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 12px rgba(0,0,0,0.1);
        }

        /* Cores Específicas dos Cards */
        .card-concept {
            background-color: #f0f9ff; /* Azul Claro */
            border-left-color: #0ea5e9;
            color: #0c4a6e;
        }
        .card-theory {
            background-color: #f5f3ff; /* Roxo Claro */
            border-left-color: #8b5cf6;
            color: #4c1d95;
        }
        .card-question {
            background-color: #fff7ed; /* Laranja Claro */
            border-left-color: #f97316;
            color: #7c2d12;
            font-weight: 500;
            font-size: 1.1rem;
            text-align: center;
        }

        /* Títulos dentro dos cards */
        .card-title {
            font-weight: 700;
            font-size: 1.2rem;
            margin-bottom: 10px;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        /* Tooltip para referências ABNT */
        .tt { position: relative; color: inherit; cursor: pointer; font-weight: 700; text-decoration: underline; text-decoration-style: dotted;}
        .tt .tt-text { visibility: hidden; width: 350px; background: #333; color: #fff; text-align: left; padding: 10px; border-radius: 8px; position: absolute; z-index: 10; top: 120%; left: 0; font-size: 0.85rem; font-weight: 400; opacity: 0; transition: opacity 0.3s;}
        .tt:hover .tt-text { visibility: visible; opacity: 1; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ==================================================================
#  CONTEÚDO DIDÁTICO EM CARDS (NOVO LAYOUT)
# ==================================================================

st.markdown('<h1 class="titulo-jedi">👩🏽‍🏫 Rubrica Docente SINAPSE-BR IA — Visão Teórica e Interativa</h1>', unsafe_allow_html=True)

# Layout em Colunas
c1, c2 = st.columns(2)

with c1:
    st.markdown(
        """
        <div class="didactic-card card-concept">
            <div class="card-title">📝 Instrumento e Foco</div>
            A <strong>Rubrica Docente SINAPSE-BR IA</strong> organiza as evidências do trabalho pedagógico.
            <br><br>
            Enquanto a rubrica discente foca o produto e o processo de aprendizagem, esta rubrica destaca:
            <ul>
                <li>A mediação pedagógica e o planejamento.</li>
                <li>As devolutivas formativas (feedback acionável).</li>
                <li>O compromisso com a **equidade** e o **cuidado** com a turma.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

with c2:
    st.markdown(
        """
        <div class="didactic-card card-theory">
            <div class="card-title">📚 Fundamentação e Rigor</div>
            Sua concepção dialoga com a literatura sobre avaliação como regulação das aprendizagens:
            <br><br>
            <ul>
                <li><span class="tt">Brookhart (2013)<span class="tt-text">Defende rubricas como ferramentas de instrução e não apenas de nota.</span></span> e <span class="tt">Perrenoud (1999)<span class="tt-text">Foco na regulação das aprendizagens e desenvolvimento de competências.</span></span>.</li>
                <li><span class="tt">Hadji (2001)<span class="tt-text">Compreende a avaliação como parte constitutiva do ensino (regras do jogo).</span></span> e <span class="tt">Luckesi (2011)<span class="tt-text">Destaca o caráter ético, dialógico e emancipador da avaliação.</span></span>.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Card da Pergunta Central
st.markdown("""
<div class="didactic-card card-question">
    🧭 A Pergunta Norteadora da Avaliação Docente:<br>
    <em>“O trabalho docente, tal como se materializa no curso, favorece aprendizagens profundas, equitativas e significativas?”</em>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

st.markdown(
    """
    <h3 style='text-align: center; color: #4b5563; margin-bottom: 1rem;'>
    AS 8 DIMENSÕES DA PRÁTICA DOCENTE
    </h3>
    <p style='text-align: center; color: #64748b; margin-bottom: 2rem;'>
    Passe o mouse sobre os blocos 3D abaixo para explorar cada dimensão da prática docente.
    </p>
    """, 
    unsafe_allow_html=True
)

# ==================================================================
#  PAINEL 3D – RUBRICA DOCENTE (COM SIGLAS ATUALIZADAS)
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
  /* Container Principal */
  .rd-container {
    display: grid;
    grid-template-columns: 1.6fr 2.2fr;
    gap: 2rem;
    padding-top: 0.5rem;
    align-items: start;
  }

  /* Grade dos Blocos - AGORA RESPONSIVO E COM FLEXBOX */
  .rd-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
    gap: 1.5rem;
    perspective: 1100px;
    padding-top: 20px;
  }

  /* O Bloco (Card) - AGORA EXPANSIVO E COM ALTURA MÍNIMA */
  .rd-block {
    width: 100%;
    min-height: 150px; /* Altura mínima para caber a sigla e o título */
    height: auto;      /* PERMITE QUE O CARD CRESÇA SE O TEXTO FOR MAIOR */
    padding: 15px;
    border-radius: 15px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    cursor: pointer;
    color: white;
    transform-style: preserve-3d;
    transition: transform 0.28s ease, box-shadow 0.28s ease, filter 0.28s ease;
    box-shadow: 0 12px 24px rgba(0,0,0,0.55);
    text-align: center;
    word-wrap: break-word;
  }

  .rd-block:hover {
    transform: translateY(-10px) scale(1.05);
    box-shadow: 0 22px 40px rgba(0,0,0,0.85);
    filter: brightness(1.14);
    z-index: 10;
  }

  .rd-block.rd-selected {
    transform: translateY(-12px) scale(1.1);
    box-shadow: 0 28px 55px rgba(0,0,0,0.9);
    outline: 4px solid rgba(255, 255, 255, 0.8);
    outline-offset: 2px;
    z-index: 20;
  }

  .rd-sigla {
    font-size: 2.2rem;
    font-weight: 900;
    text-shadow: 0 2px 6px rgba(0,0,0,0.6);
    margin-bottom: 8px;
    line-height: 1;
  }

  .rd-title {
    font-size: 0.95rem; 
    font-weight: 600;
    line-height: 1.3;
    text-shadow: 0 1px 4px rgba(0,0,0,0.5);
    word-wrap: break-word; 
  }

  /* Painel de Detalhes (Direita) - CORREÇÃO DE ALTURA CRÍTICA */
  .rd-panel {
    background: rgba(5, 10, 25, 0.94);
    border-radius: 1.2rem;
    padding: 2rem;
    min-height: 520px; /* GARANTE QUE A LISTA COMPLETA CAIBA SEM CORTAR */
    box-shadow: 0 18px 48px rgba(0,0,0,0.8);
    color: #e5e7eb;
    overflow: hidden; 
  }
  
  /* Lista de Níveis - Aumentando margem para melhor visualização */
  #rd-levels li {
    margin-bottom: 0.6rem; 
    font-size: 1.05rem;
    line-height: 1.5;
  }

  .rd-panel h2 { color: #67e8f9; font-size: 1.6rem; margin-bottom: 1rem; border-bottom: 1px solid #334155; padding-bottom: 10px; }
  .rd-panel h3 { color: #5eead4; font-size: 1.2rem; margin-top: 1.5rem; }
  .rd-panel p  { font-size: 1rem; line-height: 1.6; margin-bottom: 0.5rem; }

  @media (max-width: 1100px) {
    .rd-container { grid-template-columns: 1fr; }
    .rd-panel { min-height: 400px; } 
  }
</style>

<script>
  // ESTRUTURA DE DADOS COMPLETA
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
      desc: "Analisa se o docente utiliza a avaliação como episódio de aprendizagem (Brookhart), oferecendo devolutivas claras, específicas e orientadas para a melhoria."
    },
    {
      id: 2,
      sigla: "EC", // ALTERADO DE EQ PARA EC
      titulo: "Equidade e Cuidado com a Turma",
      desc: "Verifica se há atenção à diversidade e interseccionalidade. O professor adapta a mediação para atender às diferentes condições de vida dos estudantes, promovendo inclusão ativa."
    },
    {
      id: 3,
      sigla: "DI",
      titulo: "Diversificação de Instrumentos",
      desc: "Avalia o uso de diferentes instrumentos e metodologias (projetos, portfólios, rubricas, coavaliação) de modo coerente com os objetivos."
    },
    {
      id: 4,
      sigla: "IC", // ALTERADO DE IN PARA IC
      titulo: "Integração Curricular e BNCC/EPT",
      desc: "Examina se o professor articula saberes da EPT com a formação geral, alinhando-se aos eixos do Catálogo Nacional de Cursos Técnicos (CNCT)."
    },
    {
      id: 5,
      sigla: "TE",
      titulo: "Tecnologias Educacionais",
      desc: "Verifica o uso pedagógico e intencional de TDICs (como o SINAPSE-BR IA) para acessibilidade, engajamento e aprofundamento conceitual."
    },
    {
      id: 6,
      sigla: "DR", // ALTERADO DE DV PARA DR
      titulo: "Devolutivas e Registro",
      desc: "Analisa a qualidade dos registros avaliativos (rubricas, relatórios) e das devolutivas, bem como sua utilização para replanejar o ensino."
    },
    {
      id: 7,
      sigla: "RD", // ALTERADO DE RF PARA RD
      titulo: "Reflexão Docente",
      desc: "Observa se o professor analisa criticamente a própria prática, identifica pontos de melhoria e busca formação continuada (Meta-avaliação da prática)."
    }
  ];

  const rdCores = [
    "linear-gradient(135deg, #f97373, #ec4899)",  // PP
    "linear-gradient(135deg, #fb923c, #facc15)",  // FA
    "linear-gradient(135deg, #22c55e, #16a34a)",  // EC (antigo EQ)
    "linear-gradient(135deg, #06b6d4, #3b82f6)",  // DI
    "linear-gradient(135deg, #6366f1, #8b5cf6)",  // IC (antigo IN)
    "linear-gradient(135deg, #0ea5e9, #22c55e)",  // TE
    "linear-gradient(135deg, #a855f7, #e879f9)",  // DR (antigo DV)
    "linear-gradient(135deg, #64748b, #475569)"   // RD (antigo RF)
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
          titleEl.style.color = '#5eead4'; // Destaque visual no título
          descEl.innerHTML  = dim.desc;
        }
      });

      rdGrid.appendChild(div);
    });
  }
</script>
""")

components.html(html, height=750, scrolling=False)
st.caption("Baseado em Brookhart (2013) e adaptado para a EPT.")
