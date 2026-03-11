# /home/neirivon/SINAPSE2.0/sinapsebr_rubrica/scripts/pages/05_Mapa_Geral_Rubrica.py
# --------------------------------------------------------------------------------------
# NOME DO SCRIPT: 03_Mapa_Geral_Rubrica.py
# DESCRIÇÃO: Visualização sistêmica e interativa da arquitetura da Rubrica SINAPSE-BR IA.
#            Apresenta o Organismo Multidimensional (Grafo), o vídeo explicativo 
#            e a Régua de Progressão dos Níveis de Proficiência.
#
# FUNCIONALIDADES:
#   1. Hero Section: Arcabouço metafórico do Mainframe SINAPSE.
#   2. Grafo Interativo: Visualização das 8 Dimensões Teóricas com painel fixo (UX).
#   3. Integração Audiovisual: Vídeo narrado da arquitetura com guia didático.
#   4. Régua Pedagógica: Níveis de maturidade baseados em Vygotsky e Bloom.
#
# AUTOR: Neirivon Elias Cardoso
# PROJETO: Rubrica SINAPSE-BR IA — Sistema Integrado Neuropsicopedagógico
# TCC: Pós-Graduação em Docência para a EPT (IFTM)
# DATA: 07/02/2026
# --------------------------------------------------------------------------------------

import streamlit as st
import json
from streamlit.components.v1 import html as st_html

st.set_page_config(page_title="Mapa Geral da Rubrica", page_icon="🧠", layout="wide")

# Bloqueia tradução automática
st.markdown('<meta name="google" content="notranslate">', unsafe_allow_html=True)

# --- ESTILIZAÇÃO E CONCEITO (ARCABOUÇO METAFÓRICO) ---
st.title("🧠 Arquitetura da Rubrica SINAPSE-BR IA")

# Container de Destaque: O Modelo Mental do Projeto (UI/UX Hero Section)
st.markdown("""
<div style="background-color: #0f172a; padding: 25px; border-radius: 15px; border-left: 8px solid #ea580c; margin-bottom: 25px;">
    <h2 style="color: #f8fafc; margin-top: 0;">🌐 O Mainframe da Sinergia Educacional</h2>
    <p style="color: #cbd5e1; font-size: 1.1em; line-height: 1.6;">
        Bem-vindo ao <b>Organismo Multidimensional</b> do SINAPSE-BR IA. Diferente de rubricas estáticas, 
        este artefato opera como um mainframe de processamento pedagógico, onde a <b>Neurociência</b>, 
        o <b>Território</b> e a <b>Tecnologia</b> convergem para ampliar a percepção docente.
    </p>
    <p style="color: #94a3b8; font-style: italic;">
        Explore as conexões sinápticas abaixo para compreender como cada eixo sustenta a avaliação na EPT.
    </p>
</div>
""", unsafe_allow_html=True)

# --- DEFINIÇÃO DAS 8 DIMENSÕES ---
dimensoes = [
    {
        "id": "COG", "label": "Cognitiva", "color": "#3b82f6",
        "desc": "<b>🧠 Base: Bloom & SOLO</b><br>Avalia a progressão dos processos mentais, do 'Lembrar' ao 'Criar'. Foca na complexidade do pensamento."
    },
    {
        "id": "AFE", "label": "Afetiva", "color": "#ef4444",
        "desc": "<b>❤️ Base: Piaget & Wallon</b><br>Avalia o engajamento, a motivação intrínseca e a regulação emocional."
    },
    {
        "id": "MET", "label": "Metodológica", "color": "#10b981",
        "desc": "<b>🛠️ Base: Metodologias Ativas</b><br>Avalia a capacidade de resolver problemas (PBL) e trabalhar por projetos."
    },
    {
        "id": "NEU", "label": "Neurofuncional", "color": "#8b5cf6",
        "desc": "<b>🧬 Base: Cosenza & Guerra</b><br>Avalia funções executivas: atenção sustentada, memória de trabalho e flexibilidade cognitiva."
    },
    {
        "id": "AVA", "label": "Avaliativa", "color": "#f59e0b",
        "desc": "<b>📏 Base: Hoffmann & Brookhart</b><br>Avalia o uso do feedback para autorregulação e compreensão dos critérios de qualidade."
    },
    {
        "id": "TEC", "label": "Tecnológica", "color": "#64748b",
        "desc": "<b>💻 Base: Russell & Norvig</b><br>Avalia o letramento digital, o uso ético de IA e a interação com sistemas de dados."
    },
    {
        "id": "TER", "label": "Territorial", "color": "#14b8a6",
        "desc": "<b>🗺️ Base: Milton Santos & INEP</b><br>Avalia a compreensão do contexto socio-territorial (TMAP) e identidade local."
    },
    {
        "id": "INC", "label": "Inclusiva", "color": "#ec4899",
        "desc": "<b>♿ Base: DUA (CAST)</b><br>Avalia a acessibilidade, o respeito à diversidade e múltiplos meios de expressão."
    }
]

