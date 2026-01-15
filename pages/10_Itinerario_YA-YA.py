# /home/neirivon/SINAPSE2.0/sinapsebr_rubrica/scripts/pages/10_Itinerario_YA-YA.py
# --------------------------------------------------------------------------------------
# NOME DO SCRIPT: 10_Itinerario_YA-YA.py
# DESCRIÇÃO: Simulação de alta precisão do itinerário IFTM (2009-2012).
#            Sincronizada com vídeo real do trajeto (80s).
#
# DADOS REAIS (Baseados no Relato 14/01/2026):
#   - Início: 05:40 (Casa)
#   - Chegada TSL: 05:56 (Dist: 3.27km acumulado)
#   - Saída TSL: 06:15 (19 min espera)
#   - Saída TU: 06:46 (Rumo ao IFTM)
#   - Chegada IFTM: 07:37 (Dist: 32.33km acumulado)
#
# AUTOR: Neirivon Elias Cardoso
# COLABORAÇÃO: Gemini (Refatoração Data-Driven)
# PROJETO: Rubrica SINAPSE-BR IA
# DATA: 14/01/2026
# VERSÃO: 1.3 (Calibragem Fina de Tempo/Distância)
# --------------------------------------------------------------------------------------

import streamlit as st
import pandas as pd
import pydeck as pdk
import time
import math
from datetime import datetime, timedelta

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    layout="wide", 
    page_title="Itinerário Real YA-YA - IFTM",
    page_icon="🚌"
)

# --- CSS: ESTILO E DINAMISMO ---
st.markdown("""
<style>
    div[data-testid="metric-container"] {
        background-color: #ffffff;
        border-radius: 8px;
        padding: 10px;
        border-left: 5px solid #1e40af;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
        transition: transform 0.1s;
    }
    div[data-testid="metric-container"]:hover {
        transform: scale(1.02);
    }
    .status-box {
        padding: 15px; border-radius: 8px; font-weight: bold; 
        text-align: center; margin-bottom: 10px; font-size: 1.3em; color: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.2);
        text-transform: uppercase;
        font-family: 'Arial', sans-serif;
    }
    /* Cores de Movimento */
    .fase-verde { background-color: #166534; border: 2px solid #14532d; } 
    .fase-vermelho { background-color: #b91c1c; border: 2px solid #7f1d1d; } 
    .fase-laranja { background-color: #ea580c; border: 2px solid #9a3412; } 
    .fase-amarelo { background-color: #d97706; border: 2px solid #b45309; } 
    .fase-azul { background-color: #1e3a8a; border: 2px solid #1e40af; } 
    .fase-roxa { background-color: #6b21a8; border: 2px solid #4c1d95; } 
    .fase-noturna { background-color: #312e81; border: 2px solid #1e1b4b; } 

    /* BLOQUEIO DE VÍDEO */
    .video-wrapper {
        position: relative;
        width: 100%;
        padding-bottom: 56.25%; /* 16:9 */
        height: 0;
        overflow: hidden;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.3);
    }
    .video-wrapper iframe {
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
    }
    .video-blocker {
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background: transparent; z-index: 10; cursor: not-allowed;
    }
</style>
""", unsafe_allow_html=True)

# --- 1. GEOMETRIA DA ROTA ---
path_caminhada = [[-18.951567, -48.275365], [-18.951241, -48.274155], [-18.950827, -48.273579]]
path_a339 = [[-18.950827, -48.273579], [-18.949834, -48.271208], [-18.945834, -48.265537], [-18.940562, -48.261543]]
path_i323 = [[-18.940562, -48.261543], [-18.936661, -48.258645], [-18.922571, -48.248345], [-18.903864, -48.259575], [-18.892914, -48.253630]]
path_d281 = [[-18.892914, -48.253630], [-18.888603, -48.250705], [-18.865708, -48.234443], [-18.835348, -48.213388], [-18.784532, -48.212065]]
path_iftm_entrada = [[-18.784532, -48.212065], [-18.785000, -48.212500], [-18.785500, -48.213000]] 
path_retorno = [[-18.784532, -48.212065], [-18.835348, -48.213388]] 

