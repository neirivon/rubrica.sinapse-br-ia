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
                  <div class="name" style="text-align:center;">Dra. Professora Thays Martins Vital da Silva</div>
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
    # Texto do TCC — seções com emojis
    # ---------------------------------
    st.markdown("---")

    st.markdown("## 1. Introdução ✍️")
    st.write(
        "A Educação Profissional e Tecnológica (EPT) desempenha papel essencial na formação integral do cidadão e no "
        "desenvolvimento regional sustentável. No entanto, persistem lacunas na forma como a avaliação formativa é "
        "conduzida, sobretudo quanto à equidade territorial e à contextualização pedagógica. Após a promulgação da LGPD, "
        "o acesso a microdados educacionais tornou-se mais restrito, dificultando análises aprofundadas por localidade, "
        "instituição e perfil socioeconômico.\n\n"
        "Nesse contexto, o presente TCC propõe a **Rubrica Educacional SINAPSE-BR IA**, instrumento de avaliação e "
        "reflexão docente fundamentado em **Neuropsicopedagogia**, **Taxonomia de Bloom revisada**, **Metodologias "
        "Ativas** e nas dimensões de **Equidade, Justiça e Inclusão (EJI)**. A rubrica é acompanhada de um **protótipo "
        "computacional interativo** — desenvolvido em Streamlit, com base em dados públicos do SISTEC e do INEP — que "
        "permite visualizar a **oferta real da EPT** nos municípios do **Triângulo Mineiro e Alto Paranaíba (TMAP)**, "
        "respeitando os recortes territoriais oficiais do **IBGE de 2010 e 2017/2022**.\n\n"
        "A proposta integra dados, fundamentos teóricos e práticas pedagógicas para apoiar **avaliação formativa** e "
        "**análise territorial**.\n\n"
        "**Questão central:** *Como uma rubrica neuropsicopedagógica, territorializada e orientada por dados abertos "
        "pode fortalecer a avaliação formativa na EPT do TMAP?*\n\n"
        "**Objetivo geral:** conceber e demonstrar a **Rubrica SINAPSE-BR IA** e o **aplicativo territorial** associado, "
        "contribuindo para uma cultura avaliativa mais justa, contextualizada e tecnicamente fundamentada."
    )

    st.markdown("## 2. Fundamentação Teórica 📚")
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

    st.markdown("## 3. Metodologia 🧪")
    st.write(
        "**Tipo de pesquisa:** teórico-propositiva, qualitativa e descritiva, com desenvolvimento de protótipo digital.\n\n"
        "### 3.1 Fontes e recorte de dados\n"
        "- **Relatório IPES Escolas (2020–2023)** — SISTEC\n"
        "- **Sistec Cursos Técnicos Ativos (12/09/2022)**\n"
        "- **Suplemento Cursos Técnicos 2024** — Censo Escolar/INEP\n\n"
        "### 3.2 Tratamento dos dados\n"
        "- Mapeamento **IBGE código → nome** do município (via suplemento 2024).\n"
        "- Normalização de cabeçalhos e valores; **nenhum dado inventado/estimado**.\n\n"
        "### 3.3 Protótipo (Streamlit)\n"
        "- **TMAP 2010:** TMAP → Municípios (estrutura histórica, 1990–2017).\n"
        "- **TMAP 2017/2022:** Municípios → Zona → Instituições EPT + **mapa Folium** e filtros.\n"
        "- Descoberta automática de colunas UF/Município, tradução de códigos IBGE e **filtros TMAP**.\n\n"
        "### 3.4 Rubrica SINAPSE-BR IA\n"
        "- **8 dimensões:** Cognitiva, Afetiva, Metodológica, Neurofuncional, Avaliativa, Tecnológica, Territorial e Inclusiva.\n"
        "- **4 níveis:** Emergente, Intermediário, Proficiente, Avançado.\n"
        "- **Duas versões:** Rubrica do Aluno (autorregulação) e do Professor (planejamento/reflexão).\n\n"
        "### 3.5 Validação e ética\n"
        "- Validação de conteúdo (juízes) + índice **Kappa** e revisão qualitativa.\n"
        "- Dados **públicos e anonimizados**, respeito à **LGPD**."
    )

    st.markdown("## 4. Produto Educacional 🖥️")
    st.write(
        "Aplicativo **SINAPSE-BR IA** em **Streamlit** com:\n"
        "- Menu lateral (logos IFTM e SINAPSE-BR).\n"
        "- Página de **Apresentação** (orientando + orientadora).\n"
        "- Páginas territoriais (2010 e 2017/2022): árvores de navegação, **mapa real**, filtros e **download CSV**.\n"
        "- Execução local e **Streamlit Cloud** (com `.env`, `.gitignore`, `requirements.txt`).\n"
        "- **Somente dados reais** (SISTEC/INEP)."
    )

    st.markdown("## 5. Resultados Esperados 🎯")
    st.write(
        "- Visualizações confiáveis da **rede EPT** no **TMAP**.\n"
        "- Identificação de **lacunas regionais** de oferta/infraestrutura.\n"
        "- Apoio ao docente na **avaliação formativa** (Bloom + metodologias ativas).\n"
        "- Ferramenta para gestores analisarem **equidade territorial** e oportunidades formativas.\n"
        "- Base para **instrumentos avaliativos personalizados**."
    )

    st.markdown("## 6. Discussão 💬")
    st.write(
        "A integração entre **dados abertos**, **pedagogia** e **territorialização** fortalece políticas públicas educacionais. "
        "O uso de dados reais garante **transparência e reprodutibilidade**, enquanto Neuropsicopedagogia e Bloom fornecem base "
        "para indicadores formativos. Limitações: ausência de coordenadas geográficas em partes do SISTEC; diferenças de nomenclatura; "
        "e necessidade de atualização constante. Ainda assim, a proposta é **viável** como modelo inicial de territorialização pedagógica da EPT."
    )

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

