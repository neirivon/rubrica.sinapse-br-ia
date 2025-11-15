# Caminho completo: /home/neirivon/SINAPSE2.0/sinapsebr_rubrica/meta_rubrica_neon.py
# Arquivo: meta_rubrica_neon.py
# Visualização da Meta-Rubrica SINAPSE-BR (Rubrica Avaliativa de Rubricas)
# Estilo "tabela periódica 3D": barras verticais + painel neon com detalhes.

import streamlit as st

st.set_page_config(
    page_title="Meta-Rubrica SINAPSE-BR – Neon 3D",
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
ao produto/tarefa e à área de conhecimento. É a base para justiça, transparência
e alinhamento pedagógico.
""",
    },
    {
        "id": "distincao_niveis",
        "sigla": "DN",
        "titulo": "Distinção entre níveis de desempenho",
        "cor": "#ff6961",
        "descricao": """
Examina se os níveis (1–4) são nitidamente distintos e progressivos, permitindo
identificar evolução real de desempenho em vez de mudanças apenas cosméticas de linguagem.
""",
    },
    {
        "id": "confiabilidade",
        "sigla": "CF",
        "titulo": "Confiabilidade interavaliador",
        "cor": "#77dd77",
        "descricao": """
Avalia se diferentes avaliadores, usando a mesma rubrica, tendem a chegar a resultados
semelhantes. Alta confiabilidade indica critérios bem definidos e uso consistente da rubrica.
""",
    },
    {
        "id": "qualidade_redacao",
        "sigla": "QR",
        "titulo": "Qualidade da redação",
        "cor": "#aec6ff",
        "descricao": """
Considera se o texto da rubrica é claro, objetivo e compreensível para docentes,
estudantes e avaliadores externos, evitando jargões, ambiguidade e termos vagos.
""",
    },
    {
        "id": "comunicacao_expect",
        "sigla": "CE",
        "titulo": "Comunicação de expectativas",
        "cor": "#fdfd96",
        "descricao": """
Analisa se a rubrica é efetivamente usada para comunicar o que se espera do trabalho
antes e durante o processo, servindo como referência para orientar a produção dos estudantes.
""",
    },
    {
        "id": "participacao_discente",
        "sigla": "PD",
        "titulo": "Participação discente",
        "cor": "#ffb3e6",
        "descricao": """
Examina em que medida os estudantes participam da construção, revisão ou uso ativo
da rubrica (exemplos, sugestões, autoavaliação, avaliação por pares).
""",
    },
    {
        "id": "apoio_metacognicao",
        "sigla": "AM",
        "titulo": "Apoio à metacognição",
        "cor": "#baffc9",
        "descricao": """
Verifica se a rubrica estimula o estudante a refletir sobre o próprio processo
de aprendizagem, identificando forças, fragilidades e próximos passos.
""",
    },
    {
        "id": "aderencia_teorica",
        "sigla": "AT",
        "titulo": "Aderência teórica (BNCC, Bloom, DUA, Neuro, CTC/EJI/ESCS)",
        "cor": "#cfcfff",
        "descricao": """
Avalia se a rubrica dialoga explicitamente com referenciais teóricos pertinentes
à pesquisa (BNCC, Taxonomia de Bloom, DUA, neuropsicopedagogia, pertencimento
e equidade territorial – CTC/EJI/ESCS).
""",
    },
    {
        "id": "aplicabilidade_uso",
        "sigla": "AU",
        "titulo": "Aplicabilidade e usabilidade",
        "cor": "#e0e0e0",
        "descricao": """
Verifica se a rubrica é viável na prática: tempo de aplicação, quantidade de critérios,
clareza operacional, adequação à EPT e utilidade para feedback formativo.
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

# ------------------------ ESTADO DE NAVEGAÇÃO -------------------------

if "dimensao_selecionada" not in st.session_state:
    st.session_state.dimensao_selecionada = DIMENSOES[0]["id"]  # começa na 1ª

# ------------------------ CSS – ESTILO TABELA 3D ----------------------

st.markdown(
    """
    <style>
    .barra-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 18px;
        margin-top: 20px;
    }

    .barra-wrapper {
        text-align: center;
        font-family: sans-serif;
    }

    .barra3d {
        width: 90px;
        height: 80px; /* altura base (1 "andar") */
        margin: 0 auto;
        border-radius: 8px;
        position: relative;
        transform-origin: bottom center;
        transform: perspective(700px) rotateX(60deg);
        box-shadow: 0 18px 22px rgba(0,0,0,0.30);
        transition: height 0.25s ease, transform 0.25s ease, box-shadow 0.25s ease;
        cursor: pointer;
    }

    .barra3d-inner {
        width: 100%;
        height: 100%;
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 800;
        color: #ffffff;
        text-shadow: 0 0 4px rgba(0,0,0,0.7);
        font-size: 22px;
    }

    .barra-wrapper:hover .barra3d {
        height: 160px;  /* cresce (como no vídeo do Ne) */
        transform: perspective(700px) rotateX(60deg) translateY(-10px) scale(1.05);
        box-shadow: 0 30px 35px rgba(0,0,0,0.45);
    }

    .barra-label {
        margin-top: 10px;
        font-size: 13px;
        font-weight: 700;
    }

    .barra-wrapper:hover .barra-label {
        font-size: 14px;
    }

    /* Painel neon à direita */
    .painel-neon {
        border-radius: 12px;
        padding: 18px 22px;
        margin-top: 12px;
        background: rgba(5, 20, 40, 0.92);
        border: 2px solid #00e5ff;
        box-shadow: 0 0 18px rgba(0, 229, 255, 0.7);
        color: #e0f7ff;
    }

    .painel-neon h3 {
        margin-top: 0;
        color: #00e5ff;
    }

    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------------ FUNÇÕES DE INTERFACE ------------------------


def mostrar_barras():
    st.markdown("### Dimensões da Meta-Rubrica SINAPSE-BR (visão tipo tabela periódica 3D)")

    st.markdown('<div class="barra-grid">', unsafe_allow_html=True)

    for dim in DIMENSOES:
        selecionada = (dim["id"] == st.session_state.dimensao_selecionada)

        border_extra = "box-shadow: 0 0 15px rgba(255,255,255,0.8);" if selecionada else ""

        st.markdown('<div class="barra-wrapper">', unsafe_allow_html=True)

        # bloco 3D
        st.markdown(
            f"""
            <div class="barra3d" style="{border_extra}">
                <div class="barra3d-inner" style="background:{dim['cor']};">
                    {dim['sigla']}
                </div>
            </div>
            <div class="barra-label">{dim['titulo']}</div>
            """,
            unsafe_allow_html=True,
        )

        # botão para selecionar dimensão (drill-down)
        if st.button("Selecionar", key=f"btn_{dim['id']}"):
            st.session_state.dimensao_selecionada = dim["id"]

        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)


def mostrar_painel():
    dim = next(d for d in DIMENSOES if d["id"] == st.session_state.dimensao_selecionada)

    st.markdown(
        f"""
        <div class="painel-neon">
            <h3>{dim['sigla']} – {dim['titulo']}</h3>
            <p>{dim['descricao']}</p>
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


# ----------------------------- LAYOUT ---------------------------------

st.title("📕 Meta-Rubrica SINAPSE-BR – Visualização Neon 3D")

st.markdown(
    """
Esta tela simula uma espécie de **“tabela periódica 3D”** para a Rubrica Avaliativa de Rubricas (Meta-Rubrica SINAPSE-BR):

- cada bloco colorido representa **uma dimensão** da meta-rubrica;  
- o bloco cresce e se destaca ao passar o mouse (efeito “prédio 3D”);  
- ao clicar em **Selecionar**, o painel neon à direita mostra descritores e níveis (1–4).
"""
)

col_barras, col_painel = st.columns([2, 3])

with col_barras:
    mostrar_barras()

with col_painel:
    mostrar_painel()

