# /home/neirivon/SINAPSE2.0/sinapsebr_rubrica/scripts/pages/99_Referencias.py
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Referências Bibliográficas",
    page_icon="📚",
    layout="wide"
)

# Bloqueia tradução automática
st.markdown('<meta name="google" content="notranslate">', unsafe_allow_html=True)

# ==============================================================================
#  BASE DE DADOS DE REFERÊNCIAS (ABNT COMPLETA - SINAPSE BR IA)
# ==============================================================================
referencias_db = [
    # --- EIXO 1: TERRITÓRIO E EPT (O CHÃO DA ESCOLA) ---
    {
        "eixo": "Fundamentos da EPT (Chão da Escola)",
        "autor": "IRINEU, M. A.",
        "obra": "O chão da escola",
        "abnt": "IRINEU, Marcelo Alves. **O chão da escola e os conteúdos cordiais**: a geografia humanista no ensino médio. 2015. Tese (Doutorado em Geografia) – Universidade Federal de Goiás, Goiânia, 2015."
    },
    {
        "eixo": "Fundamentos da EPT (Chão da Escola)",
        "autor": "FRIGOTTO, G.; CIAVATTA, M.; RAMOS, M.",
        "obra": "Ensino médio integrado",
        "abnt": "FRIGOTTO, Gaudêncio; CIAVATTA, Maria; RAMOS, Marise. **Ensino médio integrado**: concepção e contradições. São Paulo: Cortez, 2005."
    },
    {
        "eixo": "Fundamentos da EPT (Chão da Escola)",
        "autor": "SAVIANI, D.",
        "obra": "Pedagogia histórico-crítica",
        "abnt": "SAVIANI, Dermeval. **Pedagogia histórico-crítica**: primeiras aproximações. 11. ed. Campinas: Autores Associados, 2011."
    },
    {
        "eixo": "Fundamentos da EPT (Chão da Escola)",
        "autor": "SANTOS, M.",
        "obra": "A Natureza do Espaço",
        "abnt": "SANTOS, Milton. **A Natureza do Espaço**: Técnica e Tempo, Razão e Emoção. 4. ed. São Paulo: Edusp, 2006."
    },

    # --- EIXO 2: AVALIAÇÃO E RUBRICAS (ENGENHARIA PEDAGÓGICA) ---
    {
        "eixo": "Avaliação & Rubricas (Engenharia)",
        "autor": "MULLINIX, B. B.",
        "obra": "Rubric for Rubrics",
        "abnt": "MULLINIX, Bonnie B. **Rubric for Rubrics**: a tool for assessing the quality of rubrics. Monmouth University, Faculty Resource Center, 2003. Disponível em: https://www.monmouth.edu. Acesso em: 10 dez. 2025."
    },
    {
        "eixo": "Avaliação & Rubricas (Engenharia)",
        "autor": "BROOKHART, S. M.",
        "obra": "How to Create and Use Rubrics",
        "abnt": "BROOKHART, Susan M. **How to Create and Use Rubrics for Formative Assessment and Grading**. Alexandria, VA: ASCD, 2013."
    },
    {
        "eixo": "Avaliação & Rubricas (Engenharia)",
        "autor": "HOFFMANN, J.",
        "obra": "Avaliação mediadora",
        "abnt": "HOFFMANN, Jussara. **Avaliação mediadora**: uma prática em construção da pré-escola à universidade. 24. ed. Porto Alegre: Mediação, 2003."
    },
    {
        "eixo": "Avaliação & Rubricas (Engenharia)",
        "autor": "LUCKESI, C. C.",
        "obra": "Avaliação da aprendizagem escolar",
        "abnt": "LUCKESI, Cipriano Carlos. **Avaliação da aprendizagem escolar**: estudos e proposições. 22. ed. São Paulo: Cortez, 2011."
    },
    {
        "eixo": "Avaliação & Rubricas (Engenharia)",
        "autor": "HADJI, C.",
        "obra": "Avaliação desmistificada",
        "abnt": "HADJI, Charles. **Avaliação desmistificada**. Porto Alegre: Artmed, 2001."
    },

    # --- EIXO 3: NEUROCIÊNCIA E COGNIÇÃO ---
    {
        "eixo": "Neurociência & Aprendizagem",
        "autor": "COSENZA, R. M.; GUERRA, L. B.",
        "obra": "Neurociência e educação",
        "abnt": "COSENZA, Ramon M.; GUERRA, Leonor B. **Neurociência e educação**: como o cérebro aprende. Porto Alegre: Artmed, 2011."
    },
    {
        "eixo": "Neurociência & Aprendizagem",
        "autor": "DEHAENE, S.",
        "obra": "É assim que aprendemos",
        "abnt": "DEHAENE, Stanislas. **É assim que aprendemos**: por que o cérebro humano aprende melhor do que qualquer máquina (ainda). Porto Alegre: Penso, 2022."
    },
    {
        "eixo": "Neurociência & Aprendizagem",
        "autor": "NICOLELIS, M.",
        "obra": "Muito além do nosso eu",
        "abnt": "NICOLELIS, Miguel. **Muito além do nosso eu**: a nova neurociência que une cérebros e máquinas. São Paulo: Companhia das Letras, 2011."
    },

    # --- EIXO 4: PSICOLOGIA E DESENVOLVIMENTO ---
    {
        "eixo": "Psicologia & Metacognição",
        "autor": "FLAVELL, J. H.",
        "obra": "Metacognition and cognitive monitoring",
        "abnt": "FLAVELL, John H. Metacognition and cognitive monitoring: A new area of cognitive-developmental inquiry. **American Psychologist**, v. 34, n. 10, p. 906–911, 1979."
    },
    {
        "eixo": "Psicologia & Metacognição",
        "autor": "VYGOTSKY, L. S.",
        "obra": "A formação social da mente",
        "abnt": "VYGOTSKY, Lev S. **A formação social da mente**: o desenvolvimento dos processos psicológicos superiores. 6. ed. São Paulo: Martins Fontes, 1998."
    },
    {
        "eixo": "Psicologia & Metacognição",
        "autor": "PIAGET, J.",
        "obra": "O nascimento da inteligência",
        "abnt": "PIAGET, Jean. **O nascimento da inteligência na criança**. 4. ed. Rio de Janeiro: Zahar, 1982."
    },
    {
        "eixo": "Psicologia & Metacognição",
        "autor": "WALLON, H.",
        "obra": "As origens do pensamento",
        "abnt": "WALLON, Henri. **As origens do pensamento na criança**. São Paulo: Manole, 1989."
    },
    {
        "eixo": "Psicologia & Metacognição",
        "autor": "BIGGS, J. B.; COLLIS, K. F.",
        "obra": "Evaluating the Quality of Learning (SOLO)",
        "abnt": "BIGGS, John B.; COLLIS, Kevin F. **Evaluating the Quality of Learning**: the SOLO taxonomy. New York: Academic Press, 1982."
    },
    {
        "eixo": "Psicologia & Metacognição",
        "autor": "ANDERSON, L. W. et al.",
        "obra": "A Taxonomy for Learning (Bloom Revisada)",
        "abnt": "ANDERSON, Lorin W. et al. **A Taxonomy for Learning, Teaching, and Assessing**: A Revision of Bloom's Taxonomy of Educational Objectives. New York: Longman, 2001."
    },

    # --- EIXO 5: TECNOLOGIA E INTELIGÊNCIA ARTIFICIAL ---
    {
        "eixo": "Tecnologia & IA",
        "autor": "RUSSELL, S. J.; NORVIG, P.",
        "obra": "Inteligência artificial",
        "abnt": "RUSSELL, Stuart J.; NORVIG, Peter. **Inteligência artificial**: uma abordagem moderna. Tradução de Daniel Vieira. 4. ed. Rio de Janeiro: LTC, 2022."
    },
    {
        "eixo": "Tecnologia & IA",
        "autor": "DUARTE JUNIOR, D. N. S.",
        "obra": "O Moodle como ferramenta",
        "abnt": "DUARTE JUNIOR, Dirceu Nogueira de Sales. **O Moodle como ferramenta da prática docente**: tecnologias digitais de informação e comunicação como possibilidade ao docente da Educação Básica. 2021. Dissertação (Mestrado Profissional em Educação) – Universidade de Uberaba, Uberlândia, 2021."
    },
    {
        "eixo": "Tecnologia & IA",
        "autor": "KENSKI, V. M.",
        "obra": "Educação e tecnologias",
        "abnt": "KENSKI, Vani Moreira. **Educação e tecnologias**: o novo ritmo da informação. 8. ed. Campinas: Papirus, 2012."
    },

    # --- EIXO 6: DADOS, LEGISLAÇÃO E INCLUSÃO ---
    {
        "eixo": "Inclusão & Diversidade",
        "autor": "CRENSHAW, K.",
        "obra": "Documento para encontro de especialistas (Protocolo Interseccional)",
        "abnt": "CRENSHAW, Kimberlé. Documento para o encontro de especialistas em aspectos da discriminação racial relativos ao gênero. **Revista Estudos Feministas**, Florianópolis, v. 10, n. 1, p. 171-188, jan. 2002. Disponível em: https://www.scielo.br/j/ref/a/mbTpP4SFXPnJZ397j8fSBQQ. Acesso em: 20 dez. 2025."
    },
    {
        "eixo": "Inclusão & Diversidade",
        "autor": "CRENSHAW, K.",
        "obra": "Demarginalizing the intersection (Gênese 1989)",
        "abnt": "CRENSHAW, Kimberlé. Demarginalizing the intersection of race and sex: a black feminist critique of antidiscrimination doctrine, feminist theory and antiracist politics. **University of Chicago Legal Forum**, Chicago, v. 1989, n. 1, p. 139-167, 1989."
    },
    {
        "eixo": "Inclusão & Diversidade",
        "autor": "CRENSHAW, K.",
        "obra": "Mapping the margins (1991)",
        "abnt": "CRENSHAW, Kimberlé. Mapping the margins: intersectionality, identity politics, and violence against women of color. **Stanford Law Review**, Stanford, v. 43, n. 6, p. 1241-1299, jul. 1991."
    },
    {
        "eixo": "Inclusão & Diversidade",
        "autor": "CRENSHAW, K.",
        "obra": "The urgency of intersectionality (Vídeo TED)",
        "abnt": "CRENSHAW, Kimberlé. **The urgency of intersectionality**. [S. l.: s. n.], 2022. 1 vídeo (18 min). Publicado pelo canal FONAMUPP. Disponível em: https://youtu.be/M2z7FCPnxQQ. Acesso em: 20 dez. 2025."
    },
    {
        "eixo": "Inclusão & Diversidade",
        "autor": "CAST",
        "obra": "Universal Design for Learning Guidelines",
        "abnt": "CAST. **Universal Design for Learning Guidelines version 2.2**. Wakefield, MA: CAST, 2018. Disponível em: http://udlguidelines.cast.org. Acesso em: 02 dez. 2025."
    },
    {
        "eixo": "Dados & Legislação",
        "autor": "INEP",
        "obra": "Microdados do Censo Escolar",
        "abnt": "INEP. **Microdados do Censo Escolar da Educação Básica 2024**. Brasília: Inep, 2024. Disponível em: https://www.gov.br/inep. Acesso em: 02 dez. 2025."
    },
    {
        "eixo": "Dados & Legislação",
        "autor": "BRASIL",
        "obra": "LDB 9394/96",
        "abnt": "BRASIL. **Lei nº 9.394, de 20 de dezembro de 1996**. Estabelece as diretrizes e bases da educação nacional. Brasília, DF: Presidência da República, 1996."
    },
    {
        "eixo": "Dados & Legislação",
        "autor": "BRASIL",
        "obra": "BNCC",
        "abnt": "BRASIL. Ministério da Educação. **Base Nacional Comum Curricular**. Brasília, DF: MEC, 2018."
    }
]

