# /home/neirivon/SINAPSE2.0/sinapsebr_rubrica/scripts/pages/11_Simulador_Geofilosofico.py
# --------------------------------------------------------------------------------------
# NOME DO SCRIPT: 11_Simulador_Geofilosofico.py
# DESCRIÇÃO: Simulador interativo baseado na metáfora ferroviária da Geofilosofia,
#            integrando os eixos da Rubrica SINAPSE-BR IA (Cognitivo, Territorial, Práxis).
# FUNCIONALIDADES:
#   1. Visualização dos 3 Motores (Eixos) e seus status na "Locomotiva Tridimensional".
#   2. Simulação do "Vagão Híbrido" (Poltrona Tech vs. Praça Maker) com DUA.
#   3. Painel de Controle Docente (CCO) com métricas de "Ping" (Latência) e "Jitter".
#   4. Transposição didática visual para defesa da Dissertação e conceituação do sistema.
# AUTOR: Neirivon Elias Cardoso (Adaptado por Gemini)
# PROJETO: Rubrica SINAPSE-BR IA
# DATA: 18/01/2026
# --------------------------------------------------------------------------------------

import streamlit as st
import time
import random

# ──────────────────────────────────────────────────────────────────────────────
# CONFIGURAÇÃO DA PÁGINA
# ──────────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Simulador Ferroviário SINAPSE",
    layout="wide",
    page_icon="🚂"
)

# CSS para Estética "Jedi/Profissional"
st.markdown("""
<style>
    .stMetric {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #6c757d;
    }
    .stProgress > div > div > div > div {
        background-color: #4CAF50;
    }
    .css-1y4p8pa {
        padding-top: 1rem;
    }
    h1, h2, h3 {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
</style>
""", unsafe_allow_html=True)

# ──────────────────────────────────────────────────────────────────────────────
# CABEÇALHO E CONTEXTUALIZAÇÃO
# ──────────────────────────────────────────────────────────────────────────────
st.title("🚂 O Trem da Educação: Modelagem Geofilosófica")
st.markdown("""
**Transposição Didática:** Esta interface traduz a complexidade da **Rubrica SINAPSE-BR IA** em uma metáfora ferroviária funcional.
Aqui, a educação não é estática; é um movimento através do território (**Geofilosofia**), impulsionado por motores potentes (**Politecnia/Neurociência**) e monitorado por redes neurais (**Tecnologia**).
""")

st.divider()

# ──────────────────────────────────────────────────────────────────────────────
# NAVEGAÇÃO ENTRE CAMADAS DO SISTEMA
# ──────────────────────────────────────────────────────────────────────────────
tab1, tab2, tab3 = st.tabs([
    "⚙️ 1. Os Motores (Eixos)", 
    "🚃 2. O Vagão Híbrido (Ambiente)", 
    "📡 3. Painel CCO (Ping/Jitter)"
])

# ──────────────────────────────────────────────────────────────────────────────
# ABA 1: OS MOTORES (A ENGENHARIA DA RUBRICA)
# ──────────────────────────────────────────────────────────────────────────────
with tab1:
    st.header("A Locomotiva Tridimensional")
    st.caption("Como a Rubrica SINAPSE move o processo de aprendizagem na ferrovia do saber.")
    
    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("🧠 **Motor Frontal (TRAÇÃO)**")
        st.markdown("### Eixo COGNITIVO")
        st.write("**Função:** Visão, Planejamento e Metacognição.")
        st.write("*É o 'Farol' da IA que prevê o caminho e ilumina os trilhos.*")
        st.metric(label="Status da IA", value="Online", delta="Rota Calculada")

    with col2:
        st.warning("🌍 **Motor Central (ESTABILIDADE)**")
        st.markdown("### Eixo TERRITORIAL")
        st.write("**Função:** Identidade, Ética e 'Chão'.")
        st.write("*O coração que impede o descarrilamento nas curvas da vida.*")
        st.metric(label="Aderência ao Chão", value="100%", delta="Estável")

    with col3:
        st.error("🛠️ **Motor Traseiro (IMPULSO)**")
        st.markdown("### Eixo PRÁXIS")
        st.write("**Função:** Politecnia e Realização.")
        st.write("*Vence a inércia e sobe a ladeira do trabalho real.*")
        st.metric(label="Torque Técnico", value="Alto", delta="Empurrando")

