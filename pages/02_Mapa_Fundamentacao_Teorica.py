# /home/neirivon/SINAPSE2.0/sinapsebr_rubrica/scripts/pages/02_Mapa_Fundamentacao_Teorica.py
# --------------------------------------------------------------------------------------
# NOME DO SCRIPT: 04_Mapa_Fundamentacao_Teorica.py
# DESCRIÇÃO: Mapa interativo de fundamentação teórica conectando eixos e tópicos acadêmicos.
#            Inclui vídeo explicativo com roteiro cinematográfico e matriz de resumo 8x5.
#
# FUNCIONALIDADES:
#   1. Grafo Dinâmico: Conexão entre eixos teóricos e bibliografia.
#   2. Painel Acadêmico: Resumos teóricos com função de cópia direta para o TCC.
#   3. Integração Audiovisual: Vídeo narrado com foco na arquitetura do conhecimento.
#   4. UX/UI Design: Interface focada em escaneabilidade e experiência didática.
#
# AUTOR: Neirivon Elias Cardoso
# PROJETO: Rubrica SINAPSE-BR IA — Sistema Integrado Neuropsicopedagógico
# TCC: Pós-Graduação em Docência para a EPT (IFTM)
# DATA: 07/02/2026
# --------------------------------------------------------------------------------------

from __future__ import annotations
import json
import streamlit as st
from streamlit.components.v1 import html as st_html

# CONFIG DA PÁGINA
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

# ESTRUTURA LÓGICA DO GRAFO (DIMENSÕES → TÓPICOS) - SEM ESPAÇOS EXTRAS NAS CHAVES
dims = [
    "Eixo Cognitivo", "Eixo Afetivo", "Eixo Metodologico", "Eixo Neurofuncional",
    "Eixo Avaliativo", "Eixo Tecnologico", "Eixo Territorial", "Eixo Inclusivo"
]
links = {
    "Eixo Cognitivo": ["Taxonomia de Bloom Revisada", "Taxonomia SOLO", "Metacognicao (Flavell)", "Psicologia cognitiva"],
    "Eixo Afetivo": ["Autorregulacao", "Engajamento e Motivacao", "Neuropsicopedagogia", "Teorias da motivacao"],
    "Eixo Metodologico": ["Metodologias ativas", "Aprendizagem baseada em projetos", "Gamificacao"],
    "Eixo Neurofuncional": ["Educacao baseada no cerebro MBE", "Plasticidade Cerebral (Cosenza)", "Memoria e Atencao", "Stanislas Dehaene"],
    "Eixo Avaliativo": ["Avaliacao Formativa (Brookhart)", "Meta-Rubrica (Mullinix)", "Feedback de qualidade"],
    "Eixo Tecnologico": ["Agentes Inteligentes (Russell & Norvig)", "Cultura de Dados", "Moodle e Bloom (Duarte Jr.)"],
    "Eixo Territorial": ["Equidade Socio-territorial", "Critica do territorio CTC", "Indicadores INEP/SAEB"],
    "Eixo Inclusivo": ["Desenho Universal (DUA)", "Acessibilidade", "Materiais multiformato"]
}

