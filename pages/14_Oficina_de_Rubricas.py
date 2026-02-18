# --------------------------------------------------------------------------------------
# CAMINHO DO ARQUIVO: /pages/14_Oficina_de_Rubricas.py
# NOME DO SCRIPT: 14_Oficina_de_Rubricas.py
#
# DESCRIÇÃO: Laboratório de Auditoria Pedagógica e Criação de Rubricas EPT.
#            Utiliza IA Generativa (Llama 3.3 via Groq) alimentada por RAG Estático
#            (Retrieval-Augmented Generation) baseado na obra de Susan Brookhart (2013).
#
# FUNCIONALIDADES:
#   1. Injeção de Contexto Teórico (OCR processado de PDF).
#   2. Auditoria de "Critério vs Tarefa" (Lógica Brookhart).
#   3. Visualização Volumétrica da Competência (Gráfico 3D Voxel).
#   4. Feedback Formativo para o Docente.
#
# AUTOR: Neirivon Elias Cardoso
# PROJETO: Rubrica SINAPSE-BR IA
# DATA: 18/02/2026 (Versão Final de Produção - Modelo Llama 3.3)
# --------------------------------------------------------------------------------------

import streamlit as st
import plotly.graph_objects as go
from groq import Groq
import time
import os

# Configuração da Página
st.set_page_config(
    page_title="Oficina de Rubricas SINAPSE",
    page_icon="🛠️",
    layout="wide"
)

