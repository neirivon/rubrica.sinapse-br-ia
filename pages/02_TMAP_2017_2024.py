# /home/neirivon/SINAPSE2.0/sinapsebr_rubrica/scripts/pages/02_TMAP_2017_2024.py
# --------------------------------------------------------------------------------------
# NOME DO SCRIPT: 02_TMAP_2017_2024.py
# DESCRIÇÃO: Visualização interativa da Rede EPT no Território (TMAP) utilizando
#            Teoria dos Grafos e Georreferenciamento Pedagógico.
# FUNCIONALIDADES:
#   1. Visualização em Grafo (Nós = Escolas/Cidades, Arestas = Conexões).
#   2. Interatividade Mouseover (Hover): Tooltips HTML com atraso (debounce) para estabilidade.
#   3. Interatividade Click: Zoom e destaque hierárquico.
#   4. Indicadores de Equidade: Cores (SAEB/Qualidade) e Tamanho (INSE/Vulnerabilidade).
# AUTOR: Neirivon Elias Cardoso (Adaptado por Gemini)
# PROJETO: Rubrica SINAPSE-BR IA
# DATA: 12/01/2026 (Atualizado com otimização de UX/Hover)
# --------------------------------------------------------------------------------------

import streamlit as st
import json
import pandas as pd
from pathlib import Path
from streamlit.components.v1 import html as st_html

st.set_page_config(page_title="TMAP • Rede EPT", page_icon="🌐", layout="wide")

# Bloqueia tradução automática do Chrome
st.markdown('<meta name="google" content="notranslate">', unsafe_allow_html=True)

# --- CONFIGURAÇÃO ---
THIS = Path(__file__).resolve()
JSON_DATA = THIS.parents[2] / "data" / "tmap_2024_completo.json"

@st.cache_data
def load_data():
    if not JSON_DATA.exists():
        st.error(f"❌ Arquivo de dados não encontrado: {JSON_DATA}")
        return []
    with open(JSON_DATA, "r", encoding="utf-8") as f:
        return json.load(f)

data = load_data()

# --- FUNÇÃO DE ESTILO ---
def get_node_style(escola):
    # Tamanho base (aumenta se for vulnerável)
    inse = escola.get('INSE_Class', 'N/A')
    if 'Nível I' in str(inse) or 'Nível II' in str(inse): size = 25
    elif 'Nível III' in str(inse) or 'Nível IV' in str(inse): size = 20
    else: size = 15

    # Cor (SAEB)
    saeb = escola.get('SAEB')
    if saeb:
        try:
            val = float(saeb)
            if val >= 275: color = "#22c55e" # Verde
            elif val >= 250: color = "#84cc16" # Verde Claro
            elif val >= 225: color = "#facc15" # Amarelo
            else: color = "#ef4444" # Vermelho
        except: color = "#94a3b8"
    else:
        color = "#94a3b8" # Cinza

    return color, size

# --- SIDEBAR ---
with st.sidebar:
    st.page_link("Apresentacao.py", label="🏠 Apresentação")
    st.divider()
    st.markdown("### 🎯 Filtros")
    all_munis = ["Todos"] + sorted([m['Municipio'] for m in data])
    sel_muni = st.selectbox("Município:", all_munis)
    
    st.info("👆 **Interação:** Clique em uma bolinha para dar **Zoom** e ver detalhes.")
    
    with st.expander("📝 Legenda Técnica (Equidade)"):
        st.markdown("""
        **Cores (Qualidade - Nota SAEB):**
        🟢 **Verde:** >= 275 (Excelente)
        🟡 **Amarelo:** 225 a 274 (Médio)
        🔴 **Vermelho:** < 225 (Atenção)
        ⚪ **Cinza (N/A):** Dado não disponível no INEP.
        
        *Nota:* O status **N/A** indica escolas que não participaram do SAEB ou não atingiram o quórum mínimo de alunos.
        
        **Tamanho (Vulnerabilidade - INSE):**
        Quanto **maior** o nó, **menor** o nível socioeconômico da escola.
        """)

# --- CONSTRUÇÃO DO GRAFO ---
nodes = []
edges = []