# --- CONSTRUÇÃO DO GRAFO ---
nodes = []
edges = []

tooltip_central = """
<div style='padding:5px;'>
    <strong style='font-size:16px; color:#ea580c'>SINAPSE-BR IA</strong>
    <hr style='margin:5px 0; border-top:1px solid #ccc'>
    O Artefato Central.<br>Integração de Dados, Neurociência e Pedagogia para a EPT.
</div>
"""
nodes.append({
    "id": "SINAPSE", "label": "SINAPSE-BR IA", 
    "color": "#ea580c", "shape": "circle", "size": 45, 
    "font": {"size": 24, "color": "white", "face": "Segoe UI"},
    "info_html": " ".join(tooltip_central.split())
})

for dim in dimensoes:
    painel_html = f"""
    <div style='padding:5px;'>
        <h3 style='margin:0; color:{dim['color']}; font-size:18px;'>{dim['label']}</h3>
        <hr style='margin:8px 0; border-top:1px solid #eee'>
        <div style='font-size:14px; line-height:1.5; color:#334155;'>{dim['desc']}</div>
    </div>
    """
    nodes.append({
        "id": dim["id"], "label": dim["label"], "color": dim["color"], "shape": "box",
        "info_html": " ".join(painel_html.split()), 
        "font": {"color": "white", "size": 18, "face": "Segoe UI"}
    })
    edges.append({"from": "SINAPSE", "to": dim["id"], "color": dim["color"], "width": 3})

# --- INTERFACE VISUAL DO GRAFO ---
c_graph, c_info = st.columns([0.75, 0.25])

with c_graph:
    options = {
        "physics": {
            "enabled": True,
            "solver": "forceAtlas2Based",
            "forceAtlas2Based": {"gravitationalConstant": -100, "springLength": 160, "springConstant": 0.08}
        },
        "layout": {"improvedLayout": True},
        "interaction": {"hover": True, "tooltipDelay": 50},
        "edges": {"smooth": {"type": "continuous"}}
    }

    # Correção: Dobramos as chaves {{ }} para que o Python as interprete como literais na f-string
    html_code = f"""
    <!DOCTYPE html>
    <html>
    <head>
      <script src="https://unpkg.com/vis-network@9.1.6/standalone/umd/vis-network.min.js"></script>
      <style>
        #net {{ width: 100%; height: 600px; background: #ffffff; border: 1px solid #e5e7eb; border-radius: 12px; }}
        #info-panel {{
            position: absolute;
            top: 15px;
            right: 15px;
            width: 260px;
            background: rgba(255, 255, 255, 0.92); 
            backdrop-filter: blur(4px);
            border: 1px solid #cbd5e1;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
            border-radius: 10px;
            padding: 15px;
            font-family: 'Segoe UI', sans-serif;
            z-index: 1000;
            display: none; 
            transition: opacity 0.3s ease;
        }}
        .fade-in {{ opacity: 1; display: block !important; }}
      </style>
    </head>
    <body>
    <div id="net"></div>
    <div id="info-panel"><div id="panel-content"></div></div>
    <script>
      var nodesData = new vis.DataSet({json.dumps(nodes)});
      var edgesData = new vis.DataSet({json.dumps(edges)});
      var container = document.getElementById('net');
      var panel = document.getElementById('info-panel');
      var content = document.getElementById('panel-content');
      
      var data = {{nodes: nodesData, edges: edgesData}};
      var options = {json.dumps(options)};
      var network = new vis.Network(container, data, options);

      network.on("hoverNode", function (params) {{
          var node = nodesData.get(params.node);
          if (node.info_html) {{
              content.innerHTML = node.info_html;
              panel.classList.add('fade-in');
          }}
      }});

      network.on("selectNode", function (params) {{
          if (params.nodes.length == 1) {{
              var node = nodesData.get(params.nodes[0]);
              if (node.info_html) {{
                  content.innerHTML = node.info_html;
                  panel.classList.add('fade-in');
              }}
              network.focus(params.nodes[0], {{
                  scale: 1.2,
                  animation: {{ duration: 600, easingFunction: 'easeInOutQuad' }}
              }});
          }}
      }});
    </script>
    </body>
    </html>
    """
    st_html(html_code, height=620)