# DICIONÁRIO DE CONTEÚDO RICO (VERSÃO ESTÁVEL) - SEM ESPAÇOS EXTRAS NAS CHAVES
details = {
    "Rubrica SINAPSE BR IA": (
        "### 🧩 O Artefato: Rubrica SINAPSE-BR IA\n\n"
        "O sistema transcende a avaliação classificatória, atuando como um Agente Racional (Russell & Norvig) "
        "que mede o desempenho do aluno (Bloom) dentro de seu contexto social e territorial (INEP).\n\n"
        "**Foco:** Medir a qualidade da aprendizagem e não a conclusão da tarefa."
    ),
    # --- EIXO COGNITIVO ---
    "Eixo Cognitivo": (
        "### 🧠 Eixo Cognitivo\n"
        "Avalia a complexidade do pensamento mobilizado. Não basta 'saber'; é preciso 'saber como e por que'.\n\n"
        "**Fundamentação:**\n"
        "- **Bloom Revisada (Anderson et al., 2001):** Hierarquia dos processos cognitivos.\n"
        "- **Taxonomia SOLO (Biggs & Collis):** Avalia a profundidade do entendimento.\n"
    ),
    "Taxonomia de Bloom Revisada": (
        "**Referência:** ANDERSON, L. W. et al. (2001).\n\n"
        "Garante que a rubrica avalie o aluno em níveis altos (Analisar, Avaliar, Criar) e não apenas na memorização (Lembrar/Entender). Essencial para a EPT."
    ),
    "Taxonomia SOLO": (
        "**Conceito:** Structuring of Observed Learning Outcomes (Estrutura dos Resultados de Aprendizagem Observados).\n\n"
        "Avalia a **qualidade** da resposta do aluno em profundidade: de respostas irrelevantes a generalizações complexas (Relacional e Abstrato Estendido)."
    ),
    "Metacognicao (Flavell)": (
        "**Referência:** FLAVELL, J. H. (1979).\n\n"
        "A capacidade do aluno de 'pensar sobre o próprio pensamento'. A rubrica Autoavaliativa (Pág. 07) ativa esse processo, permitindo que o estudante monitore suas estratégias e regule seu esforço."
    ),
    "Psicologia cognitiva": (
        "**Conceito:** O estudo de como o cérebro processa informações.\n\n"
        "No contexto do SINAPSE, sustenta o design de tarefas que não gerem sobrecarga de Memória de Trabalho e o uso de Feedback como reforço cognitivo."
    ),

    # --- EIXO AFETIVO ---
    "Eixo Afetivo": (
        "### ❤️ Eixo Afetivo\n"
        "Avalia a **vontade** e a **postura** do estudante frente ao desafio (Engajamento, Motivação, Resiliência).\n\n"
        "**Fundamentação:** Neuropsicopedagogia, Autorregulação da Aprendizagem e Teorias da Motivação."
    ),
    "Autorregulacao": (
        "**Conceito:** O processo de monitorar e ajustar o próprio comportamento, cognição e motivação. É a base da autonomia discente."
    ),
    "Engajamento e Motivacao": (
        "**Conceito:** Avalia a persistência do aluno. O feedback da rubrica é desenhado para ser motivacional (não punitivo) e intrínseco (focado no aprendizado)."
    ),
    "Neuropsicopedagogia": (
        "**Campo Transdisciplinar:** Conecta Neurociência e Pedagogia. Atua no desenvolvimento das Funções Executivas e na intervenção em dificuldades de aprendizagem."
    ),
    "Teorias da motivacao": (
        "**Conceito:** Estuda o porquê da ação humana. No SINAPSE, sustenta o design de tarefas que valorizam o processo (rubrica autoavaliativa) para gerar motivação intrínseca."
    ),

    # --- EIXO METODOLÓGICO ---
    "Eixo Metodologico": (
        "### 🛠️ Eixo Metodológico\n"
        "Avalia como a aprendizagem é construída, privilegiando a **Práxis** da EPT e o protagonismo discente.\n\n"
        "**Foco:** Uso de Metodologias Ativas (PBL, Projetos, Gamificação) que superam aulas expositivas."
    ),
    "Metodologias ativas": (
        "**Conceito:** Envolve o aluno como protagonista (Ensino Híbrido). No SINAPSE, valoriza-se a autoavaliação (co-avaliação) e o design de tarefas que exijam ação e criação (Projeto/PBL)."
    ),
    "Aprendizagem baseada em projetos": (
        "**PBL ABP:** Promove a integração de saberes e a resolução de problemas complexos e contextualizados. O critério de **Aplicabilidade** (Meta-Rubrica) exige que a tarefa seja autêntica (PBL)."
    ),
    "Gamificacao": (
        "**Conceito:** Uso de elementos de jogos (pontos, feedback, desafios) em contextos de não-jogo (avaliação). Fundamentado por **Duarte Jr. (2021)**, que mapeia atividades digitais para Bloom."
    ),

    # --- EIXO NEUROFUNCIONAL ---
    "Eixo Neurofuncional": (
        "### 🧬 Eixo Neurofuncional\n"
        "Baseado na **Neurociência da Aprendizagem**, considera a arquitetura biológica do cérebro para otimizar o ensino.\n\n"
        "**Referência:** COSENZA & GUERRA (2011)."
    ),
    "Educacao baseada no cerebro MBE": (
        "**Conceito:** *Mind, Brain, and Education (MBE)*. Uso de evidências neurocientíficas para informar e aprimorar a prática pedagógica."
    ),
    "Memoria e Atencao": (
        "**Funções Cruciais:** O design da rubrica e do feedback respeita os limites da **Memória de Trabalho** e os ciclos de **Atenção** (Cosenza), evitando a sobrecarga cognitiva (Dehaene)."
    ),
    "Plasticidade Cerebral (Cosenza)": (
        "**Conceito:** O cérebro muda fisicamente com a experiência (Neuroplasticidade).\n\n"
        "A avaliação é um processo de reforço sináptico: o erro é uma **pista** para o ajuste, não um veredito final."
    ),
    # === INSIRA ESTE TRECHO AQUI ===
    "Stanislas Dehaene": (
        "### 🧬 Stanislas Dehaene: Os Quatro Pilares da Aprendizagem\n\n"
        "**Referência:** DEHAENE, S. (2022). *É assim que aprendemos*.\n\n"
        "Sustenta a base neurocientífica da SINAPSE-BR IA através de quatro pilares fundamentais:\n"
        "1. **Atenção:** Seleção da informação (Filtro do Núcleo).\n"
        "2. **Engajamento Ativo:** O aluno como gerador de hipóteses (Práxis).\n"
        "3. **Feedback de Erro:** Comparação entre previsão e realidade (Avaliação).\n"
        "4. **Consolidação:** Automação do aprendizado (Mútua Possessão)."
    ),
    # ===============================
    

    # --- EIXO AVALIATIVO ---
    "Eixo Avaliativo": (
        "### 📏 Eixo Avaliativo\n"
        "Define a avaliação como processo contínuo e transparente. Foco na **Meta-Avaliação** (avaliação da qualidade da própria rubrica).\n\n"
        "**Referência:** Brookhart (2013) e Mullinix (2003)."
    ),
    "Avaliacao Formativa (Brookhart)": (
        "**Citação:** 'A avaliação formativa não é um teste, é um episódio de aprendizagem.' (Brookhart, 2013).\n\n"
        "A rubrica é um guia (mapa) que clarifica o objetivo e fornece **Feedback Descritivo**, essencial para a regulação."
    ),
    "Meta-Rubrica (Mullinix)": (
        "**Ferramenta:** *Rubric for Assessing Rubrics* (Mullinix, 2003).\n\n"
        "A régua para medir a qualidade das rubricas do SINAPSE (Pág. 05) em 4 níveis (Clareza, Confiabilidade, Metacognição)."
    ),
    "Feedback de qualidade": (
        "**Princípio:** Devolutivas que são **Acionáveis** (o aluno sabe o que fazer a seguir), **Específicas** e **Timely** (na hora certa). Fundamental para a regulação."
    ),

    # --- EIXO TECNOLÓGICO ---
    "Eixo Tecnologico": (
        "### 💻 Eixo Tecnológico (IA)\n"
        "A tecnologia como estruturante da análise de dados educacionais (Cultura de Dados).\n\n"
        "**Agente Racional (Russell & Norvig):** O sistema percebe o ambiente (dados) e age (sugere intervenções)."
    ),
    "Cultura de Dados": (
        "**Conceito:** A coleta e análise sistemática de dados educacionais (Censo, SAEB) para embasar a tomada de decisão do professor e do gestor."
    ),
    "Moodle e Bloom (Duarte Jr.)": (
        "**Referência:** DUARTE JUNIOR, D. N. S. (2021).\n\n"
        "Fundamenta a operacionalização da Taxonomia de Bloom em Ambientes Virtuais de Aprendizagem (Moodle), ligando atividades digitais a níveis cognitivos específicos."
    ),
    "Agentes Inteligentes (Russell & Norvig)": (
        "**Conceito:** IA é o estudo de agentes que recebem percepções do ambiente e realizam ações.\n\n"
        "No contexto do TCC, o 'Agente' é o algoritmo que processa os microdados do Censo/SAEB "
        "para identificar padrões de desigualdade e sugerir intervenções pedagógicas precisas."
    ),

    # --- EIXO TERRITORIAL ---
    "Eixo Territorial": (
        "### 🗺️ Eixo Territorial\n"
        "A avaliação é situada: ela considera a **Interseccionalidade Geográfica** (TMAP vs. Noroeste de Minas) e **Socioeconômica** (INSE).\n\n"
        "**Exemplo:** *'Uma escola rural em Veríssimo tem desafios diferentes de um campus urbano em Uberlândia.'*"
    ),
    "Equidade Socio-territorial": (
        "**Aplicação:** O sistema usa INSE (Nível Socioeconômico) e Zona (Rural/Urbana) para ponderar os resultados. Combate a **invisibilidade** de escolas rurais e de baixo INSE."
    ),
    "Critica do territorio CTC": (
        "**Conceito:** Critérios de Territorialidade, Contexto e Cultura. Garante que o conteúdo da EPT se ligue ao Arranjo Produtivo Local (Frigotto/Ciavatta)."
    ),
    "Indicadores INEP/SAEB": (
        "**Fonte de Dados:** INEP/SISTEC, SAEB (nota), INSE (Nível Socioeconômico). Os dados são a matéria-prima do Agente Racional."
    ),

    # --- EIXO INCLUSIVO ---
    "Eixo Inclusivo": (
        "### ♿ Eixo Inclusivo (DUA)\n"
        "Garante que o processo de avaliação seja acessível a todos.\n\n"
        "**Base:** Desenho Universal para a Aprendizagem (CAST).\n"
    ),
    "Desenho Universal (DUA)": (
        "**Conceito:** Eliminar barreiras antes que apareçam. A rubrica deve oferecer múltiplos meios de **Expressão** e **Representação** do conhecimento."
    ),
    "Acessibilidade": (
        "**Infraestrutura e Design:** O mapa TMAP destaca acessibilidade física (rampas, banheiros PNE) e digital (Internet/Lab) como fatores de equidade."
    ),
    "Materiais multiformato": (
        "**DUA na Prática:** O sistema incentiva o professor a receber trabalhos em texto, áudio, vídeo, e outros formatos, respeitando a diversidade neurofuncional."
    )
}

