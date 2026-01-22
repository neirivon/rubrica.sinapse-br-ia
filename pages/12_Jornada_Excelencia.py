"""
=========================================================================================
ARQUIVO:       12_Jornada_Excelencia.py
CAMINHO:       /home/neirivon/SINAPSE2.0/sinapsebr_rubrica/pages/12_Jornada_Excelencia.py
-----------------------------------------------------------------------------------------
PROJETO:       ECOSSISTEMA SINAPSE-BR IA (Educação Profissional e Tecnológica)
AUTOR:         Neirivon Elias Cardoso
VERSÃO:        1.3.2 (Platinum - Integer Scale Fix)

DESCRIÇÃO:     
    Demonstra a evolução do artefato (Nível 3 -> 4).
    AJUSTE: Gráfico agora reflete a escala inteira (Gold = 3, Platinum = 4).
=========================================================================================
"""

import streamlit as st
import json
import pandas as pd
import plotly.express as px
from pathlib import Path

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Jornada para a Excelência",
    page_icon="💎",
    layout="wide"
)

# --- FUNÇÃO DE CARREGAMENTO INTELIGENTE ---
def carregar_dados():
    caminho_script = Path(__file__).resolve()
    raiz_projeto = caminho_script.parent.parent
    caminho_arquivo = raiz_projeto / "data" / "rubrica_sinapse_br_ia.json"
    
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        st.error("❌ Erro: Arquivo JSON não encontrado. Rode o script 'refine_rubrica_platinum.py'.")
        return None

dados = carregar_dados()

# --- CABEÇALHO ---
st.title("💎 Jornada da Qualidade: O Padrão Platinum")
st.markdown("""
Esta página documenta a **engenharia pedagógica** por trás da Rubrica SINAPSE-BR IA. 
Aqui evidenciamos o salto qualitativo entre a versão auditada (Gold) e a versão final equalizada (Platinum).
""")

