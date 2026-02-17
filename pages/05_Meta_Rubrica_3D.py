# /home/neirivon/SINAPSE2.0/sinapsebr_rubrica/scripts/pages/05_Meta_Rubrica_3D.py
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

# ──────────────────────────────────────────────────────────────────────────────
# CONFIG DA PÁGINA
# ──────────────────────────────────────────────────────────────────────────────
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

# ──────────────────────────────────────────────────────────────────────────────
# ESTRUTURA LÓGICA DO GRAFO (DIMENSÕES DE QUALIDADE)
# ──────────────────────────────────────────────────────────────────────────────
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

# ──────────────────────────────────────────────────────────────────────────────
# CONTEÚDO RICO (BASEADO EM MULLINIX E BROOKHART)
# ──────────────────────────────────────────────────────────────────────────────
details = {
    "Meta-Rubrica SINAPSE": {
        "color": "#7c3aed", # Roxo vibrante
        "content": (
            "### 🌌 O que é a Meta-Rubrica?\n\n"
            "É o **'Rotor'** do sistema SINAPSE. Uma ferramenta metacognitiva que avalia se a rubrica criada pelo professor "
            "é justa, técnica e útil.\n\n"
            "**Referência Central:** Mullinix, B. B. (2003). *A Rubric for Rubrics*.\n"
            "O objetivo não é apenas dar uma nota, mas garantir que a ferramenta de avaliação seja um instrumento de aprendizagem."
        )
    },
    
    # --- CLAREZA ---
    "Clareza dos Criterios": {
        "color": "#3b82f6",
        "content": (
            "### 🔎 Clareza e Transparência\n"
            "Os critérios devem ser compreensíveis tanto para o especialista (professor) quanto para o aprendiz.\n\n"
            "**Pergunta-chave:** O aluno consegue ler a rubrica e entender exatamente o que se espera dele sem precisar perguntar ao professor?"
        )
    },
    "Linguagem Univoca": {
        "color": "#3b82f6",
        "content": "**Definição:** Uso de termos precisos, evitando adjetivos vagos como 'bom', 'adequado' ou 'interessante' sem qualificadores técnicos."
    },
    "Descritores Observaveis": {
        "color": "#3b82f6",
        "content": "**Definição:** O critério descreve uma evidência tangível (ação, produto, comportamento) e não um estado mental invisível."
    },
    "Distincao entre Niveis": {
        "color": "#3b82f6",
        "content": "**Definição:** A diferença entre o nível 3 (Esperado) e o nível 4 (Avançado) é qualitativa e clara, não apenas quantitativa."
    },

    # --- VALIDADE ---
    "Validade de Conteudo": {
        "color": "#10b981",
        "content": (
            "### 🎯 Validade (Construct Validity)\n"
            "A rubrica mede realmente o que ela diz medir? Ela está alinhada aos objetivos de aprendizagem propostos?\n\n"
            "**Fundamento:** Se a aula foi sobre 'Pensamento Crítico', a rubrica não pode avaliar apenas 'Formatação do Texto'."
        )
    },
    "Alinhamento a Bloom": {
        "color": "#10b981",
        "content": "**Aplicação:** Verifica se o verbo cognitivo exigido na rubrica (ex: Analisar) corresponde ao nível da atividade proposta."
    },
    "Cobertura do Objetivo": {
        "color": "#10b981",
        "content": "**Definição:** A rubrica cobre todas as dimensões essenciais da habilidade, sem deixar lacunas importantes."
    },

    # --- CONFIABILIDADE ---
    "Confiabilidade": {
        "color": "#f59e0b",
        "content": (
            "### ⚖️ Confiabilidade (Reliability)\n"
            "A capacidade da rubrica de gerar resultados consistentes.\n\n"
            "**Teste:** Se dois professores diferentes usarem esta rubrica para avaliar o mesmo trabalho, eles chegarão à mesma nota?"
        )
    },
    "Consistencia Inter-avaliadores": {
        "color": "#f59e0b",
        "content": "**Definição:** Redução da subjetividade individual através de critérios ancorados em evidências."
    },
    "Objetividade": {
        "color": "#f59e0b",
        "content": "**Definição:** Foco nos fatos apresentados no trabalho, minimizando a influência de preferências pessoais do avaliador."
    },

    # --- EQUIDADE ---
    "Equidade e DUA": {
        "color": "#ec4899",
        "content": (
            "### ♿ Equidade e Inclusão (DUA)\n"
            "Garante que a avaliação não penalize alunos por barreiras que não fazem parte do construto avaliado.\n\n"
            "**Base:** Desenho Universal para a Aprendizagem (CAST)."
        )
    },
    "Ausencia de Vies Cultural": {
        "color": "#ec4899",
        "content": "**Definição:** Os exemplos e temas da rubrica consideram a diversidade territorial e cultural do TMAP, evitando elitismos."
    },
    "Multiformato (Permite Audio/Video)": {
        "color": "#ec4899",
        "content": "**Aplicação:** A rubrica permite que o aluno demonstre competência por diferentes meios (texto, áudio, vídeo), conforme princípios do DUA."
    },

    # --- POTENCIAL EDUCATIVO ---
    "Potencial Educativo": {
        "color": "#ef4444",
        "content": (
            "### 🚀 Potencial Educativo (Instructional Impact)\n"
            "A rubrica serve para ensinar ou apenas para julgar?\n\n"
            "**Meta:** A rubrica deve funcionar como um roteiro de estudos para o aluno, antecipando o sucesso."
        )
    },
    "Feedback Orientador": {
        "color": "#ef4444",
        "content": "**Definição:** Os descritores de níveis inferiores explicam o que falta para chegar ao próximo nível (Feedforward)."
    },
    "Promocao da Autoregulacao": {
        "color": "#ef4444",
        "content": "**Definição:** A linguagem convida o aluno a usar a rubrica para se autoavaliar antes da entrega final."
    }
}

