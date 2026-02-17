# /scripts/13_Cubo_Sinapse_3D.py
# --------------------------------------------------------------------------------------
# NOME DO SCRIPT: 13_Cubo_Sinapse_3D.py
# LOCALIZAÇÃO:    /scripts/ (Obrigatório para Multipage Apps)
# DESCRIÇÃO:      Visualização interativa tridimensional (Cubo 3D) da Matriz de Competências
#                 SINAPSE-BR IA. Modela a interseção entre Progressão, Contexto e Dimensões.
#                 *Versão "Ultra HD": Rótulos coloridos e nítidos com anotações 3D.*
# AUTOR:          Neirivon Elias Cardoso (Gerado via Assistente IA)
# PROJETO:        Rubrica SINAPSE-BR IA
# DATA:           31/01/2026
# --------------------------------------------------------------------------------------

import streamlit as st
import plotly.graph_objects as go
import numpy as np

#==============================================================================
# 1. CONFIGURAÇÃO DA PÁGINA
#==============================================================================
st.set_page_config(
    page_title="Cubo SINAPSE-BR IA - Matriz Completa",
    layout="wide",
    page_icon="🧊"
)

#==============================================================================
# 2. DADOS E ESTRUTURAS (EIXOS) COM CORES REPRESENTATIVAS
#    ✅ CORRIGIDO: Removidos espaços extras nas chaves
#==============================================================================

# Mapeamento de cores para Níveis (Eixo X) - PROGRESSÃO
MAPA_CORES_NIVEIS = {
    "Nível 1 (Inicial)": "#00B0FF",
    "Nível 2 (Emergente)": "#0091EA",
    "Nível 3 (Autônomo)": "#01579B",
    "Nível 4 (Transformador)": "#1A237E"
}

# Mapeamento de cores para Contextos (Eixo Y) - CONTEXTO
MAPA_CORES_CONTEXTOS = {
    "Sala de Aula": "#FB8C00",        # Laranja
    "Campus": "#43A047",               # Verde
    "Comunidade": "#8E24AA",           # Roxo
    "Território (TMAP)": "#E64A19"     # Coral
}

# Mapeamento de cores para Dimensões (Eixo Z) - DIMENSÃO
MAPA_CORES_DIMENSOES = {
    "E1: Cognitivo": "#F44336",
    "E2: Afetivo": "#E91E63",
    "E3: Metodológico": "#9C27B0",
    "E4: Neurofuncional": "#673AB7",
    "E5: Avaliativo": "#3F51B5",
    "E6: Tecnológico": "#2196F3",
    "E7: Territorial": "#03A9F4",
    "E8: Inclusivo": "#00BCD4"
}

# Listas de eixos
eixo_x_niveis = list(MAPA_CORES_NIVEIS.keys())
eixo_y_contextos = list(MAPA_CORES_CONTEXTOS.keys())
eixo_z_dimensoes = list(MAPA_CORES_DIMENSOES.keys())

# Índices para plotagem
x_indices = list(range(len(eixo_x_niveis)))
y_indices = list(range(len(eixo_y_contextos)))
z_indices = list(range(len(eixo_z_dimensoes)))

#==============================================================================
# 3. DESCRIÇÕES PEDAGÓGICAS COM EXEMPLOS PRÁTICOS
#==============================================================================

DESCRICAO_DIMENSOES = {
    "E1: Cognitivo": {
        "descricao": "Processamento de informações, raciocínio lógico, resolução de problemas e pensamento crítico.",
        "exemplo": "Um estudante que analisa dados de um experimento e formula conclusões baseadas em evidências."
    },
    "E2: Afetivo": {
        "descricao": "Gestão emocional, empatia, resiliência e relações interpessoais saudáveis.",
        "exemplo": "Um aluno que reconhece suas emoções durante um conflito e busca diálogo construtivo com colegas."
    },
    "E3: Metodológico": {
        "descricao": "Planejamento, organização, estratégias de aprendizagem e gestão do tempo.",
        "exemplo": "Um estudante que cria um cronograma de estudos personalizado e utiliza técnicas de memorização eficazes."
    },
    "E4: Neurofuncional": {
        "descricao": "Adaptação cognitiva, plasticidade neural e estratégias de aprendizagem personalizadas.",
        "exemplo": "Um aluno que identifica seu estilo de aprendizagem e utiliza recursos multimodais para otimizar o estudo."
    },
    "E5: Avaliativo": {
        "descricao": "Autoavaliação, metacognição, feedback construtivo e melhoria contínua.",
        "exemplo": "Um estudante que revisa seus erros em uma prova e cria um plano de ação para sanar dificuldades."
    },
    "E6: Tecnológico": {
        "descricao": "Alfabetização digital, uso crítico de tecnologias e inovação tecnológica.",
        "exemplo": "Um aluno que utiliza ferramentas digitais para criar um projeto interdisciplinar e colaborativo."
    },
    "E7: Territorial": {
        "descricao": "Conexão com o território, sustentabilidade local e protagonismo comunitário.",
        "exemplo": "Um estudante que mapeia problemas ambientais de sua cidade e propõe soluções sustentáveis."
    },
    "E8: Inclusivo": {
        "descricao": "Respeito à diversidade, acessibilidade, equidade e justiça social.",
        "exemplo": "Um aluno que adapta materiais didáticos para torná-los acessíveis a colegas com diferentes necessidades."
    }
}

