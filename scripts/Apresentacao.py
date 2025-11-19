# /home/neirivon/SINAPSE2.0/sinapsebr_rubrica/scripts/Apresentacao.py
# Página de apresentação do SINAPSE-BR IA (orientando + orientadora) com sidebar (IFTM + SINAPSE)
# OBS: Resolve caminhos de imagens subindo diretórios até achar assets/

import os
from pathlib import Path
from io import BytesIO
import base64
from PIL import Image, ImageDraw
import streamlit as st

# ---------------------------------
# Config da página
# ---------------------------------
st.set_page_config(
    page_title="SINAPSE-BR IA — Apresentação",
    page_icon="🧠",
    layout="wide",
)

# ---------------------------------
# Localizador robusto de assets
# ---------------------------------
THIS = Path(__file__).resolve()

def find_project_root(start: Path, marker_folder: str = "assets") -> Path:
    """
    Sobe diretórios até encontrar uma pasta 'assets' (marcador do projeto).
    Retorna o diretório onde 'assets' foi encontrado; se não encontrar,
    retorna o diretório do arquivo atual.
    """
    p = start
    for _ in range(6):  # sobe até 6 níveis
        if (p / marker_folder).exists():
            return p
        if p.parent == p:
            break
        p = p.parent
    return start

# se o script estiver em /scripts, o root será o pai que contém /assets
PROJECT_ROOT = find_project_root(THIS.parent)
ASSETS_DIR   = PROJECT_ROOT / "assets"
IMG_DIR      = ASSETS_DIR / "imagens"
LOGO_DIR     = ASSETS_DIR / "logos"

NEIRIVON_IMG     = IMG_DIR / "neirivon.png"
ORIENTADORA_IMG  = IMG_DIR / "Orientadora.png"
LOGO_IFTM        = LOGO_DIR / "IFTM_360.png"
LOGO_SINAPSE     = LOGO_DIR / "sinapse.png"

# ---------------------------------
# Utilitários de imagem / HTML
# ---------------------------------
def img_circular_b64(img_path: Path, size: int = 200) -> str:
    """Converte imagem em avatar circular (base64)."""
    img = Image.open(img_path).convert("RGBA").resize((size, size))
    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size, size), fill=255)
    img.putalpha(mask)
    buff = BytesIO()
    img.save(buff, format="PNG")
    return base64.b64encode(buff.getvalue()).decode("utf-8")

def tag_html(texto: str, cls: str = "") -> str:
    cls_attr = f' class="{cls}"' if cls else ""
    return f"<div{cls_attr}>{texto}</div>"

def safe_image(path: Path, *, width: int | None = None, caption: str | None = None):
    """Exibe imagem se existir; caso contrário, mostra um aviso discreto."""
    try:
        if path.exists():
            st.image(str(path), width=width, caption=caption)
        else:
            st.warning(f"Imagem não encontrada: `{path.as_posix()}`")
    except Exception as e:
        st.error(f"Não foi possível carregar a imagem `{path.name}`. Detalhe: {e}")

