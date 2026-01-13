# /home/neirivon/SINAPSE2.0/sinapsebr_rubrica/scripts/pages/07_Rubrica_Autoavaliativa_3D.py
# --------------------------------------------------------------------------------------
# NOME DO SCRIPT: 07_Rubrica_Autoavaliativa_3D.py
# DESCRIÇÃO: Implementação da Rubrica Autoavaliativa (Discente) do ecossistema SINAPSE,
#            utilizando visualização 3D interativa para engajamento.
# FUNCIONALIDADES:
#   1. Foco no Aluno Protagonista com cards didáticos sobre metacognição.
#   2. Painel 3D (Cubos) representando as 8 dimensões da aprendizagem.
#   3. Atualização de siglas para maior clareza mnemônica (RC, PV).
#   4. Integração opcional com dados regionais (TMAP) para contextualização.
# AUTOR: Neirivon Elias Cardoso (Adaptado por Gemini)
# PROJETO: Rubrica SINAPSE-BR IA
# DATA: 04/01/2026
# --------------------------------------------------------------------------------------

import streamlit as st
import streamlit.components.v1 as components
import json
from textwrap import dedent

st.set_page_config(
    page_title="Rubrica Autoavaliativa SINAPSE-BR IA – Visão 3D",
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
            color: #0f172a;
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

        /* Tooltip (Mantido para referências) */
        .tt { position: relative; color: inherit; cursor: pointer; font-weight: 700; text-decoration: underline; text-decoration-style: dotted;}
        .tt .tt-text { visibility: hidden; width: 350px; background: #333; color: #fff; text-align: left; padding: 10px; border-radius: 8px; position: absolute; z-index: 10; top: 120%; left: 0; font-size: 0.85rem; font-weight: 400; opacity: 0; transition: opacity 0.3s;}
        .tt:hover .tt-text { visibility: visible; opacity: 1; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ==================================================================
#  CONTEÚDO DIDÁTICO EM CARDS
# ==================================================================

st.markdown('<h1 class="titulo-jedi">🧠 Rubrica Autoavaliativa: O Aluno Protagonista</h1>', unsafe_allow_html=True)

# Layout em Colunas para os Conceitos Iniciais
c1, c2 = st.columns(2)

with c1:
    st.markdown("""
    <div class="didactic-card card-concept">
        <div class="card-title">🚀 Visão Geral e Objetivo</div>
        A <strong>Rubrica Autoavaliativa SINAPSE-BR IA</strong> foi concebida para apoiar o estudante a assumir um papel de <strong>protagonista</strong>.
        <br><br>
        Em vez de ser apenas "objeto" da nota, o discente passa a:
        <ul>
            <li>Avaliar o próprio desempenho;</li>
            <li>Identificar avanços e fragilidades;</li>
            <li>Planejar os próximos passos em diálogo com o professor.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="didactic-card card-theory">
        <div class="card-title">📚 Fundamentação Científica</div>
        Esta perspectiva dialoga com a literatura de ponta sobre <strong>metacognição</strong> e <strong>autorregulação</strong>:
        <br><br>
        <ul>
            <li><span class="tt">Flavell (1987)<span class="tt-text">FLAVELL, J. Cognitive Development. 1987.</span></span>: Pensar sobre o pensar.</li>
            <li><span class="tt">Zimmerman (2002)<span class="tt-text">ZIMMERMAN, B. J. Becoming a self-regulated learner. 2002.</span></span>: Ciclos de autorregulação.</li>
            <li><span class="tt">Brookhart (2013)<span class="tt-text">BROOKHART, S. M. How to Create and Use Rubrics. ASCD, 2013.</span></span>: Avaliação como aprendizagem.</li>
        </ul>
        No âmbito da EPT, alinha-se à <strong>Avaliação Formativa</strong>, onde a rubrica serve como mapa de navegação.
    </div>
    """, unsafe_allow_html=True)

# Card da Pergunta Central (Destaque Total)
st.markdown("""
<div class="didactic-card card-question">
    🧭 A Pergunta Norteadora do Estudante:<br>
    <em>“Como estou aprendendo, o que já conquistei e o que preciso ajustar para continuar avançando?”</em>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

st.markdown(
    """
    <h3 style='text-align: center; color: #4b5563; margin-bottom: 1rem;'>
    AS 8 DIMENSÕES DA APRENDIZAGEM DISCENTE
    </h3>
    <p style='text-align: center; color: #64748b; margin-bottom: 2rem;'>
    Passe o mouse sobre os blocos 3D abaixo para explorar cada dimensão da sua trajetória.
    </p>
    """, 
    unsafe_allow_html=True
)

# ==================================================================
#  PAINEL 3D INTERATIVO (CÓDIGO DO CUBO MANTIDO E OTIMIZADO)
# ==================================================================

html = dedent("""
<div class="ra-container">
  <div class="ra-grid"></div>

  <div class="ra-panel">
    <h2 id="ra-dim-title">Selecione uma dimensão</h2>
    <p id="ra-dim-desc">
      Clique nos blocos coloridos para entender o que é esperado em cada área da sua formação.
    </p>

    <h3>Níveis de Autonomia (1–5)</h3>
    <ul id="ra-levels">
      <li><strong>1 – Ainda não desenvolvo:</strong> Preciso de muita ajuda e comandos diretos.</li>
      <li><strong>2 – Em desenvolvimento inicial:</strong> Sinais pontuais, mas sem constância.</li>
      <li><strong>3 – Praticante (Regular):</strong> Tenho autonomia básica na maior parte do tempo.</li>
      <li><strong>4 – Bem consolidada:</strong> Uso a competência de forma consciente e estratégica.</li>
      <li><strong>5 – Referência (Protagonista):</strong> Faço bem e ainda ajudo os colegas.</li>
    </ul>
  </div>
</div>

<style>
  .ra-container { display: grid; grid-template-columns: 1.5fr 2.5fr; gap: 2rem; font-family: 'Segoe UI', sans-serif; }
  .ra-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 1.2rem; perspective: 1000px; }
  
  .ra-block { 
    width: 100%; aspect-ratio: 1; 
    padding: 10px; border-radius: 12px; 
    display: flex; flex-direction: column; justify-content: center; align-items: center; 
    cursor: pointer; color: white; 
    transform-style: preserve-3d; transition: all 0.3s ease;
    box-shadow: 0 8px 15px rgba(0,0,0,0.2);
    text-align: center;
  }

  .ra-block:hover { transform: translateY(-8px) scale(1.05); box-shadow: 0 15px 25px rgba(0,0,0,0.3); filter: brightness(1.1); }
  .ra-block.ra-selected { transform: scale(1.1); box-shadow: 0 0 0 4px rgba(59, 130, 246, 0.5); z-index: 10; }

  .ra-sigla { font-size: 1.8rem; font-weight: 800; display: block; margin-bottom: 5px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); }
  .ra-title { font-size: 0.75rem; font-weight: 600; line-height: 1.2; }

  .ra-panel { 
    background: white; border: 1px solid #e2e8f0; border-radius: 12px; padding: 25px; 
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); color: #334155;
  }
  .ra-panel h2 { color: #0f172a; font-size: 1.5rem; margin-top: 0; border-bottom: 2px solid #e2e8f0; padding-bottom: 10px; }
  .ra-panel h3 { color: #0ea5e9; font-size: 1.1rem; margin-top: 20px; }
  .ra-panel p { font-size: 1rem; line-height: 1.6; }
  .ra-panel li { margin-bottom: 6px; font-size: 0.95rem; }
</style>

<script>
  const raDimensoes = [
    { id: 0, sigla: "FO", titulo: "Foco e Organização", desc: "Reflete a capacidade de organizar materiais, ambiente e tempo. Você consegue manter o <b>foco</b> na tarefa ou se distrai facilmente?" },
    { id: 1, sigla: "EM", titulo: "Engajamento e Motivação", desc: "Observa o interesse e a <b>persistência</b> (resiliência). Você desiste quando fica difícil ou busca alternativas?" },
    { id: 2, sigla: "ET", titulo: "Estratégias de Trabalho", desc: "Analisa o 'como estudar'. Você usa técnicas ativas (resumos, mapas mentais) ou apenas leitura passiva?" },
    { id: 3, sigla: "CO", titulo: "Colaboração", desc: "Verifica a atuação em grupo. Você escuta os colegas? Contribui com ideias? Pede ajuda quando precisa?" },
    { id: 4, sigla: "RC", titulo: "Reflexão Crítica", desc: "Avalia a capacidade de analisar o próprio erro. Você enxerga o erro como fracasso ou como pista para aprender?" },
    { id: 5, sigla: "PR", titulo: "Protagonismo", desc: "Observa a autonomia. Você assume a responsabilidade pelo seu aprendizado ou espera que o professor faça tudo?" },
    { id: 6, sigla: "EC", titulo: "Ética e Cuidado", desc: "Analisa atitudes de respeito, honestidade acadêmica (não copiar) e cuidado com o ambiente escolar." },
    { id: 7, sigla: "PV", titulo: "Projeto de Vida", desc: "Verifica a conexão com o futuro. Você consegue relacionar o que estuda hoje com seus sonhos e carreira na EPT?" }
  ];

  const raCores = [
    "linear-gradient(135deg, #10b981, #047857)",  // FO - Verde
    "linear-gradient(135deg, #f43f5e, #be123c)",  // EM - Rosa/Vermelho
    "linear-gradient(135deg, #3b82f6, #1d4ed8)",  // ET - Azul
    "linear-gradient(135deg, #0ea5e9, #0369a1)",  // CO - Azul Claro
    "linear-gradient(135deg, #8b5cf6, #6d28d9)",  // RC - Roxo (Antigo RF)
    "linear-gradient(135deg, #f59e0b, #b45309)",  // PR - Laranja
    "linear-gradient(135deg, #14b8a6, #0f766e)",  // EC - Verde Água
    "linear-gradient(135deg, #64748b, #334155)"   // PV - Cinza (Antigo PL)
  ];

  const raGrid = document.querySelector(".ra-grid");

  if (raGrid) {
    raDimensoes.forEach((dim, idx) => {
      const div = document.createElement("div");
      div.className = "ra-block";
      div.style.backgroundImage = raCores[idx];
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
        document.querySelectorAll(".ra-block").forEach(b => b.classList.remove("ra-selected"));
        div.classList.add("ra-selected");

        const titleEl = document.getElementById("ra-dim-title");
        const descEl  = document.getElementById("ra-dim-desc");

        if (titleEl && descEl) {
          titleEl.textContent = dim.sigla + " – " + dim.titulo;
          descEl.innerHTML = dim.desc;
        }
      });
      raGrid.appendChild(div);
    });
  }
</script>
""")

components.html(html, height=600, scrolling=False)

# ==================================================================
#  INTEGRAÇÃO TMAP - EXPLORADOR DE IDENTIDADE (NOVO BLOCO)
# ==================================================================
# Este bloco carrega o JSON 'rubrica_discente_regional.json' para mostrar
# exemplos contextualizados do Triângulo Mineiro.

@st.cache_data
def carregar_dados_discente():
    """Carrega os dados regionais do arquivo JSON com cache para performance."""
    try:
        # Tenta carregar da pasta data/ na raiz do projeto
        # Se der erro, verifique se a pasta data existe no mesmo nível da pasta que executa o 'streamlit run'
        with open("data/rubrica_discente_regional.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return None
    except Exception as e:
        return None

dados_tmap = carregar_dados_discente()

if dados_tmap:
    st.markdown("---")
    st.subheader("🕵️‍♀️ Explorador de Identidade: Como aplicar isso na minha realidade?")
    st.markdown("Selecione abaixo uma dimensão para ver exemplos reais de estudantes do **Triângulo Mineiro**:")
    
    # Seletor para aprofundamento
    # Cria uma lista de opções baseada no JSON carregado
    opcoes_siglas = [f"{d['sigla']} - {d['titulo']}" for d in dados_tmap['dimensoes']]
    escolha = st.selectbox("Escolha a dimensão:", options=opcoes_siglas)
    
    # Filtra os dados com base na escolha do usuário
    sigla_selecionada = escolha.split(" - ")[0]
    dimensao = next(d for d in dados_tmap['dimensoes'] if d['sigla'] == sigla_selecionada)
    
    # Layout de Abas: Teoria vs Prática Regional
    t1, t2 = st.tabs(["📏 A Régua (Comparativo)", "📍 Exemplos da Nossa Região"])
    
    with t1:
        c_bad, c_good = st.columns(2)
        with c_bad:
            st.error(f"**⚠️ Ponto de Atenção (Nível 1):**\n\n {dimensao['niveis'][0]['descricao']}")
        with c_good:
            st.success(f"**✅ Onde queremos chegar (Nível 5):**\n\n {dimensao['niveis'][1]['descricao']}")
            
    with t2:
        st.markdown(f"**Veja como outros estudantes aplicam o {dimensao['titulo']}:**")
        for exemplo in dimensao['exemplos_regionais']:
            # Renderiza o exemplo com um ícone de mapa
            st.markdown(f"🗺️ *{exemplo}*", unsafe_allow_html=True)

else:
    # Caso o arquivo JSON não exista, o sistema segue funcionando sem essa seção
    # Isso evita erros fatais (Crash)
    pass 

# ==================================================================
#  RODAPÉ DE REFLEXÃO
# ==================================================================
st.info("""
💡 **Dica para o Estudante:** Não tente ser "5" em tudo agora. O objetivo é olhar para o gráfico e escolher **uma** dimensão para focar nesta semana. Isso é autorregulação!
""")
