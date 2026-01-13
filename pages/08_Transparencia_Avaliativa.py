# /home/neirivon/SINAPSE2.0/sinapsebr_rubrica/scripts/pages/08_Transparencia_Avaliativa.py
# --------------------------------------------------------------------------------------
# NOME DO SCRIPT: 08_Transparencia_Avaliativa.py
# DESCRIÇÃO: Página de Meta-Avaliação do artefato SINAPSE-BR IA.
#            Utiliza um gráfico de radar para contrastar o rigor técnico (Mullinix)
#            com o compromisso ético-social (Geofilosofia/Hospitalidade).
# FUNCIONALIDADES:
#   1. Sliders de calibragem para autoavaliação do instrumento pelo usuário.
#   2. Cálculo de Índice Híbrido (Técnico + Social).
#   3. Visualização em Radar Chart (Plotly) para identificar desequilíbrios.
#   4. Interpretação qualitativa baseada na tensão Hospitalidade vs. Hostilidade (Paulo Irineu).
# AUTOR: Neirivon Elias Cardoso (Adaptado por Gemini)
# PROJETO: Rubrica SINAPSE-BR IA
# DATA: 04/01/2026
# --------------------------------------------------------------------------------------

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np

st.set_page_config(
    page_title="Transparência Avaliativa (Híbrida)",
    page_icon="🐆",
    layout="wide"
)

# Bloqueia tradução automática
st.markdown('<meta name="google" content="notranslate">', unsafe_allow_html=True)

# --- TÍTULO E CONCEITO (ATUALIZADO: GEOFILOSOFIA) ---
st.title("🐆 Transparência Avaliativa: A Ética da Hospitalidade")

st.markdown("""
Esta página materializa o princípio da **Meta-Avaliação Geofilosófica**.
Inspirado na tese de **Paulo Irineu**, este painel investiga a natureza do instrumento avaliativo:
ele opera como um mecanismo de **hostilidade** (frio, excludente e puramente técnico) ou
se constitui como um território de **hospitalidade** (acolhedor, situado e ético)?

Aqui, submetemos a Rubrica SINAPSE-BR IA a um duplo escrutínio:
* **A Precisão Técnica (Mullinix):** Clareza e confiabilidade dos critérios.
* **O Compromisso Ético (Geofilosofia):** Sensibilidade ao território e à interseccionalidade.

**Objetivo:** Garantir que a avaliação seja um **ponto de encontro**, não de exclusão.
""")

st.divider()

# --- FORMULÁRIO DE AVALIAÇÃO (LATERAL) ---
with st.sidebar:
    st.header("🎚️ Painel de Calibragem")
    st.caption("Avalie o Artefato SINAPSE nas seguintes dimensões (Escala 1-4):")
    
    st.subheader("1. Dimensão Técnica (Mullinix)")
    tec_clareza = st.slider("Clareza dos Critérios", 1, 4, 3, help="Os critérios são inequívocos? (Base: Mullinix)")
    tec_confiabilidade = st.slider("Confiabilidade", 1, 4, 3, help="Diferentes avaliadores chegariam à mesma nota?")
    tec_metacognicao = st.slider("Apoio à Metacognição", 1, 4, 4, help="Estimula o aluno a pensar sobre o aprender?")
    
    st.subheader("2. Dimensão Ética (Geofilosofia)")
    soc_territorio = st.slider("Sensibilidade Territorial", 1, 4, 4, help="Considera as disparidades do TMAP (Rural/Urbano)?")
    soc_interseccional = st.slider("Interseccionalidade", 1, 4, 4, help="Cruza Classe (INSE) com Acesso e Identidade?")
    soc_equidade = st.slider("Hospitalidade/Acolhimento", 1, 4, 4, help="A ferramenta acolhe a diversidade ou impõe barreiras?")

# --- CÁLCULO HÍBRIDO ---
# Médias
media_tec = np.mean([tec_clareza, tec_confiabilidade, tec_metacognicao])
media_soc = np.mean([soc_territorio, soc_interseccional, soc_equidade])
media_global = (media_tec + media_soc) / 2

# Lógica Qualitativa (Conceito)
if media_global >= 3.8:
    conceito = "Nível 4: Referência (Hospitalidade Plena)"
    cor_conceito = "#22c55e" # Verde
    msg = "A rubrica atinge o estado da arte, unindo rigor técnico e compromisso ético profundo."
elif media_global >= 3.0:
    conceito = "Nível 3: Consolidado"
    cor_conceito = "#3b82f6" # Azul
    msg = "A rubrica é sólida e clara, cumprindo seu papel formativo com segurança."
elif media_global >= 2.0:
    conceito = "Nível 2: Em Desenvolvimento"
    cor_conceito = "#facc15" # Amarelo
    msg = "Atenção: A ferramenta pode estar pendendo para a hostilidade técnica ou fragilidade teórica."
else:
    conceito = "Nível 1: Em Reestruturação"
    cor_conceito = "#ef4444" # Vermelho
    msg = "Crítico: O instrumento necessita revisão profunda para não gerar exclusão."

