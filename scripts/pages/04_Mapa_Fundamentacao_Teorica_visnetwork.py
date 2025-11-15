# /home/neirivon/SINAPSE2.0/sinapsebr_rubrica/scripts/pages/04_Mapa_Fundamentacao_Teorica_visnetwork.py
from __future__ import annotations

import json
from pathlib import Path

import streamlit as st
from streamlit.components.v1 import html as st_html

# ──────────────────────────────────────────────────────────────────────────────
# CONFIG DA PÁGINA
# ──────────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Fundamentação Teórica — SINAPSE-BR",
    page_icon="📚",
    layout="wide",
)

st.title("📚 Mapa de Fundamento Teórico da Rubrica")
st.caption(
    "Clique em um nó para ver o texto explicativo. "
    "O painel à direita fica pronto para copiar/colar no TCC."
)

physics = st.toggle("Física em", value=False)

# ──────────────────────────────────────────────────────────────────────────────
# ESTRUTURA LÓGICA DO GRAFO (DIMENSÕES → TÓPICOS)
# ──────────────────────────────────────────────────────────────────────────────
dims = [
    "Cognitiva", "Afetiva", "Metodologica", "Neurofuncional",
    "Avaliativa", "Tecnologica", "Territorial", "Inclusiva"
]

links = {
    "Cognitiva": ["Bloom revisada", "Taxonomia SOLO", "Psicologia cognitiva"],
    "Afetiva": ["Teorias da motivacao", "Autorregulacao da aprendizagem", "Neuropsicopedagogia"],
    "Metodologica": ["Metodologias ativas", "PBL ABP", "Aprendizagem baseada em projetos", "Gamificacao"],
    "Neurofuncional": ["Educacao baseada no cerebro MBE", "Memoria atencao funcoes executivas", "Neuropsicopedagogia"],
    "Avaliativa": ["Avaliacao formativa", "Rubricas e criterios", "Feedback de qualidade", "Coavaliacao"],
    "Tecnologica": ["Competencia digital docente", "Cultura de dados e reprodutibilidade", "Recursos educacionais abertos"],
    "Territorial": ["Critica do territorio CTC", "Equidade justica e inclusao EJI", "Indicadores locais IBGE MEC"],
    "Inclusiva": ["Desenho Universal para a Aprendizagem DUA", "Acessibilidade", "Libras materiais multiformato"]
}

# ──────────────────────────────────────────────────────────────────────────────
# CARREGAMENTO DOS DETALHES (JSON EXTERNO) COM FALLBACK
# ──────────────────────────────────────────────────────────────────────────────
details_path = Path("/home/neirivon/SINAPSE2.0/sinapsebr_rubrica/data/details_rubrica.json")

details_default = {
    "Rubrica SINAPSE BR IA": (
        "### 🧩 Rubrica SINAPSE BR IA\n"
        "Integra dimensões **cognitivas**, **afetivas**, **metodológicas**, "
        "**neurofuncionais**, **avaliativas**, **tecnológicas**, **territoriais** e "
        "**inclusivas** em um modelo formativo."
    ),
    "Cognitiva": (
        "### 🧠 Dimensão Cognitiva\n"
        "Fundamentada em **Bloom revisada** e **SOLO** para progressão de complexidade.\n"
        "- Foque em tarefas **autênticas** e contextualizadas."
    ),
    "Afetiva": (
        "### 💛 Dimensão Afetiva\n"
        "Motivação, engajamento e **autorregulação** com **feedback acionável**."
    ),
    "Metodologica": (
        "### 🛠️ Dimensão Metodológica\n"
        "ABP, projetos e **gamificação** com protagonismo discente."
    ),
    "Neurofuncional": (
        "### 🧬 Dimensão Neurofuncional\n"
        "**MBE** aplicada: memória, atenção e funções executivas."
    ),
    "Avaliativa": (
        "### 📏 Dimensão Avaliativa\n"
        "Rubricas **transparentes**, feedback acionável e co/autoavaliação."
    ),
    "Tecnologica": (
        "### 💻 Dimensão Tecnológica\n"
        "Competência digital docente, **REA** e **cultura de dados**."
    ),
    "Territorial": (
        "### 🗺️ Dimensão Territorial\n"
        "Leitura crítica do território e **EJI** com indicadores **IBGE/MEC**."
    ),
    "Inclusiva": (
        "### ♿ Dimensão Inclusiva\n"
        "**DUA**, acessibilidade e **multiformatos** desde o desenho."
    )
}

