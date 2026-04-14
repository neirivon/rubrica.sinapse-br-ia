# /home/neirivon/SINAPSE2.0/sinapsebr_rubrica/pages/10_Itinerario_YA-YA.py
# --------------------------------------------------------------------------------------
# NOME DO SCRIPT: 10_Itinerario_YA-YA.py
# DESCRIÇÃO: Simulação do itinerário IFTM (Versão Híbrida: Narrativa + Dados Reais).
#            Integra geometria real (Google API) com a teoria de Milton Santos.
#            Confronto Histórico: A geração do Mainframe (Pai) vs. A geração da IA (Filha).
#
# DADOS DE MEMÓRIA (Relato TCC):
#   - GERAÇÃO 1 (Neirivon): EAFU (Rural) -> Êxodo -> SENAC -> Mainframe (Rezende Alimentos).
#   - GERAÇÃO 2 (YA-YA): Urbano -> IFTM (Rural/Tecnológico) -> Ensino Integrado -> IA.
#
# AUTOR: Neirivon Elias Cardoso
# DATA: 16/01/2026
# VERSÃO: 9.5 (RESTAURAÇÃO TOTAL + BLINDAGEM DE VÍDEO)
# --------------------------------------------------------------------------------------

import streamlit as st
import pandas as pd
import pydeck as pdk
import time
import json
import os
import base64
import streamlit.components.v1 as components

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(layout="wide", page_title="Itinerário: YA-YA & Milton Santos", page_icon="🚌")

# --- CSS ---
st.markdown("""
<style>
    div[data-testid="metric-container"] { background-color: #f8f9fa; border-radius: 8px; padding: 8px; border-left: 4px solid #4338ca; box-shadow: 1px 1px 3px rgba(0,0,0,0.1); min-height: 110px; }
    .status-box { padding: 10px; border-radius: 8px; font-weight: bold; text-align: center; margin-bottom: 5px; font-size: 1.1em; color: white; text-transform: uppercase; font-family: 'Arial', sans-serif; }
    .fase-verde { background-color: #166534; } .fase-vermelho { background-color: #b91c1c; } .fase-laranja { background-color: #ea580c; } 
    .fase-amarelo { background-color: #d97706; } .fase-azul { background-color: #1e3a8a; } .fase-roxa { background-color: #6b21a8; } .fase-noturna { background-color: #312e81; } 
    /* Estilo do Memorial */
    .memorial-box { background: linear-gradient(to right, #ffffff, #e0f2f1); border-left: 8px solid #00695c; padding: 30px; border-radius: 8px; margin-bottom: 25px; font-family: 'Georgia', serif; }
    .metric-table { width: 100%; border-collapse: collapse; font-family: Arial; font-size: 14px; margin-top: 15px; }
    .metric-table th { background-color: #E0F2F1; color: #004D40; padding: 10px; border: 1px solid #B2DFDB; text-align: left; }
    .metric-table td { padding: 10px; border: 1px solid #B2DFDB; }
</style>
""", unsafe_allow_html=True)

# --- 1. GERENCIAMENTO DE IMAGENS ---
FALLBACK_VERDE = "https://img.icons8.com/plasticine/100/bus.png"
FALLBACK_VERMELHO = "https://img.icons8.com/color/96/double-decker-bus.png"
FALLBACK_PADRAO = "https://img.icons8.com/color/96/bus.png"

@st.cache_data
def carregar_imagem_local(caminho_absoluto, fallback_url):
    # 1. Tenta carregar localmente
    if os.path.exists(caminho_absoluto):
        try:
            with open(caminho_absoluto, "rb") as image_file:
                encoded = base64.b64encode(image_file.read()).decode()
            return f"data:image/png;base64,{encoded}", True
        except Exception as e:
            print(f"Erro ao ler imagem local: {e}")
            return fallback_url, False
    
    # 2. Se não existir, usa o fallback (URL externa)
    return fallback_url, False

# Verifique se este caminho está correto no seu servidor
PATH_VERDE = os.path.abspath("assets/logos/Onibus_Verde_Google_Maps.png")
PATH_VERMELHO = os.path.abspath("assets/logos/Onibus_Vermelho_Google_Maps.png")

