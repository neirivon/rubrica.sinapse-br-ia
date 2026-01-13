import streamlit as st
import plotly.graph_objects as go
from PIL import Image
import os

st.set_page_config(page_title="Permeabilidade Seletiva", layout="wide")

st.title("🧬 Membrana Plasmática: A Permeabilidade Seletiva")

# --- 1. DEFINIÇÃO DO CAMINHO DO ARQUIVO ---
# Caminho absoluto fornecido
caminho_imagem = "/home/neirivon/SINAPSE2.0/sinapsebr_rubrica/assets/imagens/Permeabilidade.Seletiva.Biologica.png"

# --- 2. CARREGAMENTO DA IMAGEM ---
if os.path.exists(caminho_imagem):
    try:
        img = Image.open(caminho_imagem)
    except Exception as e:
        st.error(f"Erro ao abrir o arquivo: {e}")
        st.stop()
else:
    # Fallback caso o arquivo não esteja lá (para não quebrar o app)
    st.error(f"❌ Arquivo não encontrado no caminho: {caminho_imagem}")
    st.info("Verifique se o arquivo .png está salvo exatamente nesta pasta.")
    st.stop()

# --- 3. CRIAÇÃO DO GRÁFICO (COM A IMAGEM DE FUNDO) ---
fig = go.Figure()

# Adiciona a imagem carregada ao fundo do gráfico
# O sizing="contain" garante que a imagem não distorça
fig.add_layout_image(
    dict(
        source=img,
        xref="x",
        yref="y",
        x=0,
        y=10, # Altura total do eixo Y definida abaixo
        sizex=20, # Largura total do eixo X definida abaixo
        sizey=10,
        sizing="stretch", 
        opacity=1.0,
        layer="below"
    )
)

# --- 4. RÓTULOS (TRADUÇÃO/ANALOGIA) ---
# DICA: Você precisará ajustar os valores de 'x' e 'y' (coordenadas)
# para que o texto caia EXATAMENTE em cima das palavras em inglês da sua imagem.
rotulos = [
    # (Posição X, Posição Y, Texto)
    (3, 9, "<b>Fluido Extracelular\n(Sociedade)</b>"),
    (3, 1, "<b>Citoplasma\n(Escola/Trabalho)</b>"),
    (6, 5, "<b>Bicamada Lipídica\n(Barreira de Classe)</b>"),
    (12, 5, "<b>Proteína Canal\n(Ensino Técnico)</b>"),
    (16, 5, "<b>Proteína Bomba\n(Vestibular/Barreira)</b>"),
]

for x_pos, y_pos, texto in rotulos:
    # 1. Cria o texto
    fig.add_trace(go.Scatter(
        x=[x_pos],
        y=[y_pos],
        text=[texto],
        mode="text",
        textfont=dict(color="black", size=14, family="Arial Black"),
        hoverinfo="none"
    ))
    
    # 2. Cria o retângulo branco atrás para tapar o texto original da imagem
    fig.add_shape(
        type="rect",
        x0=x_pos - 2, y0=y_pos - 0.8, # Ajuste o tamanho da 'caixa' aqui
        x1=x_pos + 2, y1=y_pos + 0.8,
        fillcolor="white", 
        opacity=0.85, # Leve transparência para integrar com a imagem
        line_width=0,
        layer="between" # Fica entre a imagem e o texto
    )

# --- 5. AJUSTES FINAIS DE LAYOUT ---
# Remove eixos e grades para parecer apenas uma imagem interativa
fig.update_xaxes(showgrid=False, zeroline=False, visible=False, range=[0, 20])
fig.update_yaxes(showgrid=False, zeroline=False, visible=False, range=[0, 10])

fig.update_layout(
    width=900, 
    height=600, 
    margin=dict(l=0, r=0, t=0, b=0),
    plot_bgcolor='rgba(0,0,0,0)' # Fundo transparente
)

st.plotly_chart(fig, use_container_width=True)

st.caption("Fonte: Adaptação conceitual sobre imagem biológica. Modelo de Mosaico Fluido aplicado à Sociologia da EPT.")