# --- 2. ROTEIRO MATEMÁTICO (CALIBRADO) ---
# Start Global: 05:40:00
# Total Distância Alvo: ~32.33 km
# Total Tempo Alvo: Chegada 07:37 (117 minutos totais)

ROTEIRO_DETALHADO = [
    # 01 - Caminhada (05:40 -> 05:44) | 4 min | 280m
    { "id": 1, "titulo": "🚶 SAINDO DE CASA (05:40)", "desc": "Caminhando 280m até o ponto do A-339.", "path": path_caminhada, "color": [255, 140, 0], "css": "fase-laranja", "zoom": 16, 
      "add_km": 0.28, "add_min": 4.0 },
    
    # 02 - A339 (05:44 -> 05:56) | 12 min | 2.99km (Total 3.27km)
    { "id": 2, "titulo": "🚌 A-339 RUMO AO T. STA LUZIA", "desc": "Trajeto de ônibus. Chegada prevista: 05:56.", "path": path_a339, "color": [0, 128, 0], "css": "fase-verde", "zoom": 15,
      "add_km": 2.99, "add_min": 12.0 },
    
    # 03 - Reflexo (05:56 -> 05:57) | 1 min | 0km (Poético/Transição)
    { "id": 3, "titulo": "🪞 REFLEXO NA JANELA", "desc": "Introspecção antes da chegada ao terminal.", "path": [path_a339[-1], path_a339[-1]], "color": [0, 100, 0], "css": "fase-verde", "zoom": 15,
      "add_km": 0.0, "add_min": 1.0 },
    
    # 04 - Espera TSL (05:57 -> 06:16) | 19 min | 0km
    { "id": 4, "titulo": "⏳ AGUARDANDO NO T. SANTA LUZIA", "desc": "19 minutos de espera. Conexão para o I-323.", "path": [[-18.940562, -48.261543], [-18.940562, -48.261543]], "color": [255, 191, 0], "css": "fase-amarelo", "zoom": 16,
      "add_km": 0.0, "add_min": 19.0 },
    
    # 05 - I323 (06:16 -> 06:46) | 30 min | 9.88km (Total 13.15km)
    # Obs: Inclui trajeto + pequena espera em Umuarama para sair 06:46 exato
    { "id": 5, "titulo": "🚍 I-323 RUMO AO T. UMUARAMA", "desc": "Expresso vermelho. Destino Terminal Umuarama.", "path": path_i323, "color": [200, 0, 0], "css": "fase-vermelho", "zoom": 14,
      "add_km": 9.88, "add_min": 30.0 },
    
    # 06 - D281 (06:46 -> 07:37) | 51 min | 19.18km (Total 32.33km)
    { "id": 6, "titulo": "🛣️ D-281 RUMO AO IFTM (06:46)", "desc": "Rodovia Municipal. 29 paradas. Chegada 07:37.", "path": path_d281, "color": [34, 139, 34], "css": "fase-verde", "zoom": 12,
      "add_km": 19.18, "add_min": 51.0 },
    
    # --- TRAVA DE CHEGADA (FASE 7) ---
    # 07 - Chegada IFTM (07:37)
    { "id": 7, "titulo": "🏫 CHEGADA NO IFTM (07:37)", "desc": "Subindo a escadaria. Tempo total de viagem: ~1h57.", "path": path_iftm_entrada, "color": [0, 0, 139], "css": "fase-azul", "zoom": 17,
      "add_km": 0, "add_min": 0 },
    
    # 08 - Refeitório
    { "id": 8, "titulo": "🍽️ REFEITÓRIO", "desc": "Almoço e convivência.", "path": [[-18.785500, -48.213000], [-18.785500, -48.213000]], "color": [0, 0, 139], "css": "fase-azul", "zoom": 17,
      "add_km": 0, "add_min": 0 },
    
    # 09 - Banda
    { "id": 9, "titulo": "🎸 BANDA EMPTY SOLUTION", "desc": "Ensaio no auditório.", "path": [[-18.785000, -48.212500], [-18.785000, -48.212500]], "color": [148, 0, 211], "css": "fase-roxa", "zoom": 17,
      "add_km": 0, "add_min": 0 },
    
    # 10 - Retorno
    { "id": 10, "titulo": "😴 VOLTANDO PARA CASA", "desc": "Fim do dia letivo.", "path": path_retorno, "color": [25, 25, 112], "css": "fase-noturna", "zoom": 13,
      "add_km": 0, "add_min": 0 }
]

