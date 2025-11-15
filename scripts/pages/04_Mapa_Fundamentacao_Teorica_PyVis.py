# /home/neirivon/SINAPSE2.0/sinapsebr_rubrica/scripts/pages/04_Mapa_Fundamentacao_Teorica_visnetwork.py

from __future__ import annotations
import json
import streamlit as st
from streamlit.components.v1 import html as st_html

st.set_page_config(page_title="Fundamentação Teórica — SINAPSE-BR", page_icon="📚", layout="wide")
st.title("📚 Mapa de Fundamento Teórico da Rubrica")
st.caption("Clique em um nó para ver o texto explicativo. O painel à direita fica pronto para copiar/colar no TCC.")

physics = st.toggle("Física em", value=False)

dims = [
    "Cognitiva","Afetiva","Metodologica","Neurofuncional",
    "Avaliativa","Tecnologica","Territorial","Inclusiva"
]

links = {
    "Cognitiva": ["Bloom revisada","Taxonomia SOLO","Psicologia cognitiva"],
    "Afetiva": ["Teorias da motivacao","Autorregulacao da aprendizagem","Neuropsicopedagogia"],
    "Metodologica": ["Metodologias ativas","PBL ABP","Aprendizagem baseada em projetos","Gamificacao"],
    "Neurofuncional": ["Educacao baseada no cerebro MBE","Memoria atencao funcoes executivas","Neuropsicopedagogia"],
    "Avaliativa": ["Avaliacao formativa","Rubricas e criterios","Feedback de qualidade","Coavaliacao"],
    "Tecnologica": ["Competencia digital docente","Cultura de dados e reprodutibilidade","Recursos educacionais abertos"],
    "Territorial": ["Critica do territorio CTC","Equidade justica e inclusao EJI","Indicadores locais IBGE MEC"],
    "Inclusiva": ["Desenho Universal para a Aprendizagem DUA","Acessibilidade","Libras materiais multiformato"]
}

details = {
  "Rubrica SINAPSE BR IA": "Integra dimensões cognitivas, afetivas, metodológicas, neurofuncionais, avaliativas, tecnológicas, territoriais e inclusivas.",
  "Cognitiva": "Bloom revisada e SOLO para progressão de complexidade; apoio ao desenho de tarefas autênticas.",
  "Afetiva": "Motivação, engajamento e autorregulação; feedback que promove autonomia.",
  "Metodologica": "ABP, projetos e gamificação com protagonismo discente.",
  "Neurofuncional": "MBE aplicada: memória, atenção e funções executivas.",
  "Avaliativa": "Rubricas transparentes, feedback acionável e co/autoavaliação.",
  "Tecnologica": "Competência digital docente, REA e cultura de dados.",
  "Territorial": "Leitura crítica do território e EJI com indicadores IBGE/MEC.",
  "Inclusiva": "DUA, acessibilidade e multiformatos."
}
for v in links.values():
    for t in v:
        details.setdefault(t, "Resumo sucinto. Edite o dicionário 'details' no script para ampliar o texto.")

# ---------- NODES & EDGES com garantia de IDs únicos ----------
nodes, edges = [], []
# nó raiz
nodes.append({"id":"Rubrica SINAPSE BR IA","label":"Rubrica SINAPSE BR IA","color":"#f4b400","shape":"dot","size":28})

# adiciona nós de dimensão
for d in dims:
    nodes.append({"id":d,"label":d,"color":"#60a5fa"})
    edges.append({"from":"Rubrica SINAPSE BR IA","to":d,"color":"#d97706"})

# tópicos únicos por label (um nó só, conectado a várias dimensões)
topic_added = set()
for d in dims:
    for t in links[d]:
        if t not in topic_added:
            nodes.append({"id":t,"label":t,"color":"#34d399"})
            topic_added.add(t)
        edges.append({"from":d,"to":t,"color":"#94a3b8"})

options = {
    "physics":{"enabled":bool(physics),"stabilization":{"enabled":True}},
    "interaction":{"hover":True},
    "edges":{"smooth":{"type":"continuous"},"color":{"opacity":0.35}},
    "nodes":{"font":{"size":16,"face":"Inter"},"borderWidth":1,"shadow":True},
    "layout":{"improvedLayout":True}
}

html_code = f"""
<!doctype html>
<html>
<head>
  <meta charset="utf-8" />
  <style>
    body {{ margin:0; font-family: Inter, Arial, sans-serif; }}
    .wrap {{ display:flex; height:760px; }}
    #net {{ flex:1 1 auto; min-height:740px; }}
    #panel {{ width:34%; max-width:520px; padding:18px 20px; border-left:1px solid #e5e7eb; background:#fafafa; overflow:auto; }}
    #panel h3 {{ margin:0 0 8px 0; }}
    .muted {{ color:#64748b; font-size:13px; }}
    .banner {{ background:#fff3cd; color:#92400e; border:1px solid #facc15; padding:8px 10px; margin:10px; border-radius:8px; display:none; }}
    .copy {{ margin-top:8px; padding:6px 10px; border:1px solid #d1d5db; background:#fff; border-radius:6px; cursor:pointer; }}
  </style>
  <script>
    function loadScriptSequential(urls, onDone, onFail) {{
      if (!urls.length) {{ onFail && onFail(); return; }}
      const s = document.createElement('script');
      s.src = urls[0];
      s.onload = onDone;
      s.onerror = () => loadScriptSequential(urls.slice(1), onDone, onFail);
      document.head.appendChild(s);
    }}
    document.addEventListener('DOMContentLoaded', function(){{
      const warn = document.getElementById('warn');
      loadScriptSequential(
        [
          'https://cdn.jsdelivr.net/npm/vis-network@9.1.6/dist/vis-network.min.js',
          'https://unpkg.com/vis-network@9.1.6/standalone/umd/vis-network.min.js'
        ],
        function onOk(){{
          try {{
            const nodes = new vis.DataSet({json.dumps(nodes, ensure_ascii=False)});
            const edges = new vis.DataSet({json.dumps(edges, ensure_ascii=False)});
            const options = {json.dumps(options, ensure_ascii=False)};
            const net = new vis.Network(document.getElementById('net'), {{nodes, edges}}, options);
            const DETAILS = {json.dumps(details, ensure_ascii=False)};
            function showDetail(id){{
              const c = document.getElementById('content');
              const txt = DETAILS[id] || 'Sem texto cadastrado ainda.';
              c.innerHTML = '<strong>'+id+'</strong><br/><br/>' + txt;
            }}
            net.on('selectNode', p => {{ if (p.nodes?.length) showDetail(p.nodes[0]); }});
          }} catch(e) {{
            warn.style.display='block';
            warn.innerText = 'Falha interna ao iniciar o grafo: ' + e;
          }}
        }},
        function onFail(){{
          warn.style.display='block';
          warn.innerText = 'Não consegui carregar a biblioteca vis-network dos CDNs.';
        }}
      );
    }});
  </script>
</head>
<body>
  <div id="warn" class="banner"></div>
  <div class="wrap">
    <div id="net"></div>
    <aside id="panel">
      <h3>Detalhes</h3>
      <p class="muted">Clique em um nó do mapa para ver o resumo teórico pronto para copiar/colar no TCC.</p>
      <div id="content" style="white-space:pre-wrap;"></div>
      <button class="copy" onclick="navigator.clipboard.writeText(document.getElementById('content').innerText)">Copiar texto</button>
    </aside>
  </div>
</body>
</html>
"""

st_html(html_code, height=800, scrolling=False)

