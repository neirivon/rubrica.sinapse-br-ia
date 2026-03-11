# /home/neirivon/SINAPSE2.0/sinapsebr_rubrica/scripts/pages/03_TMAP_2010.py
import streamlit as st
import pandas as pd
import json
import plotly.express as px
from pathlib import Path

# Configuração da Página
st.set_page_config(page_title="TMAP • Histórico Comparativo", page_icon="⏳", layout="wide")

# Bloqueia tradução automática
st.markdown('<meta name="google" content="notranslate">', unsafe_allow_html=True)

# --- CAMINHOS ---
THIS = Path(__file__).resolve()
# Arquivos gerados pelo ETL Master V2
JSON_HIST = THIS.parents[1] / "data" / "tmap_historico_comparativo.json"
JSON_2024 = THIS.parents[1] / "data" / "tmap_2024_completo.json"

# --- FUNÇÃO DE CÁLCULO GEOFILOSÓFICO (NOVA INTEGRAÇÃO) ---
def calcular_indice_atrito(distancia_km, num_onibus):
    """
    Calcula o desgaste do aluno baseada na Geofilosofia (Tempo + Corpo).
    Referência: Tese Paulo Irineu (O Tempo do Trem vs. Tempo do Lugar)
    """
    # 1. Custo da Distância (Físico)
    # A distância não é apenas métrica, é cansaço acumulado.
    peso_distancia = distancia_km * 1.5 
    
    # 2. Custo do Transbordo (Psicológico/Espera/Insegurança)
    # Cada troca de ônibus adiciona ~20min de tempo morto (espera no terminal) e estresse.
    # Fórmula: (Total de Ônibus - 1) * Fator de Penalidade
    if num_onibus > 0:
        penalidade_transbordo = (num_onibus - 1) * 20 
    else:
        penalidade_transbordo = 0
    
    indice_total = peso_distancia + penalidade_transbordo
    
    # Classificação baseada na escala de fricção territorial
    if indice_total > 80:
        return indice_total, "Nível Extremo: Exclusão Territorial (Risco Máximo de Evasão)"
    elif indice_total > 50:
        return indice_total, "Nível Alto: Desgaste Severo"
    else:
        return indice_total, "Nível Padrão"

# --- CARGA DE DADOS ---
@st.cache_data
def load_historico_unificado():
    dados = []
    
    # 1. Carrega 2017 (Histórico)
    if JSON_HIST.exists():
        with open(JSON_HIST, 'r', encoding='utf-8') as f:
            dados.extend(json.load(f))
            
    # 2. Carrega 2024 (Atual)
    if JSON_2024.exists():
        with open(JSON_2024, 'r', encoding='utf-8') as f:
            data_24 = json.load(f)
            for item in data_24:
                # Simplificação para visualização rápida
                dados.append({
                    "Municipio": item['Municipio'],
                    "Ano": 2024,
                    "Total_Escolas": len(item.get('Escolas', [])),
                    "Escolas_Rurais": len([e for e in item.get('Escolas', []) if e.get('Zona') == 'Rural'])
                })
    return dados

# Carrega Dataframe
data_raw = load_historico_unificado()
df = pd.DataFrame(data_raw)

# --- INTERFACE PRINCIPAL ---
st.title("⏳ TMAP • Arqueologia do Território (2010-2024)")
st.markdown("""
Esta seção analisa a evolução da oferta de EPT no Triângulo Mineiro, 
confrontando dados estatísticos com a realidade vivida (**Geofilosofia**).
""")

if not df.empty:
    # Filtros e Gráficos Gerais
    col1, col2 = st.columns([1, 3])
    with col1:
        cidades = df['Municipio'].unique()
        sel_cidade = st.selectbox("Filtrar Município:", ["Todos"] + list(cidades))
    
    df_view = df if sel_cidade == "Todos" else df[df['Municipio'] == sel_cidade]
    
    with col2:
        # Gráfico simples de evolução
        fig = px.bar(df_view, x='Municipio', y='Total_Escolas', color='Ano', barmode='group',
                     title="Evolução da Oferta Escolar (Comparativo)")
        st.plotly_chart(fig, use_container_width=True)

    with st.expander("📂 Ver Dados Brutos"):
        st.dataframe(df_view.sort_values(['Municipio', 'Ano']), use_container_width=True)

