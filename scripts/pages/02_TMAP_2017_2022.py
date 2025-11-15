# /home/neirivon/SINAPSE2.0/sinapsebr_rubrica/scripts/pages/02_TMAP_2017_2022.py
# TMAP (2017/2022) — Município → Zona → Instituição (SISTEC) + mapa (se houver lat/lon)
# Corrigido: page_link -> "Apresentacao.py" (relativo a /scripts), leitura robusta, dupes e Series garantidas.

from pathlib import Path
import re
import pandas as pd
import streamlit as st
from streamlit_echarts import st_echarts
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="TMAP • 2017/2022 • EPT", page_icon="🌐", layout="wide")

THIS = Path(__file__).resolve()
PROJECT_ROOT = THIS.parents[2]
DATA = PROJECT_ROOT / "data"
ASSETS = PROJECT_ROOT / "assets"
LOGOS = ASSETS / "logos"

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

# ---------- utilitários (mesmos da 01) ----------
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
    if name not in df.columns:
        return pd.Series(index=df.index, dtype="object")
    obj = df.loc[:, name]
    if isinstance(obj, pd.DataFrame):
        obj = obj.iloc[:, 0]
    return obj.astype(str)

@st.cache_data
def load_sistec_consolidado() -> pd.DataFrame:
    df1 = collapse_dupes(read_csv_robust(DATA / "Relatorio_IPES_Escolas.csv"))              # 2020–2023
    df2 = collapse_dupes(read_csv_robust(DATA / "Sistec_Cursos_Tecnicos_ativos_120922.csv")) # 2022

    if df1.empty and df2.empty:
        return pd.DataFrame(columns=["UF","Municipio","Instituicao","Rede","Dependencia","Zona","Latitude","Longitude","Endereco"])

    def normalize(df: pd.DataFrame) -> pd.DataFrame:
        if df.empty:
            return df
        ren = {}
        for c in df.columns:
            s = re.sub(r"\s+", " ", c.strip()).lower()
            if s in ["uf","estado","unidade federativa"]: ren[c] = "UF"
            elif s in ["ds_municipio","municipio","município"] or "munic" in s: ren[c] = "Municipio"
            elif s == "no_municipio": ren[c] = "Municipio"
            elif any(k in s for k in ["institu","unidade","escola","ies","unidade de ensino"]): ren[c] = "Instituicao"
            elif "rede" in s: ren[c] = "Rede"
            elif any(k in s for k in ["depend","manten"]): ren[c] = "Dependencia"
            elif "zona" in s or "localiz" in s: ren[c] = "Zona"
            elif "lat" in s: ren[c] = "Latitude"
            elif "lon" in s: ren[c] = "Longitude"
            elif any(k in s for k in ["endereco","endereço","logradouro"]): ren[c] = "Endereco"
        df = df.rename(columns=ren)
        df = collapse_dupes(df)

        for c in ["UF","Municipio","Instituicao","Rede","Dependencia","Zona","Latitude","Longitude","Endereco"]:
            if c not in df.columns:
                df[c] = ""

        UF  = get_series(df, "UF").str.upper().str.strip()
        MUN = get_series(df, "Municipio").str.strip()
        INS = get_series(df, "Instituicao").str.strip()
        RED = get_series(df, "Rede").str.strip()
        DEP = get_series(df, "Dependencia").str.strip()
        ZON = get_series(df, "Zona").str.strip()
        LAT = get_series(df, "Latitude").str.strip()
        LON = get_series(df, "Longitude").str.strip()
        END = get_series(df, "Endereco").str.strip()

        ZON = ZON.replace({
            "1":"Urbana","URBANA":"Urbana","urbana":"Urbana",
            "2":"Rural","RURAL":"Rural","rural":"Rural",
            "":"Indefinida","nan":"Indefinida","NaN":"Indefinida"
        }).fillna("Indefinida")

        return pd.DataFrame({
            "UF": UF, "Municipio": MUN, "Instituicao": INS, "Rede": RED,
            "Dependencia": DEP, "Zona": ZON, "Latitude": LAT, "Longitude": LON, "Endereco": END
        })

    out = pd.concat([normalize(df1), normalize(df2)], ignore_index=True)
    out = out[out["UF"].eq("MG")]
    out = out[out["Municipio"].str.upper().isin({m.upper() for m in TMAP_MUNIS})]
    out = out[out["Instituicao"].str.len() > 0]
    return out

df = load_sistec_consolidado()

