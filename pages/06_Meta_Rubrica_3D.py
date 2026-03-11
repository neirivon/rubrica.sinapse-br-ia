# /home/neirivon/SINAPSE2.0/sinapsebr_rubrica/pages/06_Meta_Rubrica_3D.py
# --------------------------------------------------------------------------------------
# NOME DO SCRIPT: 05_Meta_Rubrica_3D.py
# LOCALIZAÇÃO:    /pages/
# DESCRIÇÃO:      Visualização da META-RUBRICA (O instrumento de validação).
#                 Baseado em Mullinix (2003) - "Rubric for Rubrics".
#                 Permite ao usuário entender como a própria qualidade da rubrica é medida.
# FUNCIONALIDADES:
#   1. Grafo de Rede focado nos CRITÉRIOS DE QUALIDADE (Validade, Confiabilidade, etc.).
#   2. Painel lateral com definições acadêmicas de cada critério.
#   3. Distinção visual entre Dimensões (Nós Grandes) e Indicadores (Nós Pequenos).
# AUTOR:          Neirivon Elias Cardoso
# DATA:           24/01/2026
# --------------------------------------------------------------------------------------
from __future__ import annotations

import json
import streamlit as st
from streamlit.components.v1 import html as st_html

# --------------------------------------------------------------------------------------
# CONFIG DA PÁGINA
# --------------------------------------------------------------------------------------
st.set_page_config(
    page_title="Meta-Rubrica 3D — SINAPSE-BR",
    page_icon="🌌",
    layout="wide",
)

st.title("🌌 Meta-Rubrica: A Avaliação da Avaliação")
st.markdown("""
Esta página apresenta a **Meta-Rubrica SINAPSE**, um instrumento recursivo utilizado para auditar a qualidade das rubricas pedagógicas geradas.
Baseia-se nos princípios de **Mullinix (2003)** e **Brookhart (2013)**.
""")

physics = st.toggle("Ativar Simulação Física (Gravidade)", value=True)

# --------------------------------------------------------------------------------------
# ESTRUTURA LÓGICA DO GRAFO (DIMENSÕES DE QUALIDADE)
# --------------------------------------------------------------------------------------
# As dimensões aqui não são os eixos da rubrica final, mas os critérios de QUALIDADE da rubrica.

dims = [
    "Clareza dos Criterios", 
    "Validade de Conteudo", 
    "Confiabilidade", 
    "Equidade e DUA", 
    "Potencial Educativo"
]

links = {
    "Clareza dos Criterios": ["Linguagem Univoca", "Descritores Observaveis", "Distincao entre Niveis"],
    "Validade de Conteudo": ["Alinhamento a Bloom", "Cobertura do Objetivo", "Relevancia Pratica"],
    "Confiabilidade": ["Consistencia Inter-avaliadores", "Escala Equilibrada", "Objetividade"],
    "Equidade e DUA": ["Ausencia de Vies Cultural", "Multiformato (Permite Audio/Video)", "Acessibilidade Linguistica"],
    "Potencial Educativo": ["Feedback Orientador", "Promocao da Autoregulacao", "Foco no Processo"]
}

# --------------------------------------------------------------------------------------
# DICIONÁRIO DE DETALHES (CORREÇÃO DO NameError)
# --------------------------------------------------------------------------------------
# INICIALIZAÇÃO OBRIGATÓRIA: Define as dimensões principais ANTES do loop de população
details = {
    "Clareza dos Criterios": {
        "color": "#3b82f6",
        "content": "### Clareza dos Critérios\n\nA rubrica deve usar linguagem unívoca e descritores observáveis."
    },
    "Validade de Conteudo": {
        "color": "#f59e0b",
        "content": "### Validade de Conteúdo\n\nAlinhamento com objetivos de aprendizagem e Taxonomia de Bloom."
    },
    "Confiabilidade": {
        "color": "#8b5cf6",
        "content": "### Confiabilidade\n\nConsistência entre avaliadores e estabilidade da escala."
    },
    "Equidade e DUA": {
        "color": "#10b981",
        "content": "### Equidade e DUA\n\nAusência de vieses e múltiplos formatos de resposta."
    },
    "Potencial Educativo": {
        "color": "#ef4444",
        "content": "### Potencial Educativo\n\nFeedback orientador e promoção da autorregulação."
    }
}

