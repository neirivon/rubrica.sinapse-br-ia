# --------------------------------------------------------------------------------------
# NOME DO ARQUIVO: permeabilidade_seletiva_svg.py
# CAMINHO COMPLETO SUGESTIVO: /home/neirivon/SINAPSE2.0/sinapsebr_rubrica/scripts/permeabilidade_seletiva_svg.py
# DESCRIÇÃO: Gera um diagrama vetorial (SVG) interativo comparando a Membrana Plasmática 
#            com a Seletividade Social na Educação Profissional.
# --------------------------------------------------------------------------------------

import streamlit as st
import streamlit.components.v1 as components

# Configuração da página para ocupar largura total (Melhor visualização do diagrama)
st.set_page_config(layout="wide", page_title="Analogia Biológica EPT")

st.markdown("## 🧬 A Permeabilidade Seletiva: A Escola como Membrana de Classe")
st.markdown("""
Esta representação visual utiliza o **Modelo do Mosaico Fluido** da biologia para explicar 
como a dualidade estrutural histórica atua filtrando o fluxo de estudantes entre as classes sociais 
e o mundo do trabalho/poder.
""")

# --- CÓDIGO DO DIAGRAMA VETORIAL (SVG) ---
# Este bloco HTML/SVG desenha a imagem diretamente no navegador
svg_diagram = """
<div style="width: 100%; display: flex; justify-content: center; background-color: #f8f9fa; border-radius: 10px; padding: 20px;">
<svg width="900" height="500" viewBox="0 0 900 500" xmlns="http://www.w3.org/2000/svg" style="font-family: 'Helvetica Neue', Arial, sans-serif;">

  <defs>
    <linearGradient id="gradSociedade" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#e1f5fe;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#b3e5fc;stop-opacity:1" />
    </linearGradient>
    
    <linearGradient id="gradEscola" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#fff9c4;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#fff59d;stop-opacity:1" />
    </linearGradient>

    <radialGradient id="gradLipidio" cx="40%" cy="40%" r="50%">
      <stop offset="0%" style="stop-color:#ffca28;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#ff6f00;stop-opacity:1" />
    </radialGradient>

    <filter id="sombra" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="3" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.2"/>
    </filter>
  </defs>

  <rect x="0" y="0" width="900" height="220" fill="url(#gradSociedade)" />
  <text x="20" y="40" fill="#01579b" font-size="22" font-weight="bold">MEIO EXTRACELULAR (A SOCIEDADE)</text>
  <text x="20" y="65" fill="#0277bd" font-size="14">Origem dos estudantes: Classe Trabalhadora e Elite</text>

  <rect x="0" y="280" width="900" height="220" fill="url(#gradEscola)" />
  <text x="20" y="450" fill="#f57f17" font-size="22" font-weight="bold">CITOPLASMA (MERCADO & PODER)</text>
  <text x="20" y="475" fill="#f9a825" font-size="14">Destinos: Chão de Fábrica, Serviços Técnicos ou Gestão/Academia</text>


  <g transform="translate(0, 220)">
    <rect x="0" y="0" width="900" height="60" fill="#ffe0b2" opacity="0.4"/>
    
    <g id="layerTop">
       <circle cx="20" cy="0" r="14" fill="url(#gradLipidio)" stroke="#e65100" stroke-width="1"/>
       <circle cx="50" cy="0" r="14" fill="url(#gradLipidio)" stroke="#e65100" stroke-width="1"/>
       <circle cx="80" cy="0" r="14" fill="url(#gradLipidio)" stroke="#e65100" stroke-width="1"/>
       <circle cx="110" cy="0" r="14" fill="url(#gradLipidio)" stroke="#e65100" stroke-width="1"/>
       <circle cx="140" cy="0" r="14" fill="url(#gradLipidio)" stroke="#e65100" stroke-width="1"/>
       <circle cx="350" cy="0" r="14" fill="url(#gradLipidio)" stroke="#e65100" stroke-width="1"/>
       <circle cx="380" cy="0" r="14" fill="url(#gradLipidio)" stroke="#e65100" stroke-width="1"/>
       <circle cx="410" cy="0" r="14" fill="url(#gradLipidio)" stroke="#e65100" stroke-width="1"/>
       <circle cx="440" cy="0" r="14" fill="url(#gradLipidio)" stroke="#e65100" stroke-width="1"/>
       <circle cx="470" cy="0" r="14" fill="url(#gradLipidio)" stroke="#e65100" stroke-width="1"/>
       <circle cx="680" cy="0" r="14" fill="url(#gradLipidio)" stroke="#e65100" stroke-width="1"/>
       <circle cx="710" cy="0" r="14" fill="url(#gradLipidio)" stroke="#e65100" stroke-width="1"/>
       <circle cx="740" cy="0" r="14" fill="url(#gradLipidio)" stroke="#e65100" stroke-width="1"/>
       <circle cx="770" cy="0" r="14" fill="url(#gradLipidio)" stroke="#e65100" stroke-width="1"/>
       <circle cx="800" cy="0" r="14" fill="url(#gradLipidio)" stroke="#e65100" stroke-width="1"/>
       <circle cx="830" cy="0" r="14" fill="url(#gradLipidio)" stroke="#e65100" stroke-width="1"/>
       <circle cx="860" cy="0" r="14" fill="url(#gradLipidio)" stroke="#e65100" stroke-width="1"/>
    </g>

    <g id="layerBottom" transform="translate(0, 60)">
       <circle cx="20" cy="0" r="14" fill="url(#gradLipidio)" stroke="#e65100" stroke-width="1"/>
       <circle cx="50" cy="0" r="14" fill="url(#gradLipidio)" stroke="#e65100" stroke-width="1"/>
       <circle cx="80" cy="0" r="14" fill="url(#gradLipidio)" stroke="#e65100" stroke-width="1"/>
       <circle cx="110" cy="0" r="14" fill="url(#gradLipidio)" stroke="#e65100" stroke-width="1"/>
       <circle cx="140" cy="0" r="14" fill="url(#gradLipidio)" stroke="#e65100" stroke-width="1"/>

       <circle cx="350" cy="0" r="14" fill="url(#gradLipidio)" stroke="#e65100" stroke-width="1"/>
       <circle cx="380" cy="0" r="14" fill="url(#gradLipidio)" stroke="#e65100" stroke-width="1"/>
       <circle cx="410" cy="0" r="14" fill="url(#gradLipidio)" stroke="#e65100" stroke-width="1"/>
       <circle cx="440" cy="0" r="14" fill="url(#gradLipidio)" stroke="#e65100" stroke-width="1"/>
       <circle cx="470" cy="0" r="14" fill="url(#gradLipidio)" stroke="#e65100" stroke-width="1"/>

       <circle cx="680" cy="0" r="14" fill="url(#gradLipidio)" stroke="#e65100" stroke-width="1"/>
       <circle cx="710" cy="0" r="14" fill="url(#gradLipidio)" stroke="#e65100" stroke-width="1"/>
       <circle cx="740" cy="0" r="14" fill="url(#gradLipidio)" stroke="#e65100" stroke-width="1"/>
       <circle cx="770" cy="0" r="14" fill="url(#gradLipidio)" stroke="#e65100" stroke-width="1"/>
       <circle cx="800" cy="0" r="14" fill="url(#gradLipidio)" stroke="#e65100" stroke-width="1"/>
       <circle cx="830" cy="0" r="14" fill="url(#gradLipidio)" stroke="#e65100" stroke-width="1"/>
       <circle cx="860" cy="0" r="14" fill="url(#gradLipidio)" stroke="#e65100" stroke-width="1"/>
    </g>
    
    <text x="850" y="35" text-anchor="end" font-weight="bold" fill="#bf360c" font-size="14">BARREIRA DE CLASSE</text>
    <text x="850" y="50" text-anchor="end" fill="#d84315" font-size="10">(Bicamada Lipídica)</text>
  </g>


  <g transform="translate(190, 180)" filter="url(#sombra)">
     <path d="M 0,0 Q -15,70 0,140 L 80,140 Q 95,70 80,0 Z" fill="#7e57c2" stroke="#512da8" stroke-width="2"/>
     <rect x="25" y="0" width="30" height="140" fill="#d1c4e9" opacity="0.7"/>
     
     <line x1="40" y1="-50" x2="40" y2="190" stroke="#311b92" stroke-width="4" stroke-dasharray="8,4" marker-end="url(#arrow)" />
     
     <text x="40" y="-60" text-anchor="middle" font-weight="bold" fill="#4527a0" font-size="16">ENSINO TÉCNICO</text>
     <text x="40" y="-40" text-anchor="middle" fill="#5e35b1" font-size="12">(Difusão Facilitada)</text>
     
     <text x="40" y="220" text-anchor="middle" fill="#4527a0" font-size="12" font-weight="bold">Mão de Obra Operacional</text>
  </g>


  <g transform="translate(530, 170)" filter="url(#sombra)">
     <path d="M 10,0 C -25,50 -15,160 10,160 L 90,160 C 115,160 125,50 90,0 Z" fill="#ef5350" stroke="#c62828" stroke-width="2"/>
     
     <text x="50" y="-50" text-anchor="middle" font-weight="bold" fill="#b71c1c" font-size="16">UNIVERSIDADE / PODER</text>
     <text x="50" y="-30" text-anchor="middle" fill="#c62828" font-size="12">(Transporte Ativo)</text>

     <path d="M 50,180 L 50,100" stroke="#b71c1c" stroke-width="4" marker-end="url(#arrowRed)"/>
     <text x="50" y="80" text-anchor="middle" fill="white" font-weight="bold" font-size="11">ACESSO RESTRITO</text>
     <text x="50" y="95" text-anchor="middle" fill="white" font-size="10">Exige "Capital" (ATP)</text>
  </g>

  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="10" refX="0" refY="3" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L0,6 L9,3 z" fill="#311b92" />
    </marker>
    <marker id="arrowRed" markerWidth="10" markerHeight="10" refX="0" refY="3" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L0,6 L9,3 z" fill="#b71c1c" />
    </marker>
  </defs>

</svg>
</div>
"""

# Renderiza o SVG no Streamlit
components.html(svg_diagram, height=550, scrolling=False)

# Legenda Explicativa
st.info("""
**Interpretação da Analogia:**
* **Difusão Facilitada (Ensino Técnico):** Um canal aberto que permite a passagem rápida dos filhos da classe trabalhadora, mas apenas para funções operacionais específicas (citoplasma).
* **Transporte Ativo (Universidade/Poder):** Uma passagem que exige gasto de energia ("ATP" = Capital Cultural e Financeiro). A proteína (Vestibular/Sistema) bombeia contra o gradiente, tornando o acesso difícil para quem não tem essa "energia" acumulada.
""")