if data:
    # Nó Raiz
    nodes.append({
        "id": "ROOT", "label": "TMAP 2024\nRede EPT", 
        "color": "#1e40af", "shape": "box", "size": 40, 
        "font": {"color": "white", "size": 20, "face": "Arial"}
    })

    for muni in data:
        if sel_muni != "Todos" and muni['Municipio'] != sel_muni: continue

        muni_name = muni['Municipio']
        total_mat = int(float(muni.get('Total_Matriculas', 0)))
        inse_muni = muni.get('INSE_Medio_Municipal')
        
        # Cálculo rápido de estatísticas do município
        total_escolas = len(muni.get('Escolas', []))
        rurais = sum(1 for e in muni.get('Escolas', []) if 'Rural' in str(e.get('Zona', '')))
        pct_rural = (rurais / total_escolas * 100) if total_escolas > 0 else 0
        
        # TOOLTIP DO MUNICÍPIO (NOVO!)
        muni_tooltip = f"""
        <div style='padding:5px;'>
            <h3 style='margin:0; color:#f97316; font-size:16px;'>📍 {muni_name}</h3>
            <hr style='border:0; border-top:1px solid #eee; margin:5px 0;'>
            <b>🎓 Total Matrículas EPT:</b> {total_mat}<br>
            <b>🏫 Total Escolas:</b> {total_escolas}<br>
            <b>🌾 Escolas Rurais:</b> {rurais} ({pct_rural:.1f}%)<br>
            <b>📊 INSE Médio (Cidade):</b> {inse_muni if inse_muni else 'N/A'}
        </div>
        """

        # Nó Município
        nodes.append({
            "id": muni_name, "label": muni_name, 
            "color": "#f97316", "shape": "ellipse", "value": total_mat,
            "group": "city",
            "info_html": muni_tooltip, # HTML Injetado
            "font": {"size": 16}
        })
        edges.append({"from": "ROOT", "to": muni_name, "color": "#cbd5e1"})

        for esc in muni.get('Escolas', []):
            e_id = f"{muni_name}_{esc['Nome']}"
            color, size = get_node_style(esc)
            
            # Ícones DUA
            infra = esc.get('Infra', {})
            i_acc = "♿" if infra.get('Acessibilidade') else "❌"
            i_net = "📶" if infra.get('Internet') else "❌"
            i_lab = "💻" if infra.get('Lab_Info') else "❌"
            
            # Lista de Cursos
            cursos_html = ""
            if esc.get('Cursos'):
                for c in esc['Cursos']:
                    cursos_html += f"<li style='margin-bottom:4px;'>{c['Nome']} <span style='color:#666; font-size:0.85em'>({c['Matriculas']} mat.)</span></li>"
            else:
                cursos_html = "<li><i>Sem cursos registrados</i></li>"

            # CONTEÚDO DO TOOLTIP DA ESCOLA
            painel_html = f"""
            <div style='padding:5px;'>
                <h3 style='margin:0; color:{color}; font-size:16px;'>{esc['Nome']}</h3>
                <p style='margin:2px 0; font-size:11px; color:#555;'>{esc.get('Rede')} | {esc.get('Zona')}</p>
                <hr style='border:0; border-top:1px solid #eee; margin:5px 0;'>
                
                <div style='display:flex; justify-content:space-between; margin-bottom:5px;'>
                    <span>📊 <b>INSE:</b> {esc.get('INSE_Class', 'N/A')}</span>
                    <span>🎓 <b>SAEB:</b> {esc.get('SAEB') or 'N/A'}</span>
                </div>
                
                <div style='background:#f8fafc; padding:5px; border-radius:4px; font-size:12px;'>
                    <b>Infraestrutura (DUA):</b><br>
                    {i_acc} Acessibilidade &nbsp; {i_net} Internet &nbsp; {i_lab} Lab
                </div>
                
                <p style='margin:5px 0 0 0; font-weight:bold; font-size:12px;'>📚 Cursos:</p>
                <ul style='padding-left:15px; margin:2px 0; font-size:11px;'>
                    {cursos_html}
                </ul>
            </div>
            """

            nodes.append({
                "id": e_id, 
                "label": esc['Nome'],
                "color": color, 
                "size": size, 
                "shape": "dot",
                "info_html": painel_html,
                "font": {"size": 0}
            })
            edges.append({"from": muni_name, "to": e_id, "color": color})

# --- RENDERIZAÇÃO ---
st.title("🌐 Rede EPT no TMAP (2024): Equidade e Infraestrutura")
st.caption("Visualização baseada nos Microdados do Censo 2024, SAEB 2023 e INSE 2021. Clique para interagir.")

if not nodes:
    st.warning("⚠️ Nenhum dado carregado.")
