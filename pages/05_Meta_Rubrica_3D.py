# /home/neirivon/SINAPSE2.0/sinapsebr_rubrica/scripts/pages/04_Mapa_Fundamentacao_Teorica.py
from __future__ import annotations

import json
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
    "O painel à direita exibe o resumo fundamentado para uso no TCC."
)

physics = st.toggle("Ativar Física (Animação)", value=False)

# ──────────────────────────────────────────────────────────────────────────────
# ESTRUTURA LÓGICA DO GRAFO (DIMENSÕES → TÓPICOS)
# ──────────────────────────────────────────────────────────────────────────────
dims = [
    "Eixo Cognitivo", "Eixo Afetivo", "Eixo Metodologico", "Eixo Neurofuncional",
    "Eixo Avaliativo", "Eixo Tecnologico", "Eixo Territorial", "Eixo Inclusivo"
]

links = {
    "Eixo Cognitivo": ["Taxonomia de Bloom Revisada", "Taxonomia SOLO", "Metacognicao (Flavell)", "Psicologia cognitiva"],
    "Eixo Afetivo": ["Autorregulacao", "Engajamento e Motivacao", "Neuropsicopedagogia", "Teorias da motivacao"],
    "Eixo Metodologico": ["Metodologias ativas", "Aprendizagem baseada em projetos", "Gamificacao"],
    "Eixo Neurofuncional": ["Educacao baseada no cerebro MBE", "Plasticidade Cerebral (Cosenza)", "Memoria e Atencao"],
    "Eixo Avaliativo": ["Avaliacao Formativa (Brookhart)", "Meta-Rubrica (Mullinix)", "Feedback de qualidade"],
    "Eixo Tecnologico": ["Agentes Inteligentes (Russell & Norvig)", "Cultura de Dados", "Moodle e Bloom (Duarte Jr.)"],
    "Eixo Territorial": ["Equidade Socio-territorial", "Critica do territorio CTC", "Indicadores INEP/SAEB"],
    "Eixo Inclusivo": ["Desenho Universal (DUA)", "Acessibilidade", "Materiais multiformato"]
}