# --- EXIBIÇÃO DOS RESULTADOS (COLUNAS) ---
col_grafico, col_parecer = st.columns([1.5, 1])

with col_grafico:
    st.subheader("📊 Radar da Sinergia Educacional")
    
    categories = [
        'Clareza (Téc)', 'Confiabilidade (Téc)', 'Metacognição (Téc)',
        'Território (Ética)', 'Interseccionalidade (Ética)', 'Hospitalidade (Ética)'
    ]
    values = [
        tec_clareza, tec_confiabilidade, tec_metacognicao,
        soc_territorio, soc_interseccional, soc_equidade
    ]
    
    # Fechar o ciclo do gráfico
    values += values[:1]
    categories += categories[:1]

    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name='SINAPSE-BR IA',
        line_color='#ea580c'
    ))

    # Adiciona uma linha de "Referência Ideal" (Nível 4)
    fig.add_trace(go.Scatterpolar(
        r=[4]*7,
        theta=categories,
        name='Ideal (Mullinix/Irineu)',
        line_color='#94a3b8',
        line_dash='dot',
        hoverinfo='none'
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 4.5], tickvals=[1,2,3,4])
        ),
        showlegend=True,
        height=500,
        margin=dict(l=40, r=40, t=20, b=20)
    )
    
    st.plotly_chart(fig, use_container_width=True)

with col_parecer:
    st.subheader("📝 Parecer Meta-Avaliativo")
    
    # Card do Conceito
    st.markdown(f"""
    <div style="background-color: #f8fafc; border-left: 6px solid {cor_conceito}; padding: 20px; border-radius: 5px; box-shadow: 2px 2px 10px rgba(0,0,0,0.1);">
        <h2 style="margin:0; color: {cor_conceito};">{media_global:.2f} / 4.0</h2>
        <h3 style="margin:5px 0; color: #334155;">{conceito}</h3>
        <p style="margin-top:10px; font-style: italic; color: #475569;">"{msg}"</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    # Detalhamento
    st.markdown("### 🔎 Diagnóstico por Eixo")
    
    # Eixo Técnico
    delta_tec = media_tec - 3.0
    st.metric("Maturidade Técnica (Mullinix)", f"{media_tec:.2f}", delta=f"{delta_tec:.2f}", 
              help="Média dos critérios de engenharia pedagógica.")
    
    # Eixo Social
    delta_soc = media_soc - 3.0
    st.metric("Índice de Hospitalidade (Geofilosofia)", f"{media_soc:.2f}", delta=f"{delta_soc:.2f}",
              help="Média dos critérios de ética, território e acolhimento.")
    
    # Interpretação Geofilosófica (CORRIGIDA)
    st.info("""
    **Interpretação Geofilosófica:**
    
    O SINAPSE busca um "polígono cheio" e equilibrado.
    
    Se houver desequilíbrio (ex: muita técnica, pouca ética), a ferramenta **perde sua "hospitalidade" e recai na hostilidade sistêmica** (Paulo Irineu).
    
    O objetivo não é apenas medir, mas garantir que a avaliação seja um **território de acolhimento** (Praxis).
    """)

# --- RODAPÉ DIDÁTICO ---
st.markdown("---")
with st.expander("🧠 Fundamentação deste Instrumento"):
    st.markdown("""
    Esta página aplica o conceito de **Meta-Avaliação** (avaliar a avaliação).
    * **Escala 1-4:** Baseada em **Mullinix (2003)** para rubricas de qualidade.
    * **Dimensões Éticas:** Baseadas na **Geofilosofia (Paulo Irineu)** e **Interseccionalidade (Crenshaw)**.
    * **Visualização:** O gráfico de radar permite identificar se o artefato pende para o tecnicismo (hostilidade) ou para a práxis social (hospitalidade).
    """)

# --- SIDEBAR GLOBAL ---
with st.sidebar:
    st.divider()
    st.page_link("Apresentacao.py", label="🏠 Apresentação")
    st.page_link("pages/01_TMAP_2010.py", label="⏳ TMAP Histórico")
    st.page_link("pages/02_TMAP_2017_2024.py", label="🌐 TMAP 2024 (Equidade)")
    st.page_link("pages/03_Mapa_Geral_Rubrica.py", label="🧠 Mapa da Rubrica")
    st.page_link("pages/04_Mapa_Fundamentacao_Teorica.py", label="📚 Fundamentação")
    st.page_link("pages/05_Meta_Rubrica_3D.py", label="🌌 Meta-Rubrica 3D")
    st.page_link("pages/06_Rubrica_Docente_3D.py", label="👩‍🏫 Rubrica Docente 3D")
    st.page_link("pages/07_Rubrica_Autoavaliativa_3D.py", label="🎓 Autoavaliação 3D")
    st.page_link("pages/08_Transparencia_Avaliativa.py", label="🐆 Transparência (Avaliação)")
    st.page_link("pages/99_Referencias.py", label="📚 Referências")
