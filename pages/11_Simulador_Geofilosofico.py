# /home/neirivon/SINAPSE2.0/sinapsebr_rubrica/scripts/pages/11_Simulador_Geofilosofico.py
# --------------------------------------------------------------------------------------
# NOME DO SCRIPT: 11_Simulador_Geofilosofico.py
# DESCRIÇÃO: Simulador interativo baseado na metáfora ferroviária da Geofilosofia,
#            integrando os eixos da Rubrica SINAPSE-BR IA com a ética da Hospitalidade
#            (Fernandes, 2023) e a equidade territorial.
# FUNCIONALIDADES:
#   1. Visualização dos 3 Motores: Cognitivo, Territorial (Hospitalidade) e Práxis.
#   2. Simulação do "Vagão Híbrido" (Poltrona Tech vs. Praça Maker/Terra de Todos).
#   3. Painel de Controle Docente (CCO) com métricas de Latência e Acolhimento.
#   4. Transposição didática visual para defesa da Dissertação.
# AUTOR: Neirivon Elias Cardoso
# PROJETO: Rubrica SINAPSE-BR IA
# DATA: 20/01/2026
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

# CSS para Estética "Jedi/Profissional" e Acessibilidade (Alto Contraste)
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
    .big-font {
        font-size:18px !important;
        color: #31333F;
    }
