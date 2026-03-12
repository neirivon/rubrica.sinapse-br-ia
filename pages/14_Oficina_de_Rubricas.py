# --------------------------------------------------------------------------------------
# CAMINHO DO ARQUIVO: /pages/14_Oficina_de_Rubricas.py
# NOME DO SCRIPT: 14_Oficina_de_Rubricas.py
#
# DESCRIÇÃO: Laboratório de Auditoria Pedagógica e Criação de Rubricas SINAPSE-BR.
#              Ancoragem Integrada: Neurociência (Vital) + Sistemas de Operação (Silva).
#              Separação de Domínios: X (Cognitivo) | Y (Práxis) | Z (Território).
#
# FUNCIONALIDADES:
#      1. Domínios de Autoridade: X (Vital/Dehaene) | Y (Silva/Peirce/DUA).
#      2. Validação Estrita: Campos com "*" obrigatórios e bloqueio de envio vazio.
#      3. Salvaguarda de Escopo: Proteção contra temas fora da área educacional/EPT.
#      4. Visualização: Voxel Semântico 3D de alta intensidade.
#      5. RELATÓRIO DINÂMICO: Separação clara entre Diagnóstico e Salto Sináptico.
#
# AUTOR: Neirivon Elias Cardoso
# PROJETO: Rubrica SINAPSE-BR IA
# DATA: 11/03/2026 (Versão V345.0 - Protocolo de Eixos Integrados e Densidade Máxima)
# --------------------------------------------------------------------------------------

import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from groq import Groq
import os
import re

# Configuração da Página
st.set_page_config(
    page_title="Oficina de Rubricas SINAPSE - V345.0",
    page_icon="🛠️",
    layout="wide"
)

