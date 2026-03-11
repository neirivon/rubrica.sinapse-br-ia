# -*- coding: utf-8 -*-
# --------------------------------------------------------------------------------------
# NOME DO SCRIPT: 17_simulador_superconjunto_taxonomia_bloom.py
# LOCALIZAÇÃO: /pages/
# DESCRIÇÃO: Visualização do Superconjunto da Taxonomia de Bloom (Anderson & Krathwohl).
#               Substitui a hierarquia linear pela lógica de círculos concêntricos 
#               e mútua possessão. Inclui vídeo oficial do projeto em tela cheia.
#
# AUTOR: Neirivon Elias Cardoso (Aprimorado via Assistente IA)
# PROJETO: Rubrica SINAPSE-BR IA
# DATA: 04/03/2026
# --------------------------------------------------------------------------------------

import streamlit as st
import plotly.graph_objects as go
import numpy as np
import os

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="Superconjunto Bloom - SINAPSE-BR IA",
    layout="wide",
    page_icon="🔮"
)

def render_superconjunto():
    st.title("🔮 Taxonomia de Bloom: Superconjunto de Saberes")
    st.markdown("### Da Hierarquia Rígida à Mútua Possessão")

    # 2. MOTOR DE GERAÇÃO GEOMÉTRICA (OTIMIZADO PARA UX E PRECISÃO ACADÊMICA)
    # Correção dos verbos conforme Anderson & Krathwohl (2001)
    bloom_data = [
        {"name": "LEMBRAR", "color": "#FF3B30", "radius": 1.2, "verbs": "Reconhecer, Memorizar, Recordar"},
        {"name": "ENTENDER", "color": "#5AC8FA", "radius": 2.4, "verbs": "Interpretar, Exemplificar, Classificar, Explicar"},
        {"name": "APLICAR", "color": "#4CD964", "radius": 3.6, "verbs": "Usar, Implementar, Executar"},
        {"name": "ANALISAR", "color": "#FF9500", "radius": 4.8, "verbs": "Diferenciar, Organizar, Desconstruir"},
        {"name": "AVALIAR", "color": "#007AFF", "radius": 6.0, "verbs": "Julgar, Criticar, Revisar"},
        {"name": "CRIAR", "color": "#AF52DE", "radius": 7.2, "verbs": "Planejar, Produzir, Design"}
    ]

    fig = go.Figure()

    # MELHORIA DE UX: Renderização de Hemisférios para evitar bloqueio de Mouse
    for i, layer in enumerate(bloom_data):
        # Gerando apenas a metade frontal para permitir interatividade com o núcleo
        u, v = np.mgrid[0:2*np.pi:30j, 0:np.pi/2:30j]
        x = layer['radius'] * np.cos(u) * np.sin(v)
        y = layer['radius'] * np.sin(u) * np.sin(v)
        z = layer['radius'] * np.cos(v)

        fig.add_trace(go.Surface(
            x=x, y=y, z=z,
            colorscale=[[0, layer['color']], [1, layer['color']]],
            opacity=0.25 - (i * 0.02), 
            showscale=False,
            name=layer['name'],
            hoverinfo="text",
            text=f"<b>Nível: {layer['name']}</b><br>Ações: {layer['verbs']}",
            contours=dict(z=dict(show=True, usecolormap=False, project_z=False, color="white", width=1))
        ))

    fig.update_layout(
        scene=dict(
            xaxis=dict(visible=False), yaxis=dict(visible=False), zaxis=dict(visible=False),
            bgcolor='white',
            camera=dict(eye=dict(x=1.5, y=1.5, z=1.3))
        ),
        margin=dict(l=0, r=0, b=0, t=0), height=700,
        hoverlabel=dict(bgcolor="white", font_size=16, font_family="Arial")
    )

    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # 3. IMAGEM DE REFERÊNCIA
    st.subheader("🖼️ Referência Estética: Representação Isométrica")
    path_imagem = "/home/neirivon/SINAPSE2.0/sinapsebr_rubrica/assets/imagens/superconjunto_taxonomia_bloom.png"
    
    if os.path.exists(path_imagem):
        st.image(path_imagem, caption="A Camada Outermost como Integração Total.", use_container_width=True)
    else:
        st.warning("Imagem de referência estática não localizada.")

    st.divider()

    # 4. FUNDAMENTAÇÃO ACADÊMICA
    st.markdown("### 📚 Evolução Teórica da Taxonomia")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.info("#### 📑 Revisão de 2001 (Anderson & Krathwohl)")
        st.write("As categorias se **sobrepõem**. Um aluno pode criar enquanto ainda organiza o saber base.")
        st.success("#### ⭕ Círculos Concêntricos (Fuchsteiner, 2011)")
        st.write("Lógica de Diagramas de Euler: o círculo maior **CONTÉM** e abraça o menor.")

    with col_b:
        st.error("#### ⚖️ Crítica de Roland Case (2013)")
        st.write("O pensamento crítico deve permear todos os níveis, sem castas cognitivas ou pré-requisitos rígidos.")
        st.warning("#### ☸️ SINAPSE-BR IA: Mútua Possessão")
        st.write("A camada **CRIAR** é a membrana unificadora. Sem o núcleo (Lembrar), a arquitetura do saber se desfaz.")

    # 5. SEÇÃO DE VÍDEO CINEMATOGRÁFICO
    st.divider()
    st.subheader("🎬 Demonstração: SINAPSE-BR IA (8K)")
    st.video("https://youtu.be/yY5oLErTxO8")

    # 6. JORNADA NEURAL EM CARDS VERTICAIS (UI CUSTOMIZADA)
    st.markdown("### 🧠 ARQUITETURA DO SABER")
    
    for layer in bloom_data:
        st.markdown(f"""
        <div style="border-left: 8px solid {layer['color']}; 
                    padding: 15px; margin: 10px 0; 
                    background-color: #f8f9fa; 
                    border-radius: 4px;
                    box-shadow: 2px 2px 5px rgba(0,0,0,0.05);">
            <h4 style="margin:0; color:#333;">{layer['name']}</h4>
            <p style="margin:5px 0 0 0; color:#666;"><b>Ações:</b> {layer['verbs']}</p>
        </div>
        """, unsafe_allow_html=True)

    st.caption("**#SINAPSE-BR #InteligenciaArtificial #IA #Educacao #Tecnologia #IFTM #Taxonomia #Bloom #Inovacao**")
    st.markdown("---")
    st.markdown("> **Glosa Acadêmica:** Na EPT, a camada *Outermost* materializa a união entre o saber e o fazer.")

if __name__ == "__main__":
    render_superconjunto()
