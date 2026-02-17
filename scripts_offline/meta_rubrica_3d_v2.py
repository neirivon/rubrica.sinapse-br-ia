# Caminho completo: /home/neirivon/SINAPSE2.0/sinapsebr_rubrica/meta_rubrica_3d_v2.py
# Arquivo: meta_rubrica_3d_v2.py
# Meta-Rubrica SINAPSE-BR (Rubrica Avaliativa de Rubricas)
# Visualização em blocos 3D com hover bem evidente + painel de detalhes.

import streamlit as st

st.set_page_config(
    page_title="Meta-Rubrica SINAPSE-BR – 3D v2",
    layout="wide"
)

# ------------------------ DADOS DA META-RUBRICA -------------------------

DIMENSOES = [
    {
        "id": "clareza_criterios",
        "sigla": "CC",
        "titulo": "Clareza e adequação dos critérios",
        "cor": "#ffb347",
        "descricao": """
Avalia se os critérios da rubrica são específicos, objetivos, não ambíguos e adequados
ao produto/tarefa e à área de conhecimento.
""",
    },
    {
        "id": "distincao_niveis",
        "sigla": "DN",
        "titulo": "Distinção entre níveis de desempenho",
        "cor": "#ff6961",
        "descricao": """
Examina se os níveis (1–4) são nitidamente distintos e progressivos, permitindo
identificar evolução real de desempenho.
""",
    },
    {
        "id": "confiabilidade",
        "sigla": "CF",
        "titulo": "Confiabilidade interavaliador",
        "cor": "#77dd77",
        "descricao": """
Avalia se diferentes avaliadores, usando a mesma rubrica, tendem a chegar a resultados
semelhantes.
""",
    },
    {
        "id": "qualidade_redacao",
        "sigla": "QR",
        "titulo": "Qualidade da redação",
        "cor": "#aec6ff",
        "descricao": """
Considera se o texto da rubrica é claro, objetivo e compreensível para docentes e estudantes.
""",
    },
    {
        "id": "comunicacao_expect",
        "sigla": "CE",
        "titulo": "Comunicação de expectativas",
        "cor": "#fdfd96",
        "descricao": """
Analisa se a rubrica é usada para comunicar o que se espera do trabalho, antes e durante o processo.
""",
    },
    {
        "id": "participacao_discente",
        "sigla": "PD",
        "titulo": "Participação discente",
        "cor": "#ffb3e6",
        "descricao": """
Examina em que medida os estudantes participam da construção ou uso ativo da rubrica.
""",
    },
    {
        "id": "apoio_metacognicao",
        "sigla": "AM",
        "titulo": "Apoio à metacognição",
        "cor": "#baffc9",
        "descricao": """
Verifica se a rubrica estimula o estudante a refletir sobre o próprio processo de aprendizagem.
""",
    },
    {
        "id": "aderencia_teorica",
        "sigla": "AT",
        "titulo": "Aderência teórica (BNCC, Bloom, DUA, Neuro, CTC/EJI/ESCS)",
        "cor": "#cfcfff",
        "descricao": """
Avalia se a rubrica dialoga explicitamente com referenciais teóricos pertinentes à pesquisa.
""",
    },
    {
        "id": "aplicabilidade_uso",
        "sigla": "AU",
        "titulo": "Aplicabilidade e usabilidade",
        "cor": "#e0e0e0",
        "descricao": """
Verifica se a rubrica é viável na prática: tempo de aplicação, quantidade de critérios,
clareza operacional e adequação à EPT.
""",
    },
]

NIVEIS = [
    ("1 – Inaceitável",
     "A rubrica é inadequada, confusa ou desalinhada com o objetivo avaliativo."),
    ("2 – Aceitável",
     "Há alguma estrutura, mas com ambiguidade, lacunas ou fragilidades importantes."),
    ("3 – Bom/Sólido",
     "Rubrica clara e coerente, que permite avaliação formativa consistente."),
    ("4 – Exemplar",
     "Modelo de referência: criteriosamente construída, bem fundamentada e altamente funcional."),
]

# ------------------------ CSS – BLOCOS 3D + PAINEL -------------------------