URL_BUS_VERDE, status_verde = carregar_imagem_local(PATH_VERDE, FALLBACK_VERDE)
URL_BUS_VERMELHO, status_vermelho = carregar_imagem_local(PATH_VERMELHO, FALLBACK_VERMELHO)

# --- 2. DADOS DA ROTA ---
@st.cache_data
def carregar_rota_unica():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "rota_detalhada_google.json")
    if os.path.exists(path):
        with open(path, "r") as f:
            return [[p[1], p[0]] for p in json.load(f)]
    return None

full_route_points = carregar_rota_unica()

def get_slice(start_ratio, end_ratio):
    if full_route_points:
        total = len(full_route_points)
        s, e = int(total * start_ratio), int(total * end_ratio)
        return full_route_points[s:max(e, s+2)]
    return [[-48.229, -18.957], [-48.288, -18.764]]

path_caminhada = get_slice(0.00, 0.02)
path_a339 = get_slice(0.02, 0.15)
path_i323 = get_slice(0.15, 0.40)
path_d281 = get_slice(0.40, 0.98)
path_interno = get_slice(0.98, 1.00)

pt_tsl, pt_tu = path_a339[-1], path_i323[-1]
pt_iftm, pt_casa = path_d281[-1], path_caminhada[0]

# --- 3. CONFIGURAÇÃO VISUAL ---
BACKGROUND_LAYERS_DATA = [
    {"path": path_caminhada, "color": [255, 140, 0]}, 
    {"path": path_a339,      "color": [0, 128, 0]},   
    {"path": path_i323,      "color": [200, 0, 0]},   
    {"path": path_d281,      "color": [34, 139, 34]}, 
    {"path": path_interno,   "color": [0, 0, 139]}    
]

ROTEIRO = [
    { "id": 1, "horario": "05:40", "titulo": "🚶 SAINDO DE CASA", "desc": "Caminhada urbana.", "path": path_caminhada, "icon": "person", "css": "fase-laranja", "zoom": 16, "atrito": "Rugosidade", "mov": True },
    { "id": 2, "horario": "05:55", "titulo": "🚌 LINHA A-339", "desc": "Rumo ao T. Santa Luzia.", "path": path_a339, "icon": "green_bus", "css": "fase-verde", "zoom": 15, "atrito": "Vibração", "mov": True },
    { "id": 3, "horario": "06:05", "titulo": "🪞 REFLEXO (PSICOESFERA)", "desc": "Pausa poética.", "path": [path_a339[-1]]*2, "icon": "eye", "css": "fase-verde", "zoom": 15, "atrito": "Suspensão", "mov": False },
    { "id": 4, "horario": "06:20", "titulo": "⏳ T. SANTA LUZIA", "desc": "Viscosidade (Espera).", "path": [pt_tsl]*2, "icon": "clock", "css": "fase-amarelo", "zoom": 16, "atrito": "Ansiedade", "mov": False },
    { "id": 5, "horario": "06:45", "titulo": "🚍 LINHA I-323", "desc": "Expresso. Corredor.", "path": path_i323, "icon": "red_bus", "css": "fase-vermelho", "zoom": 14, "atrito": "Fadiga", "mov": True },
    { "id": 6, "horario": "07:15", "titulo": "🛣️ LINHA D-281", "desc": "Rodovia para Zona Rural.", "path": path_d281, "icon": "green_bus", "css": "fase-verde", "zoom": 11, "atrito": "Exaustão", "mov": True },
    { "id": 7, "horario": "07:37", "titulo": "🏫 CHEGADA (IFTM)", "desc": "O Lugar.", "path": path_interno, "icon": "school", "css": "fase-azul", "zoom": 17, "atrito": "Apropriação", "mov": True },
    { "id": 8, "horario": "07:37", "titulo": "🍽️ REFEITÓRIO", "desc": "Nutrição e sociabilidade.", "path": [pt_iftm]*2, "icon": "food", "css": "fase-azul", "zoom": 17, "atrito": "Recuperação", "mov": False },
    { "id": 9, "horario": "07:37", "titulo": "🎸 BANDA EMPTY SOLUTION", "desc": "Apropriação cultural.", "path": [pt_iftm]*2, "icon": "music", "css": "fase-roxa", "zoom": 17, "atrito": "Plenitude", "mov": False },
    { "id": 10,"horario": "07:37", "titulo": "😴 RETORNO NO FINAL DO DIA, PARA UMA NOVA JORNADA NO DIA SEGUINTE", "desc": "Ciclo Encerrado.", "path": [pt_casa]*2, "icon": "home", "css": "fase-noturna", "zoom": 13, "atrito": "Repouso", "mov": False }
]