# --- SIDEBAR ---
with st.sidebar:
    st.page_link("Apresentacao.py", label="🏠 Apresentação")
    st.markdown("---")
    st.page_link("pages/01_TMAP_2010.py", label="⏳ TMAP Histórico")
    st.page_link("pages/02_TMAP_2017_2024.py", label="🌐 TMAP 2024 (Equidade)")
    st.page_link("pages/03_Mapa_Geral_Rubrica.py", label="🧠 Mapa da Rubrica")
    st.page_link("pages/04_Mapa_Fundamentacao_Teorica.py", label="📚 Fundamentação")
    st.page_link("pages/05_Meta_Rubrica_3D.py", label="🌌 Meta-Rubrica 3D")
    st.page_link("pages/06_Rubrica_Docente_3D.py", label="👩‍🏫 Rubrica Docente 3D")
    st.page_link("pages/07_Rubrica_Autoavaliativa_3D.py", label="🎓 Autoavaliação 3D")
    st.page_link("pages/08_Transparencia_Avaliativa.py", label="🐆 Transparência (Avaliação)")
    st.page_link("pages/99_Referencias.py", label="📚 Referências")

# --- CORPO PRINCIPAL ---
st.title("📚 Referências Bibliográficas")
st.markdown("""
Compêndio das obras que fundamentam a arquitetura teórica e técnica do **SINAPSE-BR IA**.
As referências seguem as normas da **ABNT NBR 6023:2018** (atualizada).

> **Nota de Design:** As referências estão **agrupadas por Eixo Temático** para facilitar a consulta sem repetição visual.
""")