# --------------------------------------------------------------------------------------
# VÍDEO E ROTEIRO DE EMANCIPAÇÃO (ESTRUTURA DE CONTEÚDO RICO)
# --------------------------------------------------------------------------------------
roteiro_emancipacao = {
    "A Semente (O Cubo)": {
        "color": "#3b82f6",
        "content": (
            "### 🧊 A Semente: O Cubo Analógico\n\n"
            "Representa a transição do conceito abstrato para a materialidade. "
            "Veja como as dimensões neuropsicopedagógicas ganham volume e cor através do objeto tátil.\n\n"
            "**Foco:** Transformar teorias em ferramentas visíveis e compreensíveis para o estudante."
        )
    },
    "O Salto Sinaptico": {
        "color": "#f59e0b",
        "content": (
            "### ⚡ O Salto Sináptico\n\n"
            "É o momento da 'Manobra Sináptica'. A passagem do uso passivo da tecnologia para a "
            "**Hospitalidade Técnica** e o Geofilosofar.\n\n"
            "**Conceito:** A tecnologia deixa de ser uma barreira e passa a ser uma lente de ampliação da consciência."
        )
    },
    "A Conquista do Territorio": {
        "color": "#10b981",
        "content": (
            "### 🌍 A Conquista do Território\n\n"
            "Onde a autoavaliação encontra a vida real. Reflete a melhoria da vida no bairro, "
            "no campus e na comunidade local (TMAP).\n\n"
            "**Resultado:** O aluno reconhece seu impacto social e torna-se um habitante consciente da 'Terra de Todos'."
        )
    },
    "A Lente SINAPSE": {
        "color": "#ef4444",
        "content": (
            "### 🎯 A Lente da Percepção\n\n"
            "> *'A tecnologia não te substitui; ela é a lente que amplia a sua consciência sobre o ato de aprender.'*\n\n"
            "**Dica de Ouro:** Não tente ser 'Platinum' em tudo hoje. Escolha uma dimensão e planeje seu próximo passo."
        )
    }
}

# --------------------------------------------------------------------------------------
# RENDERIZAÇÃO NA INTERFACE
# --------------------------------------------------------------------------------------
st.divider()
st.subheader("🎬 Materialização: Do Cubo Analógico ao Digital")
st.video("https://www.youtube.com/watch?v=Ay_R1kzGll4")
st.markdown("---")

for titulo, info in roteiro_emancipacao.items():
    st.markdown(
        f"""
        <div style="padding:15px; border-radius:10px; border-left:5px solid {info['color']}; 
                    background-color:#f8fafc; margin-bottom:15px;">
            {info['content']}
        </div>
        """, 
        unsafe_allow_html=True
    )

st.caption("Ecossistema SINAPSE-BR IA | TCC Neirivon Elias Cardoso | IFTM 2026")

# --------------------------------------------------------------------------------------
# POPULAR NÓS VAZIOS (AGORA FUNCIONA COM 'details' DEFINIDO)
# --------------------------------------------------------------------------------------
for parent, topics in links.items():
    for topic in topics:
        if topic not in details:
            details[topic] = {
                "color": details[parent]["color"],
                "content": f"### {topic}\n\n**Indicador de Qualidade:** Subcomponente da dimensão **{parent}**."
            }

# --------------------------------------------------------------------------------------
# CONSTRUÇÃO DO GRAFO
# --------------------------------------------------------------------------------------
nodes, edges = [], []

# Nó Central
nodes.append({
    "id": "Meta-Rubrica SINAPSE",
    "label": "Meta-Rubrica\n(Mullinix)",
    "color": "#7c3aed",
    "shape": "diamond",
    "size": 45,
    "font": {"size": 22, "color": "white", "face": "Inter"}
})

# Nós e Arestas
topic_added = set()

for d in dims:
    c = details[d]["color"]
    # Nó da Dimensão
    nodes.append({
        "id": d, 
        "label": d, 
        "color": c, 
        "shape": "dot", 
        "size": 25,
        "font": {"color": "white", "size": 16}
    })
    edges.append({"from": "Meta-Rubrica SINAPSE", "to": d, "color": c, "width": 3})
    
    # Nós dos Indicadores
    for t in links[d]:
        if t not in topic_added:
            nodes.append({
                "id": t, 
                "label": t, 
                "color": "#e2e8f0", 
                "shape": "ellipse", 
                "font": {"size": 12, "color": "#475569"}
            })
            topic_added.add(t)
        edges.append({"from": d, "to": t, "color": c, "width": 1, "dashes": True})