ICONS_DATA = {
    "green_bus": {"url": URL_BUS_VERDE, "width": 128, "height": 128, "anchorY": 128},
    "red_bus":   {"url": URL_BUS_VERMELHO, "width": 128, "height": 128, "anchorY": 128},
    "person":    {"url": "https://img.icons8.com/color/96/walking.png", "width": 128, "height": 128, "anchorY": 128},
    "school":    {"url": "https://img.icons8.com/color/96/school.png", "width": 128, "height": 128, "anchorY": 128},
    "clock":     {"url": "https://img.icons8.com/color/96/clock--v1.png", "width": 128, "height": 128, "anchorY": 128},
    "eye":       {"url": "https://img.icons8.com/fluency/96/visible.png", "width": 128, "height": 128, "anchorY": 128},
    "music":     {"url": "https://img.icons8.com/color/96/musical-notes.png", "width": 128, "height": 128, "anchorY": 128},
    "home":      {"url": "https://img.icons8.com/color/96/home.png", "width": 128, "height": 128, "anchorY": 128},
    "food":      {"url": "https://img.icons8.com/color/96/restaurant.png", "width": 128, "height": 128, "anchorY": 128},
    "bus":       {"url": FALLBACK_PADRAO, "width": 128, "height": 128, "anchorY": 128}
}

# --- 4. INTERFACE ---
st.title("Geografia: Memória e Tecnologia")

c1, c2 = st.columns([1, 1])
with c1: st.markdown("""<div class="intro-box"><strong>🗺️ Conceitos:</strong><br>Simulação com geometria real para demonstrar fluxos territoriais.</div>""", unsafe_allow_html=True)
with c2: st.markdown("""<div class="history-box"><strong>⏳ História:</strong><br>O trajeto desenha no asfalto a narrativa da sucessão geracional.</div>""", unsafe_allow_html=True)

with st.expander("🛰️ Painel de Controle e Validação de GPS", expanded=True):
    d1, d2 = st.columns(2)
    with d1:
        st.write("Status Ícone Verde:")
        if status_verde: st.success("Arquivo Local")
        st.image(URL_BUS_VERDE, width=50)
    with d2:
        st.write("Status Ícone Vermelho:")
        if status_vermelho: st.success("Arquivo Local")
        st.image(URL_BUS_VERMELHO, width=50)
    st.markdown("""<iframe src="https://www.google.com/maps/embed?pb=!1m46!1m12!1m3!1d120818.49825087495!2d-48.351623742169814!3d-18.86141942382887!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m31!3e0!4m5!1s0x94a4500fd36b5ab9%3A0x59f33a18b499599a!2sRua%20Maria%20Os%C3%B3ria%20de%20Jesus%2C%20138%20-%20Parque%20S%C3%A3o%20Jorge%20V%2C%20Uberl%C3%A2ndia%20-%20MG!3m2!1d-18.9579529!2d-48.2299539!4m5!1s0x94a4500e5a028cbd%3A0x17633c574c11a901!2sR.%20Abelardo%20Pena%2C%20291%20-%20S%C3%A3o%20Jorge%2C%20Uberl%C3%A2ndia%20-%20MG%2C%2038410-222!3m2!1d-18.9586936!2d-48.2315737!4m5!1s0x94a44ffadac94505%3A0xc0a620931762330c!2sTerminal%20Rodovi%C3%A1rio%20Santa%20Luzia%20-%20Rua%20Clarindo%20Rodrigues%20Rezende%20-%20Santa%20Luzia%2C%20Uberl%C3%A2ndia%20-%20MG!3m2!1d-18.9375088!2d-48.2299736!4m5!1s0x94a445ef55ee5b0d%3A0x39aa5ce7c21ab3cb!2sTerminal%20Umuarama%20-%20Umuarama%2C%20Uberl%C3%A2ndia%20-%20MG!3m2!1d-18.8850513!2d-48.2540238!4m5!1s0x94a439959d2fd43f%3A0x56de55ffe5a9b204!2sIFTM%20Campus%20Uberl%C3%A2ndia%20-%20Fazenda%20Sobradinho%20-%20Cruzeiro%20dos%20Peixotos%2C%20Uberl%C3%A2ndia%20-%20MG!3m2!1d-18.7645467!2d-48.288651099999996!5e0!3m2!1spt-BR!2sbr!4v1768481729280!5m2!1spt-BR!2sbr" width="100%" height="450" style="border:0;" allowfullscreen="" loading="lazy"></iframe>""", unsafe_allow_html=True)

