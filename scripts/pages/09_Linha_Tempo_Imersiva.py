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
    <h1 style='text-align: center; color: #1e3a8a;'>⏳ A Espiral do Tempo: Da EPT à RUBRICA SINAPSE</h1>
    <p style='text-align: center; font-size: 1.2em; color: #64748b;'>
        Uma jornada interativa pela história da EPT, o CAU no território de Uberlândia e a trajetória formativa.<br>
        <span style='font-size: 0.8em;'>👆 <b>Passe o mouse</b> para ver o contexto e <b>clique nos cards</b> para mergulhar nos documentos.</span>
    </p>
    <br>
""", unsafe_allow_html=True)

# --------------------------------------------------------------------------------------
# 1. DADOS DA LINHA DO TEMPO (CAMADA DE DADOS ATUALIZADA)
# --------------------------------------------------------------------------------------
# Categorias: 'macro' (Nacional/Leis), 'micro' (Local/Institucional), 'pessoal' (Memorial)

eventos_timeline = [
    {
        "id": 1,
        "ano": "1909",
        "titulo": "A Gênese Assistencialista",
        "categoria": "macro",
        "resumo": "Decreto nº 7.566: Escolas de Aprendizes Artífices.",
        "detalhe": """
            <h3>O Marco Zero: Amparar os Desvalidos</h3>
            <p><b>Marco Jurídico:</b> Decreto nº 7.566 (Nilo Peçanha).</p>
            <p>O início da EPT no Brasil não visa à formação intelectual, mas sim "amparar os desvalidos da sorte". É uma educação para pobres, focada no ofício manual para evitar o vício e a criminalidade.</p>
            <hr>
            <p>🔍 <b>Modelo Avaliativo Inferido:</b> <i>Disciplinar e Corretivo</i>. Avaliava-se a conduta moral e a aptidão manual, não o intelecto.</p>
            <p><i>Contexto:</i> Estabelecimento da "dualidade estrutural" (Moura/Ciavatta): escola de elite (pensar) vs. escola de trabalhadores (fazer).</p>
        """
    },
    {
        "id": 2,
        "ano": "1942",
        "titulo": "Consolidação Industrial (Era Vargas)",
        "categoria": "macro",
        "resumo": "Leis Orgânicas e Criação do SENAI.",
        "detalhe": """
            <h3>A Serviço da Industrialização</h3>
            <p><b>Marco Jurídico:</b> Decreto-Lei nº 4.073.</p>
            <p>Criação do SENAI. A formação é estritamente técnica, atendendo à demanda da industrialização nascente. O ensino técnico não dava acesso ao ensino superior.</p>
            <hr>
            <p>🔍 <b>Modelo Avaliativo Inferido:</b> <i>Psicométrico e Tecnicista</i>. Testes de aptidão para selecionar "o homem certo para o lugar certo".</p>
            <p><i>Crítica (Saviani):</i> Rigidez na separação entre trabalho intelectual e manual.</p>
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
            <p><b>Marco Jurídico:</b> Lei nº 3.383 (Criação) / Instalação efetiva em 1959.</p>
            <p>Nasce a instituição mãe do atual IFTM Campus Uberlândia. A escola funcionava em regime de <b>internato rígido</b>, onde a disciplina era tão importante quanto o ensino.</p>
            <hr>
            <p>🔍 <b>Modelo Avaliativo Documentado:</b> <i>Comportamental e Moral</i>. Segundo Garcia (2011), o "Inspetor de Alunos" exercia controle total sobre os corpos e condutas. A avaliação punia desvios de comportamento.</p>
            <p><i>Fonte:</i> Dissertação de Daniele da Costa Garcia.</p>
        """
    },
    {
        "id": 35,
        "ano": "1972",
        "titulo": "A Primeira Safra de Técnicos",
        "categoria": "micro",
        "resumo": "Formatura da 1ª Turma de Técnicos em Agropecuária.",
        "detalhe": """
            <h3>Do Projeto à Realidade Territorial</h3>
            <p><b>Marco Histórico:</b> Conclusão da primeira turma (iniciada em 1969).</p>
            <p>Após anos de construção e estruturação na Fazenda Sobradinho, o Colégio Agrícola de Uberlândia forma seus primeiros Técnicos. O ensino era focado na modernização agrícola (Revolução Verde).</p>
            <hr>
            <p>🔍 <b>Modelo Avaliativo:</b> <i>Pragmático-Produtivista</i>. O aluno precisava demonstrar competência prática na lida do campo para ser aprovado. A escola servia como modelo de difusão técnica para a região.</p>
            <p><i>Fonte:</i> "História do Colégio Agrícola... (1957-1972)", Daniele Garcia.</p>
        """
    },
    {
        "id": 4,
        "ano": "1971 – 1988",
        "titulo": "O Rural em Desacordo com o Urbano",
        "categoria": "micro",
        "resumo": "Expansão urbana desordenada e tecnicismo.",
        "detalhe": """
            <h3>Tensões Territoriais</h3>
            <p><b>Marco Jurídico:</b> Lei 5.692/71 (Profissionalização Compulsória).</p>
            <p>Período de forte tecnicismo na Ditadura Militar. A escola rural sofre com a precarização e a imposição de modelos urbanos, além das tensões raciais e de gênero.</p>
            <p><i>Fonte:</i> Tese de Gelda Gonçalves Costa.</p>
        """
    },
    {
        "id": 5,
        "ano": "1979",
        "titulo": "Gestão Centralizada (COAGRI)",
        "categoria": "micro",
        "resumo": "Projetos Agropecuários e Produtivismo.",
        "detalhe": """
            <h3>A Escola-Fazenda</h3>
            <p><b>Contexto:</b> Supervisão da Coordenação Nacional do Ensino Agropecuário.</p>
            <p>Gestão focada em "projetos agropecuários" (suinocultura, olericultura) visando lucro e autossustentabilidade. A produção muitas vezes se sobrepunha à pedagogia.</p>
            <hr>
            <p>🔍 <b>Modelo Avaliativo Inferido:</b> <i>Por Produção/Resultados</i>. O aluno era avaliado pela eficiência na lida do campo e lucro gerado.</p>
            <p><i>Fonte:</i> Relatório de Gestão COAGRI 1979.</p>
        """
    },
    {
        "id": 6,
        "ano": "1990 – 1992",
        "titulo": "Minha Formação Técnica (SENAC)",
        "categoria": "pessoal",
        "resumo": "Curso Profissionalizante: Informática e Computação (630h).",
        "detalhe": """
            <h3>O Elo Pessoal (Anexo C)</h3>
            <p>Realização do curso unificado de TI no SENAC Uberlândia. Este ponto conecta a "grande história" à trajetória do autor: fruto da formação profissionalizante do Sistema S.</p>
            <ul>
                <li>Carga Horária: 630 horas.</li>
                <li>Contexto: Pós-Constituição de 88, mas ainda sob influência tecnicista.</li>
            </ul>
            <hr>
            <p>🔍 <b>Modelo Avaliativo Vivenciado:</b> <i>Competência Técnica (Saber Fazer)</i>. Foco na habilidade de programação e lógica.</p>
        """
    },
    {
        "id": 7,
        "ano": "1997",
        "titulo": "O Retrocesso da Dualidade",
        "categoria": "macro",
        "resumo": "Decreto nº 2.208/97: Proibição da Integração.",
        "detalhe": """
            <h3>A Fragmentação do Ensino</h3>
            <p>O decreto proíbe o Ensino Médio Integrado. O aluno teria que fazer o Ensino Médio em uma escola e o Técnico em outra.</p>
            <p>É o ápice da "subsunção aos interesses do mercado" (Moura). A formação geral é separada da formação para o trabalho.</p>
        """
    },
    {
        "id": 8,
        "ano": "2008",
        "titulo": "Criação dos Institutos Federais",
        "categoria": "macro",
        "resumo": "Lei 11.892: A Revolução da Rede Federal.",
        "detalhe": """
            <h3>Omnilateralidade e Verticalização</h3>
            <p>Lula sanciona a lei que cria a Rede Federal. A antiga Escola Agrotécnica (EAFU) se funde ao CEFET e nasce o <b>IFTM</b>.</p>
            <p>A EPT passa a assumir o compromisso com a formação humana integral, integrando trabalho, ciência e cultura.</p>
            <p><i>Este marco legal é a base teórica que sustenta a necessidade de uma nova rubrica.</i></p>
        """
    },
    {
        "id": 9,
        "ano": "2026 (O Agora)",
        "titulo": "A Espiral do Tempo (Minha Trajetória)",
        "categoria": "pessoal",
        "resumo": "A prova empírica da espiral: EMS/EAFU → SENAC → IFTM (Graduação) → IFTM (Pós/Mestrado).",
        "detalhe": """
            <h3>A Vivência Recursiva no Território</h3>
            <p>Este exemplo prova a <b>Espiral do Tempo</b> na EPT. Cada vez que passei pelo espaço do IFTM, tive novos aprendizados e outra visão das vivências anteriores:</p>
            <ul>
                <li><b>1. Início (EMS/EAFU):</b> Estudei na EMS, anexo da Escola Agrotécnica Federal de Uberlândia, através do convênio COAGRI (1º ano).</li>
                <li><b>2. O Giro (Forças Armadas e Sistema S):</b> Saí para as Forças Armadas. Na EPT, fui para o SENAC, onde terminei o ensino médio e a formação técnica.</li>
                <li><b>3. O Retorno (Graduação):</b> Voltei para o IFTM para cursar Tecnologia em Sistemas para Internet.</li>
                <li><b>4. A Síntese (Pós e Mestrado):</b> Estou no IFTM novamente, agora na Pós em Docência e tendo cursado disciplinas do Mestrado.</li>
            </ul>
            <hr>
            <p><b>Conclusão:</b> A Rubrica SINAPSE é o resultado dessa soma de visões, construída por quem viveu a evolução da EPT no próprio corpo.</p>
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