# Estilo CSS Profissional (Clean/Academic)
st.markdown("""
<style>
    .stTextArea textarea { font-size: 16px; border-radius: 8px; border: 1px solid #e5e7eb; }
    .feedback-card {
        padding: 20px; border-radius: 10px;
        background-color: #f8f9fa; border-left: 5px solid #7c3aed;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    .metric-container {
        background-color: #ffffff; border: 1px solid #e5e7eb;
        border-radius: 8px; padding: 15px; text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# 1. CARREGAMENTO DO CÉREBRO TEÓRICO (RAG ESTÁTICO OTIMIZADO)
# ==============================================================================
@st.cache_data
def carregar_teoria_otimizada():
    """
    Carrega o arquivo processado via OCR e prepara para o Context Window do Llama 3.3.
    Caminho relativo: data/teoria_brookhart_blindada.txt
    """
    caminho = os.path.join("data", "teoria_brookhart_blindada.txt")
    
    if os.path.exists(caminho):
        try:
            with open(caminho, "r", encoding="utf-8") as f:
                texto_completo = f.read()
                
                # OTIMIZAÇÃO DE MEMÓRIA E VELOCIDADE:
                # O modelo Llama 3.3 suporta contextos grandes, mas para a defesa
                # queremos resposta RÁPIDA (baixa latência).
                # Manteremos os primeiros 35.000 caracteres (aumentei um pouco pois o modelo aguenta).
                texto_otimizado = texto_completo[:35000]
                
                return texto_otimizado
                
        except Exception as e:
            return f"Erro de Leitura: {e}"
    else:
        return """
        AVISO DE FALLBACK: Arquivo de teoria não encontrado.
        A IA utilizará conhecimento pré-treinado sobre Susan Brookhart.
        """

# Carrega a teoria na memória RAM
TEORIA_BROOKHART = carregar_teoria_otimizada()

# ==============================================================================
# 2. FUNÇÃO DE VISUALIZAÇÃO 3D (O SALTO SINÁPTICO)
# ==============================================================================
def plot_salto_sinaptico(coord_antes, coord_depois):
    x_vals = [coord_antes[0], coord_depois[0]] # Território
    y_vals = [coord_antes[1], coord_depois[1]] # Práxis
    z_vals = [coord_antes[2], coord_depois[2]] # Cognitivo

    fig = go.Figure()

    # 1. Ponto de Partida (Original)
    fig.add_trace(go.Scatter3d(
        x=[x_vals[0]], y=[y_vals[0]], z=[z_vals[0]],
        mode='markers', marker=dict(size=12, color='gray', opacity=0.6),
        name='Rascunho Inicial'
    ))

    # 2. Ponto de Chegada (SINAPSE)
    fig.add_trace(go.Scatter3d(
        x=[x_vals[1]], y=[y_vals[1]], z=[z_vals[1]],
        mode='markers', marker=dict(size=35, color='#7c3aed', symbol='diamond', opacity=0.9),
        name='Rubrica SINAPSE'
    ))

    # 3. Vetor de Evolução
    fig.add_trace(go.Scatter3d(
        x=x_vals, y=y_vals, z=z_vals,
        mode='lines', line=dict(color='#10b981', width=8),
        name='Ganho Pedagógico'
    ))

    fig.update_layout(
        scene=dict(
            xaxis=dict(title='TERRITÓRIO (Verde)', range=[0, 6], backgroundcolor='#f0fdf4'),
            yaxis=dict(title='PRÁXIS (Laranja)', range=[0, 6], backgroundcolor='#fff7ed'),
            zaxis=dict(title='COGNITIVO (Azul)', range=[0, 6], backgroundcolor='#eff6ff'),
        ),
        margin=dict(l=0, r=0, b=0, t=30),
        height=450,
        title="Volumetria da Competência (Voxel)",
        showlegend=True
    )
    return fig

# ==============================================================================
# 3. INTERFACE DE USUÁRIO
# ==============================================================================
c_logo, c_title = st.columns([1, 6])
with c_logo:
    st.image("https://img.icons8.com/fluency/96/artificial-intelligence.png", width=70)
with c_title:
    st.title("Oficina de Rubricas SINAPSE")
    st.caption("Motor: Groq Llama 3.3 (70B Versatile) | Base Teórica: Susan Brookhart (OCR)")

st.markdown("---")

with st.form("form_auditoria"):
    col1, col2 = st.columns([1, 1])
    
    with col1:
        contexto_ept = st.selectbox(
            "📂 Contexto EPT (Cenário):",
            [
                "Selecione...",
                "🌾 Práticas de Campo e Manejo (Agro/Rural)",
                "⚙️ Operação Técnica e Laboratorial (Indústria)",
                "💻 Desenvolvimento de Projetos (TI/Maker)",
                "🤝 Trabalho em Equipe e Soft Skills",
                "🗺️ Intervenção Social e Extensão",
                "🧠 Produção Teórica e Científica"
            ]
        )
    
    with col2:
        tema = st.text_input("📝 Atividade Específica:", placeholder="Ex: Poda de Café, Soldagem MIG, Algoritmo...")
    
    st.markdown("### Seu Rascunho")
    texto_rascunho = st.text_area(
        "Descreva o critério atual (O que você quer avaliar?):",
        height=120,
        placeholder="Ex: O aluno precisa entregar o relatório formatado corretamente e sem erros de português."
    )
    
    mostrar_teoria = st.checkbox("🔍 Debug: Ver Contexto Injetado")

    btn_auditar = st.form_submit_button("🚀 Auditar e Gerar Volumetria", use_container_width=True)

# ==============================================================================
# 4. LÓGICA DE PROCESSAMENTO
# ==============================================================================
if btn_auditar:
    erros = []
    if contexto_ept == "Selecione...": erros.append("Selecione um Contexto EPT.")
    if not tema: erros.append("Defina a Atividade Específica.")
    if len(texto_rascunho) < 10: erros.append("O rascunho está muito curto.")
    
    if erros:
        for e in erros: st.error(f"❌ {e}")
    else:
        api_key = st.secrets.get("GROQ_API_KEY")
        
        if not api_key:
            st.error("🔒 ERRO: Chave GROQ_API_KEY não configurada nos Segredos.")
        else:
            with st.spinner("🤖 Llama 3.3 está lendo Brookhart (2013) e auditando..."):
                try:
                    client = Groq(api_key=api_key)
                    
                    prompt_sistema = f"""
                    ATUE COMO UM CONSULTOR PEDAGÓGICO SÊNIOR (Especialista em EPT).
                    
                    === BASE DE CONHECIMENTO (BROOKHART - TEXTO OCR) ===
                    {TEORIA_BROOKHART}
                    ====================================================
                    
                    SUA MISSÃO:
                    Analise o rascunho do professor. Aplique rigorosamente a distinção entre TAREFA (Checklist) e QUALIDADE (Rubrica).
                    
                    DADOS:
                    - Contexto: {contexto_ept}
                    - Atividade: {tema}
                    - Rascunho: "{texto_rascunho}"
                    
                    SAÍDA (Responda em Português do Brasil, Markdown):
                    1. DIAGNÓSTICO CRÍTICO: Identifique se há foco em contagem/tarefa (Erro) ou qualidade (Acerto). Cite Brookhart.
                    2. REESCRITA SINAPSE: Crie um descritor "Nível Proficiente" que integre Cognitivo, Práxis e Território.
                    3. JUSTIFICATIVA: Explique a melhoria pedagógica.
                    """
                    
                    chat_completion = client.chat.completions.create(
                        messages=[
                            {"role": "system", "content": "Você é um assistente pedagógico especializado em Rubricas."},
                            {"role": "user", "content": prompt_sistema}
                        ],
                        # ATUALIZAÇÃO CRÍTICA DO MODELO:
                        # Usando a versão recomendada no seu documento 'doc_groq.txt'
                        model="llama-3.3-70b-versatile", 
                        temperature=0.3,
                        max_tokens=1500,
                    )
                    
                    resposta_ia = chat_completion.choices[0].message.content
                    
                    # Exibição
                    if mostrar_teoria:
                        with st.expander("📜 Ver Contexto Teórico Injetado"):
                            st.info(f"Tamanho do Contexto: {len(TEORIA_BROOKHART)} caracteres")
                            st.text(TEORIA_BROOKHART[:2000] + "...")
                    
                    st.success("✅ Auditoria Concluída!")
                    
                    col_txt, col_3d = st.columns([1, 1])
                    with col_txt:
                        st.subheader("📊 Relatório da Auditoria")
                        st.markdown(f"<div class='feedback-card'>{resposta_ia}</div>", unsafe_allow_html=True)
                    
                    with col_3d:
                        st.subheader("🧊 O Salto Sináptico")
                        st.caption("Visualização do ganho de competência.")
                        fig_3d = plot_salto_sinaptico((1.5, 2.0, 1.0), (5.0, 5.0, 5.0))
                        st.plotly_chart(fig_3d, use_container_width=True)
                        st.info("👆 Gire o cubo para ver a expansão.")

                except Exception as e:
                    st.error(f"Erro na comunicação com a IA: {e}")

st.markdown("---")
st.caption("Ecossistema SINAPSE-BR IA | TCC Neirivon Elias Cardoso | IFTM 2026")