# ──────────────────────────────────────────────────────────────────────────────
# DICIONÁRIO DE CONTEÚDO RICO (FUNDAMENTADO NOS PDFS E TCCs)
# ──────────────────────────────────────────────────────────────────────────────
details = {
    "Rubrica SINAPSE BR IA": {
        "color": "#ea580c",
        "content": (
            "### 🧩 O Artefato: Rubrica SINAPSE-BR IA\n\n"
            "O sistema transcende a avaliação classificatória, atuando como um **Agente Racional** (Russell & Norvig) "
            "que mede o desempenho do aluno (Bloom) dentro de seu contexto social e territorial (INEP).\n\n"
            "**Foco:** Medir a qualidade da aprendizagem e não a conclusão da tarefa."
        )
    },
    
    # --- EIXO COGNITIVO ---
    "Eixo Cognitivo": {
        "color": "#3b82f6",
        "content": (
            "### 🧠 Eixo Cognitivo\n"
            "Avalia a complexidade do pensamento mobilizado. Não basta 'saber'; é preciso 'saber como e por que'.\n\n"
            "**Fundamentação:**\n"
            "- **Bloom Revisada (Anderson et al., 2001):** Hierarquia dos processos cognitivos.\n"
            "- **Taxonomia SOLO (Biggs & Collis):** Avalia a profundidade do entendimento.\n"
        )
    },
    "Taxonomia de Bloom Revisada": {
        "color": "#3b82f6",
        "content": (
            "**Referência:** ANDERSON, L. W. et al. (2001).\n\n"
            "Utilizada para garantir que a rubrica não estacione na memorização. Conforme Duarte Jr. (2021), "
            "no ambiente digital (Moodle), verbos como **'Analisar'** e **'Criar'** são operacionalizados através "
            "de fóruns, wikis e produção de artefatos digitais, superando a passividade."
        )
    },
    "Taxonomia SOLO": {
        "color": "#3b82f6",
        "content": (
            "**Conceito:** Structuring of Observed Learning Outcomes (Estrutura dos Resultados de Aprendizagem Observados).\n\n"
            "Avalia a **qualidade** da resposta do aluno em profundidade: de respostas irrelevantes (Unistrutural) a generalizações complexas (Relacional e Abstrato Estendido)."
        )
    },
    "Metacognicao (Flavell)": {
        "color": "#3b82f6",
        "content": (
            "**Referência:** FLAVELL, J. H. (1979).\n\n"
            "A capacidade do aluno de 'pensar sobre o próprio pensamento'. "
            "A rubrica Autoavaliativa (Pág. 07) ativa esse processo, permitindo que o estudante monitore suas estratégias e regule seu esforço."
        )
    },
    "Psicologia cognitiva": {
        "color": "#3b82f6",
        "content": (
            "**Conceito:** O estudo de como o cérebro processa informações.\n\n"
            "No contexto do SINAPSE, sustenta o design de tarefas que não gerem sobrecarga de Memória de Trabalho e o uso de Feedback como reforço cognitivo."
        )
    },
    
    # --- EIXO AFETIVO ---
    "Eixo Afetivo": {
        "color": "#ef4444",
        "content": (
            "### ❤️ Eixo Afetivo\n"
            "Avalia a **vontade** e a **postura** do estudante frente ao desafio.\n\n"
            "**Fundamentação:**\n"
            "- **Neuropsicopedagogia:** Engajamento, motivação e perseverança (resiliência).\n"
            "- **Autorregulação da Aprendizagem:** A capacidade do aluno de gerenciar emoções e recursos para atingir metas."
        )
    },
    "Autorregulacao": {
        "color": "#ef4444",
        "content": (
            "**Conceito:** O processo de monitorar e ajustar o próprio comportamento, cognição e motivação. É a base da autonomia discente."
        )
    },
    "Engajamento e Motivacao": {
        "color": "#ef4444",
        "content": (
            "**Conceito:** Avalia a persistência do aluno. O feedback da rubrica é desenhado para ser motivacional (não punitivo) e intrínseco (focado no aprendizado)."
        )
    },
    "Neuropsicopedagogia": {
        "color": "#ef4444",
        "content": (
            "**Campo Transdisciplinar:** Conecta Neurociência e Pedagogia. Atua no desenvolvimento das Funções Executivas e na intervenção em dificuldades de aprendizagem."
        )
    },
    "Teorias da motivacao": {
        "color": "#ef4444",
        "content": (
            "**Conceito:** Estuda o porquê da ação humana. No SINAPSE, sustenta o design de tarefas que valorizam o processo (rubrica autoavaliativa) para gerar motivação intrínseca."
        )
    },

    # --- EIXO METODOLÓGICO ---
    "Eixo Metodologico": {
        "color": "#10b981",
        "content": (
            "### 🛠️ Eixo Metodológico\n"
            "Avalia como a aprendizagem é construída, privilegiando a **Práxis** da EPT.\n\n"
            "**Foco:** Superar aulas expositivas. As rubricas Docente e Discente valorizam a atividade, o projeto e a autonomia."
        )
    },
    "Metodologias ativas": {
        "color": "#10b981",
        "content": (
            "**Conceito:** Envolve o aluno como protagonista (Ensino Híbrido). No SINAPSE, valoriza-se a autoavaliação (co-avaliação) e o design de tarefas que exijam ação e criação (Projeto/PBL)."
        )
    },
    "Aprendizagem baseada em projetos": {
        "color": "#10b981",
        "content": (
            "**PBL ABP:** Promove a integração de saberes e a resolução de problemas complexos e contextualizados. O critério de **Aplicabilidade** (Meta-Rubrica) exige que a tarefa seja autêntica (PBL)."
        )
    },
    "Gamificacao": {
        "color": "#10b981",
        "content": (
            "**Conceito:** Uso de elementos de jogos (pontos, feedback, desafios) em contextos de não-jogo (avaliação). Fundamentado por **Duarte Jr. (2021)**, que mapeia atividades digitais para Bloom."
        )
    },

    # --- EIXO NEUROFUNCIONAL ---
    "Eixo Neurofuncional": {
        "color": "#8b5cf6",
        "content": (
            "### 🧬 Eixo Neurofuncional\n"
            "Baseado na **Neurociência da Aprendizagem**, considera a arquitetura biológica do cérebro para otimizar o ensino.\n\n"
            "**Referência:** COSENZA & GUERRA (2011)."
        )
    },
    "Educacao baseada no cerebro MBE": {
        "color": "#8b5cf6",
        "content": (
            "**Conceito:** *Mind, Brain, and Education (MBE)*. Uso de evidências neurocientíficas para informar e aprimorar a prática pedagógica."
        )
    },
    "Memoria e Atencao": {
        "color": "#8b5cf6",
        "content": (
            "**Funções Cruciais:** O design da rubrica e do feedback respeita os limites da **Memória de Trabalho** e os ciclos de **Atenção** (Cosenza), evitando a sobrecarga cognitiva (Dehaene)."
        )
    },
    "Plasticidade Cerebral (Cosenza)": {
        "color": "#8b5cf6",
        "content": (
            "**Conceito:** O cérebro muda fisicamente com a experiência (Neuroplasticidade).\n\n"
            "A avaliação é um processo de reforço sináptico: o erro é uma **pista** para o ajuste, não um veredito final."
        )
    },

    # --- EIXO AVALIATIVO ---
    "Eixo Avaliativo": {
        "color": "#f59e0b",
        "content": (
            "### 📏 Eixo Avaliativo\n"
            "Define a avaliação como processo contínuo e transparente. Foco na **Meta-Avaliação** (avaliação da qualidade da própria rubrica).\n\n"
            "**Referência:** Brookhart (2013) e Mullinix (2003)."
        )
    },
    "Avaliacao Formativa (Brookhart)": {
        "color": "#f59e0b",
        "content": (
            "**Citação:** 'A avaliação formativa não é um teste, é um episódio de aprendizagem.' (Brookhart, 2013).\n\n"
            "A rubrica é um guia (mapa) que clarifica o objetivo e fornece **Feedback Descritivo**, essencial para a regulação."
        )
    },
    "Meta-Rubrica (Mullinix)": {
        "color": "#f59e0b",
        "content": (
            "**Ferramenta:** *Rubric for Assessing Rubrics* (Mullinix, 2003).\n\n"
            "A régua para medir a qualidade das rubricas do SINAPSE (Pág. 05) em 4 níveis (Clareza, Confiabilidade, Metacognição)."
        )
    },
    "Feedback de qualidade": {
        "color": "#f59e0b",
        "content": (
            "**Princípio:** Devolutivas que são **Acionáveis** (o aluno sabe o que fazer a seguir), **Específicas** e **Timely** (na hora certa). Fundamental para a regulação."
        )
    },

    # --- EIXO TECNOLÓGICO ---
    "Eixo Tecnologico": {
        "color": "#64748b",
        "content": (
            "### 💻 Eixo Tecnológico (IA)\n"
            "A tecnologia como estruturante da análise de dados educacionais (Cultura de Dados).\n\n"
            "**Agente Racional (Russell & Norvig):** O sistema percebe o ambiente (dados) e age (sugere intervenções)."
        )
    },
    "Cultura de Dados": {
        "color": "#64748b",
        "content": (
            "**Conceito:** A coleta e análise sistemática de dados educacionais (Censo, SAEB) para embasar a tomada de decisão do professor e do gestor."
        )
    },
    "Moodle e Bloom (Duarte Jr.)": {
        "color": "#64748b",
        "content": (
            "**Referência:** DUARTE JUNIOR, D. N. S. (2021).\n\n"
            "Fundamenta a operacionalização da Taxonomia de Bloom em Ambientes Virtuais de Aprendizagem (Moodle), ligando atividades digitais a níveis cognitivos específicos."
        )
    },
    "Agentes Inteligentes (Russell & Norvig)": {
        "color": "#64748b",
        "content": (
            "**Conceito:** IA é o estudo de agentes que recebem percepções do ambiente e realizam ações.\n\n"
            "No contexto do TCC, o 'Agente' é o algoritmo que processa os microdados do Censo/SAEB "
            "para identificar padrões de desigualdade e sugerir intervenções pedagógicas precisas."
        )
    },

    # --- EIXO TERRITORIAL ---
    "Eixo Territorial": {
        "color": "#14b8a6",
        "content": (
            "### 🗺️ Eixo Territorial\n"
            "A avaliação é situada: ela considera a **Interseccionalidade Geográfica** (TMAP vs. Noroeste de Minas) e **Socioeconômica** (INSE).\n\n"
            "**Exemplo:** *'Uma escola rural em Veríssimo tem desafios diferentes de um campus urbano em Uberlândia.'*"
        )
    },
    "Equidade Socio-territorial": {
        "color": "#14b8a6",
        "content": (
            "**Aplicação:** O sistema usa INSE (Nível Socioeconômico) e Zona (Rural/Urbana) para ponderar os resultados. Combate a **invisibilidade** de escolas rurais e de baixo INSE."
        )
    },
    "Critica do territorio CTC": {
        "color": "#14b8a6",
        "content": (
            "**Conceito:** Critérios de Territorialidade, Contexto e Cultura. Garante que o conteúdo da EPT se ligue ao Arranjo Produtivo Local (Frigotto/Ciavatta)."
        )
    },
    "Indicadores INEP/SAEB": {
        "color": "#14b8a6",
        "content": (
            "**Fonte de Dados:** INEP/SISTEC, SAEB (nota), INSE (Nível Socioeconômico). Os dados são a matéria-prima do Agente Racional."
        )
    },

    # --- EIXO INCLUSIVO ---
    "Eixo Inclusivo": {
        "color": "#ec4899",
        "content": (
            "### ♿ Eixo Inclusivo (DUA)\n"
            "Garante que o processo de avaliação seja acessível a todos.\n\n"
            "**Base:** Desenho Universal para a Aprendizagem (CAST).\n"
        )
    },
    "Desenho Universal (DUA)": {
        "color": "#ec4899",
        "content": (
            "**Conceito:** Eliminar barreiras antes que apareçam. A rubrica deve oferecer múltiplos meios de **Expressão** e **Representação** do conhecimento."
        )
    },
    "Acessibilidade": {
        "color": "#ec4899",
        "content": (
            "**Infraestrutura e Design:** O mapa TMAP destaca acessibilidade física (rampas, banheiros PNE) e digital (Internet/Lab) como fatores de equidade."
        )
    },
    "Materiais multiformato": {
        "color": "#ec4899",
        "content": (
            "**DUA na Prática:** O sistema incentiva o professor a receber trabalhos em texto, áudio, vídeo, e outros formatos, respeitando a diversidade neurofuncional."
        )
    }
}