# Opções Vis.js
options = {
    "physics": {
        "enabled": bool(physics),
        "stabilization": {"enabled": True},
        "solver": "forceAtlas2Based",
        "forceAtlas2Based": {
            "gravitationalConstant": -100, 
            "springLength": 120,
            "damping": 0.4
        }
    },
    "interaction": {"hover": True},
    "edges": {"smooth": {"type": "dynamic"}},
    "nodes": {"borderWidth": 2, "shadow": True},
    "layout": {"improvedLayout": True}
}

# --------------------------------------------------------------------------------------
# HTML/JS
# --------------------------------------------------------------------------------------
html_code = f'''
<!doctype html>
<html>
<head>
  <meta charset="utf-8" />
  <script src="https://cdn.jsdelivr.net/npm/vis-network@9.1.6/dist/vis-network.min.js"></script>
  <style>
    body {{ margin:0; font-family: "Segoe UI", sans-serif; background-color: #ffffff; }}
    .wrap {{ display:flex; height:760px; }}
    #net {{ flex:1; height:100%; background: #ffffff; }}
    #panel {{ 
        width: 380px; 
        background: #f8fafc; 
        border-left: 1px solid #e2e8f0; 
        overflow-y: auto; 
        box-shadow: -4px 0 15px rgba(0,0,0,0.05);
    }}
    .header {{ 
        padding: 20px; 
        background: linear-gradient(135deg, #7c3aed, #8b5cf6); 
        color: white; 
    }}
    .header h2 {{ margin:0; font-size: 20px; }}
    .content {{ padding: 20px; }}
    
    .card {{
        background: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        border-left: 5px solid #7c3aed;
    }}
    .card h3 {{ margin-top:0; color: #4c1d95; }}
    .card p {{ line-height: 1.6; color: #334155; font-size: 14px; }}
    .card strong {{ color: #1e293b; }}
    
    .hint {{ 
        text-align: center; 
        color: #94a3b8; 
        margin-top: 50px; 
        font-style: italic;
    }}
  </style>
</head>
<body>
  <div class="wrap">
    <div id="net"></div>
    <aside id="panel">
      <div class="header">
        <h2>🛠️ Detalhes da Validação</h2>
      </div>
      <div class="content">
        <div id="info">
            <div class="hint">
                <p>Clique nos nós do grafo para entender<br>os critérios de qualidade.</p>
            </div>
        </div>
      </div>
    </aside>
  </div>

  <script>
    const nodes = new vis.DataSet({json.dumps(nodes, ensure_ascii=False)});
    const edges = new vis.DataSet({json.dumps(edges, ensure_ascii=False)});
    const options = {json.dumps(options, ensure_ascii=False)};
    
    const container = document.getElementById('net');
    const data = {{nodes, edges}};
    const network = new vis.Network(container, data, options);
    
    const details = {json.dumps({k: v["content"] for k, v in details.items()}, ensure_ascii=False)};
    const colors = {json.dumps({k: v["color"] for k, v in details.items()}, ensure_ascii=False)};

    function parseMarkdown(text) {{
        if (!text) return "";
        return text
            .replace(/^### (.*$)/gim, '<h3>$1</h3>')
            .replace(/\*\*(.*?)\*\*/gim, '<strong>$1</strong>')
            .replace(/\\n/g, '<br>');
    }}

    network.on('selectNode', function(params) {{
        if (params.nodes.length > 0) {{
            const id = params.nodes[0];
            const text = details[id] || "Sem descrição disponível.";
            const color = colors[id] || "#7c3aed";
            
            const html = `
                <div class="card" style="border-left-color: ${{(color)}}">
                    ${{parseMarkdown(text)}}
                </div>
            `;
            document.getElementById('info').innerHTML = html;
        }}
    }});
  </script>
</body>
</html>
'''

st_html(html_code, height=800, scrolling=False)

# --------------------------------------------------------------------------------------
# VÍDEO E JORNADA CONCEITUAL
# --------------------------------------------------------------------------------------

