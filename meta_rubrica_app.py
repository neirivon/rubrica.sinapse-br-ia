# Caminho completo: /home/neirivon/SINAPSE2.0/sinapsebr_rubrica/meta_rubrica_barras.py
# Arquivo: meta_rubrica_barras.py
# Meta-Rubrica SINAPSE-BR (Rubrica Avaliativa de Rubricas)
# Visualização em formato de "barras 3D" com efeito de mouseover e drill-down em Streamlit.

import streamlit as st

st.set_page_config(
    page_title="Meta-Rubrica SINAPSE-BR – Barras 3D",
    layout="wide"
)

# --------------------------------------------------------------------
# Estado: qual dimensão está selecionada
# --------------------------------------------------------------------
if "dimensao_selecionada" not in st.session_state:
    st.session_state.dimensao_selecionada = None  # None = visão geral


# --------------------------------------------------------------------
# CSS – barras verticais com efeito de “crescer” no hover (quase 3D)
# --------------------------------------------------------------------
st.markdown(
    """
    <style>
    .barras-container {
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: flex-end;
        gap: 18px;
        margin-top: 30px;
        margin-bottom: 40px;
        min-height: 260px;
    }

    .barra-wrapper {
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 120px;
    }

    .barra {
        width: 90px;
        height: 140px; /* altura base, cresce no hover */
        border-radius: 18px 18px 6px 6px;
        background: linear-gradient(180deg, rgba(255,255,255,0.85), rgba(0,0,0,0.08));
        position: relative;
        box-shadow: 0 10px 18px rgba(0,0,0,0.18);
        transition: transform 0.25s ease, box-shadow 0.25s ease, height 0.25s ease;
        transform-origin: bottom center;
        cursor: pointer;
        border: 1px solid rgba(0,0,0,0.12);
    }

    .barra:hover {
        height: 210px; /* a barra “cresce” como se fosse um gráfico */
        transform: translateY(-8px) scale(1.03);
        box-shadow: 0 24px 35px rgba(0,0,0,0.30);
    }

    .barra-label {
        margin-top: 10px;
        text-align: center;
        font-size: 13px;
        font-weight: bold;
    }

    /* Cores específicas por dimensão */
    .dim-clareza       { background: linear-gradient(180deg, #ffe6e6, #ff9999); }
    .dim-niveis        { background: linear-gradient(180deg, #fff6d6, #ffd24d); }
    .dim-confiabilidade{ background: linear-gradient(180deg, #e3ecff, #8cb3ff); }
    .dim-aplicabilidade{ background: linear-gradient(180deg, #e6ffe6, #66cc99); }

    </style>
    """,
    unsafe_allow_html=True,
)

# --------------------------------------------------------------------
# Dados – exemplo com 4 dimensões (você pode expandir para 9)
# --------------------------------------------------------------------
DIMENSOES = [
    {
        "id": "clareza_criterios",
        "titulo": "Clareza dos Critérios",
        "classe_css": "dim-clareza",
        "descricao": """
Avalia se os critérios da rubrica são específicos, objetivos, não ambíguos e compreensíveis
por estudantes, docentes e avaliadores. Quanto maior a clareza, maior a transparência
e a justiça na avaliação.
""",
        "exemplos": """
• Exemplo fraco: “O aluno deve demonstrar conhecimento do conteúdo.” (vago, genérico).  
• Exemplo forte: “O estudante compara, explica e aplica os conceitos X e Y em situações
autênticas do contexto da EPT, justificando suas escolhas com argumentos próprios.”
""",
    },
    {
        "id": "distincao_niveis",
        "titulo": "Distinção entre os Níveis",
        "classe_css": "dim-niveis",
        "descricao": """
Avalia se os níveis (1, 2, 3 e 4) apresentam diferenças claras, progressivas e coerentes.
Uma boa rubrica permite perceber evolução real do desempenho, e não apenas mudanças
de adjetivos.
""",
        "exemplos": """
• Exemplo ruim: todos os níveis usam quase a mesma frase, mudando apenas “bom, muito bom, excelente”.  
• Exemplo bom: 1 “reconhece”, 2 “explica”, 3 “analisa”, 4 “cria/propõe soluções”.
""",
    },
    {
        "id": "confiabilidade",
        "titulo": "Confiabilidade entre Avaliadores",
        "classe_css": "dim-confiabilidade",
        "descricao": """
Avalia se diferentes avaliadores, usando a mesma rubrica, tendem a atribuir resultados
semelhantes. Alta confiabilidade indica critérios bem definidos e formação adequada dos avaliadores.
""",
        "exemplos": """
• Exemplo: dois professores avaliam a mesma atividade com a mesma rubrica e obtêm notas muito próximas,
com justificativas convergentes para os níveis atribuídos.
""",
    },
    {
        "id": "aplicabilidade",
        "titulo": "Aplicabilidade / Usabilidade",
        "classe_css": "dim-aplicabilidade",
        "descricao": """
Avalia se a rubrica é viável de ser aplicada no cotidiano da EPT: tempo de preenchimento,
linguagem objetiva, foco nos aspectos essenciais da tarefa e alinhamento com a carga de trabalho docente.
""",
        "exemplos": """
• Exemplo ruim: rubrica com 40 indicadores para uma atividade simples, inviável de usar com várias turmas.  
• Exemplo bom: rubrica com poucos critérios centrais, clara e possível de aplicar com toda a turma.
""",
    },
]