# ──────────────────────────────────────────────────────────────────────────────
# POPULAR NÓS VAZIOS
# ──────────────────────────────────────────────────────────────────────────────
for parent, topics in links.items():
    for topic in topics:
        if topic not in details:
            details[topic] = {
                "color": details[parent]["color"],
                "content": f"### {topic}\n\n**Indicador de Qualidade:** Subcomponente da dimensão **{parent}**."
            }

# ──────────────────────────────────────────────────────────────────────────────
# CONSTRUÇÃO DO GRAFO
# ──────────────────────────────────────────────────────────────────────────────
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

# ──────────────────────────────────────────────────────────────────────────────
# HTML/JS (Mantido idêntico ao padrão funcional da Pag 04)
# ──────────────────────────────────────────────────────────────────────────────
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

# ──────────────────────────────────────────────────────────────────────────────
# VÍDEO E JORNADA CONCEITUAL (INSERÇÃO ADITIVA - UI/UX DESIGN)
# ──────────────────────────────────────────────────────────────────────────────
st.divider()
st.subheader("🎬 Audiovisual: O Rotor de Auditoria SINAPSE")

# Embed Responsivo do YouTube
st.video("https://www.youtube.com/watch?v=Mj2a9K5Tb4U")

# Variável HTML isolada para proteger o restante do script de erros de aspas
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
    st.page_link("pages/01_TMAP_2010.py", label="⏳ TMAP Histórico")
    st.page_link("pages/02_TMAP_2017_2024.py", label="🌐 TMAP 2024 (Equidade)")
    st.page_link("pages/03_Mapa_Geral_Rubrica.py", label="🧠 Mapa da Rubrica")
    st.page_link("pages/04_Mapa_Fundamentacao_Teorica.py", label="📚 Fundamentação")
    st.page_link("pages/05_Meta_Rubrica_3D.py", label="🌌 Meta-Rubrica 3D")
    st.markdown("---")
    st.page_link("pages/06_Rubrica_Docente_3D.py", label="👩‍🏫 Rubrica Docente 3D")
    st.page_link("pages/07_Rubrica_Autoavaliativa_3D.py", label="🎓 Autoavaliação 3D")
    st.page_link("pages/08_Transparencia_Avaliativa.py", label="🐆 Transparência (Avaliação)")
    st.page_link("pages/99_Referencias.py", label="📚 Referências")