# ---------------------------------
# CSS leve
# ---------------------------------
st.markdown(
    """
    <style>
      .hero { background:#eef6ff; border:1px solid #d0e2f0; padding:18px 22px; border-radius:14px; margin-bottom:18px; }
      .sec-title { font-weight:700; font-size:28px; margin:2px 0 8px 0; }
      .emoji-chip { display:inline-block; padding:2px 10px; background:#f1f5f9; border:1px solid #e2e8f0; border-radius:999px; font-size:15px; }
      .avatar-wrap { display:flex; flex-direction:column; align-items:flex-start; gap:8px; }
      .avatar { width:200px; height:200px; border-radius:50%; box-shadow:0 2px 10px rgba(0,0,0,.10); }
      .name { font-weight:600; font-size:20px; }
      .role { font-size:16px; color:#334155; }
      .indent { margin-left:12px; }
      .stMarkdown, p, li, span { font-size:18px; }
      .side-caption { font-size:12.5px; color:#475569; }
      .box-content { border-left: 5px solid #2563eb; padding-left: 15px; margin-bottom: 20px; }
      /* pequenos hovers */
      img.avatar:hover { transform: scale(1.02); transition: transform .15s ease; }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------------------------
# SIDEBAR — IFTM (topo), marcador da página, SINAPSE (rodapé)
# ---------------------------------
with st.sidebar:
    safe_image(LOGO_IFTM, width=130)
    st.markdown("---")
    st.markdown("### 📑 Apresentação")
    st.caption("Visão geral do TCC, equipe e referências iniciais.")
    st.markdown("---")
    safe_image(LOGO_SINAPSE, width=200)
    st.markdown('<div class="side-caption">SINAPSE-BR • Sistema Integrado Neuropsicopedagógico</div>', unsafe_allow_html=True)

# ---------------------------------
# Cabeçalho
# ---------------------------------
st.markdown(tag_html("🧠 SINAPSE-BR IA — Rubrica Avaliativa Interpretativa para a EPT", "hero sec-title"), unsafe_allow_html=True)

# ---------------------------------
# Layout (conteúdo)
# ---------------------------------
col_side, col_main = st.columns([0.18, 0.82])

with col_main:
    # -------- Orientando --------
    st.markdown(tag_html("🧑‍🎓 Orientando", "emoji-chip"), unsafe_allow_html=True)

    if NEIRIVON_IMG.exists():
        try:
            b64_neirivon = img_circular_b64(NEIRIVON_IMG, size=200)
            st.markdown(
                f"""
                <div class="avatar-wrap">
                  <img class="avatar" src="data:image/png;base64,{b64_neirivon}" alt="Neirivon Elias Cardoso" />
                  <div class="name">Neirivon Elias Cardoso</div>
                </div>
                """,
                unsafe_allow_html=True
            )
        except Exception as e:
            st.warning(f"Falha ao processar a foto do orientando: {e}. Exibindo imagem direta.")
            st.image(str(NEIRIVON_IMG), width=200, caption="Neirivon Elias Cardoso")
    else:
        st.error(f"Imagem não encontrada: {NEIRIVON_IMG}")
        st.markdown("**Dica:** coloque a foto em `assets/imagens/neirivon.png`.")

    st.divider()

    # -------- Orientadora --------
    st.markdown(tag_html("👩‍🏫 Orientadora", "emoji-chip"), unsafe_allow_html=True)

    if ORIENTADORA_IMG.exists():
        try:
            b64_orient = img_circular_b64(ORIENTADORA_IMG, size=200)
            st.markdown(
                f"""
                <div class="avatar-wrap indent">
                  <img class="avatar" src="data:image/png;base64,{b64_orient}" alt="Dra. Professora Thays Martins Vital da Silva" />
                  <div class="name">Dra. Professora Thays Martins Vital da Silva</div>
                  <div class="role">Orientadora do TCC</div>
                </div>
                """,
                unsafe_allow_html=True
            )
        except Exception as e:
            st.warning(f"Falha ao processar a foto da orientadora: {e}. Exibindo imagem direta.")
            st.image(str(ORIENTADORA_IMG), width=200, caption="Dra. Professora Thays Martins Vital da Silva")
    else:
        st.error(f"Imagem não encontrada: {ORIENTADORA_IMG}")
        st.markdown("**Dica:** coloque a foto em `assets/imagens/Orientadora.png`.")

    # ---------------------------------
    # Estrutura do TCC (Reorganizada)
    # ---------------------------------
    st.markdown("---")
    
    # ---------------------------------
    # SEÇÃO 0: TEMA, DELIMITAÇÃO e PROBLEMA (Simplificado para evitar erro no Streamlit Cloud)
    # ---------------------------------
    with st.expander("📚 Núcleo da Proposta (TEMA, PROBLEMA e DELIMITAÇÃO)", expanded=False):
        st.markdown("### TEMA")
        # --- ALTERADO: Usando st.info em vez de tag_html para estabilidade no DOM ---
        st.info(
            "Desenvolvimento de uma rubrica educacional ampliada para avaliação formativa na Educação Profissional e Tecnológica (EPT), "
            "integrando referenciais da Neuropsicopedagogia, Taxonomias Cognitivas e Desenho Universal para a Aprendizagem (DUA)."
        )
        
        st.markdown("### PROBLEMA DE PESQUISA")
        # --- ALTERADO: Usando st.code/st.info em vez de tag_html para estabilidade no DOM ---
        st.code(
            "Como integrar princípios da Neuropsicopedagogia, das Taxonomias Cognitivas, do Desenho Universal para a Aprendizagem (DUA) e da equidade socio-territorial em uma rubrica formativa aplicável à Educação Profissional e Tecnológica?",
            language="markdown"
        )

        st.markdown("### DELIMITAÇÃO DO TEMA")
        st.write(
            "O estudo concentra-se na construção teórico-propositiva da **Rubrica SINAPSE-BR IA**, concebida para qualificar práticas avaliativas na Rede Federal de Educação Profissional e Tecnológica, com ênfase no recorte territorial do **Triângulo Mineiro e Alto Paranaíba (TMAP)**. A pesquisa utiliza documentos oficiais (BNCC, SAEB, PISA/OCDE, DCNs da EPT) e referenciais contemporâneos para fundamentar a rubrica."
        )

    st.markdown("---")

    # ---------------------------------
    # SEÇÃO 1: INTRODUÇÃO (Usando Tabs para Justificativa e Objetivos)
    # ---------------------------------
    st.markdown("## 1. Introdução & Estratégia da Pesquisa ✍️")
    
    tab_justificativa, tab_objetivos, tab_sinapse_ia = st.tabs([
        "✅ Justificativa", 
        "🎯 Objetivos", 
        "🧠 Visão Geral do SINAPSE-BR IA"
    ])

    with tab_justificativa:
        st.markdown("### Por Que SINAPSE-BR IA?")
        st.write(
            "A avaliação na Educação Profissional e Tecnológica apresenta desafios relacionados à clareza dos critérios, à personalização das aprendizagens e à equidade territorial. As rubricas atualmente disponíveis — como BNCC, SAEB e PISA/OCDE — **não contemplam plenamente as especificidades da EPT** nem integram referenciais inclusivos como a **Neuropsicopedagogia**, o **Desenho Universal para a Aprendizagem (DUA)**, e as Taxonomias de Bloom e SOLO.\n\n"
            "A criação da Rubrica SINAPSE-BR IA busca integrar esses fundamentos em um instrumento coerente, formativo e sensível às realidades socioeducacionais do TMAP, contribuindo para práticas avaliativas mais justas e alinhadas às demandas contemporâneas do ensino profissional."
        )

    with tab_objetivos:
        st.markdown("### Objetivo Geral")
        st.write(
            "Desenvolver uma rubrica educacional ampliada — denominada **SINAPSE-BR IA** — fundamentada na Neuropsicopedagogia, no Desenho Universal para a Aprendizagem (DUA), nas Taxonomias de Bloom e SOLO e em referenciais de equidade territorial (CTC/EJI/ESCS), com vistas a aprimorar as práticas avaliativas na Educação Profissional e Tecnológica e favorecer trajetórias formativas mais justas no contexto do **Triângulo Mineiro e Alto Paranaíba (TMAP)**."
        )
        st.markdown("### Objetivos Específicos")
        st.markdown("""
            * **1.** Analisar os referenciais teóricos da Neuropsicopedagogia, do DUA, das Taxonomias de Bloom e SOLO, das Metodologias Ativas e dos modelos de avaliação utilizados no SAEB, BNCC e PISA/OCDE.
            * **2.** Comparar estruturas de rubricas nacionais e internacionais (Andrade, Brookhart, Mullinix, Moskal) a fim de identificar critérios, fragilidades e lacunas que fundamentem a criação da Rubrica SINAPSE-BR IA.
            * **3.** Propor a estrutura final da Rubrica SINAPSE-BR IA (dimensões, níveis e descritores), articulando fundamentos pedagógicos, neurocientíficos e socio-territoriais aplicáveis à Educação Profissional e Tecnológica.
        """)
        
    with tab_sinapse_ia:
        st.markdown("### Sobre o Protótipo SINAPSE-BR IA")
        st.write(
            "O presente TCC propõe a **Rubrica Educacional SINAPSE-BR IA**, instrumento de avaliação e reflexão docente fundamentado nos pilares descritos acima. A rubrica é acompanhada de um **protótipo computacional interativo** — desenvolvido em Streamlit, com base em dados públicos do SISTEC e do INEP — que permite visualizar a **oferta real da EPT** nos municípios do TMAP, respeitando os recortes territoriais oficiais do IBGE de 2010 e 2017/2022. "
        )
        st.markdown("**Proposta:** integrar dados, fundamentos teóricos e práticas pedagógicas para apoiar **avaliação formativa** e **análise territorial**.")

    st.markdown("---")

    # ---------------------------------
    # SEÇÃO 2: FUNDAMENTAÇÃO TEÓRICA (Corrigindo o erro de digitação com &nbsp;)
    # ---------------------------------
    st.markdown("## 2. Fundamentação Teórica&nbsp;📚") # SOLUÇÃO DE COMPATIBILIDADE
    st.write(
        "**Neuropsicopedagogia:** oferece base para compreender processos cognitivos, afetivos e motivacionais, "
        "favorecendo práticas avaliativas humanas e formativas.\n\n"
        "**Taxonomia de Bloom revisada (Anderson & Krathwohl, 2001):** organiza níveis cognitivos "
        "(lembrar, compreender, aplicar, analisar, avaliar e criar) para estruturação de descritores/indicadores de rubricas.\n\n"
        "**Metodologias Ativas:** PBL, Aprendizagem por Projetos e Gamificação promovem autonomia, colaboração e criatividade, "
        "integradas aos níveis de Bloom.\n\n"
        "**Territorialização:** base nas definições oficiais do IBGE (2010; 2017/2022) — meso/micro e regiões intermediárias/imediatas — "
        "para compreender a distribuição espacial da EPT e apoiar a equidade.\n\n"
        "A **Rubrica Educacional** é entendida como instrumento com **dimensões, níveis e evidências observáveis**; a SINAPSE-BR IA a "
        "amplia ao incorporar **variáveis territoriais e cognitivas**."
    )

    st.markdown("---")

    # ---------------------------------
    # SEÇÃO 3: METODOLOGIA (Agora como Abas para as etapas)
    # ---------------------------------
    st.markdown("## 3. Metodologia 🧪")
    st.write("**Tipo de pesquisa:** teórico-propositiva, qualitativa e descritiva, com desenvolvimento de protótipo digital.")
    
    tab_revisao, tab_analise, tab_construcao = st.tabs([
        "1. Revisão Sistemática", 
        "2. Análise Documental", 
        "3. Construção Propositiva"
    ])
    
    with tab_revisao:
        st.markdown("### 1. Revisão Bibliográfica Sistemática")
        st.markdown("""
        Serão estudados referenciais clássicos e contemporâneos sobre:
        * **Neuropsicopedagogia** (Flavell, Piaget, Vigotski, Nicolelis, Seung)
        * **Avaliação Formativa** (Bloom, Black & Wiliam, Brookhart, Hoffmann)
        * **Rubricas e Meta-Rubricas** (Mullinix, Andrade, Moskal, Panadero & Jonsson)
        * **Metodologias Ativas** (Bacich & Moran)
        * **DUA** (CAST; Rose & Meyer)
        * **EPT** (Frigotto, Ciavatta, Ramos) e documentos avaliativos (SAEB, BNCC, PISA/OCDE).
        """)
        st.caption("Esta etapa visa consolidar o embasamento que sustenta a proposta da Rubrica SINAPSE-BR IA.")

    with tab_analise:
        st.markdown("### 2. Análise Documental Comparativa")
        st.markdown("""
        Serão analisados documentos oficiais e modelos avaliativos, incluindo:
        * BNCC, SAEB, PISA/OCDE, Diretrizes da EPT.
        * DUA, rubricas nacionais e internacionais (Andrade; Brookhart; Mullinix; Moskal).
        * Materiais normativos da Rede Federal.
        """)
        st.caption("A análise busca identificar convergências, divergências e lacunas que justifiquem a necessidade de uma rubrica integradora adequada ao contexto da Educação Profissional e Tecnológica, especialmente no TMAP.")

    with tab_construcao:
        st.markdown("### 3. Construção Propositiva da Rubrica SINAPSE-BR IA")
        st.write(
            "Será elaborada a versão final da rubrica (dimensões, níveis e descritores), integrando fundamentos neurocientíficos, pedagógicos e socio-territoriais. A rubrica será organizada para favorecer práticas avaliativas formativas, inclusivas e alinhadas à realidade da EPT. Serão indicadas, ainda, possibilidades de aplicação prática futura no contexto educacional da região TMAP."
        )

    st.markdown("### 3.4 Fontes de Dados do Protótipo")
    st.markdown("""
        * **Relatório IPES Escolas (2020–2023)** — SISTEC
        * **Sistec Cursos Técnicos Ativos (12/09/2022)**
        * **Suplemento Cursos Técnicos 2024** — Censo Escolar/INEP
    """)
    st.write("Mapeamento IBGE, normalização de cabeçalhos e valores; **nenhum dado inventado/estimado**.")
    
    st.markdown("---")

    st.markdown("## 4. Produto Educacional 🖥️")
    st.write(
        "Aplicativo **SINAPSE-BR IA** em **Streamlit** com:\n"
        "- Menu lateral (logos IFTM e SINAPSE-BR).\n"
        "- Página de **Apresentação** (orientando + orientadora).\n"
        "- Páginas territoriais (2010 e 2017/2022): árvores de navegação, **mapa real**, filtros e **download CSV**.\n"
        "- Execução local e **Streamlit Cloud** (com `.env`, `.gitignore`, `requirements.txt`).\n"
        "- **Somente dados reais** (SISTEC/INEP)."
    )

    st.markdown("---")

    st.markdown("## 5. Resultados Esperados 🎯")
    st.write(
        "- Visualizações confiáveis da **rede EPT** no **TMAP**.\n"
        "- Identificação de **lacunas regionais** de oferta/infraestrutura.\n"
        "- Apoio ao docente na **avaliação formativa** (Bloom + metodologias ativas).\n"
        "- Ferramenta para gestores analisarem **equidade territorial** e oportunidades formativas.\n"
        "- Base para **instrumentos avaliativos personalizados**."
    )

    st.markdown("---")

    st.markdown("## 6. Discussão 💬")
    st.write(
        "A integração entre **dados abertos**, **pedagogia** e **territorialização** fortalece políticas públicas educacionais. "
        "O uso de dados reais garante **transparência e reprodutibilidade**, enquanto Neuropsicopedagogia e Bloom fornecem base "
        "para indicadores formativos. Limitações: ausência de coordenadas geográficas em partes do SISTEC; diferenças de nomenclatura; "
        "e necessidade de atualização constante. Ainda assim, a proposta é **viável** como modelo inicial de territorialização pedagógica da EPT."
    )

    st.markdown("---")

    st.markdown("## 7. Considerações Finais ✅")
    st.write(
        "A **Rubrica SINAPSE-BR IA** avança na integração entre **dados educacionais**, **práticas avaliativas** e "
        "**fundamentos neuropsicopedagógicos**. O protótipo digital oferece uma nova leitura da EPT sob a ótica da **equidade**, "
        "da **cognição** e da **territorialização**.\n\n"
        "**Trabalhos futuros:** expandir para **todo MG**; validação empírica com docentes; integrar SAEB/PISA; "
        "e publicar como **Recurso Educacional Digital (RED)**.\n\n"
        "Contribui para a **docência**, a **gestão educacional** e uma cultura avaliativa pautada em **neurociência**, "
        "**dados** e **justiça educacional**."
    )

# ---------------------------------
# Rodapé
# ---------------------------------
st.markdown("---")
st.caption(
    f"Root detectado: `{PROJECT_ROOT}` • Imagens: `{IMG_DIR}` • "
    "Caminhos relativos compatíveis com execução local e Streamlit Cloud."
)