</style>
""", unsafe_allow_html=True)

# ──────────────────────────────────────────────────────────────────────────────
# CABEÇALHO E CONTEXTUALIZAÇÃO
# ──────────────────────────────────────────────────────────────────────────────
st.title("🚂 O Trem da Educação: Modelagem Geofilosófica")
st.markdown("""
<div class='big-font'>
<b>Transposição Didática:</b> Esta interface traduz a <b>Rubrica SINAPSE-BR IA</b> em uma metáfora ferroviária.
Aqui, o território (TMAP) não é apenas um mapa, mas uma <i>"Terra de (e para) todos"</i> (FERNANDES, 2023),
onde a tecnologia serve à <b>Hospitalidade</b> e ao acolhimento da diversidade cognitiva.
</div>
""", unsafe_allow_html=True)

st.divider()

# ──────────────────────────────────────────────────────────────────────────────
# NAVEGAÇÃO ENTRE CAMADAS DO SISTEMA
# ──────────────────────────────────────────────────────────────────────────────
tab1, tab2, tab3 = st.tabs([
    "⚙️ 1. Os Motores (Eixos)", 
    "🚃 2. O Vagão Híbrido (Ambiente)", 
    "📡 3. Painel CCO (Diagnóstico)"
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
        st.write("**Função:** Metacognição e Neuropsicopedagogia.")
        st.write("*O 'Farol' da IA que respeita o ritmo neural de cada aluno.*")
        st.metric(label="Status da IA", value="Online", delta="Rota Personalizada")

    with col2:
        st.warning("🌍 **Motor Central (ESTABILIDADE)**")
        st.markdown("### Eixo TERRITORIAL")
        st.write("**Função:** Geofilosofia e Hospitalidade.")
        st.write("*A ética que garante que o trem seja uma 'Terra para Todos'.*")
        st.metric(label="Índice de Hospitalidade", value="100%", delta="Acolhedor")

    with col3:
        st.error("🛠️ **Motor Traseiro (IMPULSO)**")
        st.markdown("### Eixo PRÁXIS")
        st.write("**Função:** Politecnia e Mundo do Trabalho.")
        st.write("*Vence a inércia, transformando teoria em produto real.*")
        st.metric(label="Torque Técnico", value="Alto", delta="Transformador")

# ──────────────────────────────────────────────────────────────────────────────
# ABA 2: O VAGÃO HÍBRIDO (SALA DE AULA INVERTIDA/DUA)
# ──────────────────────────────────────────────────────────────────────────────
with tab2:
    st.header("O Vagão SINAPSE: Um Território de Acolhimento")
    st.markdown("""
    Superando a sala de aula tradicional, o vagão é um espaço de **Hospitalidade Técnica**. 
    Ele permite o isolamento necessário para a reflexão (Poltrona) e a comunhão necessária para a cidadania (Praça).
    """)
    
    st.markdown("---")
    
    col_poltrona, col_praca = st.columns([1, 1])
    
    with col_poltrona:
        st.subheader("💺 A Poltrona Tech (O Eu)")
        st.markdown("🟦 **Foco: Neuropsicopedagógico (Individual)**")
        st.markdown("""
        * **Conceito:** O refúgio seguro. Onde o aluno encontra seu ritmo (DUA).
        * **Ação:** Autoavaliação sem exposição. O erro é tratado como dado, não como falha.
        * **Tecnologia:** IA adaptativa que dialoga com a singularidade do sujeito.
        """)
        
        if st.button("Simular: Acolhimento Individual na Poltrona"):
             with st.chat_message("assistant"):
                 st.write("Olá! Notei que você prefere explicações visuais. Preparei um infográfico sobre o TMAP especialmente para você.")
             with st.chat_message("user"):
                 st.write("Isso ajuda muito. Sinto-me mais seguro para ir à Praça agora.")

    with col_praca:
        st.subheader("🏗️ A Praça Maker (O Nós)")
        st.markdown("🟧 **Foco: Geofilosófico (Coletivo)**")
        st.markdown("""
        * **Conceito:** *"Uma terra de (e para) todos"*. Onde a diversidade se encontra.
        * **Ação:** Projetos que resolvem problemas reais do Triângulo Mineiro.
        * **Meta:** A construção do território existencial através do trabalho colaborativo.
        """)
        
        if st.button("Simular: Dinâmica de Grupo na Praça"):
            st.success("🔨 Grupo 'Vagão Criativo' está desenvolvendo uma solução sustentável para a comunidade local, integrando saberes.")

# ──────────────────────────────────────────────────────────────────────────────
# ABA 3: MONITORAMENTO (DIAGNÓSTICO TÉCNICO-PEDAGÓGICO)
# ──────────────────────────────────────────────────────────────────────────────
with tab3:
    st.header("📡 CCO: Centro de Controle Operacional")
    st.markdown("""
    Nesta visão, o docente atua como um **Gestor de Hospitalidade**, monitorando não apenas notas, 
    mas a **qualidade da conexão humana** e os sinais de exclusão territorial.
    """)
    
    st.info("""
    **Glossário do Sistema SINAPSE:**
    * **Ping (Latência):** Tempo de resposta. (Alto = Dificuldade cognitiva ou técnica).
    * **Jitter (Variação):** Instabilidade emocional. (Alto = Ansiedade/Necessidade de Acolhimento).
    """)
    
    st.markdown("---")
    
    # Simulação de Dados em Tempo Real
    col_a, col_b, col_c = st.columns(3)
    
    # Aluno 1: Fluxo
    with col_a:
        st.success("##### 🟢 Aluno: João (Fluxo)")
        st.metric(label="Latência (Ping)", value="15ms", delta="- Rápido")
        st.progress(95)
        st.caption("✅ **Diagnóstico:** Sinapse fluida. O aluno sente-se pertencente ao território de aprendizagem.")
    
    # Aluno 2: Dificuldade Técnica (Exclusão?)
    with col_b:
        st.warning("##### 🟡 Aluna: Maria (Bloqueio)")
        st.metric(label="Latência (Ping)", value="850ms", delta="Alto (Travado)", delta_color="inverse")
        st.progress(25)
        st.caption("⚠️ **Diagnóstico:** Alta latência na Práxis. Possível barreira de acessibilidade. O DUA precisa ser ativado.")
        
        # --- ATUALIZAÇÃO IMPORTANTE AQUI (DUA/HOSPITALIDADE) ---
        if st.button("Ativar Protocolo de Hospitalidade (Maria)"):
            with st.spinner('Analisando perfil cognitivo de Maria...'):
                time.sleep(1.5)
            
            # MUDANÇA: Exibe o sucesso e, logo abaixo, a informação detalhada fixa (sem desaparecer)
            st.success("✅ **Intervenção:** Rota de aprendizagem ajustada para o perfil neurocognitivo da aluna.")
            st.info("💙 **Ação do Sistema:** O conteúdo textual foi convertido automaticamente para **VÍDEO INTERATIVO** (Detecção de Perfil Visual).")

    # Aluno 3: Instabilidade Emocional (Jitter)
    with col_c:
        st.error("##### 🔴 Aluno: Carlos (Instabilidade)")
        # Simulando Jitter visualmente
        jitter_val = random.choice(["20ms", "400ms", "120ms", "900ms"])
        st.metric(label="Jitter (Variação)", value=jitter_val, delta="Instável", delta_color="inverse")
        st.progress(50)
        st.caption("🛑 **Diagnóstico:** Alto Jitter. Indica ansiedade ou desconforto. Requer intervenção humana e ética do acolhimento.")

# ──────────────────────────────────────────────────────────────────────────────
# RODAPÉ E REFERÊNCIAS RÁPIDAS
# ──────────────────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: grey;">
    <b>Sistema SINAPSE-BR IA</b> | <i>Dissertação de Neirivon Elias Cardoso</i> | IFTM 2026<br>
    Fundamentação: Geofilosofia (FERNANDES, 2023) & Pedagogia da Autonomia (FREIRE, 1996)
</div>
""", unsafe_allow_html=True)