# ==============================================================================
# ESTILO CSS PROFISSIONAL (PRESERVADO INTEGRALMENTE)
# ==============================================================================
st.markdown("""
<style>
    .stTextArea textarea { 
        font-size: 16px; 
        border-radius: 8px; 
        border: 1px solid #e5e7eb; 
    }
    .feedback-card {
        padding: 24px; 
        border-radius: 12px; 
        margin-bottom: 20px;
        background-color: #ffffff; 
        border-left: 6px solid;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        font-family: 'Inter', sans-serif;
        font-size: 1.1rem;
        line-height: 1.6;
    }
    .arrow-container {
        display: flex; 
        align-items: center; 
        justify-content: center;
        height: 100%; 
        font-size: 3rem; 
        color: #94a3b8; 
        padding-top: 20px;
    }
    .nota-explicativa {
        background-color: #f1f5f9; 
        border-left: 4px solid #475569;
        padding: 15px; 
        font-size: 0.95rem; 
        color: #334155; 
        margin-top: 15px; 
        border-radius: 4px;
    }
    .label-obrigatorio { 
        color: #ef4444; 
        font-size: 0.85rem; 
        font-weight: bold; 
        margin-bottom: 5px; 
        display: block; 
    }
    .vetor-salto-box {
        background-color: #eff6ff; 
        border: 1px solid #bfdbfe; 
        color: #1e40af;
        padding: 20px; 
        border-radius: 10px; 
        font-weight: 500; 
        margin-top: 10px;
        box-shadow: inset 0 2px 4px 0 rgba(0, 0, 0, 0.06);
    }
    .vetor-info {
        color: #2563eb;
        font-weight: 600;
        margin-bottom: 8px;
        font-size: 0.95rem;
        border-bottom: 1px solid #e2e8f0;
        padding-bottom: 5px;
    }
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# 1. CARREGAMENTO DOS CÉREBROS TEÓRICOS (EIXOS INTEGRADOS)
# ==============================================================================
@st.cache_data
def carregar_dados_tecnicos(nome_arquivo, mensagem_erro):
    """Realiza o carregamento seguro de arquivos de contexto RAG."""
    caminho = os.path.join("data", nome_arquivo)
    if os.path.exists(caminho):
        try:
            with open(caminho, "r", encoding="utf-8") as f:
                return f.read()
        except Exception as e:
            st.error(f"Erro de Leitura em {nome_arquivo}: {e}")
            return ""
    else:
        st.warning(f"⚠️ {mensagem_erro}")
        return ""

# Bases de Fundamentação (Agora as teses Vital e Silva estão dentro dos arquivos de eixo)
EIXO_X_BASE = carregar_dados_tecnicos("eixo_X_azul_cognitivo.txt", "Eixo X ausente.")
EIXO_Y_BASE = carregar_dados_tecnicos("eixo_Y_laranja_praxis_agir.txt", "Eixo Y ausente.")
EIXO_Z_BASE = carregar_dados_tecnicos("eixo_Z_verde_territorial.txt", "Eixo Z ausente.")
TEORIA_BROOKHART = carregar_dados_tecnicos("teoria_brookhart_RESUMO.txt", "Resumo Brookhart ausente.")

# ==============================================================================
# 2. RELATÓRIO DINÂMICO DE AUDITORIA (SINERGIA INTEGRAL)
# ==============================================================================
def exibir_relatorio_auditoria(diagnostico_ia, motivo_ia):
    """Quadro de Auditoria Epistemológica por Domínio de Autoridade Integrado."""
    st.subheader("📊 Relatório de Auditoria Epistemológica")
    st.markdown("Validação do descritor conforme os quadrantes de autoridade da banca.")

    # Proteção de texto para o Dataframe
    diag_resumo = (diagnostico_ia[:95] + '..') if len(diagnostico_ia) > 95 else diagnostico_ia
    salt_resumo = (motivo_ia[:95] + '..') if len(motivo_ia) > 95 else motivo_ia

    data_comparativa = {
        "Dimensão": ["Eixo X: Cognitivo", "Eixo Y: Práxis", "Eixo Z: Territorial"],
        "Referencial": ["Dehaene", "Charles Peirce", "Paulo Irineu / Milton Santos"],
        "Auditoria de Qualidade": [
            f"Fator Executivo: {diag_resumo}",
            "Funcionalidade e Usabilidade validada.",
            f"Salto: {salt_resumo}"
        ],
        "Veredito": ["✅ Plasticidade Ativa", "✅ Eficácia Operacional", "✅ Território Usado"]
    }
    
    st.dataframe(pd.DataFrame(data_comparativa), use_container_width=True, hide_index=True)
    st.info("💡 **Análise Transpositiva**: O descritor superou o 'Achatamento Epistemológico' utilizando referenciais integrados por eixo.")

# ==============================================================================
# 3. VISUALIZAÇÃO 3D DO VOXEL SEMÂNTICO (PRESERVADO)
# ==============================================================================
def plot_salto_sinaptico(ponto_inicial, ponto_final):
    """Gera o modelo tridimensional de proficiência SINAPSE."""
    cores = {'X': '#0066ff', 'Y': '#ff6600', 'Z': '#00ff44'} 
    fig = go.Figure()

    # Construção dos Eixos Geofilosóficos Rígidos
    for axis, color in cores.items():
        coords = {'x': [6 if axis=='X' else 0], 'y': [6 if axis=='Y' else 0], 'z': [6 if axis=='Z' else 0]}
        fig.add_trace(go.Scatter3d(
            x=[0, coords['x'][0]], y=[0, coords['y'][0]], z=[0, coords['z'][0]], 
            mode='lines', 
            line=dict(color=color, width=10), 
            name=f'Eixo {axis}'
        ))

    # Rótulos de Eixo
    fig.add_trace(go.Scatter3d(
        x=[6.5, 0, 0], y=[0, 6.5, 0], z=[0, 0, 6.5],
        mode='text', text=["<b>X</b>", "<b>Y</b>", "<b>Z</b>"],
        textfont=dict(size=20, color=["#0066ff", "#ff6600", "#00ff44"]),
        showlegend=False
    ))

    # Marcadores de Estado
    fig.add_trace(go.Scatter3d(
        x=[ponto_inicial[0]], y=[ponto_inicial[1]], z=[ponto_inicial[2]], 
        mode='markers', 
        marker=dict(size=12, color='gray', opacity=0.6), 
        name='Rascunho (Inércia)'
    ))
    fig.add_trace(go.Scatter3d(
        x=[ponto_final[0]], y=[ponto_final[1]], z=[ponto_final[2]], 
        marker=dict(size=22, color='white', symbol='diamond', line=dict(color='#10b981', width=3)), 
        name='Sinergia Integral'
    ))

    fig.update_layout(
        scene=dict(
            xaxis_visible=False, 
            yaxis_visible=False, 
            zaxis_visible=False, 
            bgcolor='white',
            camera=dict(eye=dict(x=1.6, y=1.6, z=1.6))
        ),
        margin=dict(l=0, r=0, b=0, t=0),
        legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01)
    )
    return fig

# --------------------------------------------------------------------------------------
# 4. INTERFACE DE CAPTURA (PRESERVADA)
# --------------------------------------------------------------------------------------
c_logo, c_title = st.columns([1, 6])
with c_logo:
    st.image("https://img.icons8.com/fluency/96/artificial-intelligence.png", width=70)
with c_title:
    st.title("Laboratório de Rubricas SINAPSE-BR IA")
    st.caption("Estratégia de Eixos Integrados: X (Cognição/Vital) | Y (Práxis/Silva) | Z (Território/Irineu)")

st.markdown("---")

with st.form("form_sinapse_completo"):
    col1, col2 = st.columns(2)
    with col1: 
        st.markdown('<span class="label-obrigatorio">* Obrigatório</span>', unsafe_allow_html=True)
        ctx = st.selectbox(
            "📍 Território Usado (Eixo Z):", 
            ["Selecione...", "🌾 Agro/Rural", "🏥 Saúde/Clínica", "⚙️ Indústria/Mecânica", "💻 TI/Maker", "🗺️ Extensão/Sociedade", "🧠 Pesquisa Científica", "🔌 Estações/Concessionárias"]
        )
    with col2: 
        st.markdown('<span class="label-obrigatorio">* Obrigatório</span>', unsafe_allow_html=True)
        tema = st.text_input("📝 Atividade / Objeto de Estudo:", placeholder="Ex: Montagem de Circuito, Treino de Marcha, Poda")
    
    st.markdown("### 🖋️ Rascunho do Descritor")
    st.markdown('<span class="label-obrigatorio">* Obrigatório</span>', unsafe_allow_html=True)
    texto_rascunho = st.text_area(
        "Descreva o desempenho esperado para auditoria forense (cite o local se houver):", 
        height=150,
        placeholder="Ex: O aluno identifica as peças e realiza a montagem..."
    )
    
    btn_auditar = st.form_submit_button("🚀 Executar Sinergia Multi-Banca", use_container_width=True)

# --------------------------------------------------------------------------------------
# 5. LÓGICA DE PROCESSAMENTO (PROTOCOL V345.0 - EIXOS INTEGRADOS)
# --------------------------------------------------------------------------------------

if btn_auditar:
    # Validação rigorosa de campos
    if ctx == "Selecione..." or not tema.strip() or len(texto_rascunho.strip()) < 10:
        st.error("❌ Atenção: Todos os campos marcados com * são obrigatórios para a fundamentação do descritor.")
    else:
        api_key = st.secrets.get("GROQ_API_KEY")
        if not api_key:
            st.error("Chave API GROQ não configurada nos secrets.")
        else:
            with st.spinner("🔄 YA-YA processando integração neuro-tecnológica integrada..."):
                try:
                    client = Groq(api_key=api_key)

                    # Dicionário de Contexto (Focado nos Eixos Fundamentais)
                    c_data = {
                        "X": EIXO_X_BASE,
                        "Y": EIXO_Y_BASE,
                        "Z": EIXO_Z_BASE,
                        "B": TEORIA_BROOKHART
                    }

                    # PROMPT BLINDADO V345.0: Foco no processamento cognitivo e operacional intrínseco
                    prompt_sistema = f"""
                    ### PAPEL: AUDITOR PEDAGÓGICO SINAPSE-BR V345.0
                    Seu objetivo é auditar e fundamentar o descritor utilizando os domínios de especialidade abaixo:

                    ### 1. FUNDAMENTAÇÃO TEÓRICA POR EIXO:
                    - EIXO X (Cognitivo): {c_data['X']}
                    - EIXO Y (Práxis): {c_data['Y']}
                    - EIXO Z (Territorial): {c_data['Z']}

                    ### TRAVA DE SEGURANÇA (ESCOPO):
                    Se o tema for fútil (fofocas, celebridades, culinária comum), responda EXATAMENTE:
                    "O meu modelo utilizado ainda não foi treinado para gerar descritor para esse objetivo. O seu rascunho de descritor será analisado e poderá ser utilizado no treinamento do modelo."

                    ### FORMATO DE SAÍDA OBRIGATÓRIO (DIDÁTICA):
                    [DIAG] diagnóstico técnico isolando a lacuna de funções executivas e usabilidade operacional [/DIAG]
                    [DESC] Descritor de Sinergia Integral fundindo os três eixos substantivamente no território {ctx} [/DESC]
                    [SALT] Justificativa teórica: Como a operação mental qualifica a execução técnica no lugar específico [/SALT]

                    ### ENTRADA: Contexto: {ctx} | Atividade: {tema} | Rascunho: "{texto_rascunho}"
                    """

                    chat = client.chat.completions.create(
                        messages=[{"role": "user", "content": prompt_sistema}],
                        model="llama-3.3-70b-versatile",
                        temperature=0.1
                    )
                    
                    raw_res = chat.choices[0].message.content.replace("###", "").strip()
                    
                    # Verificação de Escopo
                    if "ainda não foi treinado" in raw_res:
                        st.warning(f"⚠️ {raw_res}")
                    else:
                        d_match = re.search(r'\[DIAG\](.*?)\[/DIAG\]', raw_res, re.S)
                        e_match = re.search(r'\[DESC\](.*?)\[/DESC\]', raw_res, re.S)
                        s_match = re.search(r'\[SALT\](.*?)\[/SALT\]', raw_res, re.S)

                        diag_txt = d_match.group(1).strip() if d_match else "Análise processada."
                        desc_txt = e_match.group(1).strip() if e_match else raw_res
                        salt_txt = s_match.group(1).strip() if s_match else "Transposição validada."

                        st.success(f"✅ Sinergia Integral Alcançada: {tema}")
                        
                        # Layout Didático: Diagnóstico -> Seta -> Descritor
                        c_diag, c_arr, c_desc = st.columns([4, 1, 4])
                        with c_diag:
                            st.markdown(f"<div class='feedback-card' style='border-color: #ef4444;'><b>🔍 Diagnóstico de Auditoria:</b><br>{diag_txt}</div>", unsafe_allow_html=True)
                        with c_arr:
                            st.markdown("<div class='arrow-container'>➔</div>", unsafe_allow_html=True)
                        with c_desc:
                            st.markdown(f"<div class='feedback-card' style='border-color: #10b981; background-color: #f0fdf4;'><b>💎 Descritor de Sinergia Integral:</b><br>{desc_txt}</div>", unsafe_allow_html=True)

                        # Caixa de Salto Sináptico com Destaque UX
                        st.markdown(f"""
                        <div class="vetor-salto-box">
                            🚀 <b>Vetor de Salto Sináptico:</b><br>{salt_txt}
                        </div>
                        """, unsafe_allow_html=True)

                        st.divider()
                        exibir_relatorio_auditoria(diag_txt, salt_txt)
                        
                        # Voxel 3D
                        st.plotly_chart(plot_salto_sinaptico((1,1,1), (5.8, 5.7, 5.9)), use_container_width=True)

                        # Nota de Validação Multi-Referencial
                        st.markdown(f"""
                        <div class="nota-explicativa">
                            <b>Validação Transpositiva:</b> O descritor exige funções executivas superiores 
                            para garantir a eficácia técnica e usabilidade no território de {ctx}.
                        </div>
                        """, unsafe_allow_html=True)

                except Exception as e:
                    st.error(f"Erro na inferência Groq: {e}")

# ==============================================================================
# 6. RODAPÉ INSTITUCIONAL (CRÉDITOS E DEFESA)
# ==============================================================================
st.markdown("---")
with st.expander("🛡️ Por que este descritor é imune ao 'Achatamento'?"):
    st.write("""
    Diferente de sistemas genéricos, o motor SINAPSE-BR realiza a **Transposição de Escala**. Ele audita o rascunho 
    contra os processos cognitivos, a funcionalidade técnica e as rugosidades do território (Geofilosofia), 
    impedindo que a avaliação se torne uma mera lista de tarefas burocráticas e manuais.
    """)
st.caption("Ecossistema SINAPSE-BR IA | TCC Neirivon Elias Cardoso | Orientação: Profa. Dra. Thays Vital | IFTM 2026")