# Filtro por Eixo
eixos_unicos = sorted(list(set([r["eixo"] for r in referencias_db])))
eixos = ["Todos"] + eixos_unicos
sel_eixo = st.selectbox("🔍 Filtrar por Eixo Temático:", eixos)

st.divider()

# --- LÓGICA DE EXIBIÇÃO AGRUPADA ---
# 1. Filtra os dados se necessário
if sel_eixo == "Todos":
    dados_exibicao = referencias_db
else:
    dados_exibicao = [r for r in referencias_db if r["eixo"] == sel_eixo]

# 2. Ordena PRIMEIRO por Eixo, DEPOIS por Autor (Para o agrupamento funcionar)
# Usamos uma chave composta na lambda
dados_ordenados = sorted(dados_exibicao, key=lambda x: (x['eixo'], x['autor']))

# 3. Itera e exibe com Cabeçalhos de Seção
eixo_atual = None
contagem = 0

for ref in dados_ordenados:
    contagem += 1
    
    # Se o eixo mudou em relação ao loop anterior, imprime novo cabeçalho
    if ref['eixo'] != eixo_atual:
        eixo_atual = ref['eixo']
        st.markdown(f"### 🏷️ {eixo_atual}")
        st.markdown("---") # Linha separadora logo após o título do eixo

    # Renderiza a Referência (Sem repetir a etiqueta do eixo)
    with st.container():
        c_txt, c_btn = st.columns([0.85, 0.15])
        
        with c_txt:
            # O Markdown renderiza o negrito corretamente
            st.markdown(f"**[{contagem}]** {ref['abnt']}")
        
        with c_btn:
            # Botão de copiar
            st.code(ref["abnt"], language="markdown")
        
        # Espaçamento leve entre itens do mesmo grupo
        st.markdown("<div style='margin-bottom: 15px;'></div>", unsafe_allow_html=True)


# --- ÁREA DE DOWNLOAD (TXT PARA TCC - ALFABÉTICA GLOBAL) ---
st.markdown("---")
st.subheader("📥 Exportar para o TCC")

# Gera texto completo para download (Ordenado alfabeticamente por Autor, independente do eixo)
texto_completo = "REFERÊNCIAS BIBLIOGRÁFICAS\n\n"
refs_ordenadas_abnt = sorted(referencias_db, key=lambda x: x['abnt']) 

for ref in refs_ordenadas_abnt:
    # Remove os asteriscos do markdown para o arquivo de texto puro
    txt_limpo = ref['abnt'].replace("**", "")
    texto_completo += txt_limpo + "\n\n"

st.download_button(
    label="📄 Baixar Lista ABNT (.txt)",
    data=texto_completo,
    file_name="Referencias_SINAPSE_BR_ABNT.txt",
    mime="text/plain",
    help="Gera um arquivo de texto com todas as referências em ordem alfabética rigorosa, pronto para o Word."
)
