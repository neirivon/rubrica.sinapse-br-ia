# /home/neirivon/SINAPSE2.0/sinapsebr_rubrica/scripts/pages/03_Mapa_Geral_Rubrica.py
import streamlit as st
import json
from streamlit.components.v1 import html as st_html

st.set_page_config(page_title="Mapa Geral da Rubrica", page_icon="🧠", layout="wide")

# Bloqueia tradução automática
st.markdown('<meta name="google" content="notranslate">', unsafe_allow_html=True)

# --- INTRODUÇÃO ---
st.title("🧠 Arquitetura da Rubrica SINAPSE-BR IA")
st.markdown("""
Esta visualização apresenta a estrutura sistêmica do instrumento. 
A rubrica não é uma lista linear, mas um **organismo multidimensional** fundamentado em 8 eixos teóricos.
""")

# --- DEFINIÇÃO DAS 8 DIMENSÕES ---
dimensoes = [
    {
        "id": "COG", "label": "Cognitiva", "color": "#3b82f6", # Azul
        "desc": "<b>🧠 Base: Bloom & SOLO</b><br>Avalia a progressão dos processos mentais, do 'Lembrar' ao 'Criar'. Foca na complexidade do pensamento e na profundidade da resposta."
    },
    {
        "id": "AFE", "label": "Afetiva", "color": "#ef4444", # Vermelho
        "desc": "<b>❤️ Base: Piaget & Wallon</b><br>Avalia o engajamento, a motivação intrínseca e a regulação emocional durante a aprendizagem."
    },
    {
        "id": "MET", "label": "Metodológica", "color": "#10b981", # Verde
        "desc": "<b>🛠️ Base: Metodologias Ativas</b><br>Avalia a capacidade de resolver problemas (PBL), trabalhar por projetos e aplicar conhecimento na prática."
    },
    {
        "id": "NEU", "label": "Neurofuncional", "color": "#8b5cf6", # Roxo
        "desc": "<b>🧬 Base: Cosenza & Guerra</b><br>Avalia funções executivas: atenção sustentada, memória de trabalho e flexibilidade cognitiva."
    },
    {
        "id": "AVA", "label": "Avaliativa", "color": "#f59e0b", # Laranja
        "desc": "<b>📏 Base: Hoffmann & Brookhart</b><br>Avalia o uso do feedback para autorregulação e a compreensão dos critérios de qualidade (Avaliação Formativa)."
    },
    {
        "id": "TEC", "label": "Tecnológica", "color": "#64748b", # Cinza
        "desc": "<b>💻 Base: Russell & Norvig</b><br>Avalia o letramento digital, o uso ético de IA e a capacidade de interagir com sistemas de dados."
    },
    {
        "id": "TER", "label": "Territorial", "color": "#14b8a6", # Verde Água
        "desc": "<b>🗺️ Base: Milton Santos & INEP</b><br>Avalia a compreensão do contexto socio-territorial (TMAP) e a aplicação do conhecimento na realidade local/rural."
    },
    {
        "id": "INC", "label": "Inclusiva", "color": "#ec4899", # Rosa
        "desc": "<b>♿ Base: DUA (CAST)</b><br>Avalia a acessibilidade, o respeito à diversidade e o uso de múltiplos meios de expressão."
    }
]

# --- CONSTRUÇÃO DO GRAFO ---
nodes = []
edges = []

# 1. Nó Central (Raiz)
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

# 2. Nós das Dimensões
for dim in dimensoes:
    # HTML do Painel (Limpo e Formatado)
    painel_html = f"""
    <div style='padding:5px;'>
        <h3 style='margin:0; color:{dim['color']}; font-size:18px;'>{dim['label']}</h3>
        <hr style='margin:8px 0; border-top:1px solid #eee'>
        <div style='font-size:14px; line-height:1.5; color:#334155;'>
            {dim['desc']}
        </div>
    </div>
    """
    # Limpeza para JSON
    painel_clean = " ".join(painel_html.split())

    nodes.append({
        "id": dim["id"], 
        "label": dim["label"], 
        "color": dim["color"], 
        "shape": "box",
        "info_html": painel_clean, # Conteúdo que vai para o painel fixo
        "font": {"color": "white", "size": 18, "face": "Segoe UI"}
    })
    edges.append({"from": "SINAPSE", "to": dim["id"], "color": dim["color"], "width": 3})