# ──────────────────────────────────────────────────────────────────────────────
# GARANTIR QUE TODOS OS NÓS TENHAM CONTEÚDO
# ──────────────────────────────────────────────────────────────────────────────
for parent, topics in links.items():
    for topic in topics:
        if topic not in details:
            details[topic] = {
                "color": details[parent]["color"],
                "content": f"### {topic}\n\n**Resumo do Eixo Pai:** {details[parent]['content'].replace(f'### {parent}', '').replace('###', '').strip()}"
            }

# ──────────────────────────────────────────────────────────────────────────────
# CONSTRUÇÃO DOS NODES/EDGES
# ──────────────────────────────────────────────────────────────────────────────
nodes, edges = [], []

# Nó Raiz Central
nodes.append({
    "id": "Rubrica SINAPSE BR IA",
    "label": "SINAPSE-BR IA\n(Artefato)",
    "color": "#ea580c",
    "shape": "circle",
    "size": 35,
    "font": {"size": 20, "color": "white", "face": "Inter"}
})

# Cores para cada eixo
colors = {
    "Eixo Cognitivo": "#3b82f6",
    "Eixo Afetivo": "#ef4444",
    "Eixo Metodologico": "#10b981",
    "Eixo Neurofuncional": "#8b5cf6",
    "Eixo Avaliativo": "#f59e0b",
    "Eixo Tecnologico": "#64748b",
    "Eixo Territorial": "#14b8a6",
    "Eixo Inclusivo": "#ec4899"
}

