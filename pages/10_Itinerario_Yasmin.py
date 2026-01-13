# /home/neirivon/SINAPSE2.0/sinapsebr_rubrica/scripts/pages/10_Itinerario_Yasmin_Real.py
# --------------------------------------------------------------------------------------
# NOME DO SCRIPT: 10_Itinerario_Yasmin_Real.py
# DESCRIÇÃO: Simulação de alta precisão do itinerário IFTM (2009-2012).
#            Utiliza geometria de rota complexa (não linear) baseada em dados reais
#            fornecidos pelo usuário (ruas, durações e paradas).
# FUNCIONALIDADES:
#   1. Mapeamento de rota traçado manualmente sobre a malha viária de Uberlândia.
#   2. Odômetro de precisão baseado na soma de segmentos de Haversine do trajeto real.
#   3. Cronômetro sincronizado com as durações exatas informadas.
#   4. Cálculo de Desgaste (Fricção) e PROBABILIDADE DE EVASÃO ESCOLAR.
# AUTOR: Neirivon Elias Cardoso (Adaptado por Gemini)
# PROJETO: Rubrica SINAPSE-BR IA
# DATA: 07/01/2026
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
    page_title="Itinerário Real Yasmin - IFTM",
    page_icon="🚌"
)

# --- CSS: ESTILO DOS PAINÉIS ---
st.markdown("""
<style>
    div[data-testid="metric-container"] {
        background-color: #ffffff;
        border-radius: 8px;
        padding: 10px;
        border-left: 5px solid #1e40af;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
    }
    .status-box {
        padding: 15px; border-radius: 8px; font-weight: bold; text-align: center; margin-bottom: 10px; font-size: 1.2em; color: white;
    }
    /* Cores de Movimento */
    .moving-green { background-color: #166534; border: 2px solid #14532d; }
    .moving-red { background-color: #b91c1c; border: 2px solid #7f1d1d; }
    .moving-walk { background-color: #ea580c; border: 2px solid #9a3412; }
    .waiting { background-color: #d97706; border: 2px solid #b45309; animation: blinker 2s linear infinite; }
    
    @keyframes blinker { 50% { opacity: 0.7; } }
</style>
""", unsafe_allow_html=True)

# --- BARRA LATERAL (CONTROLES E FUNDAMENTAÇÃO) ---
with st.sidebar:
    st.header("⚙️ Configuração")
    
    velocidade_animacao = st.select_slider(
        "Velocidade da Animação:",
        options=["Muito Lenta (Analítica)", "Lenta (Padrão)", "Média", "Rápida"],
        value="Lenta (Padrão)"
    )
    
    sleep_map = {"Muito Lenta (Analítica)": 0.8, "Lenta (Padrão)": 0.4, "Média": 0.15, "Rápida": 0.05}
    SLEEP_TIME = sleep_map[velocidade_animacao]

    st.divider()
    
    st.header("📚 Fundamentação Teórica")
    st.info("Por que 100% de Risco?")
    st.markdown("""
    O cálculo de saturação baseia-se na **Constante de Marchetti** (Travel Time Budget).
    
    Segundo a literatura, o limite aceitável de deslocamento diário é de **~1 hora**. Yasmin gasta **~4 horas** (ida e volta).
    
    * **0-60 pts:** Dentro da Constante de Marchetti.
    * **61-100 pts:** Zona de Desgaste Acentuado.
    * **>100 pts (100%):** **Pobreza de Tempo**. O tempo de deslocamento consome horas vitais de sono e estudo, criando uma barreira estrutural à permanência (*Spatial Mismatch*).
    """)

# --- 1. FUNÇÕES MATEMÁTICAS ---
def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi / 2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

# --- 2. PONTOS DE REFERÊNCIA ---
LANDMARKS = [
    {"name": "🏠 CASA", "lat": -18.951567, "lon": -48.275365, "color": [0, 0, 255]},
    {"name": "🔄 T. STA LUZIA", "lat": -18.940562, "lon": -48.261543, "color": [50, 50, 50]},
    {"name": "🔄 T. UMUARAMA", "lat": -18.892914, "lon": -48.253630, "color": [50, 50, 50]},
    {"name": "🎓 IFTM", "lat": -18.784532, "lon": -48.212065, "color": [0, 100, 0]}
]