# --- INTERFACE VISUAL ---
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

    # HTML/JS COM PAINEL DOCKADO (FIXO)
    html_code = f"""
    <!DOCTYPE html>
    <html>
    <head>
      <script src="https://unpkg.com/vis-network@9.1.6/standalone/umd/vis-network.min.js"></script>
      <style>
        #net {{ width: 100%; height: 600px; background: #ffffff; border: 1px solid #e5e7eb; border-radius: 12px; }}
        
        /* O SEGREDO: Painel "Dockado" no Canto Superior Direito */
        #info-panel {{
            position: absolute;
            top: 15px;
            right: 15px;
            width: 260px;
            background: rgba(255, 255, 255, 0.92); /* Efeito Vidro */
            backdrop-filter: blur(4px);
            border: 1px solid #cbd5e1;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
            border-radius: 10px;
            padding: 15px;
            font-family: 'Segoe UI', sans-serif;
            z-index: 1000;
            display: none; /* Começa invisível */
            transition: opacity 0.3s ease;
        }}
        
        /* Animação de entrada */
        .fade-in {{ opacity: 1; display: block !important; }}
      </style>
    </head>
    <body>

    <div id="net"></div>
    
    <div id="info-panel">
        <div id="panel-content"></div>
    </div>

    <script>
      var nodesData = new vis.DataSet({json.dumps(nodes)});
      var edgesData = new vis.DataSet({json.dumps(edges)});
      var container = document.getElementById('net');
      var panel = document.getElementById('info-panel');
      var content = document.getElementById('panel-content');
      
      var data = {{nodes: nodesData, edges: edgesData}};
      var options = {json.dumps(options)};
      var network = new vis.Network(container, data, options);

      // 1. HOVER: Atualiza o painel fixo (Sem seguir o mouse = Sem cortes)
      network.on("hoverNode", function (params) {{
          var nodeId = params.node;
          var node = nodesData.get(nodeId);
          
          if (node.info_html) {{
              content.innerHTML = node.info_html;
              panel.classList.add('fade-in'); // Mostra suavemente
          }}
      }});

      // 2. BLUR: Opcional - Pode manter visível ou esconder ao sair
      // Aqui mantemos visível por um tempo ou até passar em outro
      network.on("blurNode", function (params) {{
          // panel.classList.remove('fade-in'); // Descomente se quiser que suma ao sair
      }});

      // 3. CLICK: Centraliza e destaca
      network.on("selectNode", function (params) {{
          if (params.nodes.length == 1) {{
              var nodeId = params.nodes[0];
              var node = nodesData.get(nodeId);
              
              // Garante atualização no clique também (para mobile/touch)
              if (node.info_html) {{
                  content.innerHTML = node.info_html;
                  panel.classList.add('fade-in');
              }}
              
              network.focus(nodeId, {{
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
    st.info("💡 **Como Interagir:**")
    st.markdown("""
    1. Passe o mouse sobre os nós coloridos.
    2. As informações aparecerão no **painel fixo** (canto direito do mapa).
    3. A física do grafo permite arrastar os nós para organizar a visualização.
    """)
    st.markdown("---")
    st.caption("**8 Dimensões Integradas**")
    st.caption("O sistema SINAPSE não hierarquiza as dimensões; todas orbitam o processo de aprendizagem com igual importância.")


# --- SEÇÃO: A LÓGICA DOS NÍVEIS (Abaixo do Grafo) ---
st.divider()
st.subheader("📈 A Régua de Progressão: Níveis de Proficiência")
st.markdown("""
Diferente de notas (0 a 10), a rubrica utiliza **Níveis de Maturidade** baseados na neuroplasticidade. 
Não se trata de "certo ou errado", mas de "onde o aluno está" e "qual o próximo passo".
""")

# CSS para os Cards de Nível (Estilo Cartão)
st.markdown("""
<style>
.lvl-card {
    background-color: #f8fafc; 
    border-left: 5px solid; 
    padding: 15px; 
    border-radius: 5px; 
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

with c1: st.markdown(lvl_html("#94a3b8", "1. Emergente", "Primeiros contatos. Depende de mediação constante. Atenção flutuante."), unsafe_allow_html=True)
with c2: st.markdown(lvl_html("#64748b", "2. Básico", "Compreensão inicial. Executa tarefas simples com roteiro. Início da autonomia."), unsafe_allow_html=True)
with c3: st.markdown(lvl_html("#475569", "3. Proficiente", "Consolidação. Aplica conceitos em situações padrão. Autorregulação funcional."), unsafe_allow_html=True)
with c4: st.markdown(lvl_html("#334155", "4. Avançado", "Fluência. Transfere conhecimento para novos contextos. Metacognição ativa."), unsafe_allow_html=True)
with c5: st.markdown(lvl_html("#0f172a", "5. Expert", "Inovação. Cria novas soluções. Ensina os pares. Liderança e visão sistêmica."), unsafe_allow_html=True)

st.divider()
with st.expander("📘 Fundamentação dos Níveis"):
    st.write("""
    A progressão segue a lógica da **Zona de Desenvolvimento Proximal (Vygotsky)** e a complexidade da **Taxonomia de Bloom Revisada**. 
    O objetivo do sistema SINAPSE é fornecer *scaffolding* (andaimes) para que o aluno suba de um nível para o outro.
    """)
