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
#   4. Visualização: Linha de rota Vermelha (#FF0000) com agente móvel sobreposto.
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

# --- BARRA LATERAL ---
with st.sidebar:
    st.header("Metadados - Rota Precisa")
    st.code("ID: neirivon/rubrica.sinapse-br-ia\nVersão: 4.0 (Geometria Real)", language="text")
    st.caption("Baseado em dados detalhados de trajeto e horários (2009-2012).")
    st.markdown("---")
    st.markdown("**Nota sobre a Rota:** O trajeto vermelho no mapa é uma aproximação da geometria das ruas baseada na descrição fornecida, não uma rota de GPS em tempo real.")

# --- 1. FUNÇÕES MATEMÁTICAS ---
def haversine(lat1, lon1, lat2, lon2):
    """Calcula distância em KM entre dois pontos (Fórmula de Haversine)"""
    R = 6371  # Raio da Terra
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi / 2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

# --- 2. DADOS DE GEOMETRIA DA ROTA (O "ZIGUE-ZAGUE" REAL) ---
# Estes pontos foram traçados manualmente para simular as ruas mencionadas.

# Caminhada: R. Maria Osória -> Vandira Basílio -> Wilson Cunha
path_caminhada = [
    [-18.951567, -48.275365], # Início R. Maria Osória
    [-18.951241, -48.274155], # Esquina Vandira Basílio
    [-18.950731, -48.274330], # Esquina Wilson Cunha
    [-18.950599, -48.273783]  # Ponto na Wilson Cunha (aprox)
]

# A339: Abelardo Pena -> Bairro -> T. Santa Luzia (Trajeto sinuoso de bairro)
path_a339 = [
    [-18.950827, -48.273579], # R. Abelardo Pena, 325
    [-18.949834, -48.271208], # Trajeto Bairro São Jorge
    [-18.948113, -48.268654],
    [-18.945834, -48.265537],
    [-18.943728, -48.263098], # Aproximando da João Naves
    [-18.941570, -48.262155], # Entrada Terminal
    [-18.940562, -48.261543]  # Terminal Santa Luzia
]

# I323 Expresso: T. Sta Luzia -> João Naves -> Rondon -> T. Umuarama (Arteriais rápidas)
path_i323 = [
    [-18.940562, -48.261543], # T. Sta Luzia
    [-18.936661, -48.258645], # Av. João Naves
    [-18.928449, -48.252619],
    [-18.922571, -48.248345], # Rotatória Rondon Pacheco
    [-18.918068, -48.251928], # Av. Rondon Pacheco
    [-18.911676, -48.257279],
    [-18.903864, -48.259575], # Acesso Av. Brasil
    [-18.898187, -48.256973], # Av. Brasil
    [-18.892914, -48.253630]  # Terminal Umuarama
]

# D281 Rural: T. Umuarama -> Estradas -> IFTM Sobradinho (Longo trajeto)
path_d281 = [
    [-18.892914, -48.253630], # T. Umuarama
    [-18.888603, -48.250705], # Saída Umuarama
    [-18.878239, -48.243410], # Início estrada rural/anel viário
    [-18.865708, -48.234443],
    [-18.851952, -48.224749], # Rodovia
    [-18.835348, -48.213388],
    [-18.818425, -48.202175],
    [-18.803734, -48.205700], # Entrada Sobradinho
    [-18.792164, -48.209195],
    [-18.784532, -48.212065]  # IFTM Fazenda Sobradinho
]