# --- 3. GEOMETRIA DA ROTA ---
path_caminhada = [[-18.951567, -48.275365], [-18.951241, -48.274155], [-18.950731, -48.274330], [-18.950827, -48.273579]]
path_a339 = [[-18.950827, -48.273579], [-18.949834, -48.271208], [-18.948113, -48.268654], [-18.945834, -48.265537], [-18.943728, -48.263098], [-18.941570, -48.262155], [-18.940562, -48.261543]]
path_i323 = [[-18.940562, -48.261543], [-18.936661, -48.258645], [-18.928449, -48.252619], [-18.922571, -48.248345], [-18.918068, -48.251928], [-18.911676, -48.257279], [-18.903864, -48.259575], [-18.898187, -48.256973], [-18.892914, -48.253630]]
path_d281 = [[-18.892914, -48.253630], [-18.888603, -48.250705], [-18.878239, -48.243410], [-18.865708, -48.234443], [-18.851952, -48.224749], [-18.835348, -48.213388], [-18.818425, -48.202175], [-18.803734, -48.205700], [-18.792164, -48.209195], [-18.784532, -48.212065]]

# --- 4. ROTEIRO COM CÁLCULO DE DESGASTE ---
roteiro = [
    {
        "fase": "Caminhada (Casa -> Ponto)", 
        "descricao": "Saindo de casa a pé em direção à Avenida Abelardo Pena.", 
        "transporte": "A pé", "path": path_caminhada, "hora_inicio": "05:40", "duracao_min": 5, 
        "cor_icone": [255, 140, 0], "token_text": "🚶", "velocidade_painel": "🚶 A caminho da Av. Abelardo Pena", 
        "distancia_real_km": 0.28, "status_css": "moving-walk", 
        "friction_factor": 3.0 # Fator explicativo: Esforço físico
    },
    {
        "fase": "Embarque (Av. Abelardo Pena)", 
        "descricao": "Aguardando o ônibus alimentador A-339 (Verde).", 
        "transporte": "Esperando", "path": [path_a339[0], path_a339[0]], "hora_inicio": "05:45", "duracao_min": 5, 
        "cor_icone": [255, 191, 0], "token_text": "⏳", "velocidade_painel": "✋ Aguardando A-339", 
        "distancia_real_km": 0.0, "status_css": "waiting",
        "friction_factor": 1.5 # Fator explicativo: Ansiedade
    },
    {
        "fase": "Ônibus A-339 (Verde)", 
        "descricao": "Seguindo da Av. Abelardo Pena para o Terminal Santa Luzia.", 
        "transporte": "Ônibus", "path": path_a339, "hora_inicio": "05:50", "duracao_min": 10, 
        "cor_icone": [0, 128, 0], "token_text": "A339", "velocidade_painel": "🚌 A-339 (Rumo T. Sta Luzia)", 
        "distancia_real_km": 4.50, "status_css": "moving-green",
        "friction_factor": 1.0 # Base
    },
    {
        "fase": "Espera: T. Santa Luzia (15 min)", 
        "descricao": "Aguardando conexão para o Expresso.", 
        "transporte": "Conexão", "path": [path_i323[0], path_i323[0]], "hora_inicio": "06:00", "duracao_min": 15, 
        "cor_icone": [255, 191, 0], "token_text": "15'", "velocidade_painel": "⏳ Aguardando 15 min (Expresso)", 
        "distancia_real_km": 0.0, "status_css": "waiting",
        "friction_factor": 1.8 # Tédio/Estresse alto pela demora
    },
    {
        "fase": "Ônibus I-323 (Vermelho)", 
        "descricao": "Expresso Troncal: T. Santa Luzia -> T. Umuarama.", 
        "transporte": "Ônibus", "path": path_i323, "hora_inicio": "06:15", "duracao_min": 25, 
        "cor_icone": [200, 0, 0], "token_text": "I323", "velocidade_painel": "🚍 I-323 (Expresso)", 
        "distancia_real_km": 9.20, "status_css": "moving-red",
        "friction_factor": 1.0
    },
    {
        "fase": "Espera: T. Umuarama (15 min)", 
        "descricao": "Aguardando conexão para o ônibus do Campus (D-281).", 
        "transporte": "Conexão", "path": [path_d281[0], path_d281[0]], "hora_inicio": "06:40", "duracao_min": 15, 
        "cor_icone": [255, 191, 0], "token_text": "15'", "velocidade_painel": "⏳ Aguardando 15 min (D-281)", 
        "distancia_real_km": 0.0, "status_css": "waiting",
        "friction_factor": 1.8
    },
    {
        "fase": "Ônibus D-281 (Verde)", 
        "descricao": "Linha Rural: T. Umuarama -> IFTM Campus Uberlândia.", 
        "transporte": "Ônibus", "path": path_d281, "hora_inicio": "06:55", "duracao_min": 50, 
        "cor_icone": [0, 128, 0], "token_text": "D281", "velocidade_painel": "🚌 D-281 (Rumo IFTM)", 
        "distancia_real_km": 28.50, "status_css": "moving-green",
        "friction_factor": 1.2 # Rural (maior desgaste/rugosidade)
    }
]

