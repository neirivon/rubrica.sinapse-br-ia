# /pages/13_Cubo_Sinapse_3D.py
# --------------------------------------------------------------------------------------
# NOME DO SCRIPT: 13_Cubo_Sinapse_3D.py
# LOCALIZAÇÃO:    /pages/ (Obrigatório para Multipage Apps)
# DESCRIÇÃO:      Visualização interativa tridimensional (Cubo 3D) da Matriz de Competências
#                 SINAPSE-BR IA. Modela a interseção entre Progressão, Contexto e Dimensões.
#                 Versão Didática Final: Matriz completa + Foco Ultra HD + Texto NotebookLM.
# AUTOR:          Neirivon Elias Cardoso (Aprimorado via Assistente IA)
# PROJETO:        Rubrica SINAPSE-BR IA
# DATA:           01/02/2026
# --------------------------------------------------------------------------------------

import streamlit as st
import plotly.graph_objects as go
import numpy as np

# ==============================================================================
# 1. CONFIGURAÇÃO DA PÁGINA
# ==============================================================================
st.set_page_config(
    page_title="Cubo SINAPSE-BR IA - Matriz Didática",
    layout="wide",
    page_icon="🧊"
)

# ==============================================================================
# 2. DADOS E ESTRUTURAS (EIXOS) COM CORES REPRESENTATIVAS
# ==============================================================================

MAPA_CORES_NIVEIS = {
    "Nível 1 (Inicial)": "#00B0FF",
    "Nível 2 (Emergente)": "#0091EA",
    "Nível 3 (Autônomo)": "#01579B",
    "Nível 4 (Transformador)": "#1A237E"
}

MAPA_CORES_CONTEXTOS = {
    "Sala de Aula": "#FB8C00",
    "Campus": "#43A047",
    "Comunidade": "#8E24AA",
    "Território (TMAP)": "#E64A19"
}

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

eixo_x_niveis = list(MAPA_CORES_NIVEIS.keys())
eixo_y_contextos = list(MAPA_CORES_CONTEXTOS.keys())
eixo_z_dimensoes = list(MAPA_CORES_DIMENSOES.keys())

x_indices = list(range(len(eixo_x_niveis)))
y_indices = list(range(len(eixo_y_contextos)))
z_indices = list(range(len(eixo_z_dimensoes)))

# ==============================================================================
# 3. DESCRIÇÕES PEDAGÓGICAS
# ==============================================================================

DESCRICAO_DIMENSOES = {
    "E1: Cognitivo": {"desc": "Processamento de informações e pensamento crítico.", "ex": "Analisar dados e formular conclusões baseadas em evidências."},
    "E2: Afetivo": {"desc": "Gestão emocional e relações interpessoais.", "ex": "Reconhecer emoções e buscar diálogo construtivo."},
    "E3: Metodológico": {"desc": "Planejamento e estratégias de aprendizagem.", "ex": "Criar cronogramas e utilizar técnicas de estudo eficazes."},
    "E4: Neurofuncional": {"desc": "Adaptação cognitiva e plasticidade neural.", "ex": "Identificar estilos de aprendizagem e usar recursos multimodais."},
    "E5: Avaliativo": {"desc": "Autoavaliação e metacognição.", "ex": "Revisar erros e criar planos de ação para melhoria."},
    "E6: Tecnológico": {"desc": "Alfabetização digital e inovação.", "ex": "Usar ferramentas digitais para projetos colaborativos."},
    "E7: Territorial": {"desc": "Conexão com o território e protagonismo local.", "ex": "Mapear problemas da cidade e propor soluções sustentáveis."},
    "E8: Inclusivo": {"desc": "Respeito à diversidade e equidade.", "ex": "Adaptar materiais para torná-los acessíveis a todos."}
}

DESCRICAO_NIVEIS = {
    "Nível 1 (Inicial)": "Reconhecimento básico da dimensão.",
    "Nível 2 (Emergente)": "Prática aplicada com auxílio ou guiada.",
    "Nível 3 (Autônomo)": "Operação independente da competência.",
    "Nível 4 (Transformador)": "Maestria com intervenção crítica e inovação."
}