else:
    # Aumentei o tooltipDelay para 300 para evitar disparos acidentais
    options = {
        "physics": {"enabled": True, "stabilization": {"enabled": True}},
        "layout": {"improvedLayout": True},
        "interaction": {"hover": True, "hoverConnectedEdges": False, "tooltipDelay": 300},
        "edges": {"smooth": False, "color": {"inherit": "from", "opacity": 0.3}}
    }
    
    html_code = f"""
    <!DOCTYPE html>
    <html>
    <head>
      <script src="https://unpkg.com/vis-network@9.1.6/standalone/umd/vis-network.min.js"></script>
      <style>
        #net {{ width: 100%; height: 700px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; }}
        #info-panel {{
            position: absolute;
            display: none;
            width: 320px;
            background: white;
            border: 1px solid #cbd5e1;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
            padding: 10px;
            font-family: 'Segoe UI', sans-serif;
            z-index: 1000;
            pointer-events: none;
            transition: opacity 0.2s ease-in-out; /* Suaviza a aparição */
        }}
      </style>
    </head>
    <body>
    <div id="info-panel"></div>
    <div id="net"></div>
    <script>
      var nodesData = new vis.DataSet({json.dumps(nodes)});
      var edgesData = new vis.DataSet({json.dumps(edges)});
      var container = document.getElementById('net');
      var panel = document.getElementById('info-panel');
      var data = {{nodes: nodesData, edges: edgesData}};
      var options = {json.dumps(options)};
      var network = new vis.Network(container, data, options);
      
      var hideTimeout; // Variável para controlar o atraso no fechamento

      network.on("hoverNode", function (params) {{
          // Se houver um comando para esconder pendente, cancela ele (usuário voltou rápido)
          if (hideTimeout) {{
              clearTimeout(hideTimeout);
              hideTimeout = null;
          }}

          var nodeId = params.node;
          var node = nodesData.get(nodeId);
          if (node.info_html) {{
              var pos = network.canvasToDOM(network.getPositions([nodeId])[nodeId]);
              panel.innerHTML = node.info_html;
              panel.style.display = 'block';
              panel.style.opacity = '1';
              panel.style.top = (pos.y - 20) + 'px';
              panel.style.left = (pos.x + 20) + 'px';
          }}
      }});

      network.on("blurNode", function (params) {{
          // Aguarda 200ms antes de esconder o painel (Debounce)
          hideTimeout = setTimeout(function() {{
              panel.style.opacity = '0';
              setTimeout(function(){{ 
                  if(panel.style.opacity === '0') panel.style.display = 'none'; 
              }}, 200); // Espera a transição CSS terminar para dar display none
          }}, 200);
      }});

      network.on("selectNode", function (params) {{
          if (params.nodes.length == 1) {{
              var nodeId = params.nodes[0];
              var node = nodesData.get(nodeId);
              if (nodeId !== "ROOT" && !node.group) {{
                  node.shape = 'box';
                  node.font = {{ size: 14, color: 'white', background: node.color }};
                  nodesData.update(node);
                  network.focus(nodeId, {{ scale: 1.5, animation: {{ duration: 800, easingFunction: 'easeInOutQuad' }} }});
              }}
          }}
      }});

      network.on("deselectNode", function (params) {{
          var updates = [];
          nodesData.forEach(function(node) {{
              if (node.id !== "ROOT" && !node.group) {{
                  updates.push({{id: node.id, shape: 'dot', font: {{size: 0}}}});
              }}
          }});
          nodesData.update(updates);
          network.fit({{ animation: {{ duration: 800, easingFunction: 'easeInOutQuad' }} }});
      }});

      network.on("stabilizationIterationsDone", function () {{
          network.setOptions( {{ physics: false }} );
      }});
    </script>
    </body>
    </html>
    """
    st_html(html_code, height=720)

# --- TABELA DE DADOS ---
with st.expander("📂 Ver Tabela de Dados Brutos"):
    rows = []
    for m in data:
        if sel_muni != "Todos" and m['Municipio'] != sel_muni: continue
        for esc in m['Escolas']:
            base = {
                "Município": m['Municipio'], 
                "Escola": esc['Nome'], 
                "Rede": esc.get('Rede'),
                "Zona": esc.get('Zona'),
                "INSE": esc.get('INSE_Class'), 
                "SAEB": esc.get('SAEB')
            }
            if esc.get('Cursos'):
                for c in esc['Cursos']:
                    r = base.copy()
                    r.update({"Curso": c['Nome'], "Matrículas": c['Matriculas']})
                    rows.append(r)
            else:
                r = base.copy()
                r.update({"Curso": "Sem cursos técnicos", "Matrículas": 0})
                rows.append(r)
    
    if rows: st.dataframe(pd.DataFrame(rows), use_container_width=True)