# 🔑 CORREÇÃO CRÍTICA: Resolve KeyError garantindo chave raiz sem espaços
details.setdefault(
    "Rubrica SINAPSE BR IA",
    "### 🧩 O Artefato: Rubrica SINAPSE-BR IA\n\nO sistema transcende a avaliação classificatória."
)

# 💥 CORTE INFERNAL (GARANTE TEXTO RICO EM TODOS OS NÓS)
topic_to_parent = {}
for parent, topics in links.items():
    rich_parent_text = details.get(parent, "Sem descrição do Eixo Pai.")
    for topic in topics:
        if topic not in details:
            clean_text = rich_parent_text.replace(f'### {parent}', '').replace('###', '').strip()
            details[topic] = f"### {topic}\n\nResumo do Eixo Pai: {clean_text}"

# CONSTRUÇÃO DOS NODES/EDGES
nodes, edges = [], []
# Nó Raiz Central
nodes.append({
    "id": "Rubrica SINAPSE BR IA",
    "label": "SINAPSE-BR IA\n(Artefato)",
    "color": "#ea580c",  # Laranja forte
    "shape": "circle",
    "size": 35,
    "font": {"size": 20, "color": "white", "face": "Inter"}
})
# Cores para cada eixo (mesma paleta do TCC)
colors = {
    "Eixo Cognitivo": "#3b82f6",      # Azul
    "Eixo Afetivo": "#ef4444",        # Vermelho
    "Eixo Metodologico": "#10b981",   # Verde
    "Eixo Neurofuncional": "#8b5cf6", # Roxo
    "Eixo Avaliativo": "#f59e0b",     # Laranja Claro
    "Eixo Tecnologico": "#64748b",    # Cinza
    "Eixo Territorial": "#14b8a6",    # Verde Água
    "Eixo Inclusivo": "#ec4899"       # Rosa
}
# Adiciona Eixos e Tópicos
topic_added = set()
for d in dims:
    c = colors.get(d, "#60a5fa")
    # Nó do Eixo
    nodes.append({"id": d, "label": d, "color": c, "shape": "box", "font": {"color": "white"}})
    edges.append({"from": "Rubrica SINAPSE BR IA", "to": d, "color": c, "width": 2})
    # Nós dos Tópicos
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

