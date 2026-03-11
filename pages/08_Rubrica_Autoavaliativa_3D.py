# /home/neirivon/SINAPSE2.0/sinapsebr_rubrica/scripts/pages/08_Rubrica_Autoavaliativa_3D.py
# --------------------------------------------------------------------------------------
# NOME DO SCRIPT: 07_Rubrica_Autoavaliativa_3D.py
# DESCRIÇÃO: Implementação da Rubrica Autoavaliativa (Discente) do ecossistema SINAPSE,
#            utilizando visualização 3D interativa e Paleta de Cores Sólidas (Definitiva).
# FUNCIONALIDADES:
#   1. Foco no Aluno Protagonista com cards didáticos sobre metacognição.
#   2. Painel 3D (Cubos) representando as 8 dimensões da aprendizagem.
#   3. Integração com dados regionais (TMAP) para contextualização.
# AUTOR: Neirivon Elias Cardoso
# DATA: 07/02/2026
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
#  CSS — ESTILO VISUAL APRIMORADO
# ==================================================================

st.markdown(
    """
    <style>
        .titulo-jedi {
            font-size: 2.6rem !important;
            font-weight: 800;
            color: #0f172a;
            text-align: center;
            margin-bottom: 2rem;
            font-family: 'Segoe UI', sans-serif;
        }
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
        .didactic-card:hover { transform: translateY(-2px); box-shadow: 0 8px 12px rgba(0,0,0,0.1); }
        .card-concept { background-color: #f0f9ff; border-left-color: #0ea5e9; color: #0c4a6e; }
        .card-theory { background-color: #f5f3ff; border-left-color: #8b5cf6; color: #4c1d95; }
        .card-question { background-color: #fff7ed; border-left-color: #f97316; color: #7c2d12; text-align: center; font-weight: 500; font-size: 1.1rem; }
        .card-title { font-weight: 700; font-size: 1.2rem; margin-bottom: 10px; display: flex; align-items: center; gap: 10px; }
        .tt { position: relative; color: inherit; cursor: pointer; font-weight: 700; text-decoration: underline; text-decoration-style: dotted;}
        .tt .tt-text { visibility: hidden; width: 350px; background: #333; color: #fff; text-align: left; padding: 10px; border-radius: 8px; position: absolute; z-index: 10; top: 120%; left: 0; font-size: 0.85rem; font-weight: 400; opacity: 0; transition: opacity 0.3s;}
        .tt:hover .tt-text { visibility: visible; opacity: 1; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ==================================================================
#  CONTEÚDO DIDÁTICO
# ==================================================================

st.markdown('<h1 class="titulo-jedi">🧠 Rubrica Autoavaliativa: O Aluno Protagonista</h1>', unsafe_allow_html=True)

c1, c2 = st.columns(2)
with c1:
    st.markdown("""
    <div class="didactic-card card-concept">
        <div class="card-title">🚀 Visão Geral e Objetivo</div>
        A <strong>Rubrica Autoavaliativa</strong> apoia o estudante a assumir o <strong>protagonismo</strong> da sua própria aprendizagem.
        <ul>
            <li>Avaliar o próprio desempenho de forma crítica;</li>
            <li>Identificar avanços no território;</li>
            <li>Planejar os próximos passos com autonomia.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="didactic-card card-theory">
        <div class="card-title">📚 Fundamentação Científica</div>
        Esta perspectiva baseia-se em conceitos de <strong>metacognição</strong>:
        <ul>
            <li><span class="tt">Flavell (1987)<span class="tt-text">Pensar sobre o próprio pensar.</span></span></li>
            <li><span class="tt">Brookhart (2013)<span class="tt-text">Avaliação Formativa como processo de aprendizagem.</span></span></li>
        </ul>
        No âmbito da EPT, o foco é a formação de sujeitos autônomos e conscientes de sua realidade local.
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="didactic-card card-question">🧭 "Como estou aprendendo e o que preciso ajustar para continuar avançando?"</div>', unsafe_allow_html=True)
st.divider()

# ==================================================================
#  PAINEL 3D INTERATIVO
# ==================================================================

html_3d = dedent("""
<div class="ra-container">
  <div class="ra-grid"></div>
  <div class="ra-panel">
    <h2 id="ra-dim-title">Selecione uma dimensão</h2>
    <p id="ra-dim-desc">Passe o mouse ou clique nos blocos para entender as competências discentes.</p>
    <h3>Níveis de Autonomia (1–5)</h3>
    <ul id="ra-levels">
      <li><strong>1:</strong> Dependência de mediação constante.</li>
      <li><strong>3:</strong> Autonomia básica na execução.</li>
      <li><strong>5:</strong> Protagonismo e liderança de pares.</li>
    </ul>
  </div>
</div>
<style>
  .ra-container { display: grid; grid-template-columns: 1.5fr 2.5fr; gap: 2rem; font-family: sans-serif; }
  .ra-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 1rem; }
  .ra-block { aspect-ratio: 1; padding: 10px; border-radius: 12px; display: flex; flex-direction: column; justify-content: center; align-items: center; cursor: pointer; color: white; transition: all 0.3s; box-shadow: 0 4px 10px rgba(0,0,0,0.2); text-align: center; }
  .ra-block:hover { transform: translateY(-5px); filter: brightness(1.1); }
  .ra-sigla { font-size: 1.5rem; font-weight: 800; display: block; }
  .ra-title { font-size: 0.7rem; font-weight: 600; }
  .ra-panel { background: white; border: 1px solid #e2e8f0; border-radius: 12px; padding: 20px; color: #334155; }
</style>
<script>
  const raDimensoes = [
    { sigla: "FO", titulo: "Foco e Organização", desc: "Gestão do tempo e dos materiais de estudo.", cor: "#2F5597" },
    { sigla: "EM", titulo: "Engajamento", desc: "Motivação intrínseca e persistência acadêmica.", cor: "#2F5597" },
    { sigla: "ET", titulo: "Estratégias", desc: "Uso de técnicas de estudo ativas.", cor: "#2F5597" },
    { sigla: "CO", titulo: "Colaboração", desc: "Trabalho em equipe e escuta ativa.", cor: "#ED7D31" },
    { sigla: "RC", titulo: "Reflexão Crítica", desc: "Capacidade de analisar os próprios erros.", cor: "#ED7D31" },
    { sigla: "PR", titulo: "Protagonismo", desc: "Responsabilidade pela construção do saber.", cor: "#548235" },
    { sigla: "EC", titulo: "Ética e Cuidado", desc: "Respeito ao coletivo e ao ambiente.", cor: "#548235" },
    { sigla: "PV", titulo: "Projeto de Vida", desc: "Conexão entre o curso e sonhos de carreira.", cor: "#548235" }
  ];
  const grid = document.querySelector(".ra-grid");
  raDimensoes.forEach(dim => {
    const div = document.createElement("div");
    div.className = "ra-block";
    div.style.backgroundColor = dim.cor;
    div.innerHTML = `<span class="ra-sigla">${dim.sigla}</span><span class="ra-title">${dim.titulo}</span>`;
    div.onclick = () => {
      document.getElementById("ra-dim-title").innerText = dim.titulo;
      document.getElementById("ra-dim-title").style.color = dim.cor;
      document.getElementById("ra-dim-desc").innerText = dim.desc;
    };
    grid.appendChild(div);
  });
</script>
""")
components.html(html_3d, height=600)

# ==================================================================
#  INTEGRAÇÃO TMAP / JSON
# ==================================================================
@st.cache_data
def carregar_dados():
    try:
        with open("data/rubrica_discente_regional.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except: return None

dados_tmap = carregar_dados()
if dados_tmap:
    st.subheader("🕵️‍♀️ Explorador Regional")
    escolha = st.selectbox("Escolha a dimensão:", [f"{d['sigla']} - {d['titulo']}" for d in dados_tmap['dimensoes']])
    dim = next(d for d in dados_tmap['dimensoes'] if d['sigla'] == escolha.split(" - ")[0])
    t1, t2 = st.tabs(["📏 A Régua", "📍 Exemplos Regionais"])
    with t1: st.info(dim['niveis'][1]['descricao'])
    with t2:
        for ex in dim['exemplos_regionais']: st.markdown(f"🗺️ *{ex}*")

# ==================================================================
#  VÍDEO E STORYTELLING (CORRIGIDO)
# ==================================================================
st.divider()
st.subheader("🎬 A Jornada do Herói: O Estudante no Território")
st.video("https://www.youtube.com/watch?v=Ay_R1kzGll4")

st.info("""
Este vídeo materializa o **Cubo SINAPSE-BR IA**, narrando a evolução de um estudante do Triângulo Mineiro: do uso passivo da tecnologia à transformação do seu território (Nível 4 - Expert).
""")


# Renderiza o texto didático logo abaixo do vídeo

st.warning("💡 **Dica de Autorregulação:** Comece escolhendo **uma** dimensão para focar hoje e celebre seu progresso!")