DESCRICAO_NIVEIS = {
    "Nível 1 (Inicial)": "Reconhecimento básico da dimensão. O estudante demonstra familiaridade inicial com os conceitos.",
    "Nível 2 (Emergente)": "Prática aplicada com auxílio ou guiada. O estudante começa a utilizar a competência em situações reais.",
    "Nível 3 (Autônomo)": "Operação independente da competência. O estudante aplica a dimensão sem necessidade de suporte constante.",
    "Nível 4 (Transformador)": "Maestria com intervenção crítica. O estudante não apenas domina, mas transforma e inova na dimensão."
}

#==============================================================================
# 4. INTERFACE DO UTILIZADOR (SIDEBAR)
#==============================================================================

st.sidebar.header("🎛️ Configuração da Interseção")
st.sidebar.markdown("Ajuste os eixos para explorar diferentes interseções de competências.")

selected_x = st.sidebar.select_slider(
    "Eixo X: Progressão ('O Quanto')",
    options=eixo_x_niveis,
    value="Nível 4 (Transformador)"
)

selected_y_base = st.sidebar.select_slider(
    "Eixo Y: Contexto ('Onde/Quem')",
    options=eixo_y_contextos,
    value="Território (TMAP)"
)

selected_z = st.sidebar.selectbox(
    "Eixo Z: Dimensões ('O Que')",
    options=eixo_z_dimensoes,
    index=5  # Padrão E6: Tecnológico
)

specific_context = st.sidebar.text_input(
    "Nome do Contexto Específico (Opcional)",
    value="Iturama",
    help="Ex: Nome da cidade, projeto ou laboratório específico."
)

# Índices selecionados
ix = eixo_x_niveis.index(selected_x)
iy = eixo_y_contextos.index(selected_y_base)
iz = eixo_z_dimensoes.index(selected_z)

display_context = f"{selected_y_base}: {specific_context}" if specific_context else selected_y_base

#==============================================================================
# 5. FUNÇÃO PARA CRIAR VOXEL (CUBO SÓLIDO)
#==============================================================================