# HTML/JS INJETADO (RENDERIZAÇÃO) - COM PARSEMARKDOWN OTIMIZADO E SEGURO
html_code = f"""
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <script src="https://cdn.jsdelivr.net/npm/vis-network@9.1.6/dist/vis-network.min.js"></script>
  <style>
    body {{ margin:0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #ffffff; }}
    .wrap {{ display:flex; height:760px; }}
    #net {{ flex:1; height:100%; background: #ffffff; }}
    #panel {{ 
        width: 350px; 
        padding: 20px; 
        background: #f8fafc; 
        border-left: 1px solid #e2e8f0; 
        overflow-y: auto; 
        box-shadow: -2px 0 10px rgba(0,0,0,0.05);
    }}
    #panel h3 {{ color: #1e40af; margin-top: 0; font-size: 18px; }}
    #content {{ font-size: 14px; line-height: 1.6; color: #334155; padding: 10px 0; }}
    #content strong {{ color: #0f172a; font-weight: 600; }}
    #content ul {{ padding-left: 20px; margin: 12px 0; }}
    #content li {{ margin-bottom: 6px; line-height: 1.5; }}
    #content p {{ margin: 8px 0; line-height: 1.6; }}
    .copy-btn {{
        margin-top: 20px;
        padding: 10px 15px;
        background-color: #fff;
        border: 1px solid #cbd5e1;
        border-radius: 8px;
        cursor: pointer;
        font-size: 13px;
        transition: all 0.2s;
        color: #475569;
        display: block;
        width: 100%;
        font-weight: 500;
    }}
    .copy-btn:hover {{ background-color: #f1f5f9; border-color: #94a3b8; }}
    .copy-btn:active {{ transform: translateY(1px); }}
    .copy-btn:after {{ content: "📋"; margin-right: 8px; }}
  </style>
</head>
<body>
  <div class="wrap">
    <div id="net"></div>
    <div id="panel">
      <div id="color-indicator" style="display:none;">
      <div class="color-chip">
        <span id="color-dot" class="dot"></span>
        <span id="color-name"></span>
      </div>
      </div>
      <h3>📘 Fundamentação Acadêmica</h3>
      <div id="content">
        <p style="color:#64748b; font-style:italic; padding:15px; background:#f8fafc; border-radius:8px;">
          Clique em um nó do mapa para visualizar o resumo teórico, as referências bibliográficas e a aplicação no TCC.
        </p>
      </div>
      <button class="copy-btn" onclick="copyText()">Copiar Texto para o TCC</button>
    </div>
  </div>
  <script>
    const nodes = new vis.DataSet({json.dumps(nodes, ensure_ascii=False)});
    const edges = new vis.DataSet({json.dumps(edges, ensure_ascii=False)});
    const options = {json.dumps(options, ensure_ascii=False)};
    
    const network = new vis.Network(document.getElementById('net'), {{nodes, edges}}, options);
    
    // Dicionário de Detalhes (Python -> JS)
    const details = {json.dumps(details, ensure_ascii=False)};

    // Função robusta e segura de Markdown -> HTML
    function parseMarkdown(text) {{
        if (!text || text.trim() === '') return "<em>Selecione um tópico.</em>";
        
        // Processamento em etapas para evitar falhas
        let html = text
            .replace(/\\n\\n/g, '||DOUBLE||')
            .replace(/\\n/g, '<br>')
            .replace(/\\|\\|DOUBLE\\|\\|/g, '</p><p>')
            .replace(/^### (.*$)/gm, '<h3 style="color:#0284c7; margin:15px 0 8px 0; font-size:16px;">$1</h3>')
            .replace(/^## (.*$)/gm, '<h2 style="color:#1e40af; margin:20px 0 10px 0; font-size:18px;">$1</h2>')
            .replace(/\\*\\*(.*?)\\*\\*/g, '<strong>$1</strong>')
            .replace(/\\*(.*?)\\*/g, '<em>$1</em>')
            .replace(/^- (.*$)/gm, '<li style="margin-bottom:6px; line-height:1.5;">$1</li>')
            .replace(/<li>/g, '<ul style="padding-left:20px; margin:10px 0;"><li>')
            .replace(/<\\/li>(?!<\\/ul>)/g, '</li></ul>');
        
        // Garantir que o conteúdo esteja envolvido em parágrafo se não tiver tags estruturais
        if (!html.includes('<h') && !html.includes('<ul') && !html.includes('<p')) {{
            html = `<p style="margin:8px 0; line-height:1.6;">${{html}}</p>`;
        }}
        
        return html || "<em>Conteúdo não disponível.</em>";
    }}

// Localize network.on('selectNode', ...) e substitua por este:
    network.on('selectNode', function(params) {{
    if (params.nodes.length > 0) {{
        const nodeId = params.nodes[0];
        
        // Mapeamento de cores (Recupera do objeto JS)
        const parentId = topicParent[nodeId] || nodeId;
        const colorData = colorsMap[parentId];

        if(colorData) {{
            document.getElementById('color-indicator').style.display = 'flex';
            document.getElementById('color-dot').style.backgroundColor = colorData.hex;
            document.getElementById('color-name').innerText = "Eixo: " + colorData.nome;
        }} else {{
            document.getElementById('color-indicator').style.display = 'none';
        }}
        
        // Sua lógica original de parseMarkdown
        const rawText = details[nodeId] || "<em>Texto não encontrado.</em>";
        document.getElementById('content').innerHTML = parseMarkdown(rawText);
       }}
    }});

    function copyText() {{
        const text = document.getElementById('content').innerText;
        navigator.clipboard.writeText(text).then(() => {{
            const btn = document.querySelector('.copy-btn');
            btn.innerHTML = '✅ Copiado!';
            setTimeout(() => {{
                btn.innerHTML = '📋 Copiar Texto para o TCC';
            }}, 2000);
        }}).catch(err => {{
            alert('Erro ao copiar: ' + err);
        }});
    }}
  </script>
</body>
</html>
"""
st_html(html_code, height=800, scrolling=False)