st.markdown(
    """
    <style>
    .grid-3d {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 24px;
        margin-top: 16px;
    }

    .tile-link {
        text-decoration: none;
        color: inherit;
    }

    .tile-wrapper {
        text-align: center;
        font-family: sans-serif;
    }

    .tile {
        width: 110px;
        height: 70px;  /* base: bloco mais baixo */
        margin: 0 auto;
        border-radius: 10px;
        position: relative;
        transform-origin: bottom center;
        transform: perspective(800px) rotateX(55deg);
        box-shadow: 0 12px 18px rgba(0,0,0,0.30);
        transition: transform 0.25s ease, height 0.25s ease, box-shadow 0.25s ease;
    }

    .tile-inner {
        width: 100%;
        height: 100%;
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 900;
        font-size: 24px;
        color: #ffffff;
        text-shadow: 0 0 4px rgba(0,0,0,0.7);
    }

    /* HOVER forte: cresce MUITO e “vem pra frente” */
    .tile-wrapper:hover .tile {
        height: 150px;
        transform: perspective(800px) rotateX(55deg) translateY(-15px) scale(1.08);
        box-shadow: 0 28px 35px rgba(0,0,0,0.55);
    }

    .tile-label {
        margin-top: 10px;
        font-size: 13px;
        font-weight: 700;
        line-height: 1.2;
        min-height: 2.8em;
    }

    .tile-wrapper:hover .tile-label {
        font-size: 14px;
    }

    .painel {
        margin-top: 10px;
        border-radius: 14px;
        padding: 18px 22px;
        background: linear-gradient(90deg, #00151f, #003344);
        border: 2px solid #00e5ff;
        box-shadow: 0 0 18px rgba(0,229,255,0.6);
        color: #e0f7ff;
    }

    .painel h3 {
        margin-top: 0;
        color: #00e5ff;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------------ SELEÇÃO VIA QUERYSTRING -------------------------

params = st.experimental_get_query_params()
dim_id = params.get("dim", [DIMENSOES[0]["id"]])[0]
dim_sel = next(d for d in DIMENSOES if d["id"] == dim_id)

# ----------------------------- LAYOUT --------------------------------------

st.title("📕 Meta-Rubrica SINAPSE-BR – Visualização 3D (v2)")

st.markdown(
    """
Esta tela mostra as **9 dimensões** da Rubrica Avaliativa de Rubricas (Meta-Rubrica SINAPSE-BR)
como blocos 3D:

- passe o mouse sobre um bloco para vê-lo crescer (efeito 3D);
- clique no bloco para abrir a dimensão correspondente no painel à direita.
"""
)

col_esq, col_dir = st.columns([2, 3])

# -------- ESQUERDA: blocos 3D --------
with col_esq:
    st.markdown('<div class="grid-3d">', unsafe_allow_html=True)

    for dim in DIMENSOES:
        st.markdown('<div class="tile-wrapper">', unsafe_allow_html=True)

        st.markdown(
            f"""
            <a class="tile-link" href="?dim={dim['id']}">
                <div class="tile">
                    <div class="tile-inner" style="background:{dim['cor']};">
                        {dim['sigla']}
                    </div>
                </div>
                <div class="tile-label">{dim['titulo']}</div>
            </a>
            """,
            unsafe_allow_html=True,
        )

        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# -------- DIREITA: painel da dimensão selecionada --------
with col_dir:
    st.markdown(
        f"""
        <div class="painel">
            <h3>{dim_sel['sigla']} – {dim_sel['titulo']}</h3>
            <p>{dim_sel['descricao']}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("#### Níveis da Meta-Rubrica (1–4) para esta dimensão")
    st.table(
        {
            "Nível": [n[0] for n in NIVEIS],
            "Descrição": [n[1] for n in NIVEIS],
        }
    )

    st.write("#### Uso desta dimensão na pesquisa")
    st.markdown(
        """
- Apoiar a validação das rubricas **discente, docente e autoavaliativa** do SINAPSE-BR;  
- Servir como critério na análise por juízes especialistas;  
- Sustentar revisões sucessivas até que a rubrica atinja padrão **Bom/Sólido (3)** ou **Exemplar (4)** em todas as dimensões.
"""
    )

