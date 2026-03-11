# --------------------------------------------------------------------------------------
# CAMINHO DO ARQUIVO: /pages/15_Gerador_Matriz.py
# NOME DO SCRIPT: 15_Gerador_Matriz.py
#
# DESCRIÇÃO: Desdobramento Operacional do Cubo 3D em uma Matriz 2D de Avaliação.
#            Gera uma Rubrica Analítica Completa (5x5) baseada nos eixos da 
#            Sinapse-BR, com ordem decrescente de níveis, tooltips seletivos
#            nos cabeçalhos e critérios, e exportação direta (CSV).
#
# AUTOR: Neirivon Elias Cardoso
# PROJETO: neirivon/rubrica.sinapse-br-ia
# DATA: 20/02/2026 
# --------------------------------------------------------------------------------------

import streamlit as st
import pandas as pd
from groq import Groq
import re

st.set_page_config(page_title="Gerador de Matriz 2D SINAPSE", page_icon="📊", layout="wide")

# Estilização CSS para a Tabela e Tooltips (Otimizada)
st.markdown("""
<style>
    /* Estilo da Tabela */
    .custom-table {
        width: 100%;
        border-collapse: collapse;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif;
        margin: 20px 0;
        background-color: white;
    }
    
    .custom-table th {
        background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
        color: white;
        padding: 14px 12px;
        text-align: left;
        font-weight: 600;
        font-size: 0.95rem;
        border: 1px solid #0f172a;
        position: sticky;
        top: 0;
    }
    
    .custom-table td {
        padding: 12px;
        border: 1px solid #cbd5e1;
        font-size: 0.9rem;
        line-height: 1.5;
        color: #1e293b;
    }
    
    .custom-table tbody tr:nth-child(odd) {
        background-color: #f8fafc;
    }
    
    .custom-table tbody tr:nth-child(even) {
        background-color: #ffffff;
    }
    
    .custom-table tbody tr:hover {
        background-color: #f1f5f9;
        transition: background-color 0.15s ease-in-out;
    }
    
    .custom-table td:first-child {
        font-weight: 600;
        background-color: #f0f4f8;
        min-width: 200px;
        color: #0f172a;
    }
    
    .custom-table tbody tr:hover td:first-child {
        background-color: #e2e8f0;
    }

    /* Estilo do Tooltip para Cabeçalhos e Critérios */
    .tooltip-header {
        position: relative;
        display: inline-block;
        cursor: help;
        border-bottom: 1px dotted rgba(255, 255, 255, 0.5);
    }
    
    .tooltip-header:hover {
        border-bottom: 1px dotted rgba(255, 255, 255, 1);
    }

    .tooltip-criterion {
        position: relative;
        display: inline-block;
        cursor: help;
        border-bottom: 1px dotted #1e40af;
    }
    
    .tooltip-criterion:hover {
        border-bottom: 1px dotted #0f172a;
    }

    /* Estilo do Tooltip Text */
    .tooltip-text {
        visibility: hidden;
        position: absolute;
        z-index: 9999;
        bottom: 120%;
        left: 50%;
        transform: translateX(-50%);
        background-color: #1e293b;
        color: #f1f5f9;
        text-align: center;
        padding: 10px 12px;
        border-radius: 6px;
        font-size: 0.85rem;
        font-weight: 500;
        line-height: 1.4;
        white-space: normal;
        width: 240px;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
        border: 1px solid #334155;
        opacity: 0;
        transition: opacity 0.2s ease-in-out, visibility 0.2s ease-in-out;
        pointer-events: none;
    }
    
    /* Seta do Tooltip */
    .tooltip-text::after {
        content: "";
        position: absolute;
        top: 100%;
        left: 50%;
        margin-left: -5px;
        border-width: 5px;
        border-style: solid;
        border-color: #1e293b transparent transparent transparent;
    }
    
    .tooltip-header:hover .tooltip-text,
    .tooltip-criterion:hover .tooltip-text {
        visibility: visible;
        opacity: 1;
    }
    
    .header-text { 
        color: #475569; 
        font-size: 1.1rem; 
        margin-top: 10px;
    }
    
    .info-box {
        background-color: #eff6ff;
        border-left: 4px solid #3b82f6;
        padding: 12px 16px;
        border-radius: 4px;
        margin: 15px 0;
        font-size: 0.9rem;
        color: #1e40af;
    }
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# CABEÇALHO
# ==============================================================================
col_logo, col_title = st.columns([1, 8])
with col_logo:
    st.image("https://img.icons8.com/fluency/96/matrix.png", width=60)
with col_title:
    st.title("Gerador de Matriz Analítica 2D")
    st.markdown("<p class='header-text'>Desdobramento prático dos eixos da Sinapse-BR em instrumento de sala de aula.</p>", unsafe_allow_html=True)

st.markdown("---")

# ==============================================================================
# INTERFACE DE ENTRADA
# ==============================================================================
with st.form("form_matriz"):
    st.markdown("### Configuração da Atividade")
    col1, col2 = st.columns(2)
    
    with col1:
        contexto_ept = st.selectbox(
            "📂 Contexto EPT:",
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
        tema = st.text_input("📝 Atividade Específica (Alvo da Avaliação):", placeholder="Ex: Usinagem CNC, Poda de Café...")
        
    btn_gerar = st.form_submit_button("⚙️ Gerar Matriz de Rubrica 2D", use_container_width=True)

# ==============================================================================
# LÓGICA DO MOTOR LLM (GROQ)
# ==============================================================================
if btn_gerar:
    if contexto_ept == "Selecione..." or not tema:
        st.error("❌ Preencha o Contexto e a Atividade para gerar a matriz.")
    else:
        api_key = st.secrets.get("GROQ_API_KEY")
        if not api_key:
            st.error("🔒 ERRO: Chave GROQ_API_KEY não configurada nos Segredos do Streamlit.")
        else:
            with st.spinner("🔄 Construindo a Matriz Analítica 2D (5x5)... Isso leva alguns segundos."):
                try:
                    client = Groq(api_key=api_key)

                    prompt_matriz = f"""
                    Você é um Especialista em Avaliação Formativa na EPT.
                    Sua tarefa é criar o texto de uma Matriz de Rubrica Bidimensional (5 colunas) para a seguinte atividade:
                    
                    - Contexto: {contexto_ept}
                    - Atividade: {tema}
                    
                    A matriz DEVE refletir os pilares da Politecnia e da Geofilosofia.
                    
                    Os 5 Critérios (Linhas) DEVEM ser estritamente estes:
                    1. Fundamentação Científico-Tecnológica (Cognitivo)
                    2. Execução Técnica e Processual (Práxis)
                    3. Impacto e Sustentabilidade Local (Território)
                    4. Autonomia e Resolução de Problemas (SOLO)
                    5. Postura Ética e Profissional (Atitudinal)
                    
                    As 4 Colunas de Nível DEVEM estar em ORDEM DECRESCENTE (do maior para o menor):
                    Avançado (4), Proficiente (3), Em Desenvolvimento (2), Iniciante (1).
                    
                    ATENÇÃO À POLITECNIA: No nível Avançado (4) da "Execução Técnica", não descreva rapidez de mercado, mas sim precisão aliada à apropriação tecnológica.
                    
                    FORMATO DE SAÍDA OBRIGATÓRIO:
                    Você deve retornar APENAS os dados separados por pipe (|). 
                    NÃO escreva introdução. NÃO use código Markdown (como ```). 
                    Siga estritamente este padrão de 6 linhas:
                    
                    Critério Avaliado|Avançado (4)|Proficiente (3)|Em Desenvolvimento (2)|Iniciante (1)
                    Fundamentação (Cognitivo)|[desc_4]|[desc_3]|[desc_2]|[desc_1]
                    Execução Técnica (Práxis)|[desc_4]|[desc_3]|[desc_2]|[desc_1]
                    Impacto Local (Território)|[desc_4]|[desc_3]|[desc_2]|[desc_1]
                    Autonomia (SOLO)|[desc_4]|[desc_3]|[desc_2]|[desc_1]
                    Postura Ética (Atitudinal)|[desc_4]|[desc_3]|[desc_2]|[desc_1]
                    """

                    chat_completion = client.chat.completions.create(
                        messages=[{"role": "user", "content": prompt_matriz}],
                        model="llama-3.3-70b-versatile",
                        temperature=0.2, 
                        max_tokens=2000,
                    )
                    
                    resposta_bruta = chat_completion.choices[0].message.content.strip()
                    
                    # --- FILTRO BLINDADO ANTI-ALUCINAÇÃO ---
                    linhas = resposta_bruta.split('\n')
                    dados_limpos = []
                    
                    for linha in linhas:
                        if '|' in linha and '---' not in linha:
                            dados_limpos.append([item.strip() for item in linha.split('|') if item.strip() != ''])

                    if len(dados_limpos) >= 6 and all(len(row) == 5 for row in dados_limpos[:6]): 
                        colunas = dados_limpos[0]
                        linhas_df = dados_limpos[1:6] 
                        
                        df_rubrica = pd.DataFrame(linhas_df, columns=colunas)
                        
                        st.success("✅ Matriz Gerada com Sucesso!")
                        
                        # ==========================================================
                        # EXIBIÇÃO UX/UI COM TOOLTIPS SELETIVOS
                        # ==========================================================
                        st.markdown(f"#### Instrumento de Avaliação: {tema}")
                        st.markdown('<div class="info-box">💡 <b>Dica:</b> Passe o mouse sobre os cabeçalhos (níveis) e critérios para ver explicações teóricas.</div>', unsafe_allow_html=True)
                        
                        # Dicionário de Tooltips por Nível (Colunas)
                        tooltips_niveis = {
                            "Avançado (4)": "Taxonomia SOLO: Abstrato Estendido. Inovação, resolução de problemas inéditos e visão sistêmica.",
                            "Proficiente (3)": "Taxonomia SOLO: Relacional. Conexão clara entre teoria e prática. Padrão esperado na EPT.",
                            "Em Desenvolvimento (2)": "Taxonomia SOLO: Multiestrutural. Execução de etapas de forma mecânica ou com lacunas de conexão.",
                            "Iniciante (1)": "Taxonomia SOLO: Uniestrutural. Foco em aspectos isolados, necessita de supervisão constante."
                        }
                        
                        # Dicionário de Tooltips por Critério (Dimensão)
                        tooltips_criterios = {
                            "Fundamentação (Cognitivo)": "Politecnia de Saviani: Compreensão dos fundamentos científico-tecnológicos subjacentes à atividade.",
                            "Execução Técnica (Práxis)": "Práxis: Precisão, segurança e apropriação tecnológica, não mera repetição mecânica.",
                            "Impacto Local (Território)": "Geofilosofia: Consciência ambiental, sustentabilidade e impacto ético na comunidade.",
                            "Autonomia (SOLO)": "Andaime Pedagógico: Grau de independência, proatividade e capacidade de autorregulação.",
                            "Postura Ética (Atitudinal)": "Soft Skills EPT: Segurança, colaboração, responsabilidade social e uso ético de ferramentas."
                        }

                        # Construção da Tabela HTML com Tooltips Seletivos
                        html_table = '<table class="custom-table"><thead><tr><th>Critério Avaliado</th>'
                        
                        # Cabeçalhos com Tooltips nos Níveis
                        for col in colunas[1:]:
                            tooltip_text = tooltips_niveis.get(col, "Descrição do nível de desempenho.")
                            html_table += f'''<th>
                                <div class="tooltip-header">
                                    {col}
                                    <span class="tooltip-text">{tooltip_text}</span>
                                </div>
                            </th>'''
                        
                        html_table += '</tr></thead><tbody>'

                        for _, row in df_rubrica.iterrows():
                            html_table += '<tr>'
                            # Primeira coluna (Critério) com Tooltip
                            criterion_name = row[colunas[0]]
                            criterion_tooltip = tooltips_criterios.get(criterion_name, "Critério de avaliação.")
                            html_table += f'''<td>
                                <div class="tooltip-criterion">
                                    {criterion_name}
                                    <span class="tooltip-text">{criterion_tooltip}</span>
                                </div>
                            </td>'''
                            
                            # Colunas de Níveis SEM Tooltips (apenas o conteúdo limpo)
                            for col in colunas[1:]:
                                cell_content = row[col]
                                html_table += f'<td>{cell_content}</td>'
                            
                            html_table += '</tr>'
                        
                        html_table += '</tbody></table>'
                        
                        # Renderiza a tabela HTML
                        st.markdown(html_table, unsafe_allow_html=True)
                        
                        # ==========================================================
                        # BOTÃO DE EXPORTAÇÃO (PLANILHA LIMPA)
                        # ==========================================================
                        st.markdown("<br>", unsafe_allow_html=True)
                        csv = df_rubrica.to_csv(index=False, sep=';').encode('utf-8-sig')
                        
                        st.download_button(
                            label="📊 Exportar Matriz para Planilha (.CSV)",
                            data=csv,
                            file_name=f"Rubrica_Sinapse_{tema.replace(' ', '_')}.csv",
                            mime="text/csv",
                            use_container_width=True
                        )
                        
                        # ==========================================================
                        # NOTAS DIDÁTICAS
                        # ==========================================================
                        st.markdown("<hr style='margin: 20px 0px; border-top: 1px solid #e2e8f0;'>", unsafe_allow_html=True)
                        st.markdown("### 💡 Embasamento Teórico da Matriz")
                        
                        with st.expander("📖 Ver fundamentação dos Eixos e Níveis", expanded=True):
                            st.markdown("""
                            **Os Níveis de Proficiência (Colunas):**
                            * **Avançado (4):** *Taxonomia SOLO (Abstrato Estendido)*. O aluno inova e resolve problemas inéditos.
                            * **Proficiente (3):** *Taxonomia SOLO (Relacional)*. O aluno conecta teoria e prática (Padrão esperado na EPT).
                            * **Em Desenv. (2):** *Taxonomia SOLO (Multiestrutural)*. Executa etapas de forma mecânica ou desconexa.
                            * **Iniciante (1):** *Taxonomia SOLO (Uniestrutural)*. Foca em aspecto isolado e precisa de supervisão.
                            
                            **Os Eixos Avaliativos (Linhas):**
                            * **Fundamentação:** *Politecnia de Saviani* (Compreensão dos fundamentos científico-tecnológicos).
                            * **Execução Técnica:** *Práxis* (Precisão, segurança e apropriação tecnológica, não repetição).
                            * **Impacto Local:** *Geofilosofia* (Consciência ambiental, sustentabilidade e impacto ético).
                            * **Autonomia:** *Andaime Pedagógico* (Grau de independência e proatividade).
                            * **Postura Ética:** *Soft Skills EPT* (Segurança, colaboração e uso responsável de ferramentas).
                            """)
                        
                    else:
                        st.error("A IA alterou a estrutura da tabela. Por favor, clique em 'Gerar' novamente.")
                        with st.expander("Ver erro técnico"):
                            st.code(resposta_bruta)

                except Exception as e:
                    st.error(f"Erro na geração da Matriz: {e}")

st.markdown("---")
st.caption("Ecossistema SINAPSE-BR IA | TCC Neirivon Elias Cardoso | IFTM 2026")