# BLOCAGEM DIDÁTICA (Resumo da Matriz 8x5)
st.divider()
st.markdown("## 📊 A Matriz 8x5: Sumário da Estrutura SINAPSE")
# Tabela estática de resumo (8x5)
st.markdown("""
<style>
.matrix-table {
    width: 100%;
    border-collapse: collapse;
    margin: 20px 0;
    font-size: 0.95rem;
    box-shadow: 0 2px 10px rgba(0,0,0,0.08);
    border-radius: 8px;
    overflow: hidden;
}
.matrix-table th, .matrix-table td {
    border: 1px solid #cbd5e1;
    padding: 10px 12px;
    text-align: left;
}
.matrix-table th {
    background-color: #1e40af;
    color: white;
    font-weight: 600;
}
.matrix-table tr:nth-child(even) {
    background-color: #f8fafc;
}
.matrix-table tr:hover {
    background-color: #dbeafe;
}
.level-head {
    text-align: center !important;
    background-color: #3b82f6;
    color: white;
    font-weight: bold;
}
.highlight {
    background-color: #fff9e6;
    font-weight: 500;
    border-left: 3px solid #f59e0b;
}
</style>
<table class="matrix-table">
    <thead>
        <tr>
            <th>EIXO (O QUE AVALIAR)</th>
            <th class="level-head">1. Emergente</th>
            <th class="level-head">2. Básico</th>
            <th class="level-head">3. Proficiente</th>
            <th class="level-head">4. Avançado</th>
            <th class="level-head">5. Expert</th>
        </tr>
    </thead>
    <tbody>
        <tr class="highlight">
            <td><strong>🧠 Cognitivo (Bloom/SOLO)</strong></td>
            <td>Lembrar fatos</td>
            <td>Interpretar/Exemplificar</td>
            <td>Aplicar procedimentos</td>
            <td>Analisar/Avaliar</td>
            <td>Criar/Generalizar</td>
        </tr>
        <tr>
            <td><strong>❤️ Afetivo (Motivação)</strong></td>
            <td>Engajamento oscilante</td>
            <td>Aceita feedback</td>
            <td>Busca feedback</td>
            <td>Autorregula emoções</td>
            <td>Lidera com empatia</td>
        </tr>
        <tr>
            <td><strong>🛠️ Metodológico (Práxis)</strong></td>
            <td>Segue roteiros</td>
            <td>Escolhe estratégia</td>
            <td>Executa projetos (PBL)</td>
            <td>Integra metodologias</td>
            <td>Desenha intervenções</td>
        </tr>
        <tr>
            <td><strong>🧬 Neurofuncional (FE)</strong></td>
            <td>Atenção Curta</td>
            <td>Usa anotações</td>
            <td>Usa metacognição</td>
            <td>Alterna focos</td>
            <td>Ensina estratégias</td>
        </tr>
        <tr>
            <td><strong>📏 Avaliativo (Brookhart)</strong></td>
            <td>Precisa de critérios</td>
            <td>Usa rubrica para revisar</td>
            <td>Coavalia pares</td>
            <td>Constrói rubricas</td>
            <td>Conduz avaliação</td>
        </tr>
        <tr>
            <td><strong>💻 Tecnológico (IA/Dados)</strong></td>
            <td>Utiliza ferramentas básicas</td>
            <td>Opera AVA</td>
            <td>Integra planilhas</td>
            <td>Automatiza fluxos</td>
            <td>Cria apps/scripts</td>
        </tr>
        <tr>
            <td><strong>🗺️ Territorial (Equidade)</strong></td>
            <td>Reconhece local</td>
            <td>Relaciona ao curso</td>
            <td>Analisa indicadores</td>
            <td>Propõe soluções regionais</td>
            <td>Articula políticas</td>
        </tr>
        <tr>
            <td><strong>♿ Inclusivo (DUA)</strong></td>
            <td>Reconhece diversidade</td>
            <td>DUA básico</td>
            <td>Adapta materiais</td>
            <td>Desenha trilhas acessíveis</td>
            <td>Promove cultura inclusiva</td>
        </tr>
    </tbody>
</table>
""", unsafe_allow_html=True)

