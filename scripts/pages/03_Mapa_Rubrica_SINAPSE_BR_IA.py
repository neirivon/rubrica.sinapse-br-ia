# /home/neirivon/SINAPSE2.0/sinapsebr_rubrica/scripts/pages/04_Mapa_Fundamentacao_Teorica.py
# Streamlit + Mermaid mindmap SEM parênteses
# Mostra: (1) Correspondencias teóricas por dimensão
#         (2) Descritores por nível em 8 dimensões
# Renderização via bloco Markdown ```mermaid (sem JS externo)

import streamlit as st
from textwrap import dedent

st.set_page_config(
    page_title="Fundamentacao da Rubrica — SINAPSE-BR IA",
    page_icon="📚",
    layout="wide",
)

st.markdown("## 📚 Fundamentacao da Rubrica — SINAPSE BR IA")
st.caption(
    "Dois mapas em Mermaid mindmap. Renderizados via Markdown nativo do Streamlit. "
    "Sem parenteses nos nos e prontos para exportar."
)

def render_mermaid_md(code: str):
    # Render MERMAID de forma nativa no Streamlit (sem JS externo)
    st.markdown("```mermaid\n" + code.strip() + "\n```")

# ---------- MAPA 1: CORRESPONDÊNCIAS TEÓRICAS ----------
mermaid_theory = dedent("""
mindmap
  raiz Mapa de Fundamentacao Teorica
    Dimensoes
      Cognitiva
        - Bloom revisada
        - Taxonomia SOLO
        - Psicologia cognitiva
      Afetiva
        - Neuropsicopedagogia
        - Teorias da motivacao
        - Autoregulacao da aprendizagem
      Metodologica
        - Metodologias ativas
        - PBL ABP
        - Aprendizagem baseada em projetos
        - Gamificacao
      Neurofuncional
        - Neuropsicopedagogia
        - Educacao baseada no cerebro MBE
        - Memoria atencao funcoes executivas
      Avaliativa
        - Avaliacao formativa
        - Rubricas e criterios
        - Feedback de qualidade
        - Coavaliacao
      Tecnologica
        - Competencia digital docente
        - Cultura de dados e reproducibilidade
        - Recursos educacionais abertos
      Territorial
        - Critica do territorio CTC
        - Equidade justica e inclusao EJI
        - Indicadores locais IBGE MEC
      Inclusiva
        - Desenho Universal para a Aprendizagem DUA
        - Educacao inclusiva
        - Acessibilidade comunicacional
""")

# ---------- MAPA 2: DESCRITORES POR NÍVEL ----------
mermaid_levels = dedent("""
mindmap
  raiz Rubrica SINAPSE BR IA
    Cognitiva
      Niveis
        Emergente
          - Lembra termos basicos
          - Reconhece conceitos essenciais
        Intermediario
          - Explica com as proprias palavras
          - Interpreta tabelas e graficos simples
        Proficiente
          - Aplica procedimentos em situacoes conhecidas
          - Resolve problemas padrao
        Avancado
          - Analisa causas e relacoes
          - Compara alternativas com criterio
        Expert
          - Cria solucoes originais
          - Generaliza para novos contextos
    Afetiva
      Niveis
        Emergente
          - Engajamento oscilante
          - Necessita orientacao constante
        Intermediario
          - Participa quando solicitado
          - Aceita feedback
        Proficiente
          - Participa ativamente
          - Busca feedback e melhora
        Avancado
          - Autorregula emocao e tempo
          - Coopera de forma consistente
        Expert
          - Lidera com empatia
          - Persevera diante de desafios
    Metodologica
      Niveis
        Emergente
          - Segue roteiros passo a passo
        Intermediario
          - Escolhe estrategia entre opcoes dadas
        Proficiente
          - Planeja etapas e executa PBL simples
        Avancado
          - Integra diferentes metodologias ativas
        Expert
          - Desenha intervencoes e avalia impacto
    Neurofuncional
      Niveis
        Emergente
          - Atencao curta
          - Memoria de trabalho limitada
        Intermediario
          - Usa anotacoes e pausas para foco
        Proficiente
          - Utiliza tecnicas metacognitivas
        Avancado
          - Alterna focos mantendo desempenho
        Expert
          - Ensina estrategias e adapta ambiente
    Avaliativa
      Niveis
        Emergente
          - Precisa de criterios explicitos
        Intermediario
          - Usa rubrica para revisar o proprio trabalho
        Proficiente
          - Coavalia pares com justificativas
        Avancado
          - Construi rubricas com o professor
        Expert
          - Conduz processos de avaliacao formativa
    Tecnologica
      Niveis
        Emergente
          - Utiliza ferramentas basicas
        Intermediario
          - Opera AVA e editores com autonomia
        Proficiente
          - Integra planilhas e dados
        Avancado
          - Automatiza fluxos e gera dashboards
        Expert
          - Cria apps e scripts reprodutiveis
    Territorial
      Niveis
        Emergente
          - Reconhece realidade local
        Intermediario
          - Relaciona curso ao territorio
        Proficiente
          - Analisa indicadores locais
        Avancado
          - Propõe solucoes alinhadas a cadeias regionais
        Expert
          - Articula redes intermunicipais e politicas
    Inclusiva
      Niveis
        Emergente
          - Reconhece diversidade
        Intermediario
          - Aplica recomendacoes DUA basicas
        Proficiente
          - Adapta materiais e linguagem
        Avancado
          - Desenha trilhas acessiveis personalizadas
        Expert
          - Promove cultura inclusiva e monitoramento
""")

tab1, tab2 = st.tabs(["🔎 Correspondencias teoricas", "🧩 Descritores por nivel"])

with tab1:
    render_mermaid_md(mermaid_theory)
    st.markdown("**Legenda**  •  Bloom  SOLO  MBE  CTC  EJI  DUA")
    st.download_button(
        "Baixar mapa teorico .mmd",
        data=mermaid_theory.encode("utf-8"),
        file_name="mapa_fundamentacao_teorica.mmd",
        mime="text/plain",
        use_container_width=True,
    )

with tab2:
    st.markdown("### 🧩 Descritores por nivel em 8 dimensoes")
    render_mermaid_md(mermaid_levels)
    st.download_button(
        "Baixar mapa descritores .mmd",
        data=mermaid_levels.encode("utf-8"),
        file_name="mapa_descritores_niveis.mmd",
        mime="text/plain",
        use_container_width=True,
    )

st.markdown("---")
st.caption("Elaboracao propria — Neirivon Elias Cardoso  •  Mermaid mindmap sem parenteses  •  Compatível com Streamlit")

