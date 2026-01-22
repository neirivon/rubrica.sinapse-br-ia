# /home/neirivon/SINAPSE2.0/sinapsebr_rubrica/scripts/pages/08_Transparencia_Avaliativa.py
# --------------------------------------------------------------------------------------
# NOME DO SCRIPT: 08_Transparencia_Avaliativa.py
# DESCRIÇÃO: Página de Meta-Avaliação do artefato SINAPSE-BR IA.
#            Utiliza a metodologia HÍBRIDA de Mullinix (2003): Quali (Descritores) + Quanti (Scoring).
# FUNCIONALIDADES:
#   1. Sliders baseados nos 5 critérios de Mullinix + 1 Critério Ético (Hospitalidade).
#   2. Cálculo de Score Total (Soma) como na ferramenta original de Mullinix.
#   3. Diagnóstico Automático (Needs Improvement -> Exemplary).
# AUTOR: Neirivon Elias Cardoso
# DATA: 20/01/2026
# --------------------------------------------------------------------------------------

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(
    page_title="Meta-Avaliação (Mullinix)",
    page_icon="⚖️",
    layout="wide"
)

# --- CABEÇALHO ---
st.title("⚖️ Meta-Avaliação do Sistema SINAPSE")
st.markdown("""
Esta ferramenta realiza a **validação técnica** da própria rubrica, seguindo rigorosamente 
o instrumento *'Rubric for Assessing Rubrics'* da **Dra. Bonnie B. Mullinix (2003)**.
""")

st.info("ℹ️ **Metodologia Híbrida:** Assim como na obra original, atribuímos pesos (1-4) para gerar um diagnóstico final de qualidade.")

# --- COLUNAS DE AVALIAÇÃO (CRITÉRIOS DE MULLINIX) ---
c1, c2 = st.columns([1, 1])

with c1:
    st.subheader("1. Critérios Técnicos (Mullinix)")
    
    clareza = st.slider(
        "1. Clareza dos Critérios", 
        1, 4, 3, 
        help="1=Confuso | 4=Critérios distintos, claros e apropriados."
    )
    
    distincao = st.slider(
        "2. Distinção entre Níveis", 
        1, 4, 4, 
        help="1=Sem distinção | 4=Progressão clara e lógica entre níveis."
    )
    
    confiabilidade = st.slider(
        "3. Confiabilidade (Reliability)", 
        1, 4, 3, 
        help="1=Inconsistente | 4=Diferentes avaliadores chegam à mesma nota."
    )

with c2:
    st.subheader("2. Impacto Pedagógico & Ético")
    
    metacognicao = st.slider(
        "4. Apoio à Metacognição", 
        1, 4, 4, 
        help="1=Não ajuda | 4=Ajuda o aluno a entender COMO aprende."
    )
    
    engajamento = st.slider(
        "5. Envolvimento do Aluno", 
        1, 4, 3, 
        help="1=Passivo | 4=Aluno co-constrói ou usa para autoavaliação."
    )
    
    # Critério Extra: Geofilosofia (O diferencial do seu TCC)
    hospitalidade = st.slider(
        "6. Ética da Hospitalidade (Fernandes)", 
        1, 4, 4, 
        help="1=Excludente | 4=Território de acolhimento e equidade."
    )

# --- CÁLCULO DO SCORE (LÓGICA MULLINIX) ---
# Mullinix usa soma simples. Como temos 6 critérios (ela usa 5 ou 6 dependendo da versão),
# o máximo é 24 pontos.
total_score = clareza + distincao + confiabilidade + metacognicao + engajamento + hospitalidade

# Definição das Faixas de Diagnóstico (Baseado na imagem enviada)
# 0-10: Needs Improvement
# 11-15: Workable
# 16-20: Solid/Good
# 21-24: Exemplary

diagnostico = ""
cor_diag = ""
icone = ""

if total_score <= 10:
    diagnostico = "NEEDS IMPROVEMENT (Precisa Melhorar)"
    cor_diag = "inverse" # Vermelho/Preto
    icone = "🚨"
elif total_score <= 15:
    diagnostico = "WORKABLE (Funcional/Aceitável)"
    cor_diag = "off" # Cinza/Amarelo
    icone = "⚠️"
elif total_score <= 20:
    diagnostico = "SOLID / GOOD (Sólido/Bom)"
    cor_diag = "normal" # Verde claro
    icone = "✅"
else:
    diagnostico = "EXEMPLARY (Exemplar/Estado da Arte)"
    cor_diag = "normal" # Verde forte (no toast/sucesso usamos success)
    icone = "🏆"

# --- EXIBIÇÃO DO RESULTADO ---
st.divider()
c_res1, c_res2 = st.columns([2, 3])

with c_res1:
    st.metric(label="SCORE TOTAL (Mullinix)", value=f"{total_score} / 24")
    
    if total_score > 20:
        st.success(f"### {icone} {diagnostico}")
        st.caption("A rubrica atinge o nível máximo de qualidade psicométrica e pedagógica.")
    elif total_score > 15:
        st.info(f"### {icone} {diagnostico}")
    else:
        st.warning(f"### {icone} {diagnostico}")

with c_res2:
    # Gráfico de Radar para visualizar o equilíbrio
    categories = ['Clareza', 'Distinção', 'Confiabilidade', 'Metacognição', 'Engajamento', 'Hospitalidade']
    
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=[clareza, distincao, confiabilidade, metacognicao, engajamento, hospitalidade],
        theta=categories,
        fill='toself',
        name='SINAPSE-BR IA'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 4])
        ),
        showlegend=False,
        height=350,
        margin=dict(l=40, r=40, t=20, b=20)
    )
    st.plotly_chart(fig, use_container_width=True)

# --- RODAPÉ COM A FONTE EXATA ---
st.markdown("---")
with st.expander("📚 Fonte de Validação"):
    st.markdown("""
    **Referência Base:**
    * **Autora:** Dr. Bonnie B. Mullinix (Monmouth University, 2003).
    * **Instrumento:** *Rubric for Assessing Rubrics*.
    * **Lógica de Scoring:**
        * 0 - 10 = Needs Improvement
        * 11 - 15 = Workable
        * 16 - 20 = Solid/Good
        * **21 - 24 = Exemplary** (Meta do SINAPSE)
    """)