st.divider()

col_controles, col_video, col_mapa = st.columns([1, 2, 2])

with col_controles:
    st.warning("⚠️ Interação com o vídeo bloqueada para garantir a sincronia.")
    delay_rede = st.slider("Compensação de Lag (s)", 0.0, 5.0, 1.5)
    iniciar = st.button("▶️ INICIAR VIAGEM", type="primary", use_container_width=True)

with col_video:
    video_id = "AzGyshHLN3k"
    autoplay = "1" if iniciar else "0"
    video_html = f"""
    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; border-radius: 10px;">
        <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 999; background: transparent; cursor: not-allowed;"></div>
        <iframe src="https://www.youtube.com/embed/{video_id}?autoplay={autoplay}&controls=0&rel=0&disablekb=1" 
        frameborder="0" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" allow="autoplay"></iframe>
    </div>"""
    components.html(video_html, height=300)
    status_ph, desc_ph = st.empty(), st.empty()

with col_mapa:
    st.markdown("**📡 GPS da Narrativa**")
    mapa_ph = st.empty()

# --- MEMORIAL ACADÊMICO TERRITORIAL ---
st.divider()
with st.container():
    st.markdown("""
    <div class="memorial-box">
        <h2 style="color: #004D40; margin-top: 0;">O Itinerário de Yasmin: Memorial Acadêmico Territorial</h2>
        <p style="text-align: justify;"><strong>Nota à Docência:</strong> Este memorial traduz a geografia vivida pela estudante. A futura integração deste mapeamento socioterritorial a uma IA preditiva constitui pretensão de pesquisa para Mestrado.</p>
        <hr style="border-top: 1px solid #B2DFDB;">
        <h4 style="color: #00695c;">1. A Odisseia da Desterritorialização</h4>
        <p style="text-align: justify;">A jornada às 05h40 configura violência geográfica. Ao submeter-se à tripla conexão, a estudante sofre desterritorialização diária entre a periferia e o isolamento rural.</p>
        <h4 style="color: #00695c;">2. A Teoria das Rugosidades</h4>
        <p style="text-align: justify;">Os pontos de parada da linha D-281 atuam como rugosidades geográficas (Milton Santos), consumindo a energia vital da aluna antes da aula.</p>
        <h4 style="color: #00695c;">3. A Ética da Hospitalidade</h4>
        <p style="text-align: justify;">O campus torna-se refúgio. O café da manhã (pão com margarina) no IFTM é a ética da hospitalidade (Lévinas) que acolhe a vulnerabilidade do aluno.</p>
        <h4 style="color: #00695c;">4. Reterritorialização (Empty Solution)</h4>
        <p style="text-align: justify;">A limpeza de uma sala abandonada para a banda de rock <em>Empty Solution</em> reterritorializa a escola, criando um lugar de pertencimento.</p>
        <div style="background-color: #ffffff; border: 1px solid #B2DFDB; padding: 15px; border-radius: 6px; margin-top: 20px;">
            <h4 style="color: #004D40; text-align: center; margin-top: 0;">Métricas da Existência (Apêndice de Metadados Narrativos)</h4>
            <table class="metric-table">
                <tr><th>Variável Conceitual</th><th>Fórmula Fenomenológica</th></tr>
                <tr><td><strong>Índice de Rugosidade (IR)</strong></td><td>f (Paradas + Tempo de Espera)</td></tr>
                <tr><td><strong>Vetor de Hospitalidade (VH)</strong></td><td>f (Café da Manhã + Almoço no Campus)</td></tr>
            </table>
        </div>
    </div>""", unsafe_allow_html=True)

    with st.expander("⚙️ Auditoria da Práxis: A Materialidade do Esforço Discente", expanded=False):
        st.info("""
        ### 📖 Tradução Didática: O Algoritmo do "Custo do Cotidiano"
        Este trecho de código não é apenas uma automação; ele é a representação matemática do esforço territorial da aluna. Ele funciona como um "cronômetro espacial" que prova a materialidade da odisseia diária.

        **O que o código executa na prática?**
        
        **1. Cálculo do Desgaste (Variável progresso):**
        O algoritmo subtrai o tempo atual do tempo de partida e divide pela duração total da viagem.
        
        *Significado Pedagógico:* Esta variável mede o progresso do cansaço. Quanto maior o número, mais "rugosidade" (Milton Santos) a aluna já enfrentou e mais energia vital foi consumida pelo trajeto.

        **2. A Luta contra a Distância (Interpolação de longitude e latitude):**
        As linhas de cálculo de latitude e longitude realizam uma Interpolação Linear. Elas calculam onde o corpo da aluna está exatamente em relação à distância que falta percorrer.
        
        *Significado Pedagógico:* É a prova de que o território não é um desenho estático, mas um espaço sendo atravessado por uma ação. Prova que a aluna está superando a "violência da distância" entre a cidade e o campus rural.

        **3. A Chegada à Ética da Hospitalidade (Se o progresso do aluno >= 1.0):**
        Quando o progresso atinge 100% (1.0), o loop (laço) de esforço é interrompido (para).
        
        *Significado Pedagógico:* Este é o exato momento em que a desterritorialização termina e a Ética da Hospitalidade (Lévinas) começa. O corpo exausto finalmente alcança o acolhimento do campus e o café da manhã no refeitório.
        """)
        
        st.code("""
# Algoritmo de Custo do Cotidiano: Interpolação Linear Espaço-Tempo
while True:
    current_time = get_current_time()
    # Progresso = Desgaste temporal e vitória sobre rugosidades
    progress = (current_time - start_time) / total_duration 
    if progress >= 1.0: break 
    lon = start_lon + (end_lon - start_lon) * progress
    lat = start_lat + (end_lat - start_lat) * progress
    atualizar_renderizacao_mapa(lon, lat)""", language='python')

