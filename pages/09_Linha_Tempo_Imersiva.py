# /home/neirivon/SINAPSE2.0/sinapsebr_rubrica/scripts/pages/09_Linha_Tempo_Imersiva.py
# --------------------------------------------------------------------------------------
# NOME DO SCRIPT: 09_Linha_Tempo_Imersiva.py
# DESCRIÇÃO: Implementação de uma Linha do Tempo Interativa (Timeline) utilizando
#            HTML/CSS/JS injetados.
# FUNCIONALIDADES:
#   1. Visualização cronológica vertical (Macro/Micro/Pessoal).
#   2. Interatividade Mouseover (Hover): Mostra feedback visual e resumo.
#   3. Interatividade Click (Modal): Abre janela detalhada com contexto histórico.
#   4. Narrativa Cronotópica: Evolução da Avaliação na EPT (do disciplinar à IA).
# AUTOR: Neirivon Elias Cardoso (Adaptado por Gemini)
# PROJETO: Rubrica SINAPSE-BR IA
# DATA: 12/01/2026 (Atualizado com Trajetória Pessoal Recursiva)
# --------------------------------------------------------------------------------------

import streamlit as st
import streamlit.components.v1 as components
import json

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Linha do Tempo • Memória EPT",
    page_icon="⏳",
    layout="wide"
)

# Bloqueia tradução automática do navegador para não quebrar termos técnicos
st.markdown('<meta name="google" content="notranslate">', unsafe_allow_html=True)

# --- TÍTULO E CONTEXTUALIZAÇÃO ---
st.markdown("""
    <h1 style='text-align: center; color: #1e3a8a;'>🌀 A Espiral do Tempo: Da Gênese à SINAPSE-BR IA</h1>
    <p style='text-align: center; font-size: 1.2em; color: #4b5563;'>
        Uma jornada cronotópica pela evolução da avaliação e da Educação Profissional no Brasil.
    </p>
""", unsafe_allow_html=True)