with st.sidebar:
    st.page_link("Apresentacao.py", label="Apresentação", icon="🏠")
    st.page_link("pages/01_TMAP_2010.py", label="TMAP (Estrut. 1990–2017)", icon="🗺️")
    st.page_link("pages/02_TMAP_2017_2022.py", label="TMAP (2017/2022 EPT)", icon="🌐")
    st.divider()
    if (LOGOS / "IFTM_360.png").exists():
        st.image(str(LOGOS / "IFTM_360.png"), use_column_width=True)

st.markdown("## 🌐 TMAP (2017/2022) — Municípios → Zona → **Instituições EPT**")
st.caption("Tudo vem **dos seus CSVs** (SISTEC/Relatório IPES). O mapa usa Latitude/Longitude se existirem.")

if df.empty:
    st.info("Não encontrei instituições TMAP em `Relatorio_IPES_Escolas.csv` e/ou `Sistec_Cursos_Tecnicos_ativos_120922.csv` (após filtros de MG/TMAP).")
    st.stop()

# -------- Árvore Município → Zona → Instituições --------
tree_children = []
for muni, g1 in df.groupby("Municipio", sort=True):
    zonas_children = []
    for zona, g2 in g1.groupby("Zona", sort=True):
        inst_nodes = [{"name": f"{r['Instituicao']} [{r['Rede'] or 'Rede?'}]"} for _, r in g2.sort_values("Instituicao").iterrows()]
        zonas_children.append({"name": f"Zona {zona}", "children": inst_nodes})
    tree_children.append({"name": muni, "children": zonas_children})

opts = {
    "tooltip":{"trigger":"item","triggerOn":"mousemove"},
    "series":[{
        "type":"tree",
        "data":[{"name":"TMAP — EPT (2017/2022)", "children": tree_children}],
        "top":"5%","left":"2%","bottom":"5%","right":"20%",
        "symbolSize":10,
        "label":{"position":"left","verticalAlign":"middle","align":"right","fontSize":12},
        "leaves":{"label":{"position":"right","align":"left"}},
        "expandAndCollapse": True,
        "initialTreeDepth": 2,
        "animationDuration": 250
    }]
}

left, right = st.columns([1.05, 1])

with left:
    st_echarts(opts, height="560px", key="tree-real-2017")

with right:
    munis = sorted(df["Municipio"].unique().tolist())
    redes = sorted([x for x in df["Rede"].unique().tolist() if x])
    zonas = ["Urbana","Rural","Indefinida"]

    c1, c2, c3 = st.columns(3)
    muni_sel = c1.multiselect("Município", munis, default=munis[:3])
    rede_sel = c2.multiselect("Rede", redes)
    zona_sel = c3.multiselect("Zona", zonas)

    fil = df.copy()
    if muni_sel: fil = fil[fil["Municipio"].isin(muni_sel)]
    if rede_sel: fil = fil[fil["Rede"].isin(rede_sel)]
    if zona_sel: fil = fil[fil["Zona"].isin(zona_sel)]

    m = folium.Map(location=[-19.2, -47.9], zoom_start=7, control_scale=True)
    from folium.plugins import MarkerCluster
    cluster = MarkerCluster().add_to(m)

    color_by_rede = {
        "Federal":"#1f77b4","Estadual":"#2ca02c","Municipal":"#8c564b",
        "Privada":"#ff7f0e","Sistema S":"#9467bd","Comunitária":"#17becf","Filantrópica":"#e377c2"
    }

    have_points = 0
    for _, r in fil.iterrows():
        lat, lon = r.get("Latitude",""), r.get("Longitude","")
        try:
            latf = float(str(lat).replace(",", "."))
            lonf = float(str(lon).replace(",", "."))
        except Exception:
            continue
        have_points += 1
        html = f"<b>{r['Instituicao']}</b><br/>{r['Rede']} · {r['Dependencia']}<br/>{r['Municipio']} / {r['Zona']}<br/><small>{r['Endereco']}</small>"
        folium.CircleMarker(
            location=[latf, lonf], radius=6,
            color=color_by_rede.get(r["Rede"], "#444"),
            fill=True, fill_opacity=0.9, popup=folium.Popup(html, max_width=360),
            tooltip=r["Instituicao"]
        ).add_to(cluster)

    st_folium(m, height=560, returned_objects=[])

    if have_points == 0:
        st.info("Para os filtros atuais não há Latitude/Longitude nos CSVs. O mapa fica vazio; confira a tabela abaixo.")

st.markdown("#### Instituições (dados reais do SISTEC)")
st.dataframe(
    fil.sort_values(["Municipio","Zona","Rede","Instituicao"]).reset_index(drop=True),
    use_container_width=True, hide_index=True
)
st.download_button(
    "Baixar CSV filtrado (real)",
    data=fil.to_csv(index=False).encode("utf-8"),
    file_name="tmap_ept_real_2017_2022.csv",
    mime="text/csv"
)