# ==============================================================================
# 4. INTERFACE (SIDEBAR)
# ==============================================================================
st.sidebar.header("🎛️ Configuração da Interseção")

selected_x = st.sidebar.select_slider("Eixo X: Progressão", options=eixo_x_niveis, value="Nível 4 (Transformador)")
selected_y_base = st.sidebar.select_slider("Eixo Y: Contexto", options=eixo_y_contextos, value="Território (TMAP)")
selected_z = st.sidebar.selectbox("Eixo Z: Dimensões", options=eixo_z_dimensoes, index=5)
specific_context = st.sidebar.text_input("Contexto Específico", value="Uberlândia (Sobradinho)")

ix, iy, iz = eixo_x_niveis.index(selected_x), eixo_y_contextos.index(selected_y_base), eixo_z_dimensoes.index(selected_z)
display_context = f"{selected_y_base}: {specific_context}" if specific_context else selected_y_base

# ==============================================================================
# 5. LÓGICA DE PLOTAGEM 3D
# ==============================================================================

def create_cube_mesh(x, y, z, size=0.4, color='#76b900', opacity=0.9, name="Voxel"):
    dx, dy, dz = size, size, size
    x_corners = [x-dx, x-dx, x+dx, x+dx, x-dx, x-dx, x+dx, x+dx]
    y_corners = [y-dy, y+dy, y+dy, y-dy, y-dy, y+dy, y+dy, y-dy]
    z_corners = [z-dz, z-dz, z-dz, z-dz, z+dz, z+dz, z+dz, z+dz]
    return go.Mesh3d(
        x=x_corners, y=y_corners, z=z_corners,
        i=[7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
        j=[3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
        k=[0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6],
        opacity=opacity, color=color, name=name, hoverinfo='skip'
    )

fig = go.Figure()

# A. Grade de Referência
xx, yy, zz = np.meshgrid(x_indices, y_indices, z_indices)
fig.add_trace(go.Scatter3d(
    x=xx.flatten(), y=yy.flatten(), z=zz.flatten(),
    mode='markers', marker=dict(size=2, color='lightgrey', opacity=0.2),
    name='Grade', hoverinfo='none'
))

# B. Voxel em Foco (Destaque Principal)
cor_foco = MAPA_CORES_DIMENSOES[selected_z]
fig.add_trace(create_cube_mesh(ix, iy, iz, size=0.45, color=cor_foco, opacity=0.95, name="Foco Atual"))

# C. Linhas Guia Coloridas
fig.add_trace(go.Scatter3d(x=[ix, ix], y=[iy, iy], z=[-0.5, iz], mode='lines', line=dict(color=cor_foco, width=5), showlegend=False))
fig.add_trace(go.Scatter3d(x=[ix, ix], y=[-0.5, iy], z=[iz, iz], mode='lines', line=dict(color=cor_foco, width=5), showlegend=False))
fig.add_trace(go.Scatter3d(x=[-0.5, ix], y=[iy, iy], z=[iz, iz], mode='lines', line=dict(color=cor_foco, width=5), showlegend=False))

# D. Anotações 3D (Alta Resolução)
annotations = []
for i, nivel in enumerate(eixo_x_niveis):
    annotations.append(dict(showarrow=False, x=i, y=-0.8, z=-0.8, text=nivel, font=dict(color=MAPA_CORES_NIVEIS[nivel], size=12), xanchor="center", yanchor="top"))
for j, contexto in enumerate(eixo_y_contextos):
    annotations.append(dict(showarrow=False, x=-0.8, y=j, z=-0.8, text=contexto, font=dict(color=MAPA_CORES_CONTEXTOS[contexto], size=12), xanchor="right", yanchor="middle"))
for k, dimensao in enumerate(eixo_z_dimensoes):
    annotations.append(dict(showarrow=False, x=-0.8, y=-0.8, z=k, text=dimensao, font=dict(color=MAPA_CORES_DIMENSOES[dimensao], size=11), xanchor="right", yanchor="middle"))

# E. Layout Otimizado
fig.update_layout(
    scene=dict(
        xaxis=dict(title='Progressão', showticklabels=False, backgroundcolor="rgba(245,245,245,0.5)"),
        yaxis=dict(title='Contexto', showticklabels=False, backgroundcolor="rgba(245,245,245,0.5)"),
        zaxis=dict(title='Dimensão', showticklabels=False, backgroundcolor="rgba(245,245,245,0.5)"),
        annotations=annotations,
        aspectmode='cube',
        camera=dict(eye=dict(x=1.8, y=1.8, z=1.4))
    ),
    margin=dict(l=0, r=0, b=0, t=50),
    height=750,
    paper_bgcolor="white",
    title={'text': "<b>Matriz de Competências SINAPSE-BR IA</b>", 'x': 0.5, 'xanchor': 'center'}
)

# ==============================================================================
# 6. RENDERIZAÇÃO PRINCIPAL (UI/UX ORGANIZADA POR ABAS)
# ==============================================================================
st.title("🧊 Cubo SINAPSE-BR IA: Do Digital ao Analógico")
st.markdown("### Integração de Práxis Pedagógica e Tecnologia")

aba_digital, aba_analogico = st.tabs(["🎮 Simulador Digital Interativo", "🛠️ Objeto de Aprendizagem Analógico"])

with aba_digital:
    col1, col2 = st.columns([3, 2], gap="large")

    with col1:
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("#### 🧠 A Volumetria da Aprendizagem")
        st.write("""
        A avaliação tradicional tende a ser linear e bidimensional (uma nota em um papel). 
        O **Simulador SINAPSE 3D** rompe com essa lógica ao propor a **Volumetria da Competência**:

        1.  **Profundidade Neurofuncional (Eixo Z):** Não avaliamos apenas "o que" o aluno aprendeu, mas *quais funções executivas* (memória, atenção, controle inibitório) foram mobilizadas (COSENZA; GUERRA, 2011).
        2.  **Situação Territorial (Eixo Y):** Baseado na Geofilosofia e no entendimento de que o espaço é um sistema de objetos e ações, o aprendizado é indissociável do território (SANTOS, 2006).
        3.  **Progressão Cognitiva (Eixo X):** Evolução do *Nível Emergente* ao *Transformador*, alinhando-se à concepção de que o ser humano é "programado para aprender", mas carece de mediação para sua própria inconclusão (FREIRE, 1996).

        **O Voxel (Volume + Pixel):** Cada cubo colorido representa a intersecção exata entre a capacidade cognitiva do aluno, o suporte oferecido pelo ambiente e o estágio de autonomia alcançado.
        """)
        
        st.markdown("---")
        st.markdown("#### 🧭 Como Interpretar a Matriz Tridimensional")
        col_inst1, col_inst2, col_inst3 = st.columns(3)

        with col_inst1:
            st.markdown("**1. O Eixo Azul (X)**")
            st.caption("Indica **ONDE** o aluno está na escalada da autonomia. \n*De: Dependência (Nível 1) \nPara: Inovação e Crítica (Nível 4)*")

        with col_inst2:
            st.markdown("**2. O Eixo Laranja (Y)**")
            st.caption("Indica **ONDE** a aprendizagem acontece. \n*A competência se sustenta na escola ou se aplica no território real (SANTOS, 2006)?*")

        with col_inst3:
            st.markdown("**3. O Eixo Vermelho (Z)**")
            st.caption("Indica **O QUE** sustenta a aprendizagem. \n*São as dimensões estruturantes sob a ótica neuropsicopedagógica (COSENZA; GUERRA, 2011).*")

        st.warning("**Interação:** Utilize os controles na barra lateral (sidebar) para 'navegar' pela estrutura cognitiva do estudante.")

    with col2:
        st.markdown("### 🧠 Painel de Interpretação")
        
        st.markdown(f"""
            <div style="background-color:#f8f9fa; padding:20px; border-radius:12px; border-left:8px solid {cor_foco}; box-shadow: 2px 2px 10px rgba(0,0,0,0.05);">
                <h4 style="margin:0; color:#333;">Foco Selecionado</h4>
                <p style="margin:10px 0 5px 0; color:{cor_foco}; font-weight:bold; font-size:18px;">{selected_z}</p>
                <p style="margin:0; color:{MAPA_CORES_NIVEIS[selected_x]}; font-weight:bold;">{selected_x}</p>
                <p style="margin:0; color:{MAPA_CORES_CONTEXTOS[selected_y_base]}; font-weight:bold;">{display_context}</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        info = DESCRICAO_DIMENSOES[selected_z]
        st.markdown(f"**O que é esta Dimensão?**")
        st.write(info['desc'])
        st.success(info['ex'])
        
        st.markdown("---")
        st.markdown(f"**Nível de Progressão:**")
        st.info(DESCRICAO_NIVEIS[selected_x])

with aba_analogico:
    st.markdown("### 🎞️ Materialização: O Cubo Analógico em Ação")
    
    st.video("https://www.youtube.com/watch?v=rccCtHzHFSk")
    
    st.markdown("---")
    
    st.markdown("## Da Abstração à Concretude: A Materialização da Rubrica SINAPSE-BR IA")
    
    st.write("""
    O vídeo acima ilustra a concepção do **Cubo SINAPSE 3D Analógico**, um artefato pedagógico que traduz a complexidade da avaliação educacional em uma estrutura tátil e tridimensional. 
    Em consonância com os princípios da Politecnia e da superação da dualidade histórica entre trabalho manual e intelectual, este modelo demonstra que a avaliação na EPT não deve ser linear ou unidimensional, mas sim volumétrica e contextualizada.
    
    **A codificação visual apresentada no vídeo segue a lógica da matriz avaliativa proposta nesta pesquisa:**
    """)

    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.markdown(f"**🔵 Eixo X – Progressão Cognitiva**")
        st.caption("Trajetória do estudante até a Autonomia, alinhando-se à concepção de que o ser humano é 'programado para aprender', mas carece de mediação para sua própria inconclusão (FREIRE, 1996).")
    
    with col_b:
        st.markdown(f"**🟠 Eixo Y – Contexto Territorial**")
        st.caption("Simboliza a territorialização (Uberlândia/TMAP). A avaliação ocorre no 'chão' de Sobradinho, integrando o sistema de objetos e ações locais (SANTOS, 2006).")
    
    with col_c:
        st.markdown(f"**🔴 Eixo Z – Dimensões Neuropsicopedagógicas**")
        st.caption("Representa a profundidade da análise das funções cerebrais. É a estrutura vertical que sustenta o olhar sobre como o aluno aprende (COSENZA; GUERRA, 2011).")

    st.markdown("#### ⚡ A Metáfora da Sinapse")
    st.write("""
    No momento em que os três eixos se cruzam e o marcador (voxel) se fixa, o vídeo exibe um feixe de luz. Este fenômeno visual representa a **"Sinapse Pedagógica"**: o instante em que a avaliação deixa de ser um mero julgamento classificatório e se torna um ato de compreensão integral do sujeito.
    
    > *"A tecnologia é intelecto humano objetivado"* (MARX; SAVIANI).
    
    Ao construir este cubo, materializamos a tese de que a Inteligência Artificial não deve substituir o professor, mas servir como ferramenta de ampliação da sua capacidade de análise. O cubo devolve ao docente a tangibilidade do processo avaliativo, evitando a educação automatizada como 'caixa preta'.
    """)
    
    st.warning("⚠️ **Fundamentação:** Práxis pedagógica baseada em Freire, Milton Santos, Saviani e Neurociência aplicada.")

st.success("✅ Script completo com fundamentação teórica e fontes integradas.")