# --- SEÇÃO GEOFILOSÓFICA (O CORAÇÃO DA TESE) ---
st.divider()
st.header("🗺️ Calibragem do Algoritmo: O Fator Humano")
st.markdown("""
Para que a Inteligência Artificial não reproduza desigualdades, o algoritmo de **"Custo do Cotidiano"** foi calibrado com base em dados reais de mobilidade pendular (2010-2012).
""")

# Layout em colunas: Estudo de Caso vs Simulador
c_caso, c_sim = st.columns(2)

with c_caso:
    st.subheader("📁 Estudo de Caso Piloto (Ground Truth)")
    st.caption("Referência: Discente A.F. (2010-2012) | Validação via Google Maps & SIT")
    
    # DADOS REAIS ATUALIZADOS COM SUAS INFORMAÇÕES
    # A = Alimentador (Bairro->Terminal)
    # T = Troncal (Terminal->Terminal)
    # D = Distrital (Terminal->Rural)
    
    linhas_bairro = ["A-326", "A-327", "A-339"]
    
    st.markdown("""
    * **Origem:** Zona de Abrangência Terminal Santa Luzia
    * **Destino:** IFTM Campus Sobradinho
    * **Logística:** Alimentador ➔ Troncal ➔ Distrital
    """)

    # Exibe as opções de saída (A prova da redundância local vs escassez rural)
    st.markdown("**🚌 1ª Perna: Zona de Captura (Alimentadores):**")
    # Mostra os códigos como tags visuais
    cols_tags = st.columns(len(linhas_bairro))
    for i, linha in enumerate(linhas_bairro):
        cols_tags[i].code(linha)
    
    st.info("""
    **Análise de Fluxo:** O aluno possui 3 opções para sair do bairro, mas todas funilam 
    para o mesmo gargalo (**Terminal Sta. Luzia**), obrigando o transbordo para o sistema Troncal 
    e posteriormente Distrital.
    """)

    # DADOS DE CÁLCULO
    dist_real = 32.5 
    onibus_real = 3 # A + T + D
    
    # Cálculo
    indice_real, class_real = calcular_indice_atrito(dist_real, onibus_real)
    
    st.metric(label="Distância Multimodal Total", value=f"{dist_real} km")
    st.metric(label="Trocas Obrigatórias (Cadeia)", value=f"{onibus_real} (A + T + D)")
    
    st.markdown("---")
    st.markdown(f"#### 📉 Índice de Atrito: **{indice_real}**")
    st.error(f"**Diagnóstico:** {class_real}")
    
    st.markdown("""
    > *"O trajeto em Zigue-Zague (Leste-Oeste-Norte) evidenciado pelo Google Maps 
    > comprova o desacordo entre o planejamento urbano e a escola rural."*
    """)

with c_sim:
    st.subheader("🎚️ Simulador de Atrito Territorial")
    st.caption("Teste como a geografia impacta a avaliação de outros estudantes:")
    
    # Sliders para a Banca testar
    sim_km = st.slider("Distância Casa-Escola (Km)", 0, 60, 10)
    sim_bus = st.slider("Número de Ônibus/Transportes", 1, 4, 1)
    
    # Cálculo Dinâmico
    idx_sim,cls_sim = calcular_indice_atrito(sim_km, sim_bus)
    
    # Visualização Dinâmica
    if idx_sim > 80:
        st.error(f"Índice: {idx_sim} | {cls_sim}")
    elif idx_sim > 50:
        st.warning(f"Índice: {idx_sim} | {cls_sim}")
    else:
        st.success(f"Índice: {idx_sim} | {cls_sim}")
        
    # Explicação da Fórmula
    st.code(f"""
    # Lógica do Cálculo (Python):
    Peso Distância = {sim_km} * 1.5 = {sim_km * 1.5}
    Penalidade Transbordo = ({sim_bus} - 1) * 20 = {(sim_bus - 1) * 20}
    
    TOTAL = {sim_km * 1.5} + {(sim_bus - 1) * 20} = {idx_sim}
    """, language="python")

# --- NOTA DE RODAPÉ ---
st.divider()
st.caption("Sistema de Rubrica SINAPSE-BR IA • Módulo de Análise Territorial • Baseado na Tese de Dr. Paulo Irineu (Geofilosofia) e Dra. Gelda Costa.")