# ──────────────────────────────────────────────────────────────────────────────
# ABA 2: O VAGÃO HÍBRIDO (SALA DE AULA INVERTIDA/DUA)
# ──────────────────────────────────────────────────────────────────────────────
with tab2:
    st.header("O Vagão SINAPSE (Ambiente de Aprendizagem)")
    st.markdown("""
    Superando a sala de aula tradicional, o vagão é dividido em dois momentos pedagógicos distintos, 
    respeitando o tempo do indivíduo (DUA) e a força do coletivo (Geofilosofia).
    """)
    
    st.markdown("---")
    
    col_poltrona, col_praca = st.columns([1, 1])
    
    with col_poltrona:
        st.subheader("💺 A Poltrona Tech (O Casulo)")
        # Simulação visual de ícone
        st.markdown("🟦 **Foco: Individual (Cognitivo)**")
        st.markdown("""
        * **Interface:** Tela Touch com IA e Fones.
        * **Ação:** O aluno estuda a teoria, revê o mapa e preenche sua **Autoavaliação (Script 07)**.
        * **Privacidade:** Espaço seguro para errar sem julgamento público.
        """)
        
        if st.button("Simular: Aluno acessando conteúdo na Poltrona"):
             with st.chat_message("assistant"):
                 st.write("Olá! Percebi que você tem interesse em Neurociência. Recomendei 3 vídeos novos na sua trilha.")
             with st.chat_message("user"):
                 st.write("Obrigado! Vou assistir antes de ir para a Praça Maker.")

    with col_praca:
        st.subheader("🏗️ A Praça Maker (O Chão)")
        # Simulação visual de ícone
        st.markdown("🟧 **Foco: Coletivo (Territorial/Práxis)**")
        st.markdown("""
        * **Interface:** Bancadas, Ferramentas, Janelas amplas para a Cidade.
        * **Ação:** Onde o "Eu" vira "Nós". Construção de projetos reais.
        * **Geofilosofia:** Olhar pela janela e conectar o projeto à comunidade local.
        """)
        
        if st.button("Simular: Grupo apresentando projeto na Praça"):
            st.success("🔨 Grupo 'Vagão Criativo' está prototipando uma solução para a antiga estação ferroviária!")

# ──────────────────────────────────────────────────────────────────────────────
# ABA 3: MONITORAMENTO (DIAGNÓSTICO TÉCNICO-PEDAGÓGICO)
# ──────────────────────────────────────────────────────────────────────────────
with tab3:
    st.header("📡 CCO: Centro de Controle Operacional")
    st.markdown("""
    Nesta visão, o docente atua como **Engenheiro de Redes**, monitorando não apenas a nota final, 
    mas a **qualidade da conexão** cognitiva e emocional do estudante durante a viagem.
    """)
    
    st.info("""
    **Conceito Técnico:**
    * **Ping (Latência):** Tempo de resposta do aluno ao estímulo. (Ping Alto = Travamento/Dificuldade).
    * **Jitter (Variação):** Instabilidade emocional/cognitiva. (Jitter Alto = Oscilação de humor/atenção).
    """)
    
    st.markdown("---")
    
    # Simulação de Dados em Tempo Real
    col_a, col_b, col_c = st.columns(3)
    
    # Aluno 1: Fluxo
    with col_a:
        st.success("##### 🟢 Aluno: João (Fluxo)")
        st.metric(label="Latência (Ping)", value="15ms", delta="- Rápido")
        st.progress(95)
        st.caption("✅ **Diagnóstico:** Sinapse fluida. O aluno responde aos estímulos imediatamente. Estado de Flow.")
    
    # Aluno 2: Dificuldade Técnica
    with col_b:
        st.warning("##### 🟡 Aluna: Maria (Bloqueio)")
        st.metric(label="Latência (Ping)", value="850ms", delta="Alto (Travado)", delta_color="inverse")
        st.progress(25)
        st.caption("⚠️ **Diagnóstico:** Alta latência no Eixo Práxis. O aluno parou na mesma tela há 20min.")
        
        if st.button("Enviar 'Ping' de Ajuda para Maria"):
            with st.spinner('Enviando suporte discreto via tela da poltrona...'):
                time.sleep(1.5)
            st.toast('Suporte enviado! O professor interveio sem expor a aluna.', icon='✅')

    # Aluno 3: Instabilidade Emocional (Jitter)
    with col_c:
        st.error("##### 🔴 Aluno: Carlos (Instabilidade)")
        # Simulando Jitter visualmente
        jitter_val = random.choice(["20ms", "400ms", "120ms", "900ms"])
        st.metric(label="Jitter (Variação)", value=jitter_val, delta="Instável", delta_color="inverse")
        st.progress(50)
        st.caption("🛑 **Diagnóstico:** Alto Jitter (Oscilação). Indica instabilidade emocional ou fadiga. Requer acolhimento antes de conteúdo.")

# ──────────────────────────────────────────────────────────────────────────────
# RODAPÉ E REFERÊNCIAS RÁPIDAS
# ──────────────────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: grey;">
    <b>Sistema SINAPSE-BR IA</b> | <i>Dissertação de Neirivon Elias Cardoso</i> | IFTM 2026<br>
    Baseado na Geofilosofia de Paulo Irineu & Pedagogia de Paulo Freire
</div>
""", unsafe_allow_html=True)