# --- LEGENDA SEMÂNTICA (Ajustada com as cores exatas) ---
st.markdown("""
    <div style="display: flex; justify-content: center; gap: 30px; margin-bottom: 30px; flex-wrap: wrap; background-color: #f8fafc; padding: 15px; border-radius: 10px;">
        <div style="display: flex; align-items: center; gap: 10px;">
            <span style="background-color: #ef4444; width: 22px; height: 22px; border-radius: 50%; display: inline-block; border: 2px solid #fff; box-shadow: 0 2px 4px rgba(0,0,0,0.1);"></span>
            <span style="font-size: 0.95em; color: #1e293b;"><b>Nível Macro (Vermelho):</b> Políticas, Leis e Tensões Nacionais</span>
        </div>
        <div style="display: flex; align-items: center; gap: 10px;">
            <span style="background-color: #10b981; width: 22px; height: 22px; border-radius: 50%; display: inline-block; border: 2px solid #fff; box-shadow: 0 2px 4px rgba(0,0,0,0.1);"></span>
            <span style="font-size: 0.95em; color: #1e293b;"><b>Nível Local e Pessoal (Verde):</b> IFTM, Território e Trajetória do Autor</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# --------------------------------------------------------------------------------------
# 1. DADOS DA LINHA DO TEMPO (SEQUÊNCIA CORRIGIDA 0-9)
# --------------------------------------------------------------------------------------
eventos_timeline = [
    {
        "id": 0,
        "ano": "1809",
        "titulo": "🌀 O Embrião: Colégio de Fábricas",
        "categoria": "macro",
        "resumo": "D. João VI e a origem da dualidade assistencialista.",
        "detalhe": """
            <h3>A Pré-História da EPT no Brasil</h3>
            <p><b>Contexto:</b> Criado por D. João VI logo após a chegada da Corte ao Rio de Janeiro.</p>
            <p>Primeira tentativa oficial de ensino de ofícios, com viés assistencialista para 'órfãos e expostos'.</p>
            <hr>
            <p>🔍 <b>Importância:</b> Explica a raiz da <b>Dualidade Estrutural</b>: trabalho manual como caridade ou punição, não como direito educativo.</p>
        """
    },
    {
        "id": 1,
        "ano": "1909",
        "titulo": "A Gênese Assistencialista",
        "categoria": "macro",
        "resumo": "Decreto nº 7.566: Escolas de Aprendizes Artífices.",
        "detalhe": """
            <h3>O Marco Zero: Amparar os Desvalidos</h3>
            <p><b>Marco Jurídico:</b> Decreto nº 7.566 (Nilo Peçanha).</p>
            <p>A Rede Federal nasce para "amparar os desvalidos da sorte", focando no ofício manual para evitar o vício.</p>
            <hr>
            <p>🔍 <b>Modelo Avaliativo:</b> <i>Disciplinar e Corretivo</i>. Avaliava-se a conduta moral em vez do intelecto.</p>
        """
    },
    {
        "id": 2,
        "ano": "1937 - 1942",
        "titulo": "Liceus Industriais e Era Vargas",
        "categoria": "macro",
        "resumo": "Reforma Capanema e Consolidação Industrial.",
        "detalhe": """
            <h3>A Serviço da Industrialização</h3>
            <p><b>Contexto:</b> Transição do modelo artesanal para o industrial. O ensino técnico torna-se estratégico para a economia.</p>
            <hr>
            <p>🔍 <b>Modelo Avaliativo:</b> <i>Psicométrico</i>. Testes para selecionar "o homem certo para o lugar certo" (Taylorismo escolar).</p>
        """
    },
    {
        "id": 3,
        "ano": "1957",
        "titulo": "O Nascimento do CAU (Uberlândia)",
        "categoria": "micro",
        "resumo": "Lei nº 3.383: Criação do Colégio Agrícola na Fazenda Sobradinho.",
        "detalhe": """
            <h3>A Vocação Rural e o Internato</h3>
            <p>Nasce a instituição mãe do IFTM Uberlândia. Funcionava em regime de <b>internato rígido</b>.</p>
            <hr>
            <p>🔍 <b>Modelo Avaliativo:</b> <i>Comportamental</i>. O controle sobre os corpos era total, punindo desvios de conduta (Garcia, 2011).</p>
        """
    },
    {
        "id": 4,
        "ano": "1971",
        "titulo": "Lei 5.692/71: Tecnicismo Compulsório",
        "categoria": "macro",
        "resumo": "Ensino Técnico Obrigatório no 2º Grau.",
        "detalhe": """
            <h3>O Auge do Capital Humano</h3>
            <p><b>Contexto:</b> Ditadura Militar. Profissionalização obrigatória para conter a demanda pelo ensino superior.</p>
            <hr>
            <p>🔍 <b>Crítica:</b> Fracassou por falta de estrutura e rejeição social, sendo revogada em 1982.</p>
        """
    },
    {
        "id": 5,
        "ano": "1972",
        "titulo": "A 1ª Safra de Técnicos (CAU)",
        "categoria": "micro",
        "resumo": "Formatura da 1ª Turma de Técnicos em Agropecuária.",
        "detalhe": """
            <h3>Modernização Agrícola no Cerrado</h3>
            <p>O CAU forma seus primeiros técnicos sob a égide da Revolução Verde e modernização do campo.</p>
            <hr>
            <p>🔍 <b>Modelo Avaliativo:</b> <i>Pragmático-Produtivista</i>. Foco total no "saber fazer" técnico/operacional.</p>
        """
    },
    {
        "id": 6,
        "ano": "1960 - 1980",
        "titulo": "Sistema Escola-Fazenda",
        "categoria": "micro",
        "resumo": "Gestão COAGRI e o Lema 'Aprender a Fazer'.",
        "detalhe": """
            <h3>A Escola como Empresa Rural</h3>
            <p><b>Princípio:</b> "Aprender a fazer e fazer para aprender". Busca por autossustentabilidade financeira.</p>
            <hr>
            <p>🔍 <b>Crítica:</b> Aluno como mão de obra barata para manutenção do internato (Vargas e Gatti).</p>
        """
    },
    {
        "id": 7,
        "ano": "1990 – 1997",
        "titulo": "Retrocesso e Fragmentação",
        "categoria": "macro",
        "resumo": "Decreto nº 2.208/97 e a hegemonia neoliberal.",
        "detalhe": """
            <h3>A Separação Compulsória</h3>
            <p>Governo FHC proíbe o Ensino Médio Integrado. Separação entre formação geral e técnica.</p>
            <hr>
            <p>🔍 <b>Elo Pessoal:</b> Minha formação técnica em TI no SENAC ocorreu neste cenário de fragmentação.</p>
        """
    },
    {
        "id": 8,
        "ano": "2008",
        "titulo": "Criação dos Institutos Federais",
        "categoria": "macro",
        "resumo": "Lei 11.892: A Revolução da Rede Federal.",
        "detalhe": """
            <h3>Omnilateralidade e Formação Integral</h3>
            <p>Criação do IFTM. Retomada do Ensino Médio Integrado (Trabalho, Ciência e Cultura).</p>
            <hr>
            <p>🔍 <b>Novo Paradigma:</b> Base teórica para a necessidade de avaliações formativas e humanas.</p>
        """
    },
    {
        "id": 9,
        "ano": "2026 (O Agora)",
        "titulo": "🌀 A Síntese: Rubrica Sinapse-BR IA",
        "categoria": "pessoal",
        "resumo": "Avaliação Diagnóstica e Formativa mediada por IA.",
        "detalhe": """
            <h3>A Vivência Recursiva</h3>
            <p>Resultado da espiral histórica vivida no corpo (EAFU → SENAC → IFTM).</p>
            <hr>
            <p><b>A Proposta:</b> Usar IA para garantir a avaliação formativa que a EPT crítica sempre defendeu.</p>
        """
    }
]
# Converter dados para JSON seguro para injetar no JS
dados_json = json.dumps(eventos_timeline)

# --------------------------------------------------------------------------------------
# 2. IMPLEMENTAÇÃO DO COMPONENTE (HTML + CSS + JS)
# --------------------------------------------------------------------------------------

html_code = f"""
<!DOCTYPE html>
<html lang="pt-br">
<head>
<style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap');
    
    :root {{
        --color-macro: #ef4444;   /* Vermelho (Política Nacional) */
        --color-micro: #22c55e;   /* Verde (Território/Agro) */
        --color-pessoal: #3b82f6; /* Azul (Memorial) */
        --bg-color: #ffffff;
        --text-color: #334155;
    }}

    body {{
        font-family: 'Roboto', sans-serif;
        background-color: transparent;
        margin: 0;
        padding: 20px;
        overflow-x: hidden;
    }}

    /* --- LINHA CENTRAL --- */
    .timeline {{
        position: relative;
        max-width: 1000px;
        margin: 0 auto;
        padding: 40px 0;
    }}

    .timeline::after {{
        content: '';
        position: absolute;
        width: 4px;
        background-color: #cbd5e1;
        top: 0;
        bottom: 0;
        left: 50%;
        margin-left: -2px;
        border-radius: 2px;
    }}

    /* --- CONTAINER DO CARD --- */
    .container {{
        padding: 10px 40px;
        position: relative;
        background-color: inherit;
        width: 50%;
        box-sizing: border-box;
        opacity: 0;
        animation: slideIn 0.8s forwards;
    }}

    .left {{ left: 0; text-align: right; }}
    .right {{ left: 50%; text-align: left; }}

    /* BOLINHA NA LINHA */
    .container::after {{
        content: '';
        position: absolute;
        width: 20px;
        height: 20px;
        right: -10px;
        background-color: #fff;
        border: 4px solid #94a3b8;
        top: 25px;
        border-radius: 50%;
        z-index: 1;
        transition: all 0.3s ease;
    }}
    .right::after {{ left: -10px; }}

    /* --- CARD DE CONTEÚDO --- */
    .content {{
        padding: 20px 25px;
        background-color: white;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05), 0 1px 3px rgba(0,0,0,0.1);
        cursor: pointer;
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
        position: relative;
        border-top: 5px solid #ccc; /* Cor definida via JS */
        overflow: hidden;
    }}

    /* INTERATIVIDADE (HOVER) */
    .content:hover {{
        transform: scale(1.03) translateY(-5px);
        box-shadow: 0 15px 30px rgba(0,0,0,0.15), 0 5px 15px rgba(0,0,0,0.1);
        z-index: 10;
    }}

    .container:hover::after {{
        background-color: var(--active-color);
        border-color: var(--active-color);
        transform: scale(1.3);
    }}

    .year-badge {{
        display: inline-block;
        padding: 4px 12px;
        border-radius: 20px;
        color: white;
        font-weight: bold;
        font-size: 0.85rem;
        margin-bottom: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }}

    h2 {{
        margin: 5px 0 10px 0;
        font-size: 1.4rem;
        color: #1e293b;
    }}

    p.resumo {{
        margin: 0;
        color: #64748b;
        font-size: 0.95rem;
        line-height: 1.5;
    }}

    /* Dica "Clique para ver mais" */
    .click-hint {{
        margin-top: 15px;
        font-size: 0.8rem;
        color: #1e40af;
        font-weight: 500;
        opacity: 0;
        transform: translateY(10px);
        transition: all 0.3s ease;
        display: flex;
        align-items: center;
        justify-content: flex-end; /* ou flex-start dependendo do lado */
    }}
    
    .left .click-hint {{ justify-content: flex-end; }}
    .right .click-hint {{ justify-content: flex-start; }}

    .content:hover .click-hint {{
        opacity: 1;
        transform: translateY(0);
    }}

    /* --- MODAL (POP-UP) --- */
    .modal {{
        display: none; 
        position: fixed; 
        z-index: 999; 
        left: 0; top: 0; width: 100%; height: 100%; 
        background-color: rgba(15, 23, 42, 0.8); /* Fundo escuro com blur */
        backdrop-filter: blur(4px);
        animation: fadeIn 0.3s;
    }}
    
    .modal-content {{
        background-color: #f8fafc;
        margin: 5% auto; 
        padding: 0;
        border: none;
        width: 90%;
        max-width: 700px;
        border-radius: 16px;
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
        position: relative;
        max-height: 85vh;
        overflow-y: auto;
        animation: slideUp 0.4s;
    }}

    .modal-header {{
        padding: 20px 30px;
        color: white;
        border-radius: 16px 16px 0 0;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }}

    .modal-body {{
        padding: 30px;
        font-size: 1.1rem;
        line-height: 1.7;
        color: #334155;
    }}

    .close-btn {{
        color: white;
        font-size: 28px;
        font-weight: bold;
        cursor: pointer;
        transition: transform 0.2s;
    }}
    .close-btn:hover {{ transform: scale(1.2); }}

    /* ANIMAÇÕES */
    @keyframes slideIn {{ from {{ opacity: 0; transform: translateY(30px); }} to {{ opacity: 1; transform: translateY(0); }} }}
    @keyframes fadeIn {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }}
    @keyframes slideUp {{ from {{ transform: translateY(50px); opacity: 0; }} to {{ transform: translateY(0); opacity: 1; }} }}

    /* CORES DINÂMICAS */
    .c-macro {{ border-color: var(--color-macro); }}
    .bg-macro {{ background-color: var(--color-macro); }}
    
    .c-micro {{ border-color: var(--color-micro); }}
    .bg-micro {{ background-color: var(--color-micro); }}
    
    .c-pessoal {{ border-color: var(--color-pessoal); }}
    .bg-pessoal {{ background-color: var(--color-pessoal); }}