st.markdown("---")

# --- LÓGICA DE EXECUÇÃO SINCRONIZADA ---
if iniciar:
    time.sleep(delay_rede)
    m1, m2, m3, m4 = st.columns(4)
    box_relogio, box_fase, box_dist, box_atrito = m1.empty(), m2.empty(), m3.empty(), m4.empty()
    NUM_FASES, STEP_TIME = len(ROTEIRO), 8.0
    start_t = time.time()
    
    while True:
        elapsed = time.time() - start_t
        if elapsed > (NUM_FASES * STEP_TIME): break
        idx = min(int(elapsed // STEP_TIME), NUM_FASES - 1)
        step = ROTEIRO[idx]
        progress = (elapsed % STEP_TIME) / STEP_TIME
        
        status_ph.markdown(f'<div class="status-box {step["css"]}">{step["titulo"]}</div>', unsafe_allow_html=True)
        desc_ph.info(step['desc'])
        box_relogio.metric("⏰ Horário", step['horario'])
        box_fase.metric("Fase", f"{idx+1}/{NUM_FASES}")
        box_atrito.metric("⚡ Atrito", step['atrito'])
        
        path_len = len(step['path'])
        if step['mov'] and path_len > 1:
            curr_idx = min(int(progress * (path_len - 1)), path_len - 1)
            lon, lat = step['path'][curr_idx]
        else: lon, lat = step['path'][0]
            
        view = pdk.ViewState(latitude=lat, longitude=lon, zoom=step['zoom'], pitch=50)
        deck = pdk.Deck(
            layers=[
                pdk.Layer("PathLayer", data=BACKGROUND_LAYERS_DATA, get_path="path", get_color="color", get_width=40, opacity=0.7),
                pdk.Layer("IconLayer", data=pd.DataFrame({'lon':[lon], 'lat':[lat]}), get_position='[lon, lat]',
                          get_icon=lambda d: ICONS_DATA.get(step['icon'], ICONS_DATA['bus']), get_size=50, size_scale=8)
            ],
            initial_view_state=view, map_style="mapbox://styles/mapbox/light-v10"
        )
        mapa_ph.pydeck_chart(deck)
        time.sleep(0.1)

    st.success("🏁 Ciclo encerrado.")
    time.sleep(2)
    st.rerun()