st.divider()

st.markdown("### 🗺️ A Nova Geometria da Avaliação")

col_text, col_formula = st.columns([2, 1])

with col_text:
    # O texto deve estar estritamente dentro das aspas triplas do st.info
    st.info("""
**Interpretação: Do Achatamento ao Volume (V343)**

A Rubrica SINAPSE-BR IA transcende a nota unidimensional e a antiga matriz plana. Ela opera na **Volumetria da Competência**, onde cada eixo representa um pilar fundamental da formação humana integral:

* **🔵 Eixo X – Cognitivo (Azul):** Funções executivas, profundidade e neuroplasticidade (Tese Profa. Thays). Baseado nos pilares de **Stanislas Dehaene**.
* **🟠 Eixo Y – Práxis/Agir (Laranja):** Maestria operacional, técnica e rigor (Tese Prof. Alexandre).
* **🟢 Eixo Z – Territorial (Verde):** O 'Geofilosofar' e a Ética da Hospitalidade (Tese Prof. Paulo Irineu).
    """)
    
with col_formula:
    # Métrica visual do Volume de Emancipação
    st.metric(label="Capacidade Volumétrica", value="V343", delta="343 Possibilidades")
    st.caption("Fórmula: V = (X+1) * (Y+1) * (Z+1)")