# --- 3. INTERFACE ---
st.title("Itinerário Real: YA-YA (2009-2012)")
st.markdown("##### 📍 Sincronização: Narrativa Visual e Geográfica")

col_mapa, col_midia = st.columns([1.6, 1])

with col_mapa:
    mapa_placeholder = st.empty()
    st.caption("Acompanhe o deslocamento real no mapa à medida que o vídeo avança.")

with col_midia:
    st.markdown("**🎥 Registro Visual (Sincronizado)**")
    video_placeholder = st.empty()
    
    st.divider()
    status_placeholder = st.empty()
    desc_placeholder = st.empty()
    
    # Placeholders para métricas
    m1, m2, m3 = st.columns(3)
    relogio_box = m1.empty()
    passo_box = m2.empty()
    odometro_box = m3.empty()

# --- 4. ESTADO ---
if 'simulacao_ativa' not in st.session_state:
    st.session_state.simulacao_ativa = False

def run_simulation():
    st.session_state.simulacao_ativa = True

# Botão de Início
if not st.session_state.simulacao_ativa:
    st.markdown("---")
    st.button("▶️ INICIAR SIMULAÇÃO SINCRONIZADA (80 segundos)", on_click=run_simulation, type="primary")

# --- 5. EXECUÇÃO (MODO DINÂMICO/TURBO) ---
if st.session_state.simulacao_ativa:
    
    # Vídeo
    video_html = """
    <div class="video-wrapper">
        <iframe 
            src="https://www.youtube.com/embed/AzGyshHLN3k?autoplay=1&mute=0&controls=0&disablekb=1&modestbranding=1&rel=0&showinfo=0&start=0" 
            title="Itinerario YA-YA" frameborder="0" allow="autoplay; encrypted-media">
        </iframe>
        <div class="video-blocker"></div>
    </div>
    """
    video_placeholder.markdown(video_html, unsafe_allow_html=True)
    
    # Buffer de Sincronia
    with status_placeholder:
        st.warning("🔄 Sincronizando vídeo... ALINHANDO SATÉLITES.")
    time.sleep(3.5) # Buffer

    # Configuração
    TOTAL_DURATION = 80.0
    STEP_DURATION = 8.0 # Sincronizado com os cortes do vídeo
    
    # Mapa Base
    full_route_path = []
    for p in [path_caminhada, path_a339, path_i323, path_d281]: full_route_path.extend(p)
    
    # Hora Inicial: 05:40 da manhã
    HORA_INICIO = datetime(2026, 1, 1, 5, 40, 0)
    
    start_time = time.time()
    
    # Variáveis de Estado Anterior (para calcular delta)
    last_km = 0.0
    
    # LOOP PRINCIPAL
    while True:
        now = time.time()
        elapsed_time = now - start_time
        
        if elapsed_time >= TOTAL_DURATION:
            break
            
        # Índice da Etapa
        current_step_index = int(elapsed_time // STEP_DURATION)
        if current_step_index >= len(ROTEIRO_DETALHADO): current_step_index = len(ROTEIRO_DETALHADO) - 1
        
        # Progresso (0 a 1)
        step_progress = (elapsed_time % STEP_DURATION) / STEP_DURATION
        
        step = ROTEIRO_DETALHADO[current_step_index]
        path_atual = step['path']
        
        # --- CÁLCULO CUMULATIVO (Com Trava na Fase 7) ---
        km_acumulado = 0.0
        minutos_acumulados = 0.0
        
        # Soma etapas passadas
        for i in range(current_step_index):
            if ROTEIRO_DETALHADO[i]['id'] < 7: # Só soma se for antes da trava
                km_acumulado += ROTEIRO_DETALHADO[i]['add_km']
                minutos_acumulados += ROTEIRO_DETALHADO[i]['add_min']
        
        # Soma fração da etapa atual (SE for menor que 7)
        if step['id'] < 7:
            km_acumulado += step['add_km'] * step_progress
            minutos_acumulados += step['add_min'] * step_progress
        
        # --- ATUALIZAÇÃO VISUAL DINÂMICA ---
        status_html = f"""<div class="status-box {step['css']}">{step['titulo']}</div>"""
        status_placeholder.markdown(status_html, unsafe_allow_html=True)
        desc_placeholder.info(step['desc'])
        
        # Métricas com DELTA
        passo_box.metric(
            "Fase", 
            f"{step['id']}/10",
            delta="Em andamento..." if step['id'] < 7 else "Destino",
            delta_color="off"
        )
        
        # Odômetro com Delta (Mostra variação em metros)
        diff_km = km_acumulado - last_km
        odometro_box.metric(
            "📏 Distância Real", 
            f"{km_acumulado:.3f} km", 
            delta=f"+{(diff_km*1000):.1f} m" if diff_km > 0 else None
        )
        last_km = km_acumulado
        
        # Relógio Real com Segundos
        hora_atual_simulada = HORA_INICIO + timedelta(minutes=minutos_acumulados)
        relogio_box.metric(
            "⏰ Horário", 
            hora_atual_simulada.strftime("%H:%M:%S"),
            delta=f"+{int(elapsed_time)}s simulação"
        )
        
        # Mapa (Interpolação)
        if len(path_atual) > 1:
            idx_float = step_progress * (len(path_atual) - 1)
            idx_int = int(idx_float)
            if idx_int >= len(path_atual): idx_int = len(path_atual) - 1
            lat_atual = path_atual[idx_int][0]
            lon_atual = path_atual[idx_int][1]
        else:
            lat_atual = path_atual[0][0]
            lon_atual = path_atual[0][1]
            
        view_state = pdk.ViewState(latitude=lat_atual, longitude=lon_atual, zoom=step['zoom'], pitch=45)
        layer_route = pdk.Layer("PathLayer", data=[{"path": full_route_path}], get_path="path", get_color=[200, 200, 200, 100], get_width=10, width_min_pixels=3)
        layer_marker = pdk.Layer("ScatterplotLayer", data=pd.DataFrame({'lat': [lat_atual], 'lon': [lon_atual]}), get_position='[lon, lat]', get_color=step['color'], get_radius=150, stroked=True, filled=True, get_line_color=[255,255,255], line_width_min_pixels=2)
        
        deck = pdk.Deck(layers=[layer_route, layer_marker], initial_view_state=view_state, map_style="mapbox://styles/mapbox/light-v10")
        mapa_placeholder.pydeck_chart(deck)
        
        time.sleep(0.04) # 25 FPS no Python

    st.success("🏁 Jornada Finalizada.")
    time.sleep(3)
    st.session_state.simulacao_ativa = False
    st.rerun()

# Estado Inicial
if not st.session_state.simulacao_ativa:
    initial_view = pdk.ViewState(latitude=-18.91, longitude=-48.24, zoom=11, pitch=0)
    deck_static = pdk.Deck(layers=[pdk.Layer("PathLayer", data=[{"path": path_d281 + path_i323 + path_a339}], get_path="path", get_color=[100, 100, 100], get_width=10)], initial_view_state=initial_view, map_style="mapbox://styles/mapbox/light-v10")
    mapa_placeholder.pydeck_chart(deck_static)
    video_placeholder.markdown("""<div style="background-color: #f0f2f6; border-radius: 10px; height: 250px; display: flex; align-items: center; justify-content: center; color: #555;"><h3>Aguardando Início...</h3></div>""", unsafe_allow_html=True)
