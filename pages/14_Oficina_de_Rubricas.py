# --------------------------------------------------------------------------------------
# CAMINHO DO ARQUIVO: /pages/14_Oficina_de_Rubricas.py
# NOME DO SCRIPT: 14_Oficina_de_Rubricas.py
#
# DESCRIÇÃO: Laboratório de Auditoria Pedagógica e Criação de Rubricas EPT.
#            Utiliza IA Generativa (Llama 3.3 via Groq) com Estratégia de "Texto Integrado".
#            Foca na fusão das dimensões (Cognitivo/Práxis/Território) em um único descritor.
#
# FUNCIONALIDADES:
#   1. Injeção de Contexto Otimizado (Resumo Técnico).
#   2. Engenharia de Prompt "Fórmula de Fusão" (Sem JSON para evitar erros).
#   3. Visualização Comparativa (Antes vs Depois) com setas direcionais.
#   4. Visualização Volumétrica Decomposta (Hastes de Projeção Coloridas).
#
# AUTOR: Neirivon Elias Cardoso
# PROJETO: Rubrica SINAPSE-BR IA
# DATA: 18/02/2026 (Versão Final Cloud - Texto Integrado & Projeção 3D)
# --------------------------------------------------------------------------------------

import streamlit as st
import plotly.graph_objects as go
from groq import Groq
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
        font-family: 'Source Sans Pro', sans-serif;
        font-size: 1.1rem;
        line-height: 1.6;
    }
    .arrow-container {
        display: flex;
        align-items: center;
        justify-content: center;
        height: 100%;
        font-size: 3rem;
        color: #9ca3af;
    }
    .nota-explicativa {
        background-color: #f8fafc;
        border-left: 4px solid #94a3b8;
        padding: 15px;
        font-size: 0.95rem;
        color: #475569;
        margin-top: 15px;
        border-radius: 4px;
    }
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# 1. CARREGAMENTO DO CÉREBRO TEÓRICO (Resumo de Alta Densidade)
# ==============================================================================
@st.cache_data
def carregar_teoria_final():
    """
    Carrega o Resumo Técnico Denso de Susan Brookhart.
    Arquivo: data/teoria_brookhart_RESUMO.txt
    """
    caminho = os.path.join("data", "teoria_brookhart_RESUMO.txt")
    
    if os.path.exists(caminho):
        try:
            with open(caminho, "r", encoding="utf-8") as f:
                return f.read()
        except Exception as e:
            st.error(f"Erro de Leitura do Cérebro: {e}")
            return ""
    else:
        st.warning("⚠️ Arquivo de resumo não encontrado. Usando conhecimento base.")
        return "Rubricas devem avaliar a qualidade da aprendizagem, não a contagem de tarefas."

TEORIA_BROOKHART = carregar_teoria_final()