# --- 5. INTERFACE DO USUÁRIO ---
st.title("Itinerário Real: Yasmin (2009-2012)")
st.markdown("##### 📍 A Jornada Diária: Do Parque São Jorge ao IFTM Sobradinho")

# Layout de 4 Colunas para incluir o Desgaste
col1, col2, col3, col4 = st.columns(4)
with col1: relogio_box = st.empty()
with col2: odometro_box = st.empty()
with col3: desgaste_box = st.empty()
with col4: evasion_box = st.empty() # Nova caixa de Evasão

status_msg = st.empty() # Barra de status larga

c_mapa, c_info = st.columns([3, 1])
mapa_placeholder = c_mapa.empty()
info_placeholder = c_info.empty()

if st.button("▶️ INICIAR ANÁLISE DE VULNERABILIDADE"):
    
    km_acumulado = 0.0
    wear_accumulated = 0.0
    
    # 100% = Saturação da Constante de Marchetti (~160 pts de atrito acumulado)
    MAX_TOLERANCE = 160.0 
    
    # Prepara Rota de Fundo
    full_route_path = []
    for etapa in roteiro: full_route_path.extend(etapa['path'])

    layer_rota = pdk.Layer(
        "PathLayer", data=[{"path": full_route_path}], get_path="path",
        get_color=[180, 180, 180], get_width=12, width_min_pixels=3,
    )
    layer_textos = pdk.Layer(
        "TextLayer", data=LANDMARKS, get_position="[lon, lat]", get_text="name",
        get_color=[0, 0, 0], get_size=15, get_alignment_baseline="'top'",
        get_background_color=[255, 255, 255, 200], show_border=True, border_width=1, font_weight="bold"
    )
    layer_pontos_fixos = pdk.Layer(
        "ScatterplotLayer", data=LANDMARKS, get_position="[lon, lat]",
        get_color="color", get_radius=150, pickable=True
    )

    for etapa in roteiro:
        path_points = etapa['path']
        total_points = len(path_points)
        
        # Fator de Correção de Distância
        dist_visual_total = 0.0
        if total_points > 1:
            for k in range(len(path_points) - 1):
                dist_visual_total += haversine(path_points[k][0], path_points[k][1], path_points[k+1][0], path_points[k+1][1])
        dist_factor = etapa['distancia_real_km'] / dist_visual_total if dist_visual_total > 0 and etapa['distancia_real_km'] > 0 else 0

        # Tempos
        tempo_base = datetime.strptime(etapa['hora_inicio'], "%H:%M")
        segundos_totais = etapa['duracao_min'] * 60
        segundos_frame = segundos_totais / total_points if total_points > 0 else 0
        wear_per_frame = (segundos_frame / 60.0) * etapa['friction_factor']
        
        # Painel Status
        status_html = f"""<div class="status-box {etapa['status_css']}">{etapa['velocidade_painel']}</div>"""
        status_msg.markdown(status_html, unsafe_allow_html=True)
        info_placeholder.info(f"📍 **{etapa['fase']}**\n\n📝 {etapa['descricao']}\n\n⚡ **Fator de Atrito:** {etapa['friction_factor']}x")

        for i, point in enumerate(path_points):
            lat, lon = point[0], point[1]
            
            # Odômetro
            if i > 0 and etapa['transporte'] not in ["Esperando", "Conexão"]:
                d_seg = haversine(path_points[i-1][0], path_points[i-1][1], lat, lon)
                km_acumulado += d_seg * dist_factor
            
            # Desgaste Acumulado
            wear_accumulated += wear_per_frame
            
            # CÁLCULO DE VULNERABILIDADE
            vulnerabilidade = (wear_accumulated / MAX_TOLERANCE) * 100.0
            
            # Relógio
            delta_t = timedelta(seconds=segundos_frame * i)
            hora_atual = (tempo_base + delta_t).strftime("%H:%M:%S")
            
            relogio_box.metric("⏰ Horário", hora_atual)
            odometro_box.metric("📏 Distância", f"{km_acumulado:.2f} km")
            desgaste_box.metric("⚡ Desgaste", f"{wear_accumulated:.0f} pts")
            
            # Mostrador de Vulnerabilidade
            label_vuln = "Vulnerabilidade"
            if vulnerabilidade >= 100:
                evasion_box.metric(f"⚠️ {label_vuln}", f"{vulnerabilidade:.0f}%", delta="POBREZA DE TEMPO", delta_color="inverse")
            elif vulnerabilidade > 80:
                evasion_box.metric(f"⚠️ {label_vuln}", f"{vulnerabilidade:.0f}%", delta="RISCO CRÍTICO", delta_color="inverse")
            else:
                 evasion_box.metric(f"📉 {label_vuln}", f"{vulnerabilidade:.0f}%", delta="MODERADO")

            # Token
            layer_token_base = pdk.Layer(
                "ScatterplotLayer", data=pd.DataFrame({'lat': [lat], 'lon': [lon]}),
                get_position='[lon, lat]', get_color=etapa['cor_icone'], get_radius=120,
                radius_min_pixels=18, radius_max_pixels=30, stroked=True, filled=True,
                line_width_min_pixels=2, get_line_color=[255, 255, 255],
            )
            layer_token_label = pdk.Layer(
                "TextLayer", data=pd.DataFrame({'lat': [lat], 'lon': [lon], 'text': [etapa['token_text']]}),
                get_position='[lon, lat]', get_text='text', get_color=[255, 255, 255], get_size=12,
                get_alignment_baseline="'middle'", get_text_anchor="'middle'", font_weight="bold"
            )

            view = pdk.ViewState(latitude=lat, longitude=lon, zoom=14, pitch=50)

            r = pdk.Deck(
                layers=[layer_rota, layer_textos, layer_pontos_fixos, layer_token_base, layer_token_label],
                initial_view_state=view, map_style="mapbox://styles/mapbox/light-v10",
                tooltip={"text": "{name}"}
            )
            mapa_placeholder.pydeck_chart(r)
            time.sleep(SLEEP_TIME)

    final_time = (datetime.strptime(roteiro[-1]['hora_inicio'], "%H:%M") + timedelta(minutes=roteiro[-1]['duracao_min'])).strftime("%H:%M")
    
    # Conclusão Científica
    if wear_accumulated >= MAX_TOLERANCE:
        st.error(f"🚨 ANÁLISE FINAL: Índice de Vulnerabilidade atingiu {vulnerabilidade:.0f}%. O tempo de deslocamento violou a Constante de Marchetti, caracterizando 'Pobreza de Tempo' e risco estrutural de evasão.")
    else:
        st.success(f"🏁 Chegada no IFTM! O deslocamento permaneceu dentro dos limites da Constante de Marchetti.")
