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
# VERSÃO: 7.3 (Correção Lógica Temporal + Sincronia 1s=1min)
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
    .video-wrapper { position: relative; width: 100%; padding-bottom: 56.25%; height: 0; overflow: hidden; border-radius: 10px; margin-bottom: 10px; }
    .video-wrapper iframe { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }
    .video-blocker { position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: transparent; z-index: 10; cursor: not-allowed; }
    .fase-verde { background-color: #166534; } .fase-vermelho { background-color: #b91c1c; } .fase-laranja { background-color: #ea580c; } 
    .fase-amarelo { background-color: #d97706; } .fase-azul { background-color: #1e3a8a; } .fase-roxa { background-color: #6b21a8; } .fase-noturna { background-color: #312e81; } 
</style>
""", unsafe_allow_html=True)

# --- 1. GERENCIAMENTO DE IMAGENS (LOCAL + FALLBACK WEB) ---
# Se o arquivo local falhar, usa estes links que JÁ SÃO VERDES/VERMELHOS
FALLBACK_VERDE = "https://img.icons8.com/plasticine/100/bus.png" # Um ônibus colorido padrão
FALLBACK_VERMELHO = "https://img.icons8.com/color/96/double-decker-bus.png" # Vermelho (Estilo Londres)
FALLBACK_PADRAO = "https://img.icons8.com/color/96/bus.png"

@st.cache_data
def carregar_imagem_local(caminho_absoluto, fallback_url):
    """Lê arquivo local e converte para Base64. Se der erro, retorna URL web."""
    if os.path.exists(caminho_absoluto):
        try:
            with open(caminho_absoluto, "rb") as image_file:
                encoded = base64.b64encode(image_file.read()).decode()
            return f"data:image/png;base64,{encoded}", True # True = carregou local
        except Exception as e:
            return fallback_url, False
    return fallback_url, False

# Caminhos exatos fornecidos
PATH_VERDE = "/home/neirivon/SINAPSE2.0/sinapsebr_rubrica/assets/logos/Onibus_Verde_Google_Maps.png"
PATH_VERMELHO = "/home/neirivon/SINAPSE2.0/sinapsebr_rubrica/assets/logos/Onibus_Vermelho_Google_Maps.png"

# Carregamento
URL_BUS_VERDE, status_verde = carregar_imagem_local(PATH_VERDE, FALLBACK_VERDE)
URL_BUS_VERMELHO, status_vermelho = carregar_imagem_local(PATH_VERMELHO, FALLBACK_VERMELHO)

# --- 2. DADOS DA ROTA (JSON) ---
@st.cache_data
def carregar_rota_unica():
    # Tenta achar o JSON na pasta do script
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "rota_detalhada_google.json")
    if os.path.exists(path):
        try:
            with open(path, "r") as f:
                raw = json.load(f)
                return [[p[1], p[0]] for p in raw] # Inverte Lat/Lon -> Lon/Lat
        except: return None
    return None

full_route_points = carregar_rota_unica()

def get_slice(start_ratio, end_ratio):
    if full_route_points:
        total = len(full_route_points)
        s, e = int(total * start_ratio), int(total * end_ratio)
        if e <= s: e = s + 2
        return full_route_points[s:e]
    return [[-48.229, -18.957], [-48.288, -18.764]]

# Trechos (Fatiamento Geográfico)
path_caminhada = get_slice(0.00, 0.02)
path_a339 = get_slice(0.02, 0.15)
path_i323 = get_slice(0.15, 0.40)
path_d281 = get_slice(0.40, 0.98)
path_interno = get_slice(0.98, 1.00)

# Pontos Chave
pt_tsl, pt_tu = path_a339[-1], path_i323[-1]
pt_iftm, pt_casa = path_d281[-1], path_caminhada[0]

# --- 3. CONFIGURAÇÃO VISUAL (LAYERS) ---
BACKGROUND_LAYERS_DATA = [
    {"path": path_caminhada, "color": [255, 140, 0]}, # Laranja
    {"path": path_a339,      "color": [0, 128, 0]},   # Verde
    {"path": path_i323,      "color": [200, 0, 0]},   # Vermelho
    {"path": path_d281,      "color": [34, 139, 34]}, # Verde Floresta
    {"path": path_interno,   "color": [0, 0, 139]}    # Azul
]

# ROTEIRO: RELÓGIO CONGELA NA FASE 7, MAS AS FASES CONTINUAM ATÉ A 10
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
    { "id": 10,"horario": "07:37", "titulo": "😴 FIM", "desc": "Ciclo Encerrado.", "path": [pt_casa]*2, "icon": "home", "css": "fase-noturna", "zoom": 13, "atrito": "Repouso", "mov": False }
]

# MAPA DE ÍCONES
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

if full_route_points: st.toast(f"✅ GPS: {len(full_route_points)} pontos.", icon="🛰️")
else: st.toast("⚠️ JSON não encontrado. Rota simulada.", icon="📏")

c1, c2 = st.columns([1, 1])
with c1: st.markdown("""<div class="intro-box"><strong>🗺️ Conceitos:</strong><br>Simulação com geometria real e colorida para demonstrar os diferentes fluxos (Bairro, Corredor, Rural).</div>""", unsafe_allow_html=True)
with c2: st.markdown("""<div class="history-box"><strong>⏳ História:</strong><br>O trajeto desenha no asfalto a narrativa da sucessão geracional na EPT.</div>""", unsafe_allow_html=True)

# DEBUG DE IMAGENS E MAPA REAL
with st.expander("📍 Mapa Real & Status dos Ícones (Debug)", expanded=True):
    d1, d2 = st.columns(2)
    with d1:
        st.write("Status Ícone Verde:")
        if status_verde: st.success("Arquivo Local Carregado")
        else: st.warning("Usando Fallback Web (Arquivo não achado)")
        st.image(URL_BUS_VERDE, width=50)
    with d2:
        st.write("Status Ícone Vermelho:")
        if status_vermelho: st.success("Arquivo Local Carregado")
        else: st.warning("Usando Fallback Web (Arquivo não achado)")
        st.image(URL_BUS_VERMELHO, width=50)
        
    st.markdown("""<iframe src="https://www.google.com/maps/embed?pb=!1m46!1m12!1m3!1d120818.49825087495!2d-48.351623742169814!3d-18.86141942382887!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m31!3e0!4m5!1s0x94a4500fd36b5ab9%3A0x59f33a18b499599a!2sRua%20Maria%20Os%C3%B3ria%20de%20Jesus%2C%20138%20-%20Parque%20S%C3%A3o%20Jorge%20V%2C%20Uberl%C3%A2ndia%20-%20MG!3m2!1d-18.9579529!2d-48.2299539!4m5!1s0x94a4500e5a028cbd%3A0x17633c574c11a901!2sR.%20Abelardo%20Pena%2C%20291%20-%20S%C3%A3o%20Jorge%2C%20Uberl%C3%A2ndia%20-%20MG%2C%2038410-222!3m2!1d-18.9586936!2d-48.2315737!4m5!1s0x94a44ffadac94505%3A0xc0a620931762330c!2sTerminal%20Rodovi%C3%A1rio%20Santa%20Luzia%20-%20Rua%20Clarindo%20Rodrigues%20Rezende%20-%20Santa%20Luzia%2C%20Uberl%C3%A2ndia%20-%20MG!3m2!1d-18.9375088!2d-48.2299736!4m5!1s0x94a445ef55ee5b0d%3A0x39aa5ce7c21ab3cb!2sTerminal%20Umuarama%20-%20Umuarama%2C%20Uberl%C3%A2ndia%20-%20MG!3m2!1d-18.8850513!2d-48.2540238!4m5!1s0x94a439959d2fd43f%3A0x56de55ffe5a9b204!2sIFTM%20Campus%20Uberl%C3%A2ndia%20-%20Fazenda%20Sobradinho%20-%20Cruzeiro%20dos%20Peixotos%2C%20Uberl%C3%A2ndia%20-%20MG!3m2!1d-18.7645467!2d-48.288651099999996!5e0!3m2!1spt-BR!2sbr!4v1768481729280!5m2!1spt-BR!2sbr" width="100%" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>""", unsafe_allow_html=True)

st.divider()

if 'simulacao_ativa' not in st.session_state: st.session_state.simulacao_ativa = False
def start(): st.session_state.simulacao_ativa = True

if not st.session_state.simulacao_ativa:
    st.button("▶️ INICIAR SIMULAÇÃO REAL (Todas as Fases)", on_click=start, type="primary", use_container_width=True)
    # Preview
    view = pdk.ViewState(latitude=-18.90, longitude=-48.25, zoom=10)
    prev_layer = pdk.Layer("PathLayer", data=BACKGROUND_LAYERS_DATA, get_path="path", get_color="color", get_width=30)
    st.pydeck_chart(pdk.Deck(layers=[prev_layer], initial_view_state=view, map_style="mapbox://styles/mapbox/light-v10"))

if st.session_state.simulacao_ativa:
    c_video, c_mapa = st.columns([1, 1.4])
    with c_video:
        st.markdown("**🎥 Registro Visual**")
        st.markdown("""<div class="video-wrapper"><iframe src="https://www.youtube.com/embed/AzGyshHLN3k?autoplay=1&mute=0&controls=0&start=0" frameborder="0" allow="autoplay; encrypted-media"></iframe><div class="video-blocker"></div></div>""", unsafe_allow_html=True)
        status_ph = st.empty(); desc_ph = st.empty()
    with c_mapa:
        st.markdown("**📡 GPS em Tempo Real**")
        mapa_ph = st.empty()
        
    st.markdown("---")
    m1, m2, m3, m4 = st.columns(4)
    box_relogio, box_fase, box_dist, box_atrito = m1.empty(), m2.empty(), m3.empty(), m4.empty()
    
    time.sleep(1)
    
    # --- CONFIGURAÇÃO DA ANIMAÇÃO ---
    NUM_FASES = len(ROTEIRO) # 10 Fases
    STEP_TIME = 8.0          # Tempo de cada fase
    TOTAL_TIME = NUM_FASES * STEP_TIME 
    
    start_t = time.time()
    
    while True:
        elapsed = time.time() - start_t
        if elapsed > TOTAL_TIME: break
        
        idx = int(elapsed // STEP_TIME)
        if idx >= NUM_FASES: idx = NUM_FASES - 1
        step = ROTEIRO[idx]
        progress = (elapsed % STEP_TIME) / STEP_TIME
        
        status_ph.markdown(f"""<div class="status-box {step['css']}">{step['titulo']}</div>""", unsafe_allow_html=True)
        desc_ph.info(step['desc'])
        
        # O RELÓGIO SEGUE O DADO DO ROTEIRO
        # Nas fases 8, 9 e 10, ele mostra "07:37" fixo, conforme configurado na lista ROTEIRO
        box_relogio.metric("⏰ Horário", step['horario'])
        
        box_fase.metric("Fase", f"{step['id']}/10")
        box_atrito.metric("⚡ Atrito", step['atrito'], delta_color="inverse")
        
        # GPS Logic
        path_len = len(step['path'])
        if step['mov'] and path_len > 1:
            curr_idx = int(progress * (path_len - 1))
            if curr_idx >= path_len: curr_idx = path_len - 1
            lon = step['path'][curr_idx][0]
            lat = step['path'][curr_idx][1]
        else:
            # Para fases estáticas (como Refeitório e Banda), mantemos a posição fixa
            lon = step['path'][0][0]
            lat = step['path'][0][1]
            
        view = pdk.ViewState(latitude=lat, longitude=lon, zoom=step['zoom'], pitch=50)
        
        # Layers
        layer_road = pdk.Layer("PathLayer", data=BACKGROUND_LAYERS_DATA, get_path="path", get_color="color", get_width=40, opacity=0.7)
        
        current_icon = ICONS_DATA.get(step['icon'], ICONS_DATA['bus'])
        layer_icon = pdk.Layer(
            "IconLayer",
            data=pd.DataFrame({'lon': [lon], 'lat': [lat]}),
            get_position='[lon, lat]',
            get_icon=lambda d: current_icon,
            get_size=50,        
            size_scale=8,       
            pickable=True
        )
        
        deck = pdk.Deck(layers=[layer_road, layer_icon], initial_view_state=view, map_style="mapbox://styles/mapbox/light-v10", tooltip={"text": step['desc']})
        mapa_ph.pydeck_chart(deck)
        time.sleep(0.1)

    st.success("🏁 Fim do Itinerário.")
    time.sleep(3)
    st.session_state.simulacao_ativa = False
    st.rerun()
