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
# DICIONÁRIO DE CONTEÚDO RICO (VERSÃO ESTÁVEL)
# ──────────────────────────────────────────────────────────────────────────────
details = {
    "Rubrica SINAPSE BR IA": (
        "### 🧩 O Artefato: Rubrica SINAPSE-BR IA\n\n"
        "O sistema transcende a avaliação classificatória, atuando como um **Agente Racional** (Russell & Norvig) "
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

# ──────────────────────────────────────────────────────────────────────────────
# 💥 CORTE INFERNAL (GARANTE TEXTO RICO EM TODOS OS NÓS)
# ──────────────────────────────────────────────────────────────────────────────
# Mapeia as relações pai-filho
topic_to_parent = {}
for parent, topics in links.items():
    rich_parent_text = details.get(parent, "Sem descrição do Eixo Pai.")
    for topic in topics:
        # Se o tópico não tiver uma descrição específica, ele herda do Eixo pai.
        if topic not in details:
            # O tópico folha recebe o texto rico do Eixo pai + um aviso de que é o resumo
            details[topic] = f"### {topic}\n\n**Resumo do Eixo Pai:** {rich_parent_text.replace(f'### {parent}', '').replace('###', '').strip()}"

# Garante que o Nó Raiz esteja sempre presente
details.setdefault(
    "Rubrica SINAPSE BR IA",
    details["Rubrica SINAPSE BR IA"]
)

# ──────────────────────────────────────────────────────────────────────────────
# CONSTRUÇÃO DOS NODES/EDGES
# ──────────────────────────────────────────────────────────────────────────────
nodes, edges = [], []

# Nó Raiz Central
nodes.append({
    "id": "Rubrica SINAPSE BR IA",
    "label": "SINAPSE-BR IA\n(Artefato)",
    "color": "#ea580c", # Laranja forte
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
            # Cor mais clara para o tópico
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
# HTML/JS INJETADO (RENDERIZAÇÃO)
# ──────────────────────────────────────────────────────────────────────────────
html_code = f"""
<!doctype html>
<html>
<head>
  <meta charset="utf-8" />
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
    #panel h3 {{ color: #1e40af; margin-top: 0; }}
    #content {{ font-size: 14px; line-height: 1.6; color: #334155; }}
    #content strong {{ color: #0f172a; }}
    
    /* Estilo do botão de copiar */
    .copy-btn {{
        margin-top: 15px;
        padding: 8px 15px;
        background-color: #fff;
        border: 1px solid #cbd5e1;
        border-radius: 6px;
        cursor: pointer;
        font-size: 12px;
        transition: all 0.2s;
        color: #475569;
        display: block;
        width: 100%;
    }}
    .copy-btn:hover {{ background-color: #f1f5f9; border-color: #94a3b8; }}
    .copy-btn:active {{ transform: translateY(1px); }}
  </style>
</head>
<body>
  <div class="wrap">
    <div id="net"></div>
    <aside id="panel">
      <h3>📘 Fundamentação Acadêmica</h3>
      <div id="content">
        <p style="color:#64748b; font-style:italic;">
          Clique em um nó do mapa para visualizar o resumo teórico, as referências bibliográficas e a aplicação no TCC.
        </p>
      </div>
      <button class="copy-btn" onclick="copyText()">📋 Copiar Texto para o TCC</button>
    </aside>
  </div>

  <script>
    const nodes = new vis.DataSet({json.dumps(nodes, ensure_ascii=False)});
    const edges = new vis.DataSet({json.dumps(edges, ensure_ascii=False)});
    const options = {json.dumps(options, ensure_ascii=False)};
    
    const network = new vis.Network(document.getElementById('net'), {{nodes, edges}}, options);
    
    // Dicionário de Detalhes (Python -> JS)
    const details = {json.dumps(details, ensure_ascii=False)};

    // Função simples de Markdown -> HTML (Para o painel lateral)
    function parseMarkdown(text) {{
        if (!text) return "<em>Selecione um tópico.</em>";
        return text
            .replace(/^### (.*$)/gim, '<h3 style="color:#0284c7; margin-bottom:5px;">$1</h3>')
            .replace(/^## (.*$)/gim, '<h2>$1</h2>')
            .replace(/\*\*(.*?)\*\*/gim, '<strong>$1</strong>') // Negrito
            .replace(/- (.*$)/gim, '<li>$1</li>') // Listas
            .replace(/\\n/g, '<br>'); // Quebra de linha
    }}

    network.on('selectNode', function(params) {{
        if (params.nodes.length > 0) {{
            const nodeId = params.nodes[0];
            const rawText = details[nodeId] || "<em>Erro: Texto não encontrado para este nó.</em>"; // Fallback final
            // A mágica acontece aqui: usamos o parser de Markdown para renderizar o texto rico
            document.getElementById('content').innerHTML = parseMarkdown(rawText); 
            document.getElementById('content').setAttribute('data-raw', rawText);
        }}
    }});

    function copyText() {{
        const text = document.getElementById('content').innerText;
        navigator.clipboard.writeText(text).then(() => {{
            const btn = document.querySelector('.copy-btn');
            btn.innerText = "✅ Copiado!";
            setTimeout(() => btn.innerText = "📋 Copiar Texto para o TCC", 2000);
        }});
    }}
  </script>
</body>
</html>
"""

st_html(html_code, height=800, scrolling=False)

# ──────────────────────────────────────────────────────────────────────────────
# BLOCAGEM DIDÁTICA (Resumo da Matriz 8x5)
# ──────────────────────────────────────────────────────────────────────────────

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
}
.matrix-table th, .matrix-table td {
    border: 1px solid #cbd5e1;
    padding: 8px 12px;
    text-align: left;
}
.matrix-table th {
    background-color: #f1f5f9;
    color: #1e40af;
    font-weight: 600;
}
.matrix-table tr:nth-child(even) {
    background-color: #f9f9f9;
}
.level-head {
    text-align: center !important;
    background-color: #e2e8f0;
}
.highlight {
    background-color: #fff9e6;
    font-weight: 500;
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
    <tr>
        <td>🧠 Cognitivo (Bloom/SOLO)</td>
        <td>Lembrar fatos</td>
        <td>Interpretar/Exemplificar</td>
        <td class="highlight">Aplicar procedimentos</td>
        <td>Analisar/Avaliar</td>
        <td>Criar/Generalizar</td>
    </tr>
    <tr>
        <td>❤️ Afetivo (Motivação)</td>
        <td>Engajamento oscilante</td>
        <td>Aceita feedback</td>
        <td>Busca feedback</td>
        <td>Autorregula emoções</td>
        <td>Lidera com empatia</td>
    </tr>
    <tr>
        <td>🛠️ Metodológico (Práxis)</td>
        <td>Segue roteiros</td>
        <td>Escolhe estratégia</td>
        <td>Executa projetos (PBL)</td>
        <td>Integra metodologias</td>
        <td>Desenha intervenções</td>
    </tr>
    <tr>
        <td>🧬 Neurofuncional (FE)</td>
        <td>Atenção Curta</td>
        <td>Usa anotações</td>
        <td>Usa metacognição</td>
        <td>Alterna focos</td>
        <td>Ensina estratégias</td>
    </tr>
    <tr>
        <td>📏 Avaliativo (Brookhart)</td>
        <td>Precisa de critérios</td>
        <td>Usa rubrica para revisar</td>
        <td>Coavalia pares</td>
        <td>Constrói rubricas</td>
        <td>Conduz avaliação</td>
    </tr>
    <tr>
        <td>💻 Tecnológico (IA/Dados)</td>
        <td>Utiliza ferramentas básicas</td>
        <td>Opera AVA</td>
        <td>Integra planilhas</td>
        <td>Automatiza fluxos</td>
        <td>Cria apps/scripts</td>
    </tr>
    <tr>
        <td>🗺️ Territorial (Equidade)</td>
        <td>Reconhece local</td>
        <td>Relaciona ao curso</td>
        <td>Analisa indicadores</td>
        <td>Propõe soluções regionais</td>
        <td>Articula políticas</td>
    </tr>
    <tr>
        <td>♿ Inclusivo (DUA)</td>
        <td>Reconhece diversidade</td>
        <td>DUA básico</td>
        <td>Adapta materiais</td>
        <td>Desenha trilhas acessíveis</td>
        <td>Promove cultura inclusiva</td>
    </tr>
</tbody>
</table>
""", unsafe_allow_html=True)

st.info("""
    **Interpretação:** A matriz 8x5 (8 Eixos x 5 Níveis) é a espinha dorsal da rubrica.
    * **Eixos (Vertical):** Representam os construtos teóricos (Neuro, Social, Técnico) que definem O QUE avaliar.
    * **Níveis (Horizontal):** Representam a progressão de competência (Vygotsky) e complexidade (Bloom).
    * **Ponto Focal (3. Proficiente):** É o nível esperado para o aluno ao final da unidade/curso, focando no **Aplicar/Desenvolver** da Taxonomia de Bloom Revisada.

    Essa visualização garante que a avaliação seja **multidimensional** e **formativa**, focando na evolução do aluno e não apenas no resultado.
""")
