# -----------------------------------------------------------------------
# CAMINHO: /SINAPSE2.0/sinapsebr_rubrica/pages/16_Omnilateridade_Sinaptica.py
# PROJETO: RUBRICA SINAPSE-BR IA
# AUTOR: Neirivon Elias Cardoso
# IDENTIFICADOR: neirivon/rubrica.sinapse-br-ia
# DESCRIÇÃO: Simulador de Práxis em Redes de Alta Tensão (Inspirado no 
#            trabalho de RV do Prof. Alexandre para Concessionárias).
# -----------------------------------------------------------------------

import streamlit as st
import plotly.graph_objects as go
import numpy as np

# Configuração da Página
st.set_page_config(page_title="15. Omnilateridade Sináptica", layout="wide")

st.title("🧠 15. Omnilateridade Sináptica")
st.subheader("Simulador de Treinamento em Riscos Fatais (Concessionárias de Energia)")

# --- ESPAÇO DA SIMULAÇÃO (O "LABORATÓRIO VIRTUAL") ---
st.info("💻 CONTEXTO: Manutenção em Transformador de Distribuição (Alta Tensão).")

col_sim, col_cubo = st.columns([1, 1])

with col_sim:
    st.write("### Painel de Manobra")
    st.warning("⚠️ ATENÇÃO: Risco de Arco Elétrico e Choque Fatal.")
    
    # Passos da NR-10 simulados
    passo_1 = st.checkbox("1. Equipar EPIs Completos (Arco Elétrico)")
    passo_2 = st.checkbox("2. Realizar Seccionamento (Abertura de Chaves)")
    passo_3 = st.checkbox("3. Impedir Reenergização (Bloqueio/Sinalização)")
    passo_4 = st.checkbox("4. Constatar Ausência de Tensão")
    
    executar = st.button("Executar Manutenção no Circuito")

    # Lógica de Avaliação Automática
    pontuacao_tecnica = 0
    if executar:
        if not passo_1:
            st.error("💥 ERRO FATAL: Você iniciou a manobra sem EPI adequado. Arco elétrico detectado.")
            pontuacao_tecnica = 0
        elif not passo_2 or not passo_3:
            st.error("⚡ ERRO CRÍTICO: Circuito ainda energizado ou sem bloqueio. Perigo de morte.")
            pontuacao_tecnica = 1
        elif not passo_4:
            st.warning("⚠️ RISCO: Manutenção iniciada sem teste de tensão. Falha de protocolo.")
            pontuacao_tecnica = 3
        else:
            st.success("✅ SUCESSO: Manobra executada com segurança plena (Protocolo Prof. Alexandre).")
            pontuacao_tecnica = 6

# --- EIXOS DO CUBO BASEADOS NA SIMULAÇÃO ---
# Se o aluno erra o EPI, a cognição (segurança) trava no zero.
eixo_x = pontuacao_tecnica # Técnica/Operação
eixo_y = 4 if passo_1 and passo_3 else 1 # Social/Segurança e Trabalho
eixo_z = pontuacao_tecnica # Cognição/Bloom (Aplicação e Análise)

# --- VISUALIZAÇÃO DO CUBO 3D ---
with col_cubo:
    vol_atual = (eixo_x + 1) * (eixo_y + 1) * (eixo_z + 1)
    
    X, Y, Z = np.mgrid[0:7, 0:7, 0:7]
    mask = (X <= eixo_x) & (Y <= eixo_y) & (Z <= eixo_z)
    
    fig = go.Figure(data=go.Volume(
        x=X.flatten(), y=Y.flatten(), z=Z.flatten(),
        value=mask.flatten().astype(float),
        isomin=0.1, isomax=1.0, opacity=0.5,
        surface_count=15, colorscale='Electric', showscale=False
    ))
    
    fig.update_layout(scene=dict(xaxis_title='Técnica', yaxis_title='Social', zaxis_title='Cognição'),
                      margin=dict(l=0, r=0, b=0, t=0), height=400)
    st.plotly_chart(fig, use_container_width=True)
    st.metric("Volume de Emancipação", f"V{int(vol_atual)}")

# --- FEEDBACK DIALÉTICO ---
st.divider()
if executar:
    st.write("### 📢 Feedback da IA Sinapse-br")
    if eixo_x == 6:
        st.success(f"**V{vol_atual}:** Sua espiral atingiu o nível de Práxis. A latência da segurança permitiu a transformação do ambiente.")
    else:
        st.error(f"**V{vol_atual}:** A espiral foi interrompida por falha de segurança. Lembre-se: no nível 6, o cuidado com a vida é latente em cada ação.")

st.markdown("---")
st.caption("Integração: Simulação de Alta Tensão + Rubrica Tridimensional.")
