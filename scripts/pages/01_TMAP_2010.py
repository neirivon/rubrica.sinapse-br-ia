# /home/neirivon/SINAPSE2.0/sinapsebr_rubrica/scripts/pages/01_TMAP_2010.py
# TMAP (estrutura histórica 1990–2017) a partir DOS SEUS CSVs (SISTEC/Censo), sem inventar dados.
# Corrigido: page_link -> "Apresentacao.py" (relativo a /scripts), leitura robusta, dupes e Series garantidas.

from pathlib import Path
import re
import pandas as pd
import streamlit as st
from streamlit_echarts import st_echarts

st.set_page_config(page_title="TMAP • Estrutura (1990–2017)", page_icon="🗺️", layout="wide")

THIS = Path(__file__).resolve()
PROJECT_ROOT = THIS.parents[2]
DATA = PROJECT_ROOT / "data"
ASSETS = PROJECT_ROOT / "assets"
LOGOS = ASSETS / "logos"

# -- Lista factual (filtro territorial TMAP)
TMAP_MUNIS = {
    "Araxá","Araguari","Carmo do Paranaíba","Carneirinho","Conceição das Alagoas","Frutal",
    "Ituiutaba","Iturama","João Pinheiro","Monte Alegre de Minas","Monte Carmelo","Patos de Minas",
    "Patrocínio","Prata","Sacramento","Serra do Salitre","Santa Vitória","Tapira","Uberaba",
    "Uberlândia","Unaí","Campina Verde","Canápolis","Centralina","Gurinhatã","Capinópolis",
    "Indianópolis","Iraí de Minas","Nova Ponte","Romaria","Estrela do Sul","Cascalho Rico",
    "Comendador Gomes","Delta","Conquista","Campo Florido","Pedrinópolis","Perdizes","Arapuá",
    "Coromandel","Guimarânia","Cruzeiro da Fortaleza","Abadia dos Dourados","Douradoquara",
    "Grupiara","Santa Juliana","Veríssimo","Tiros","Lagoa Formosa","Presidente Olegário",
    "Vazante","Paracatu"
}

# ---------- utilitários robustos ----------
def read_csv_robust(path: Path) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame()
    for enc in ("utf-8", "latin-1", "cp1252"):
        try:
            return pd.read_csv(path, sep=None, engine="python", dtype=str, encoding=enc)
        except Exception:
            continue
    try:
        return pd.read_csv(path, dtype=str, engine="python")
    except Exception:
        return pd.DataFrame()

def collapse_dupes(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df
    df = df.copy()
    df.columns = [str(c).strip() for c in df.columns]
    if df.columns.duplicated().any():
        df = df.T.groupby(level=0).first().T
    return df

def get_series(df: pd.DataFrame, name: str) -> pd.Series:
    """Sempre devolve Series (mesmo se houver colunas duplicadas)."""
    if name not in df.columns:
        return pd.Series(index=df.index, dtype="object")
    obj = df.loc[:, name]
    if isinstance(obj, pd.DataFrame):
        obj = obj.iloc[:, 0]
    return obj.astype(str)

@st.cache_data
def load_municipios_presentes() -> pd.DataFrame:
    bases = []
    bases.append(read_csv_robust(DATA / "Relatorio_IPES_Escolas.csv"))
    bases.append(read_csv_robust(DATA / "Sistec_Cursos_Tecnicos_ativos_120922.csv"))
    bases.append(read_csv_robust(DATA / "microdados_censo_escolar_2024/dados/suplemento_cursos_tecnicos_2024.csv"))

    bases = [collapse_dupes(b) for b in bases if not b.empty]
    if not bases:
        return pd.DataFrame(columns=["UF", "Municipio"])

    df = pd.concat(bases, ignore_index=True)
    # mapear cabeçalhos
    ren = {}
    for c in df.columns:
        s = re.sub(r"\s+", " ", c.strip()).lower()
        if s in ["uf","estado","unidade federativa"]: ren[c] = "UF"
        elif s in ["ds_municipio", "municipio", "município"] or "munic" in s: ren[c] = "Municipio"
        elif s == "no_municipio": ren[c] = "Municipio"
        elif s == "co_municipio": ren[c] = "CodIBGE"
    df = df.rename(columns=ren)
    df = collapse_dupes(df)

    for c in ["UF", "Municipio", "CodIBGE"]:
        if c not in df.columns:
            df[c] = ""

    UF  = get_series(df, "UF").str.upper().str.strip()
    MUN = get_series(df, "Municipio").str.strip()
    COD = get_series(df, "CodIBGE").str.strip()

    # traduzir código IBGE -> nome quando Município vier vazio
    if (MUN.eq("") & COD.ne("")).any():
        supl = read_csv_robust(DATA / "microdados_censo_escolar_2024/dados/suplemento_cursos_tecnicos_2024.csv")
        supl = collapse_dupes(supl)
        if not supl.empty:
            mapa = (
                supl.rename(columns={"CO_MUNICIPIO": "CodIBGE", "NO_MUNICIPIO": "Nome"})
                    .loc[:, ["CodIBGE", "Nome"]]
                    .dropna()
            )
            mapa["CodIBGE"] = mapa["CodIBGE"].astype(str).str.strip()
            dct = dict(zip(mapa["CodIBGE"], mapa["Nome"]))
            MUN = MUN.mask(MUN.eq("") & COD.ne(""), COD.map(dct).fillna(MUN))

    df["UF"] = UF
    df["Municipio"] = MUN

    df = df[df["UF"].eq("MG")]
    if TMAP_MUNIS:
        df = df[df["Municipio"].str.upper().isin({m.upper() for m in TMAP_MUNIS})]

    return df[["UF", "Municipio"]].drop_duplicates().sort_values("Municipio")

presentes = load_municipios_presentes()

with st.sidebar:
    st.page_link("Apresentacao.py", label="Apresentação", icon="🏠")
    st.page_link("pages/01_TMAP_2010.py", label="TMAP (Estrut. 1990–2017)", icon="🗺️")
    st.page_link("pages/02_TMAP_2017_2022.py", label="TMAP (2017/2022 EPT)", icon="🌐")
    st.divider()
    if (LOGOS / "IFTM_360.png").exists():
        st.image(str(LOGOS / "IFTM_360.png"), use_column_width=True)

st.markdown("## 🗺️ TMAP — **estrutura histórica (1990–2017)**")
st.caption("Exibe municípios a partir de **seus CSVs** (SISTEC/Censo). Códigos IBGE → nomes quando necessário.")

if presentes.empty:
    st.warning("Sem municípios após os filtros. Verifique `data/Relatorio_IPES_Escolas.csv`, `Sistec_Cursos_Tecnicos_ativos_120922.csv` e o suplemento 2024.")
else:
    data = {"name": "TMAP (1990–2017)", "children": [{"name": m} for m in presentes["Municipio"].unique().tolist()]}
    opts = {
        "tooltip": {"trigger": "item", "triggerOn": "mousemove"},
        "series": [{
            "type": "tree", "data": [data],
            "top": "5%", "left": "2%", "bottom": "5%", "right": "20%",
            "symbolSize": 10,
            "label": {"position": "left", "verticalAlign": "middle", "align": "right", "fontSize": 12},
            "leaves": {"label": {"position": "right", "align": "left"}},
            "expandAndCollapse": True,
            "initialTreeDepth": 1,
            "animationDuration": 250
        }]
    }
    st_echarts(opts, height="540px", key="tree-2010-real")
    st.dataframe(presentes, use_container_width=True, hide_index=True)