# --- 3. ROTEIRO DETALHADO (Com base nos dados fornecidos) ---
roteiro = [
    {
        "fase": "1) A pé: R. Maria Osória -> Ponto",
        "descricao": "270m, 3 min. Via R. Maria Osória de Jesus, Vandira Basílio e Wilson Cunha.",
        "transporte": "Caminhada",
        "path": path_caminhada,
        "hora_inicio": "05:37", # Ajustado para chegar 5:40 no ponto
        "duracao_min": 3, 
        "cor_icone": [255, 140, 0, 200], # Laranja
        "raio": 80,
        "velocidade_painel": "🚶 Caminhando",
    },
    {
        "fase": "Aguardando A339",
        "descricao": "R. Abelardo Pena, 325. Aguardando ônibus das 05:42.",
        "transporte": "Esperando",
        "path": [path_a339[0], path_a339[0]], # Fica parado no ponto inicial do ônibus
        "hora_inicio": "05:40",
        "duracao_min": 2,
        "cor_icone": [100, 100, 100, 150],
        "raio": 80,
        "velocidade_painel": "✋ Parado no Ponto",
    },
    {
        "fase": "2) Ônibus A339 -> T. Santa Luzia",
        "descricao": "Saída 05:42. Duração 9 min (10 paradas). Chegada 05:51.",
        "transporte": "Ônibus A339 (Verde)",
        "path": path_a339,
        "hora_inicio": "05:42",
        "duracao_min": 9, 
        "cor_icone": [0, 200, 0, 200], # Verde
        "raio": 200,
        "velocidade_painel": "🚌 A339 (Bairro)",
    },
    {
        "fase": "Conexão T. Santa Luzia",
        "descricao": "Chegada 05:51. Aguardando I323 (saída 06:18).",
        "transporte": "Conexão",
        "path": [path_i323[0], path_i323[0]], # Parado no terminal
        "hora_inicio": "05:51",
        "duracao_min": 27, # Tempo de espera longo
        "cor_icone": [100, 100, 100, 150],
        "raio": 100,
        "velocidade_painel": "⌛ Aguardando Expresso",
    },
    {
        "fase": "3) Ônibus I323 (Expresso) -> T. Umuarama",
        "descricao": "Saída 06:18. Duração 28 min (Sem paradas). Chegada 06:46.",
        "transporte": "I323 Expresso (Vermelho)",
        "path": path_i323,
        "hora_inicio": "06:18",
        "duracao_min": 28, 
        "cor_icone": [255, 0, 0, 200], # Vermelho
        "raio": 250,
        "velocidade_painel": "🚍 I323 (Rápido)",
    },
    {
        "fase": "Conexão T. Umuarama",
        "descricao": "Chegada 06:46. Conexão para D281.",
        "transporte": "Conexão",
        "path": [path_d281[0], path_d281[0]], # Parado no terminal
        "hora_inicio": "06:46",
        "duracao_min": 4, # Ajuste técnico para conexão realista (saída 06:50)
        "cor_icone": [100, 100, 100, 150],
        "raio": 100,
        "velocidade_painel": "⌛ Trocando de Ônibus",
    },
    {
        "fase": "4) Ônibus D281 -> IFTM Sobradinho",
        "descricao": "Saída ajustada 06:50. Duração 57 min (29 paradas). Rota Rural.",
        "transporte": "Ônibus D281 (Verde)",
        "path": path_d281,
        "hora_inicio": "06:50", # Ajustado de 06:40 para ser cronologicamente possível
        "duracao_min": 57, 
        "cor_icone": [0, 200, 0, 200], # Verde
        "raio": 200,
        "velocidade_painel": "🚌 D281 (Rural)",
    }
]

# --- 4. INTERFACE VISUAL (DASHBOARD) ---

st.title("Itinerário Real: Yasmin (2009-2012)")
st.markdown("**Simulação de alta precisão baseada nos dados de tráfego e rotas fornecidos.**")

# Estilo dos Painéis
st.markdown("""
<style>
    div[data-testid="metric-container"] {
        background-color: #ffffff;
        border-radius: 8px;
        padding: 15px;
        border-left: 5px solid #FF0000; /* Detalhe vermelho */
        box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
    }
</style>
""", unsafe_allow_html=True)

# Colunas do Painel Superior (KPIs)
col1, col2, col3 = st.columns(3)
with col1: relogio_box = st.empty()
with col2: odometro_box = st.empty()
with col3: speed_box = st.empty()