st.success("""
**✨ Ponto Focal: Emancipação Tridimensional**
Diferente da matriz tradicional, aqui o foco é a sinergia. Quando os eixos se expandem, 
o aluno deixa de ser um 'operário treinado' para se tornar um 'habitante consciente' da Terra de Todos.
""")

st.markdown("""
<div style='background-color: #f0fdf4; padding: 15px; border-radius: 10px; border-left: 5px solid #22c55e; color: #166534;'>
    <strong>🌟 Insight Pedagógico:</strong> O SINAPSE-BR IA atua como um Auditor de Competência, 
    garantindo que o descritor final possua <strong>Volume Social e Profundidade Humana</strong>, superando o achatamento da prensa hidráulica.
</div>
""", unsafe_allow_html=True)

# 🎥 SEÇÃO DE VÍDEO EXPLICATIVO
st.divider()

st.markdown("""
<div style="text-align: center; background: linear-gradient(135deg, rgba(30, 58, 138, 0.08) 0%, rgba(2, 6, 23, 0.08) 100%); border-radius: 16px; padding: 28px; margin: 30px 0; border: 1px solid rgba(59, 130, 246, 0.25);">
    <h2 style="color: #1e40af; margin-bottom: 12px; font-weight: 700;">🎥 Arquitetura do Conhecimento SINAPSE-BR IA</h2>
</div>
""", unsafe_allow_html=True)