# ==============================================================================
# 2. FUNÇÃO DE VISUALIZAÇÃO 3D (COM HASTES DE PROJEÇÃO PURAS)
# ==============================================================================
def plot_salto_sinaptico(coord_antes, coord_depois):
    # Coordenadas Finais
    xf, yf, zf = coord_depois[0], coord_depois[1], coord_depois[2]
    
    # Coordenadas Iniciais
    xi, yi, zi = coord_antes[0], coord_antes[1], coord_antes[2]

    fig = go.Figure()

    # --- 1. O PONTO FINAL (A "Jóia" da Competência) ---
    def get_mix_color(x, y, z):
        r = min(int((y / 6.0) * 255), 255)
        g = min(int((x / 6.0) * 255), 255)
        b = min(int((z / 6.0) * 255), 255)
        return f'rgb({r}, {g}, {b})'
    
    cor_final = get_mix_color(xf, yf, zf)

    fig.add_trace(go.Scatter3d(
        x=[xf], y=[yf], z=[zf],
        mode='markers',
        marker=dict(size=30, color=cor_final, symbol='diamond', opacity=1.0, line=dict(width=2, color='white')),
        name='Competência Final'
    ))

    # --- 2. PONTO INICIAL (Fantasma) ---
    fig.add_trace(go.Scatter3d(
        x=[xi], y=[yi], z=[zi],
        mode='markers',
        marker=dict(size=10, color='gray', opacity=0.5),
        name='Rascunho Inicial'
    ))

    # --- 3. HASTES DE PROJEÇÃO (Solução de Componentes Puros) ---
    fig.add_trace(go.Scatter3d(
        x=[0, xf], y=[yf, yf], z=[zf, zf],
        mode='lines',
        line=dict(color='#22c55e', width=5), # Verde
        name='Ganho em Território'
    ))
    
    fig.add_trace(go.Scatter3d(
        x=[xf, xf], y=[0, yf], z=[zf, zf],
        mode='lines',
        line=dict(color='#f97316', width=5), # Laranja
        name='Ganho em Práxis'
    ))

    fig.add_trace(go.Scatter3d(
        x=[xf, xf], y=[yf, yf], z=[0, zf],
        mode='lines',
        line=dict(color='#3b82f6', width=5), # Azul
        name='Ganho Cognitivo'
    ))

    # Configuração do Ambiente 3D
    fig.update_layout(
        scene=dict(
            xaxis=dict(
                title='TERRITÓRIO (Verde)', range=[0, 6], 
                backgroundcolor='#f0fdf4', color='green', 
                gridcolor='green', showbackground=True
            ),
            yaxis=dict(
                title='PRÁXIS (Laranja)', range=[0, 6], 
                backgroundcolor='#fff7ed', color='#d97706', 
                gridcolor='#d97706', showbackground=True
            ),
            zaxis=dict(
                title='COGNITIVO (Azul)', range=[0, 6], 
                backgroundcolor='#eff6ff', color='blue', 
                gridcolor='blue', showbackground=True
            ),
        ),
        margin=dict(l=0, r=0, b=0, t=30),
        height=500,
        title="Volumetria Decomposta (Eixos Puros)",
        showlegend=False
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
    st.caption("Motor: Groq Llama 3.3 | Estratégia: Texto Integrado (Fórmula da Fusão)")

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
    
    # --- Guia Didático para o Professor ---
    with st.expander("💡 Não sabe como começar? Veja como rascunhar um Descritor"):
        st.markdown("""
        O **Descritor** é o texto que define exatamente o que o aluno precisa fazer para atingir a competência. 
        Para criar um bom rascunho, junte três elementos básicos:
        1. **Ação:** O que o aluno vai fazer? *(Ex: Elaborar um relatório)*
        2. **Condição:** Como ele vai fazer? *(Ex: utilizando as regras de formatação da ABNT)*
        3. **Critério de Qualidade:** O que torna o trabalho excelente? *(Ex: sem erros ortográficos e com argumentação clara)*
        
        *Escreva do seu jeito. O ecossistema SINAPSE vai auditar seu rascunho e injetar a Teoria, a Técnica e o Território adequados!*
        """)
    
    texto_rascunho = st.text_area(
        "Rascunho do Descritor (Como você descreveria a expectativa de aprendizagem para esta atividade?):",
        height=120,
        placeholder="Ex: O aluno precisa entregar o relatório formatado corretamente e sem erros de português."
    )
    
    btn_auditar = st.form_submit_button("🚀 Auditar e Gerar Descritor", use_container_width=True)

# ==============================================================================
# 4. LÓGICA DE PROCESSAMENTO (TEXTO PURO - BLINDADO)
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
            with st.spinner("🔄 A IA está fundindo Técnica, Teoria e Impacto..."):
                try:
                    client = Groq(api_key=api_key)

                    prompt_sistema = f"""
                    Você é um Especialista Sênior em Rubricas Técnicas.
                    
                    TAREFA: Converta o rascunho do professor em um DESCRITOR DE RUBRICA INTEGRADO (Nível Proficiente).
                    
                    DADOS:
                    - Atividade: {tema} ({contexto_ept})
                    - Rascunho Original (Ruim/Tarefa): "{texto_rascunho}"
                    
                    REGRA DE OURO (FÓRMULA DE ESCRITA):
                    O TEXTO DA NOVA RUBRICA deve ser obrigatoriamente UM ÚNICO PARÁGRAFO CORRIDO seguindo esta estrutura lógica:
                    [O ALUNO EXECUTA A TÉCNICA X] + [BASEADO NO CONHECIMENTO TÉCNICO Y] + [PARA GARANTIR O IMPACTO Z NO CONTEXTO REAL].
                    
                    RESTRIÇÕES ABSOLUTAS:
                    1. NÃO use listas, bullet points ou quebras de linha.
                    2. NÃO escreva rótulos como "Cognitivo:", "Práxis:" ou "Território:".
                    3. NÃO seja conversacional (Não diga "Aqui está" ou "Entendido").
                    
                    FORMATO OBRIGATÓRIO DE RESPOSTA (EM UMA ÚNICA LINHA):
                    DIAGNOSTICO CURTO (O que faltou no rascunho)|||TEXTO DA NOVA RUBRICA (O parágrafo fundido)|||JUSTIFICATIVA DO GANHO (1 frase)
                    """

                    chat_completion = client.chat.completions.create(
                        messages=[
                            {"role": "user", "content": prompt_sistema}
                        ],
                        model="llama-3.3-70b-versatile",
                        temperature=0.3, # Reduzido para focar na obediência ao formato
                        max_tokens=800,
                    )
                    
                    # Limpeza extra para evitar quebras de linha acidentais geradas pela IA
                    resposta_raw = chat_completion.choices[0].message.content.strip()
                    resposta_raw = resposta_raw.replace('\n', ' ') 
                    
                    try:
                        partes = resposta_raw.split("|||")
                        if len(partes) >= 3:
                            diagnostico = partes[0].strip()
                            nova_rubrica = partes[1].strip()
                            motivo = partes[2].strip()
                        else:
                            raise ValueError("A IA não retornou os separadores corretamente.")
                    except Exception as parse_err:
                        # Fallback de segurança atualizado
                        diagnostico = "Rascunho focado em tarefa."
                        nova_rubrica = resposta_raw.replace('|||', '') # Exibe o texto limpo caso algo dê muito errado
                        motivo = "Expansão de competência via IA."

                    # ==========================================================
                    # VISUALIZAÇÃO
                    # ==========================================================
                    st.success("✅ Descritor SINAPSE Gerado!")
                    
                    with st.container():
                        col_antes, col_arrow, col_depois = st.columns([4, 1, 4])
                        
                        with col_antes:
                            st.markdown("#### ❌ Rascunho (Tarefa)")
                            st.info(f'"{texto_rascunho}"')
                            st.caption(f"🚨 **Problema:** {diagnostico}")
                        
                        with col_arrow:
                             st.markdown("<div class='arrow-container'>➔</div>", unsafe_allow_html=True)
                        
                        with col_depois:
                            st.markdown("#### ✅ Rubrica (Competência)")
                            st.success(f'"{nova_rubrica}"')
                            st.caption(f"✨ **Ganho:** {motivo}")
                            
                            st.markdown("""
                            <small>
                            <span style='color:blue'><b>[Cognitivo]</b></span> Justificativa &nbsp;|&nbsp; 
                            <span style='color:#d97706'><b>[Práxis]</b></span> Técnica &nbsp;|&nbsp; 
                            <span style='color:green'><b>[Território]</b></span> Impacto
                            </small>
                            """, unsafe_allow_html=True)
                            
                    st.markdown("---")
                    
                    # Gráfico 3D Voxel Decomposto
                    col_3d_center, _ = st.columns([2,1]) 
                    with col_3d_center:
                        st.subheader("🧊 Visualização Volumétrica Decomposta")
                        st.caption("Expansão tridimensional do aprendizado (Hastes = Projeção nos Eixos).")
                        # Coordenadas fixas para demonstração do salto
                        fig_3d = plot_salto_sinaptico((1.5, 1.5, 1.0), (5.5, 5.0, 5.5))
                        st.plotly_chart(fig_3d, use_container_width=True)
                        
                        # --- Nota Explicativa da Escala 0 a 6 ---
                        st.markdown("<hr style='margin: 10px 0px; border-top: 1px solid #e2e8f0;'>", unsafe_allow_html=True)
                        st.markdown("""
                        <div class='nota-explicativa'>
                            <strong>📌 Nota Explicativa (Escala de 0 a 6):</strong> A arquitetura espacial mapeia os níveis de <strong>1 a 6</strong> estritamente na progressão da Taxonomia de Bloom revisada (Lembrar a Criar). O <strong>nível 0</strong> não representa um processo cognitivo, mas sim o <em>Ponto de Inércia (Omissão)</em>. Na Educação Profissional e Tecnológica (EPT), é comum uma tarefa atingir alto nível Cognitivo, mas apresentar nível 0 no eixo Territorial, refletindo a desconexão com a realidade e a geofilosofia do aluno. O sistema diagnostica essa nulidade e projeta o descritor para um nível operante.
                        </div>
                        """, unsafe_allow_html=True)

                except Exception as e:
                    st.error(f"Erro técnico: {e}")

st.markdown("---")
st.caption("Ecossistema SINAPSE-BR IA | TCC Neirivon Elias Cardoso | IFTM 2026")