# Adiciona Eixos e Tópicos
topic_added = set()

for d in dims:
    c = colors.get(d, "#60a5fa")
    nodes.append({"id": d, "label": d, "color": c, "shape": "box", "font": {"color": "white"}})
    edges.append({"from": "Rubrica SINAPSE BR IA", "to": d, "color": c, "width": 2})
    
    for t in links[d]:
        if t not in topic_added:
            nodes.append({"id": t, "label": t, "color": "#e2e8f0", "shape": "ellipse", "font": {"size": 14, "color": "#333"}})
            topic_added.add(t)
        edges.append({"from": d, "to": t, "color": "#cbd5e1", "width": 1})

# Opções Vis.js
options = {
    "physics": {
        "enabled": bool(physics),
        "stabilization": {"enabled": True},
        "solver": "forceAtlas2Based",
        "forceAtlas2Based": {"gravitationalConstant": -80, "springLength": 100}
    },
    "interaction": {"hover": True, "tooltipDelay": 100},
    "edges": {"smooth": {"type": "continuous"}},
    "nodes": {"borderWidth": 1, "shadow": True},
    "layout": {"improvedLayout": True}
}

# ──────────────────────────────────────────────────────────────────────────────
# HTML/JS INJETADO (RENDERIZAÇÃO COM PAINEL RICO)
# ──────────────────────────────────────────────────────────────────────────────
html_code = f'''
<!doctype html>
<html>
<head>
  <meta charset="utf-8" />
  <script src="https://cdn.jsdelivr.net/npm/vis-network@9.1.6/dist/vis-network.min.js"></script>
  <style>
    body {{ margin:0; font-family: "Segoe UI", system-ui, sans-serif; background-color: #ffffff; }}
    .wrap {{ display:flex; height:760px; }}
    #net {{ flex:1; height:100%; background: #ffffff; }}
    #panel {{ 
        width: 400px; 
        padding: 0;
        background: #f8fafc; 
        border-left: 1px solid #e2e8f0; 
        overflow-y: auto; 
        box-shadow: -2px 0 12px rgba(0,0,0,0.08);
    }}
    .panel-header {{ 
        padding: 20px; 
        background: linear-gradient(135deg, #1e40af, #3b82f6); 
        color: white; 
        margin-bottom: 0;
    }}
    .panel-header h3 {{ margin:0; font-size: 18px; display:flex; align-items:center; gap:8px; }}
    .panel-header p {{ margin:8px 0 0 0; opacity:0.9; font-size:13px; }}
    
    .content-container {{ padding: 20px; }}
    
    /* Card Estilizado */
    .theory-card {{
        background: white;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        border-left: 6px solid #3b82f6;
        transition: transform 0.2s, box-shadow 0.2s;
    }}
    .theory-card:hover {{
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(0,0,0,0.08);
    }}
    
    .theory-card h3 {{
        color: #1e40af;
        margin-top: 0;
        margin-bottom: 12px;
        font-size: 18px;
        border-bottom: 2px solid #e2e8f0;
        padding-bottom: 8px;
    }}
    
    .theory-card .content {{
        font-size: 14px;
        line-height: 1.7;
        color: #334155;
    }}
    
    .theory-card .content strong {{
        color: #0f172a;
        font-weight: 600;
    }}
    
    .theory-card .content ul {{
        padding-left: 20px;
        margin: 10px 0;
    }}
    
    .theory-card .content li {{
        margin-bottom: 6px;
    }}
    
    .tag {{
        display: inline-block;
        background: #eff6ff;
        color: #1d4ed8;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 600;
        margin-bottom: 12px;
    }}
    
    /* Botão de copiar */
    .copy-btn {{
        margin-top: 15px;
        padding: 10px 16px;
        background-color: #3b82f6;
        color: white;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        font-size: 13px;
        font-weight: 600;
        transition: all 0.2s;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 8px;
        width: 100%;
    }}
    .copy-btn:hover {{ background-color: #2563eb; }}
    .copy-btn:active {{ transform: translateY(1px); }}
    
    .empty-state {{
        text-align: center;
        padding: 40px 20px;
        color: #64748b;
    }}
    .empty-state h4 {{ color: #475569; margin-bottom: 8px; }}
    .empty-state p {{ font-size: 14px; }}
  </style>
</head>
<body>
  <div class="wrap">
    <div id="net"></div>
    <aside id="panel">
      <div class="panel-header">
        <h3>📘 Fundamentação Teórica</h3>
        <p>Clique em um nó para visualizar o resumo teórico, referências e aplicação no TCC.</p>
      </div>
      <div class="content-container">
        <div id="content">
          <div class="empty-state">
            <h4>Selecione um conceito</h4>
            <p>Clique em qualquer nó do mapa para começar a explorar a fundamentação teórica da Rubrica SINAPSE-BR IA.</p>
          </div>
        </div>
        <button class="copy-btn" onclick="copyText()">
          <span>📋</span> Copiar Texto para o TCC
        </button>
      </div>
    </aside>
  </div>

  <script>
    const nodes = new vis.DataSet({json.dumps(nodes, ensure_ascii=False)});
    const edges = new vis.DataSet({json.dumps(edges, ensure_ascii=False)});
    const options = {json.dumps(options, ensure_ascii=False)};
    
    const network = new vis.Network(document.getElementById('net'), {{nodes, edges}}, options);
    
    // Dicionário de Detalhes
    const details = {json.dumps({k: v["content"] for k, v in details.items()}, ensure_ascii=False)};
    const colors = {json.dumps({k: v["color"] for k, v in details.items()}, ensure_ascii=False)};

    // Função para converter markdown para HTML
    function parseMarkdown(text) {{
        if (!text) return "<em>Selecione um tópico.</em>";
        return text
            .replace(/^### (.*$)/gim, '<h3>$1</h3>')
            .replace(/\*\*(.*?)\*\*/gim, '<strong>$1</strong>')
            .replace(/- (.*$)/gim, '<li>$1</li>')
            .replace(/\\n/g, '<br>');
    }}

    // Função para criar o card estilizado
    function createTheoryCard(title, content, color) {{
        return `
        <div class="theory-card" style="border-left-color: ${{color}};">
            <div class="tag" style="background-color: ${{color}}20; color: ${{color}};">
                ${{title.split(' ')[0]}}
            </div>
            <div class="content">
                ${{parseMarkdown(content)}}
            </div>
        </div>
        `;
    }}

    network.on('selectNode', function(params) {{
        if (params.nodes.length > 0) {{
            const nodeId = params.nodes[0];
            const rawText = details[nodeId] || "<em>Texto não encontrado para este nó.</em>";
            const nodeColor = colors[nodeId] || "#3b82f6";
            
            const cardHTML = createTheoryCard(nodeId, rawText, nodeColor);
            document.getElementById('content').innerHTML = cardHTML;
            document.getElementById('content').setAttribute('data-raw', rawText);
        }}
    }});

    function copyText() {{
        const text = document.getElementById('content').innerText;
        navigator.clipboard.writeText(text).then(() => {{
            const btn = document.querySelector('.copy-btn');
            const originalText = btn.innerHTML;
            btn.innerHTML = '<span>✅</span> Copiado para área de transferência!';
            btn.style.backgroundColor = '#10b981';
            
            setTimeout(() => {{
                btn.innerHTML = originalText;
                btn.style.backgroundColor = '#3b82f6';
            }}, 2000);
        }});
    }}
    
    // Exibir card inicial
    document.addEventListener('DOMContentLoaded', function() {{
        const initialCard = createTheoryCard(
            "Rubrica SINAPSE BR IA", 
            details["Rubrica SINAPSE BR IA"], 
            colors["Rubrica SINAPSE BR IA"]
        );
        document.getElementById('content').innerHTML = initialCard;
        document.getElementById('content').setAttribute('data-raw', details["Rubrica SINAPSE BR IA"]);
    }});
  </script>
</body>
</html>
'''

st_html(html_code, height=800, scrolling=False)

# --- SIDEBAR ---
with st.sidebar:
    st.page_link("Apresentacao.py", label="🏠 Apresentação")
    st.markdown("---")
    st.page_link("pages/01_TMAP_2010.py", label="⏳ TMAP Histórico")
    st.page_link("pages/02_TMAP_2017_2024.py", label="🌐 TMAP 2024 (Equidade)")
    st.page_link("pages/03_Mapa_Geral_Rubrica.py", label="🧠 Mapa da Rubrica")
    st.page_link("pages/04_Mapa_Fundamentacao_Teorica.py", label="📚 Fundamentação")
    st.markdown("---")
    st.page_link("pages/05_Meta_Rubrica_3D.py", label="🌌 Meta-Rubrica 3D")
    st.page_link("pages/06_Rubrica_Docente_3D.py", label="👩‍🏫 Rubrica Docente 3D")
    st.page_link("pages/07_Rubrica_Autoavaliativa_3D.py", label="🎓 Autoavaliação 3D")
    st.page_link("pages/08_Transparencia_Avaliativa.py", label="🐆 Transparência (Avaliação)")
    st.page_link("pages/99_Referencias.py", label="📚 Referências")