jornada_meta_html = """
<div style="background: white; border-radius: 18px; padding: 32px; box-shadow: 0 6px 25px rgba(0, 0, 0, 0.08); border: 1px solid #e2e8f0; margin: 15px 0 45px; position: relative; overflow: hidden; max-width: 100%;">
    <div style="position: absolute; top: 0; left: 0; width: 6px; height: 100%; background: linear-gradient(to bottom, #7c3aed, #4c1d95);"></div>
    <h3 style="color: #0f172a; margin-top: 0; font-size: 1.55rem; display: flex; align-items: center; gap: 12px; font-weight: 700;">
        <span style="background: #f3e8ff; color: #7c3aed; width: 36px; height: 36px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; font-size: 1.1rem; flex-shrink: 0;">💎</span>
        O Rotor da Meta-Rubrica: Auditando a Inteligência
    </h3>
    <div style="margin: 28px 0 20px; padding-left: 8px;">
        <div style="display: flex; align-items: flex-start; gap: 20px; margin: 22px 0; border-left: 3px solid #3b82f6; padding-left: 12px; padding-bottom: 8px;">
            <span style="font-size: 1.7rem; flex-shrink: 0;">🎯</span>
            <div>
                <strong style="color: #0f172a; font-size: 1.2rem; display: block; margin-bottom: 4px;">Clareza e Validade</strong>
                <span style="color: #475569; line-height: 1.6; font-size: 1rem;">O Rotor verifica se a linguagem é exata e se os objetivos seguem rigorosamente a Taxonomia de Bloom.</span>
            </div>
        </div>
        <div style="display: flex; align-items: flex-start; gap: 20px; margin: 22px 0; border-left: 3px solid #f59e0b; padding-left: 12px; padding-bottom: 8px;">
            <span style="font-size: 1.7rem; flex-shrink: 0;">⚖️</span>
            <div>
                <strong style="color: #0f172a; font-size: 1.2rem; display: block; margin-bottom: 4px;">Confiabilidade</strong>
                <span style="color: #475569; line-height: 1.6; font-size: 1rem;">Auditamos a estabilidade da régua. A nota deve se manter justa e estável, independentemente do avaliador.</span>
            </div>
        </div>
        <div style="display: flex; align-items: flex-start; gap: 20px; margin: 22px 0; border-left: 3px solid #ec4899; padding-left: 12px; padding-bottom: 8px;">
            <span style="font-size: 1.7rem; flex-shrink: 0;">🌿</span>
            <div>
                <strong style="color: #0f172a; font-size: 1.2rem; display: block; margin-bottom: 4px;">Equidade (DUA)</strong>
                <span style="color: #475569; line-height: 1.6; font-size: 1rem;">A rubrica é validada por aceitar múltiplos formatos (áudio/vídeo/texto), respeitando a diversidade.</span>
            </div>
        </div>
        <div style="display: flex; align-items: flex-start; gap: 20px; margin: 22px 0; border-left: 3px solid #ef4444; padding-left: 12px; padding-bottom: 8px;">
            <span style="font-size: 1.7rem; flex-shrink: 0;">🚀</span>
            <div>
                <strong style="color: #0f172a; font-size: 1.2rem; display: block; margin-bottom: 4px;">Potencial Educativo</strong>
                <span style="color: #475569; line-height: 1.6; font-size: 1rem;">A avaliação não apenas julga, ela ensina e aponta o caminho para a autonomia do aprendiz.</span>
            </div>
        </div>
    </div>
    <div style="background: #f8fafc; border-radius: 14px; padding: 24px; border: 1px solid #e2e8f0;">
        <div style="font-style: italic; color: #1e40af; border-left: 4px solid #7c3aed; padding-left: 18px; font-weight: 500;">
            "SINAPSE-BR IA: Inteligência Pedagógica que audita a si mesma para garantir ética e técnica na EPT."
        </div>
    </div>
</div>
"""
st.markdown(jornada_meta_html, unsafe_allow_html=True)

# --- SIDEBAR (NAVEGAÇÃO) ---
with st.sidebar:
    st.page_link("Apresentacao.py", label="🏠 Apresentação")
    st.markdown("---")
    st.page_link("pages/02_Mapa_Fundamentacao_Teorica.py", label="📚 Fundamentação")
    st.page_link("pages/03_TMAP_2010.py", label="🟢 TMAP Histórico (Territorial)")
    st.page_link("pages/04_TMAP_2017_2024.py", label="🌐 TMAP 2024 (Equidade)")
    st.page_link("pages/05_Mapa_Geral_Rubrica.py", label="🧠 Mapa da Rubrica")

    st.page_link("pages/06_Meta_Rubrica_3D.py", label="🌌 Meta-Rubrica 3D")
    st.markdown("---")
    st.page_link("pages/07_Rubrica_Docente_3D.py", label="👩‍🏫 Rubrica Docente 3D")
    st.page_link("pages/08_Rubrica_Autoavaliativa_3D.py", label="🎓 Autoavaliação 3D")
    st.page_link("pages/09_Transparencia_Avaliativa.py", label="🐆 Transparência (Avaliação)")
    st.page_link("pages/99_Referencias.py", label="📚 Referências")