# Tenta ler o JSON externo (com emojis, Markdown e/ou HTML inline)
details: dict[str, str]
try:
    if details_path.exists():
        details = json.loads(details_path.read_text(encoding="utf-8"))
    else:
        details = details_default.copy()
except Exception:
    details = details_default.copy()

# Garante que todos os nós tenham pelo menos um texto genérico
for d in dims:
    details.setdefault(d, details_default.get(d, ""))
for d, topics in links.items():
    for t in topics:
        details.setdefault(
            t,
            "Resumo sucinto. Edite o arquivo **details_rubrica.json** para ampliar o texto."
        )

# Também para o nó raiz
details.setdefault(
    "Rubrica SINAPSE BR IA",
    details_default["Rubrica SINAPSE BR IA"]
)

# ──────────────────────────────────────────────────────────────────────────────
# CONSTRUÇÃO DOS NODES/EDGES (IDs ÚNICOS)
# ──────────────────────────────────────────────────────────────────────────────
nodes, edges = [], []

# raiz
nodes.append({
    "id": "Rubrica SINAPSE BR IA",
    "label": "Rubrica SINAPSE BR IA",
    "color": "#f4b400",
    "shape": "dot",
    "size": 28
})

# dimensões
for d in dims:
    nodes.append({"id": d, "label": d, "color": "#60a5fa"})
    edges.append({"from": "Rubrica SINAPSE BR IA", "to": d, "color": "#d97706"})

# tópicos únicos por label
topic_added = set()
for d in dims:
    for t in links[d]:
        if t not in topic_added:
            nodes.append({"id": t, "label": t, "color": "#34d399"})
            topic_added.add(t)
        edges.append({"from": d, "to": t, "color": "#94a3b8"})

# opções vis-network
options = {
    "physics": {"enabled": bool(physics), "stabilization": {"enabled": True}},
    "interaction": {"hover": True},
    "edges": {"smooth": {"type": "continuous"}, "color": {"opacity": 0.35}},
    "nodes": {"font": {"size": 16, "face": "Inter"}, "borderWidth": 1, "shadow": True},
    "layout": {"improvedLayout": True}
}

