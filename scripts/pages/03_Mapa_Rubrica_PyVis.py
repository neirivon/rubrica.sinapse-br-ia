# /home/neirivon/SINAPSE2.0/sinapsebr_rubrica/scripts/pages/03_Mapa_Rubrica_visnetwork.py
# Mapa mental interativo da Rubrica SINAPSE-BR IA usando vis-network (sem PyVis)

from __future__ import annotations
import json
import streamlit as st
from streamlit.components.v1 import html as st_html

st.set_page_config(page_title="Mapa Rubrica — vis-network", page_icon="🧠", layout="wide")

st.title("🧠 Mapa Mental — Rubrica SINAPSE-BR IA")
st.caption("Interativo, visual e sem dependências extras. Renderiza direto com vis-network via CDN.")

c1, c2, c3 = st.columns(3)
physics = c1.toggle("Física em", value=False)
hierarchical = c2.toggle("Layout hierárquico", value=True)
show_flow = c3.toggle("Mostrar fluxo formativo", value=True)

# --------- Dados do grafo ---------
dims = [
    "Cognitiva","Afetiva","Metodologica","Neurofuncional",
    "Avaliativa","Tecnologica","Territorial","Inclusiva"
]
levels = ["Emergente","Intermediario","Proficiente","Avancado","Expert"]
flow = ["Planejamento","Evidencias observaveis","Feedback formativo","Ajustes didaticos","Reavaliacao"]

nodes = []
edges = []

# Raiz
nodes.append({
    "id": "rubrica",
    "label": "Rubrica SINAPSE BR IA",
    "shape": "ellipse",
    "color": "#1f77b4",
    "font": {"size": 22, "bold": True}
})

# Dimensões
for d in dims:
    nodes.append({"id": d, "label": d, "shape": "box", "color": "#ffd900"})
    edges.append({"from": "rubrica", "to": d})

# Níveis
for d in dims:
    for lv in levels:
        nid = f"{d}:{lv}"
        nodes.append({"id": nid, "label": lv, "shape": "box", "color": "#f3f4f6"})
        edges.append({"from": d, "to": nid, "color": {"color": "#cbd5e1"}})

# Fluxo formativo
if show_flow:
    prev = "rubrica"
    for step in flow:
        sid = f"flow:{step}"
        nodes.append({"id": sid, "label": step, "shape": "box", "color": "#dcfce7"})
        edges.append({"from": prev, "to": sid, "dashes": True, "color": {"color": "#34d399"}})
        prev = sid

# Opções do vis-network
layout_hier = {
    "enabled": True,
    "direction": "LR",
    "sortMethod": "hubsize",
    "levelSeparation": 180,
    "nodeSpacing": 140,
    "treeSpacing": 180,
} if hierarchical else {"enabled": False}

options = {
    "physics": {
        "enabled": bool(physics),
        "solver": "forceAtlas2Based",
        "forceAtlas2Based": {
            "gravitationalConstant": -26,
            "springConstant": 0.08,
            "avoidOverlap": 0.6
        },
        "stabilization": {"enabled": True}
    },
    "layout": {"hierarchical": layout_hier},
    "nodes": {
        "shape": "box",
        "borderWidth": 1,
        "shadow": True,
        "font": {"size": 16, "face": "Inter"}
    },
    "edges": {
        "smooth": {"type": "continuous"},
        "color": {"opacity": 0.35},
        "arrows": {"to": {"enabled": False}}
    },
    "interaction": {"hover": True, "tooltipDelay": 120}
}

nodes_json = json.dumps(nodes, ensure_ascii=False)
edges_json = json.dumps(edges, ensure_ascii=False)
options_json = json.dumps(options, ensure_ascii=False)

# --------- HTML + JS (vis-network via CDN) ---------
html_code = f"""
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8"/>
  <script src="https://unpkg.com/vis-network@9.1.6/standalone/umd/vis-network.min.js"></script>
  <style>
    body {{ margin: 0; }}
    #net {{ width: 100%; height: 760px; background: #ffffff; }}
    .vis-tooltip {{ font-family: Inter, system-ui, Arial; font-size: 14px; }}
  </style>
</head>
<body>
  <div id="net"></div>
  <script>
    const nodes = new vis.DataSet({nodes_json});
    const edges = new vis.DataSet({edges_json});
    const container = document.getElementById('net');
    const data = {{ nodes: nodes, edges: edges }};
    const options = {options_json};
    const network = new vis.Network(container, data, options);
    // Zoom inicial suave
    network.once("stabilizationIterationsDone", function(){{
      network.fit({{animation: true, minZoomLevel: 0.4}});
    }});
  </script>
</body>
</html>
"""

st_html(html_code, height=780, scrolling=False)
st.caption("Renderizado com vis-network. Sem PyVis, sem Jinja2 e sem dor de cabeça 😴")