# --------------------------------------------------------------------
# Tela 1 – Visão geral (barras)
# --------------------------------------------------------------------
def mostrar_home():
    st.title("📕 Meta-Rubrica SINAPSE-BR – Visualização em Barras")

    st.markdown(
        """
Esta visualização apresenta a **Rubrica Avaliativa de Rubricas (Meta-Rubrica SINAPSE-BR)** em formato de
<b>barras interativas</b>, aproximando-se da estética de um gráfico de barras 3D:

- Cada barra representa uma dimensão da meta-rubrica;
- Ao passar o mouse, a barra “cresce” e se destaca;
- Ao clicar no botão abaixo da barra, você acessa a página detalhada da dimensão selecionada.
""",
        unsafe_allow_html=True,
    )

    st.markdown('<div class="barras-container">', unsafe_allow_html=True)

    # Renderiza barras lado a lado
    for dim in DIMENSOES:
        st.markdown('<div class="barra-wrapper">', unsafe_allow_html=True)

        # A barra em si (efeito visual)
        st.markdown(
            f'<div class="barra {dim["classe_css"]}"></div>',
            unsafe_allow_html=True,
        )

        # Rótulo
        st.markdown(
            f'<div class="barra-label">{dim["titulo"]}</div>',
            unsafe_allow_html=True,
        )

        # Botão de clique para drill-down dessa dimensão
        if st.button(f"Ver detalhes", key=f"btn_{dim['id']}"):
            st.session_state.dimensao_selecionada = dim["id"]

        st.markdown('</div>', unsafe_allow_html=True)  # fecha barra-wrapper

    st.markdown('</div>', unsafe_allow_html=True)  # fecha barras-container


# --------------------------------------------------------------------
# Tela 2 – Detalhamento de uma dimensão (níveis, exemplos, etc.)
# --------------------------------------------------------------------
def mostrar_dimensao(dim_id: str):
    dim = next(d for d in DIMENSOES if d["id"] == dim_id)

    st.markdown(
        f"<h1 style='color:#333;'>{dim['titulo']}</h1>",
        unsafe_allow_html=True,
    )

    st.write("## 📘 Descrição geral da dimensão")
    st.write(dim["descricao"])

    st.write("## 📊 Níveis da Meta-Rubrica (1–4)")
    st.table(
        {
            "Nível": [
                "1 – Inaceitável",
                "2 – Aceitável",
                "3 – Bom/Sólido",
                "4 – Exemplar",
            ],
            "Descrição": [
                "A rubrica é inadequada, confusa ou incapaz de orientar a avaliação.",
                "Há algum alinhamento, mas ainda com ambiguidade ou lacunas importantes.",
                "Estrutura coerente, com níveis distintos e utilizáveis na prática.",
                "Modelo de referência: clara, criterial, bem fundamentada e altamente útil para avaliação formativa.",
            ],
        }
    )

    st.write("## 🌍 Exemplos práticos na EPT")
    st.info(dim["exemplos"])

    st.write("## 🧠 Papel desta dimensão na pesquisa")
    st.markdown(
        """
- Apoiar a validação das rubricas **discente, docente e autoavaliativa** do SINAPSE-BR;  
- Servir como referência na análise por juízes especialistas;  
- Permitir ajustes sucessivos das rubricas até atingir um padrão de qualidade exemplar.
"""
    )

    if st.button("⬅️ Voltar para as barras"):
        st.session_state.dimensao_selecionada = None


# --------------------------------------------------------------------
# Roteamento simples
# --------------------------------------------------------------------
if st.session_state.dimensao_selecionada is None:
    mostrar_home()
else:
    mostrar_dimensao(st.session_state.dimensao_selecionada)