# ──────────────────────────────────────────────────────────────────────────────
# HTML (vis-network via CDN) + MARCADOR MARKDOWN (marked.js)
# ──────────────────────────────────────────────────────────────────────────────
html_code = f"""
<!doctype html>
<html>
<head>
  <meta charset="utf-8" />
  <style>
    body {{
      margin:0;
      font-family: Inter, Arial, sans-serif;
      background:#ffffff;
    }}
    .wrap {{
      display:flex;
      height:760px;
    }}
    #net {{
      flex:1 1 auto;
      min-height:740px;
    }}
    #panel {{
      width:34%;
      max-width:520px;
      padding:18px 20px;
      border-left:1px solid #e5e7eb;
      background:#fafafa;
      overflow:auto;
    }}
    #panel h3 {{
      margin:0 0 8px 0;
    }}
    #content h1, #content h2, #content h3 {{
      margin:0 0 6px 0;
    }}
    #content p, #content li {{
      line-height:1.45;
    }}
    .muted {{
      color:#64748b;
      font-size:13px;
    }}
    .banner {{
      background:#fff3cd;
      color:#92400e;
      border:1px solid #facc15;
      padding:8px 10px;
      margin:10px;
      border-radius:8px;
      display:none;
    }}
    .copy {{
      margin-top:8px;
      padding:6px 10px;
      border:1px solid #d1d5db;
      background:#fff;
      border-radius:6px;
      cursor:pointer;
    }}
    .copy:active {{
      transform: translateY(1px);
    }}
  </style>

  <script>
    // Carrega scripts em sequência com fallback:
    function loadScriptSequential(urls, onDone, onFail) {{
      if (!urls.length) {{ onFail && onFail(); return; }}
      const s = document.createElement('script');
      s.src = urls[0];
      s.onload = () => onDone();
      s.onerror = () => loadScriptSequential(urls.slice(1), onDone, onFail);
      document.head.appendChild(s);
    }}

    document.addEventListener('DOMContentLoaded', function(){{
      const warn = document.getElementById('warn');

      // 1) vis-network
      loadScriptSequential(
        [
          'https://cdn.jsdelivr.net/npm/vis-network@9.1.6/dist/vis-network.min.js',
          'https://unpkg.com/vis-network@9.1.6/standalone/umd/vis-network.min.js'
        ],
        function onVisOk(){{
          // 2) marked.js (Markdown parser) — para render a partir do JSON
          loadScriptSequential(
            [
              'https://cdn.jsdelivr.net/npm/marked@12.0.1/marked.min.js',
              'https://unpkg.com/marked@12.0.1/marked.min.js'
            ],
            function onMarkedOk(){{
              try {{
                const nodes = new vis.DataSet({json.dumps(nodes, ensure_ascii=False)});
                const edges = new vis.DataSet({json.dumps(edges, ensure_ascii=False)});
                const options = {json.dumps(options, ensure_ascii=False)};
                const net = new vis.Network(
                  document.getElementById('net'),
                  {{ nodes, edges }},
                  options
                );

                const DETAILS = {json.dumps(details, ensure_ascii=False)};

                function showDetail(id){{
                  const c = document.getElementById('content');
                  const txt = DETAILS[id] || 'Sem texto cadastrado ainda.';
                  // Se começar com '<', damos como HTML; senão, renderizamos como Markdown
                  if (String(txt).trim().startsWith('<')) {{
                    c.innerHTML = txt;
                  }} else {{
                    c.innerHTML = (typeof marked !== 'undefined')
                      ? marked.parse(txt)
                      : txt.replace(/\\n/g, '<br/>');
                  }}
                }}

                net.on('selectNode', p => {{
                  if (p.nodes?.length) showDetail(p.nodes[0]);
                }});

                // estado inicial: mostra o texto do nó raiz
                showDetail('Rubrica SINAPSE BR IA');

              }} catch(e) {{
                warn.style.display='block';
                warn.innerText = 'Falha interna ao iniciar o grafo: ' + e;
              }}
            }},
            function onMarkedFail(){{
              warn.style.display='block';
              warn.innerText = 'Não consegui carregar a biblioteca de Markdown (marked.js). '
                             + 'Os textos serão exibidos sem formatação.';
              try {{
                const nodes = new vis.DataSet({json.dumps(nodes, ensure_ascii=False)});
                const edges = new vis.DataSet({json.dumps(edges, ensure_ascii=False)});
                const options = {json.dumps(options, ensure_ascii=False)};
                const net = new vis.Network(
                  document.getElementById('net'),
                  {{ nodes, edges }},
                  options
                );
                const DETAILS = {json.dumps(details, ensure_ascii=False)};
                function showDetail(id){{
                  const c = document.getElementById('content');
                  const txt = DETAILS[id] || 'Sem texto cadastrado ainda.';
                  c.innerHTML = txt.replace(/\\n/g, '<br/>');
                }}
                net.on('selectNode', p => {{
                  if (p.nodes?.length) showDetail(p.nodes[0]);
                }});
                showDetail('Rubrica SINAPSE BR IA');
              }} catch(e) {{
                warn.style.display='block';
                warn.innerText = 'Falha interna ao iniciar o grafo (sem marked.js): ' + e;
              }}
            }}
          );
        }},
        function onVisFail(){{
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
      <div id="content" style="white-space:normal;"></div>
      <button class="copy" onclick="navigator.clipboard.writeText(document.getElementById('content').innerText)">Copiar texto</button>
    </aside>
  </div>
</body>
</html>
"""

st_html(html_code, height=800, scrolling=False)