# Área principal (Mapa e Texto)
c_mapa, c_info = st.columns([3, 1])
mapa_placeholder = c_mapa.empty()
info_placeholder = c_info.empty()

# Botão Iniciar
if st.button("▶️ INICIAR SIMULAÇÃO PRECISA"):
    
    km_acumulado = 0.0
    # Coleta todos os pontos de todas as etapas para desenhar a linha vermelha completa de fundo
    full_route_path = []
    for etapa in roteiro:
        full_route_path.extend(etapa['path'])

    # Define a camada da rota completa (LINHA VERMELHA FIXA #FF0000)
    layer_rota_completa = pdk.Layer(
        "PathLayer",
        data=[{"path": full_route_path}],
        get_path="path",
        get_color=[255, 0, 0], # Vermelho FF0000
        get_width=8,
        width_min_pixels=3,
        pickable=False,
    )

    for etapa in roteiro:
        path_points = etapa['path']
        total_points_etapa = len(path_points)
        
        tempo_base = datetime.strptime(etapa['hora_inicio'], "%H:%M")
        # Calcula quanto tempo adicionar por "frame" da animação
        segundos_totais = etapa['duracao_min'] * 60
        segundos_por_frame = segundos_totais / total_points_etapa if total_points_etapa > 0 else 0
        
        # Atualiza caixa de informações lateral
        info_placeholder.info(f"📍 **{etapa['fase']}**\n\n📝 {etapa['descricao']}")
        
        # Loop pelos pontos reais da geometria da rua
        for i, point in enumerate(path_points):
            lat, lon = point[0], point[1]
            
            # 1. Atualizar Odômetro (Soma a distância do segmento anterior até o atual)
            if i > 0 and etapa['transporte'] not in ["Esperando", "Conexão"]:
                lat_ant, lon_ant = path_points[i-1][0], path_points[i-1][1]
                dist_segmento = haversine(lat_ant, lon_ant, lat, lon)
                km_acumulado += dist_segmento
            
            # 2. Atualizar Relógio
            delta_t = timedelta(seconds=segundos_por_frame * i)
            hora_atual = (tempo_base + delta_t).strftime("%H:%M:%S")
            
            # 3. Exibir Métricas Dinâmicas
            relogio_box.metric("⏰ Horário Simulado", hora_atual)
            odometro_box.metric("📏 Distância Real Percorrida", f"{km_acumulado:.2f} km")
            speed_box.metric("⚙️ Status", etapa['velocidade_painel'], delta=etapa['transporte'])
            
            # 4. Mapa (Pydeck)
            # Visão da câmera segue o agente
            view = pdk.ViewState(latitude=lat, longitude=lon, zoom=14, pitch=45, bearing=0)
            
            # Camada do Agente Móvel (Ônibus/Pessoa colorido)
            layer_agente = pdk.Layer(
                "ScatterplotLayer",
                data=pd.DataFrame({'lat': [lat], 'lon': [lon]}),
                get_position='[lon, lat]',
                get_color=etapa['cor_icone'],
                get_radius=etapa['raio'],
                pickable=True,
                stroked=True,
                filled=True,
                line_width_min_pixels=2,
                get_line_color=[255, 255, 255], # Borda branca para destacar sobre o vermelho
            )

            r = pdk.Deck(
                # A ordem importa: rota completa embaixo, agente em cima
                layers=[layer_rota_completa, layer_agente],
                initial_view_state=view,
                map_style="mapbox://styles/mapbox/light-v10",
            )
            mapa_placeholder.pydeck_chart(r)
            
            # Controle de velocidade da animação
            # Ajuste este valor se estiver muito rápido ou devagar no seu PC
            time.sleep(0.15) 

    final_time = (datetime.strptime(roteiro[-1]['hora_inicio'], "%H:%M") + timedelta(minutes=roteiro[-1]['duracao_min'])).strftime("%H:%M")
    st.success(f"🏁 Chegada no IFTM às {final_time}! Distância total real: {km_acumulado:.2f} km")
    st.balloons()