video_iframe = '''
<div style="display: flex; justify-content: center; margin: 25px 0 40px; padding: 25px; background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%); border-radius: 22px;">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/Ay_R1kzGll4" frameborder="0" allowfullscreen></iframe>
</div>
'''
# 1. DEFINIÇÃO DA VARIÁVEL (Sempre antes de usar no st.markdown)
jornada_conceitual_html = """
<div style="background: white; border-radius: 18px; padding: 32px; box-shadow: 0 6px 25px rgba(0, 0, 0, 0.08); border: 1px solid #e2e8f0; margin: 15px 0 45px; position: relative; overflow: hidden; max-width: 100%;">
    <div style="position: absolute; top: 0; left: 0; width: 6px; height: 100%; background: linear-gradient(to bottom, #3b82f6, #1e40af);"></div>
    <h3 style="color: #0f172a; margin-top: 0; font-size: 1.55rem; display: flex; align-items: center; gap: 12px; font-weight: 700; padding-left: 12px;">
        <span style="background: #dbeafe; color: #1e40af; width: 36px; height: 36px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; font-size: 1.1rem; flex-shrink: 0;">5</span>
        Fases da Jornada Conceitual SINAPSE-BR
    </h3>
    <div style="margin: 28px 0 20px; padding-left: 8px;">
        <div style="display: flex; align-items: flex-start; gap: 20px; margin: 22px 0; padding-left: 12px; border-left: 3px solid #3b82f6; padding-bottom: 8px;">
            <span style="font-size: 1.7rem; margin-top: 6px; flex-shrink: 0;">🔵</span>
            <div>
                <strong style="color: #0f172a; font-size: 1.2rem; display: block; margin-bottom: 6px; font-weight: 600;">Fase 1: Eixo X - Cognição (Azul)</strong>
                <span style="color: #475569; line-height: 1.65; font-size: 1.02rem; display: block;">
                    Baseado em <strong>Stanislas Dehaene</strong> e na Neuroplasticidade. Foco nos processos de Atenção e Memória de Trabalho para a consolidação do saber.
                </span>
            </div>
        </div>
        <div style="display: flex; align-items: flex-start; gap: 20px; margin: 22px 0; padding-left: 12px; border-left: 3px solid #f59e0b; padding-bottom: 8px;">
            <span style="font-size: 1.7rem; margin-top: 6px; flex-shrink: 0;">🟠</span>
            <div>
                <strong style="color: #0f172a; font-size: 1.2rem; display: block; margin-bottom: 6px; font-weight: 600;">Fase 2: Eixo Y - Práxis (Laranja)</strong>
                <span style="color: #475569; line-height: 1.65; font-size: 1.02rem; display: block;">
                    O engajamento ativo e a técnica. É a maestria operacional no Mundo do Trabalho, onde a teoria se transforma em intervenção real.
                </span>
            </div>
        </div>
        <div style="display: flex; align-items: flex-start; gap: 20px; margin: 22px 0; padding-left: 12px; border-left: 3px solid #10b981; padding-bottom: 8px;">
            <span style="font-size: 1.7rem; margin-top: 6px; flex-shrink: 0;">🟢</span>
            <div>
                <strong style="color: #0f172a; font-size: 1.2rem; display: block; margin-bottom: 6px; font-weight: 600;">Fase 3: Eixo Z - Territorial (Verde)</strong>
                <span style="color: #475569; line-height: 1.65; font-size: 1.02rem; display: block;">
                    A Geofilosofia e a Ética da Hospitalidade. O saber situado no contexto real, garantindo a emancipação social.
                </span>
            </div>
        </div>
    </div>
</div>
"""

# 2. RENDERIZAÇÃO DOS COMPONENTES (FORA DE QUALQUER BLOCO DE TEXTO OU INFO)

# Insight Pedagógico
st.markdown("""
<div style='background-color: #f0fdf4; padding: 15px; border-radius: 10px; border-left: 5px solid #22c55e; color: #166534; margin-bottom: 20px;'>
    <strong>🌟 Insight Pedagógico:</strong> O SINAPSE-BR IA atua como um Auditor de Competência, 
    garantindo que o descritor final possua <strong>Volume Social e Profundidade Humana</strong>.
</div>
""", unsafe_allow_html=True)

# Seção de Vídeo Direta
st.divider()
st.markdown("<h2 style='text-align: center; color: #1e40af;'>🎥 Arquitetura do Conhecimento SINAPSE-BR IA</h2>", unsafe_allow_html=True)
st.video("https://www.youtube.com/watch?v=Ay_R1kzGll4")
st.caption("Vídeo explicativo: A jornada do conhecimento através dos eixos Cognitivo, Práxis e Territorial.")

# Renderização final da jornada das 5 fases
st.markdown(jornada_conceitual_html, unsafe_allow_html=True)