def create_cube_mesh(x, y, z, size=0.4, color='#76b900', opacity=0.9, name="Voxel"):
    """Cria o Voxel (Cubo Sólido) para plotagem 3D"""
    dx, dy, dz = size, size, size
    x_corners = [x-dx, x-dx, x+dx, x+dx, x-dx, x-dx, x+dx, x+dx]
    y_corners = [y-dy, y+dy, y+dy, y-dy, y-dy, y+dy, y+dy, y-dy]
    z_corners = [z-dz, z-dz, z-dz, z-dz, z+dz, z+dz, z+dz, z+dz]
    return go.Mesh3d(
        x=x_corners, y=y_corners, z=z_corners,
        i=[7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
        j=[3, 4, 1, , 6, 5, 2, 0, 1, 6, 3],
        k=[0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6],
        opacity=opacity,
        color=color,
        name=name,
        hoverinfo='skip'
    )

#==============================================================================
# 6. LÓGICA DE PLOTAGEM 3D (PLOTLY) - MATRIZ COMPLETA
#==============================================================================

fig = go.Figure()

# A. Grade de Pontos (Estrutura de referência)
xx, yy, zz = np.meshgrid(x_indices, y_indices, z_indices)
fig.add_trace(go.Scatter3d(
    x=xx.flatten(), y=yy.flatten(), z=zz.flatten(),
    mode='markers',
    marker=dict(size=2, color='lightgrey', opacity=0.2),
    name='Grade de Referência',
    hoverinfo='none'
))

# B. SOMBRA DO CAMINHO PERCORRIDO (ACÚMULO DE SABER) - ✅ MELHORIA PRINCIPAL
cor_foco = MAPA_CORES_DIMENSOES[selected_z]
for nivel_anterior in range(ix + 1):
    # Opacidade diminui conforme vamos para níveis mais antigos
    opacidade_nivel = 0.15 + (0.85 * (nivel_anterior / ix)) if ix > 0 else 0.9
    
    # Voxel da sombra (caminho percorrido)
    fig.add_trace(create_cube_mesh(
        nivel_anterior, 
        iy, 
        iz, 
        size=0.38, 
        color=cor_foco, 
        opacity=opacidade_nivel,
        name=f"Sombra Nível {nivel_anterior+1}"
    ))

# C. VOXEL EM FOCO - DESTAQUE ADICIONAL
fig.add_trace(create_cube_mesh(ix, iy, iz, size=0.42, color=cor_foco, opacity=0.95, name="Foco Atual"))

# D. LINHAS GUIA - Conectando o voxel ao plano de cada eixo
fig.add_trace(go.Scatter3d(
    x=[ix, ix], y=[iy, iy], z=[-0.5, iz],
    mode='lines',
    line=dict(color=cor_foco, width=3, dash='solid'),
    showlegend=False,
    hoverinfo='none'
))
fig.add_trace(go.Scatter3d(
    x=[ix, ix], y=[-0.5, iy], z=[iz, iz],
    mode='lines',
    line=dict(color=cor_foco, width=3, dash='solid'),
    showlegend=False,
    hoverinfo='none'
))
fig.add_trace(go.Scatter3d(
    x=[-0.5, ix], y=[iy, iy], z=[iz, iz],
    mode='lines',
    line=dict(color=cor_foco, width=3, dash='solid'),
    showlegend=False,
    hoverinfo='none'
))

# E. PONTOS NAS INTERSEÇÕES DOS EIXOS (para melhor visualização)
fig.add_trace(go.Scatter3d(
    x=[ix], y=[iy], z=[-0.5],
    mode='markers',
    marker=dict(size=6, color=MAPA_CORES_NIVEIS[selected_x], symbol='circle'),
    name='Nível',
    hoverinfo='none',
    showlegend=False
))
fig.add_trace(go.Scatter3d(
    x=[ix], y=[-0.5], z=[iz],
    mode='markers',
    marker=dict(size=6, color=MAPA_CORES_CONTEXTOS[selected_y_base], symbol='circle'),
    name='Contexto',
    hoverinfo='none',
    showlegend=False
))
fig.add_trace(go.Scatter3d(
    x=[-0.5], y=[iy], z=[iz],
    mode='markers',
    marker=dict(size=6, color=cor_foco, symbol='circle'),
    name='Dimensão',
    hoverinfo='none',
    showlegend=False
))

# F. TOOLTIP INFORMAVITO NO VOXEL FOCO
fig.add_trace(go.Scatter3d(
    x=[ix], y=[iy], z=[iz],
    mode='markers',
    marker=dict(size=0.1, color='rgba(0,0,0,0)'),
    hovertemplate=(
        f"<b>🎲 Dimensão:</b> {selected_z}<br>"
        f"<b>📖 Nível:</b> {selected_x}<br>"
        f"<b>📍 Contexto:</b> {display_context}<br>"
        f"<b>📊 Interseção:</b> ({ix+1}, {iy+1}, {iz+1})<br>"
        f"<b>🧮 Total de Voxels:</b> 128<br>"
        "<extra></extra>"
    ),
    name="Informações",
    showlegend=False
))

# G. ANOTAÇÕES 3D - RÓTULOS DOS EIXOS
annotations = []

# Rótulos do Eixo X (Níveis) - ABAIXO
for i, nivel in enumerate(eixo_x_niveis):
    annotations.append(dict(
        showarrow=False,
        x=i, y=-1.2, z=-1.2,
        text=f"<b>{nivel}</b>",
        font=dict(color=MAPA_CORES_NIVEIS[nivel], size=11, family="Arial"),
        xanchor="center",
        yanchor="top",
        bgcolor="rgba(255,255,255,0.7)",
        borderpad=4
    ))

# Rótulos do Eixo Y (Contextos) - LATERAL ESQUERDA
for j, contexto in enumerate(eixo_y_contextos):
    annotations.append(dict(
        showarrow=False,
        x=-1.2, y=j, z=-1.2,
        text=f"<b>{contexto}</b>",
        font=dict(color=MAPA_CORES_CONTEXTOS[contexto], size=11, family="Arial"),
        xanchor="right",
        yanchor="middle",
        bgcolor="rgba(255,255,255,0.7)",
        borderpad=4
    ))

# Rótulos do Eixo Z (Dimensões) - VERTICAL
for k, dimensao in enumerate(eixo_z_dimensoes):
    annotations.append(dict(
        showarrow=False,
        x=-1.2, y=-1.2, z=k,
        text=f"<b>{dimensao}</b>",
        font=dict(color=MAPA_CORES_DIMENSOES[dimensao], size=10, family="Arial"),
        xanchor="right",
        yanchor="middle",
        bgcolor="rgba(255,255,255,0.7)",
        borderpad=4
    ))

# H. LEGENDA VISUAL - Mini amostras de cores
legend_annotations = [
    dict(showarrow=False, x=4.5, y=-1.5, z=7.5,
         text="<b>🎨 Legenda de Cores</b>",
         font=dict(size=12, color="black"), bgcolor="rgba(255,255,255,0.9)"),
    dict(showarrow=False, x=4.5, y=-1.5, z=7.0,
         text="🔵 <b>Níveis</b>", font=dict(size=10, color="#1A237E")),
    dict(showarrow=False, x=4.5, y=-1.5, z=6.5,
         text="🟠🟢🟣 <b>Contextos</b>", font=dict(size=10, color="#43A047")),
    dict(showarrow=False, x=4.5, y=-1.5, z=6.0,
         text="🔴 <b>Dimensões</b>", font=dict(size=10, color="#F44336"))
]
annotations.extend(legend_annotations)

# I. LAYOUT FINAL COM PLANOS DE FUNDO COLORIDOS
fig.update_layout(
    title={
        'text': "<b>Matriz Completa de Competências SINAPSE-BR IA</b><br>"
                "<sup style='color:#666'>128 Interseções • Foco Atual Destacado</sup>",
        'y': 0.98,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': dict(size=20)
    },
    scene=dict(
        # Rótulos explícitos dos eixos
        xaxis=dict(
            title=dict(
                text="<b>Eixo X: Progressão</b><br><i style='color:#666'>'O Quanto'</i>",
                font=dict(size=14, color="#01579B")
            ),
            showticklabels=False,
            showgrid=True,
            zeroline=False,
            backgroundcolor="rgba(0,176,255,0.08)",  # Azul claro
            gridcolor="rgba(0,176,255,0.2)",
            gridwidth=1
        ),
        yaxis=dict(
            title=dict(
                text="<b>Eixo Y: Contexto</b><br><i style='color:#666'>'Onde/Quem'</i>",
                font=dict(size=14, color="#FB8C00")
            ),
            showticklabels=False,
            showgrid=True,
            zeroline=False,
            backgroundcolor="rgba(251,140,0,0.08)",  # Laranja claro
            gridcolor="rgba(251,140,0,0.2)",
            gridwidth=1
        ),
        zaxis=dict(
            title=dict(
                text="<b>Eixo Z: Dimensão</b><br><i style='color:#666'>'O Quê'</i>",
                font=dict(size=14, color="#F44336")
            ),
            showticklabels=False,
            showgrid=True,
            zeroline=False,
            backgroundcolor="rgba(244,67,54,0.08)",  # Vermelho claro
            gridcolor="rgba(244,67,54,0.2)",
            gridwidth=1
        ),
        annotations=annotations,
        aspectmode='manual',
        aspectratio=dict(x=1, y=1, z=0.9),
        camera=dict(eye=dict(x=2.0, y=2.0, z=1.6))
    ),
    margin=dict(r=40, l=40, b=40, t=80),
    height=850,
    paper_bgcolor="white",
    legend=dict(
        x=0.01,
        y=0.99,
        bgcolor="rgba(255,255,255,0.8)",
        bordercolor="black",
        borderwidth=1
    )
)

#==============================================================================
# 7. RENDERIZAÇÃO - INTERFACE PRINCIPAL
#==============================================================================

st.title("🧊 Cubo Tridimensional SINAPSE-BR IA")
st.markdown("### Visualização Interativa da Matriz Completa de Competências")
st.caption("Explore as 128 interseções entre Progressão, Contexto e Dimensões")

# Layout em colunas: Visualização 3D + Painel Didático
col1, col2 = st.columns([3, 2], gap="large")

with col1:
    # Gráfico 3D
    st.plotly_chart(fig, use_container_width=True)
    
    # Informação sobre a matriz
    st.info("💡 **Dica:** Gire, zoom e arraste a visualização 3D para explorar diferentes perspectivas da matriz.")

with col2:
    # ========================================
    # PAINEL DIDÁTICO SUPERIOR
    # ========================================
    
    st.markdown("### 🧠 Interpretação Pedagógica")
    st.markdown("**Interseção Atual Selecionada:**")
    
    # ✅ CORREÇÃO: Usando elementos HTML corretos
    st.markdown(
        f"""
        <div style="background-color:#f0f8ff; padding:15px; border-radius:8px; border-left:4px solid {MAPA_CORES_DIMENSOES[selected_z]}">
            <p style="margin:0; font-size:14px; color:#555"><b>📍 Posição na Matriz:</b> ({ix+1}, {iy+1}, {iz+1})</p>
            <p style="margin:5px 0 0 0; font-size:16px; color:{MAPA_CORES_DIMENSOES[selected_z]}; font-weight:bold">
                <b>🎲 Dimensão:</b> {selected_z}
            </p>
            <p style="margin:5px 0 0 0; font-size:15px; color:{MAPA_CORES_NIVEIS[selected_x]}; font-weight:bold">
                <b>📖 Nível:</b> {selected_x}
            </p>
            <p style="margin:5px 0 0 0; font-size:15px; color:{MAPA_CORES_CONTEXTOS[selected_y_base]}; font-weight:bold">
                <b>🌍 Contexto:</b> {display_context}
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("---")
    
    # ========================================
    # DESCRIÇÃO DA DIMENSÃO
    # ========================================
    
    st.markdown("### 📚 Sobre esta Dimensão")
    
    dim_info = DESCRICAO_DIMENSOES.get(selected_z, {
        "descricao": "Descrição não disponível.",
        "exemplo": "Exemplo não disponível."
    })
    
    cor_dim = MAPA_CORES_DIMENSOES[selected_z]
    
    st.markdown(
        f"""
        <div style="background:linear-gradient(135deg, {cor_dim}15, {cor_dim}05); 
                    padding:15px; border-radius:8px; border:1px solid {cor_dim}30">
            <p style="margin:0; font-size:14px; line-height:1.6; color:#333">
                {dim_info['descricao']}
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("---")
    
    # ========================================
    # EXEMPLO PRÁTICO
    # ========================================
    
    st.markdown("### 💡 Exemplo Prático no Contexto")
    
    st.markdown(
        f"""
        <div style="background-color:#e8f5e9; padding:15px; border-radius:8px; border-left:4px solid #43A047">
            <p style="margin:0; font-style:italic; line-height:1.6; color:#2E7D32">
                <b>Cenário:</b> {dim_info['exemplo']}
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("---")
    
    # ========================================
    # DESCRIÇÃO DO NÍVEL
    # ========================================
    
    st.markdown("### 📊 Sobre este Nível de Progressão")
    
    nivel_cor = MAPA_CORES_NIVEIS[selected_x]
    nivel_desc = DESCRICAO_NIVEIS.get(selected_x, "Descrição não disponível.")
    
    st.markdown(
        f"""
        <div style="background-color:#e3f2fd; padding:12px; border-radius:8px; border-left:4px solid {nivel_cor}">
            <p style="margin:0; font-size:13px; line-height:1.5; color:#1565C0">
                <b>{selected_x}:</b> {nivel_desc}
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("---")
    
    # ========================================
    # ESTATÍSTICAS DA MATRIZ
    # ========================================
    
    st.markdown("### 📈 Estatísticas da Matriz")
    
    col_stats1, col_stats2, col_stats3 = st.columns(3)
    
    with col_stats1:
        st.metric(label="Total de Voxels", value="128")
    
    with col_stats2:
        st.metric(label="Níveis", value="4")
    
    with col_stats3:
        st.metric(label="Dimensões", value="8")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col_stats4, col_stats5 = st.columns(2)
    
    with col_stats4:
        st.metric(label="Contextos", value="4")
    
    with col_stats5:
        st.metric(label="Status", value="✅ Ativo")
    
    st.markdown("---")
    
    # ========================================
    # LEGENDA VISUAL COMPACTA
    # ========================================
    
    st.markdown("### 🎨 Legenda Visual")
    
    # Níveis
    st.markdown("**Níveis (Eixo X):**")
    nivel_cols = st.columns(4)
    for idx, (nivel, cor) in enumerate(MAPA_CORES_NIVEIS.items()):
        with nivel_cols[idx]:
            st.markdown(
                f"<div style='background-color:{cor}; height:20px; border-radius:4px; margin:2px'></div>"
                f"<small style='color:{cor}; font-weight:bold'>{nivel.split('(')[0]}</small>",
                unsafe_allow_html=True
            )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Dimensões (amostra)
    st.markdown("**Dimensões (Eixo Z):**")
    dim_cols = st.columns(4)
    for idx, (dim, cor) in enumerate(list(MAPA_CORES_DIMENSOES.items())[:4]):
        with dim_cols[idx]:
            st.markdown(
                f"<div style='background-color:{cor}; height:20px; border-radius:4px; margin:2px'></div>"
                f"<small style='color:{cor}; font-weight:bold'>{dim.split(':')[0]}</small>",
                unsafe_allow_html=True
            )
    
    dim_cols2 = st.columns(4)
    for idx, (dim, cor) in enumerate(list(MAPA_CORES_DIMENSOES.items())[4:]):
        with dim_cols2[idx]:
            st.markdown(
                f"<div style='background-color:{cor}; height:20px; border-radius:4px; margin:2px'></div>"
                f"<small style='color:{cor}; font-weight:bold'>{dim.split(':')[0]}</small>",
                unsafe_allow_html=True
            )

#==============================================================================
# 8. EXPANDER COM DEFINIÇÕES COMPLETAS
#==============================================================================

with st.expander("📖 Manual Completo - Definições de Todos os Eixos", expanded=False):
    
    st.markdown("### 📌 Níveis de Progressão")
    for nivel, desc in DESCRICAO_NIVEIS.items():
        cor = MAPA_CORES_NIVEIS[nivel]
        st.markdown(
            f"<div style='background-color:#f5f5f5; padding:10px; margin:5px 0; border-left:3px solid {cor}'>"
            f"<b style='color:{cor}'>{nivel}:</b> {desc}"
            f"</div>",
            unsafe_allow_html=True
        )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("### 📌 Dimensões com Exemplos Completos")
    for dim, info in DESCRICAO_DIMENSOES.items():
        cor = MAPA_CORES_DIMENSOES[dim]
        st.markdown(
            f"<div style='background-color:#fff3e0; padding:12px; margin:8px 0; border-left:4px solid {cor}'>"
            f"<h4 style='color:{cor}; margin:0'>{dim}</h4>"
            f"<p style='margin:5px 0; font-size:14px'><b>Descrição:</b> {info['descricao']}</p>"
            f"<p style='margin:5px 0; font-size:14px; font-style:italic; color:#555'>"
            f"<b>Exemplo:</b> {info['exemplo']}</p>"
            f"</div>",
            unsafe_allow_html=True
        )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("### 📌 Contextos")
    contextos_desc = {
        "Sala de Aula": "Ambiente formal de ensino-aprendizagem dentro da instituição educacional.",
        "Campus": "Espaço ampliado da instituição, incluindo laboratórios, bibliotecas e áreas comuns.",
        "Comunidade": "Entorno social imediato da instituição, incluindo bairros e redes locais.",
        "Território (TMAP)": "Região ampliada com suas especificidades culturais, econômicas e ambientais."
    }
    
    for contexto, desc in contextos_desc.items():
        cor = MAPA_CORES_CONTEXTOS[contexto]
        st.markdown(
            f"<div style='background-color:#e8f5f9; padding:10px; margin:5px 0; border-left:3px solid {cor}'>"
            f"<b style='color:{cor}'>{contexto}:</b> {desc}"
            f"</div>",
            unsafe_allow_html=True
        )

#==============================================================================
# 9. MENSAGEM DE SUCESSO
#==============================================================================

st.success("✅ **Visualização Didática Aprimorada carregada com sucesso!**")
st.caption("💡 Explore a matriz completa de 128 interseções. O voxel em destaque representa a competência selecionada.")