# --- CONTEÚDO ---
if dados:
    lista_eixos = dados.get('eixos', [])
    
    # --- 1. O SALTO EVOLUTIVO (DASHBOARD) ---
    st.header("📈 A Evolução: Do Nível Proficiente (3) ao Avançado (4)")
    st.markdown("A auditoria algorítmica revelou que a versão Gold era tecnicamente correta (Nível 3), mas carecia de identidade local. A versão Platinum atingiu o Nível 4 através da **Territorialidade Profunda**.")

    c1, c2 = st.columns([1.5, 1]) 

    with c1:
        # --- GRÁFICO DE MATURIDADE (ESCALA 1 a 4) ---
        
        df_evolucao = pd.DataFrame({
            "Eixo": [e['id'] for e in lista_eixos],
            # Gold: Nível 3 (Proficiente - Bom, mas genérico)
            "Versão Gold (Anterior)": [3] * len(lista_eixos), 
            # Platinum: Nível 4 (Avançado - Contextualizado)
            "Versão Platinum (Atual)": [4] * len(lista_eixos)
        })
        
        df_long = df_evolucao.melt('Eixo', var_name='Versão', value_name='Nível de Maturidade')
        
        fig = px.bar(
            df_long, x="Eixo", y="Nível de Maturidade", color="Versão", barmode="group",
            color_discrete_map={"Versão Gold (Anterior)": "#94a3b8", "Versão Platinum (Atual)": "#3b82f6"},
            height=480, 
            title="Evolução do Nível de Maturidade (Escala Mullinix)"
        )
        
        # Eixo Y ajustado para inteiros, começando de 0 visualmente mas com ticks de 1 a 4
        fig.update_yaxes(
            range=[0, 4.5], 
            tickvals=[1, 2, 3, 4], 
            title="Nível da Rubrica (1 = Emergente ... 4 = Avançado)"
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Métrica de Ganho Qualitativo
        st.info("**Resultado:** A injeção de contexto territorial foi o diferencial para elevar a rubrica do nível **Proficiente (3)** para o **Exemplar (4)**.")

    with c2:
        # --- O QUADRO CONCEITUAL ---
        st.markdown("### 🧬 Entenda o Salto de Qualidade")
        st.markdown("O que diferencia a nota 3 da nota 4?")

        # Card 1: Nível 3 (Gold)
        st.markdown("""
        <div style="background-color: #f1f5f9; padding: 12px; border-radius: 6px; margin-bottom: 10px; border-left: 4px solid #94a3b8;">
            <strong style="color: #475569;">Nível 3. Proficiente (Versão Gold)</strong><br>
            <em>"O aluno resolve problemas de logística."</em><br>
            <span style="font-size: 0.9em; color: #64748b;">⚠️ <strong>Diagnóstico:</strong> A rubrica está tecnicamente correta e avalia a competência, mas é asséptica e sem "alma".</span>
        </div>
        """, unsafe_allow_html=True)

        # Card 2: Nível 4 (Platinum)
        st.markdown("""
        <div style="background-color: #eff6ff; padding: 12px; border-radius: 6px; margin-bottom: 10px; border-left: 4px solid #2563eb; box-shadow: 0 4px 6px rgba(37, 99, 235, 0.1);">
            <strong style="color: #1e40af;">Nível 4. Avançado (Versão Platinum)</strong><br>
            <em>"O aluno resolve problemas da <strong>cafeicultura em Patrocínio</strong>."</em><br>
            <span style="font-size: 0.9em; color: #166534;">✅ <strong>Diagnóstico:</strong> Territorialidade Profunda. O aluno mobiliza o saber técnico para transformar sua realidade local.</span>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        st.caption("Nota: A escala segue a taxonomia de avaliação de rubricas onde o nível máximo exige adaptação ao contexto.")

    st.markdown("---")

    # --- 2. RAIO-X DA TERRITORIALIZAÇÃO (FINAL) ---
    st.subheader("🔍 Evidências da Territorialidade Profunda (Por Eixo)")
    
    if lista_eixos:
        escolha = st.selectbox("Selecione o Eixo para auditar:", [e['nome'] for e in lista_eixos])
        eixo = next(e for e in lista_eixos if e['nome'] == escolha)

        with st.container(border=True):
            col_esq, col_dir = st.columns([1, 2])
            
            with col_esq:
                st.markdown(f"### 🎯 {eixo['id']}")
                st.caption(eixo['foco'])
                
                # AQUI MOSTRAMOS O CONTRASTE MÁXIMO (1 vs 4) PARA EFEITO DIDÁTICO
                st.markdown("**Do Genérico (Nível 1)...**")
                st.warning(f"_{eixo.get('niveis', {}).get('1')}_")
                
                st.markdown("**...Para a Excelência (Nível 4)**")
                st.success(f"_{eixo.get('niveis', {}).get('4')}_")
                
                st.markdown(f"**Status:** `Equalizado (Nível 4)`")
            
            with col_dir:
                st.markdown("### 🗺️ Exemplos no Triângulo Mineiro")
                
                for i, ex in enumerate(eixo.get('exemplos_tmap', [])):
                    if ":" in ex:
                        cidade, texto = ex.split(":", 1)
                    else:
                        cidade, texto = "TMAP", ex
                    
                    # Destaque para o 3º exemplo (Platinum)
                    destaque = "border: 2px solid #22c55e;" if i == 2 else "border-left: 4px solid #3b82f6;"
                    badge = "✨ NOVO (Platinum)" if i == 2 else ""
                    
                    st.markdown(f"""
                    <div style="background-color:#f8fafc; {destaque} padding:10px; margin-bottom:10px; border-radius:4px;">
                        <div style="display:flex; justify-content:space-between;">
                            <strong style="color:#1e40af;">📍 {cidade.strip()}</strong>
                            <span style="font-size:0.8em; color:#15803d; font-weight:bold;">{badge}</span>
                        </div>
                        {texto.strip()}
                    </div>
                    """, unsafe_allow_html=True)

else:
    st.stop()