with c_info:
    st.info("💡 **Navegação Sinergética**")
    st.markdown("""
    1. Passe o mouse sobre os nós coloridos.
    2. As informações aparecerão no **painel fixo**.
    3. Arraste os nós para organizar a visão.
    """)
    st.markdown("---")
    st.caption("**8 Dimensões Integradas**")
    st.caption("O Mainframe processa estas 8 frentes em tempo real.")

# --- SEÇÃO: O VÍDEO EXPLICATIVO (YOUTUBE) ---
st.divider()
col_v1, col_v2 = st.columns([0.6, 0.4])

with col_v1:
    st.subheader("🎬 Audiovisual: A Arquitetura em Movimento")
    st.video("https://www.youtube.com/watch?v=4gDTF8Wkh50")

with col_v2:
    st.subheader("📖 Guia do Mainframe SINAPSE")
    st.markdown("""
    Este vídeo apresenta a fundamentação estrutural do **SINAPSE-BR IA**.

    * **Integração Multidimensional:** Veja como os oito eixos teóricos orbitam o centro, unindo dados do **INEP/SISTEC**, neurociência e pedagogia.
    * **Régua de Progressão:** Entenda a transição da complexidade do grafo para os níveis pedagógicos.
    * **IA Centrada no Humano:** O sistema atua como um amplificador da expertise docente.
    """)

# --- SEÇÃO: A LÓGICA DOS NÍVEIS ---
st.divider()
st.subheader("📈 A Régua de Progressão: Níveis de Proficiência")

st.markdown("""
<style>
.lvl-card {
    background-color: #f8fafc; 
    border-left: 5px solid; 
    padding: 15px; 
    border-radius: 5px; 
    height: 160px;
    margin-bottom: 10px;
    box-shadow: 2px 2px 5px rgba(0,0,0,0.05);
    transition: transform 0.2s;
}
.lvl-card:hover { transform: translateY(-3px); }
.lvl-title { font-weight: bold; font-size: 1.1em; margin-bottom: 5px; }
.lvl-desc { font-size: 0.9em; color: #475569; }
</style>
""", unsafe_allow_html=True)

c1, c2, c3, c4, c5 = st.columns(5)

def lvl_html(cor, titulo, desc):
    return f"""
    <div class="lvl-card" style="border-left-color: {cor};">
        <div class="lvl-title" style="color: {cor};">{titulo}</div>
        <div class="lvl-desc">{desc}</div>
    </div>
    """

with c1: st.markdown(lvl_html("#94a3b8", "1. Emergente", "Primeiros contatos. Depende de mediação constante."), unsafe_allow_html=True)
with c2: st.markdown(lvl_html("#64748b", "2. Básico", "Compreensão inicial. Executa tarefas simples com roteiro."), unsafe_allow_html=True)
with c3: st.markdown(lvl_html("#475569", "3. Proficiente", "Consolidação. Aplica conceitos em situações padrão."), unsafe_allow_html=True)
with c4: st.markdown(lvl_html("#334155", "4. Avançado", "Fluência. Transfere conhecimento para novos contextos."), unsafe_allow_html=True)
with c5: st.markdown(lvl_html("#0f172a", "5. Expert", "Inovação. Cria novas soluções e liderança sistêmica."), unsafe_allow_html=True)

st.divider()
with st.expander("📘 Fundamentação dos Níveis"):
    st.write("A progressão segue a lógica da Zona de Desenvolvimento Proximal (Vygotsky) e a complexidade da Taxonomia de Bloom Revisada.")