</style>
</head>
<body>

<div class="timeline" id="timeline-root"></div>

<div id="infoModal" class="modal">
  <div class="modal-content">
    <div id="m-header" class="modal-header">
        <div>
            <span id="m-ano" style="background: rgba(255,255,255,0.2); padding: 4px 10px; border-radius: 10px; font-size: 0.8em;">ANO</span>
            <h2 id="m-titulo" style="margin: 5px 0 0 0; color: white; font-size: 1.5em;">Título</h2>
        </div>
        <span class="close-btn" onclick="closeModal()">&times;</span>
    </div>
    <div id="m-body" class="modal-body">
        </div>
  </div>
</div>

<script>
    const eventos = {dados_json};
    const root = document.getElementById('timeline-root');
    const modal = document.getElementById('infoModal');

    // Mapeamento de Cores para JS
    const cores = {{
        'macro': 'var(--color-macro)',
        'micro': 'var(--color-micro)',
        'pessoal': 'var(--color-pessoal)'
    }};

    // RENDERIZAR A LINHA DO TEMPO
    eventos.forEach((ev, index) => {{
        const isLeft = index % 2 === 0;
        const container = document.createElement('div');
        container.className = `container ${{isLeft ? 'left' : 'right' }}`;
        
        // Define classe de cor baseada na categoria
        let themeClass = 'c-macro';
        let bgClass = 'bg-macro';
        let activeColor = cores['macro'];

        if(ev.categoria === 'micro') {{ themeClass = 'c-micro'; bgClass = 'bg-micro'; activeColor = cores['micro']; }}
        if(ev.categoria === 'pessoal') {{ themeClass = 'c-pessoal'; bgClass = 'bg-pessoal'; activeColor = cores['pessoal']; }}

        // Define a variável CSS para o hover da bolinha
        container.style.setProperty('--active-color', activeColor);

        container.innerHTML = `
            <div class="content ${{themeClass}}" onclick="openModal(${{ev.id}})">
                <span class="year-badge ${{bgClass}}">${{ev.ano}}</span>
                <h2>${{ev.titulo}}</h2>
                <p class="resumo">${{ev.resumo}}</p>
                <div class="click-hint">
                    ${{isLeft ? 'Ver detalhes 🔎' : '🔎 Ver detalhes'}}
                </div>
            </div>
        `;
        root.appendChild(container);
    }});

    // LÓGICA DO MODAL
    function openModal(id) {{
        const ev = eventos.find(e => e.id === id);
        
        // Configura cores do header do modal
        const header = document.getElementById('m-header');
        let corHeader = cores['macro']; 
        if(ev.categoria === 'micro') corHeader = cores['micro'];
        if(ev.categoria === 'pessoal') corHeader = cores['pessoal'];
        
        header.style.backgroundColor = corHeader;

        document.getElementById('m-ano').innerText = ev.ano;
        document.getElementById('m-titulo').innerText = ev.titulo;
        document.getElementById('m-body').innerHTML = ev.detalhe;
        
        modal.style.display = "block";
        document.body.style.overflow = "hidden"; // Evita scroll do fundo
    }}

    function closeModal() {{
        modal.style.display = "none";
        document.body.style.overflow = "auto"; // Libera scroll
    }}

    // Fecha ao clicar fora do modal
    window.onclick = function(event) {{
        if (event.target == modal) {{
            closeModal();
        }}
    }}
    
    // Fecha com tecla ESC
    document.addEventListener('keydown', function(event) {{
        if (event.key === "Escape") {{
            closeModal();
        }}
    }});
</script>

</body>
</html>
"""

# Renderiza o HTML com altura suficiente para permitir o scroll
components.html(html_code, height=1200, scrolling=True)
