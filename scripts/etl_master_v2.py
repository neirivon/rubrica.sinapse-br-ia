# Arquivo: /home/neirivon/SINAPSE2.0/sinapsebr_rubrica/scripts/etl_master_v2.py
import pandas as pd
import json
import numpy as np
from pathlib import Path
import warnings

warnings.simplefilter(action='ignore', category=pd.errors.DtypeWarning)
warnings.simplefilter(action='ignore', category=UserWarning)

# --- CONFIGURAÇÃO DE CAMINHOS ---
BASE_DIR = Path("/home/neirivon/SINAPSE2.0/sinapsebr_rubrica/data")

FILE_CURSOS_24 = BASE_DIR / "microdados_censo_escolar_2024/dados/suplemento_cursos_tecnicos_2024.csv"
FILE_INFRA_24  = BASE_DIR / "microdados_censo_escolar_2024/dados/microdados_ed_basica_2024.csv"
FILE_CENSO_17  = BASE_DIR / "microdados_censo_escolar_2017/dados/microdados_ed_basica_2017.csv"
FILE_INSE_ESC  = BASE_DIR / "INSE_2021/INSE_2021_escolas.xlsx"
FILE_INSE_MUN  = BASE_DIR / "INSE_2021/INSE_2021_municipios.xlsx"
FILE_SAEB      = BASE_DIR / "MICRODADOS_SAEB_2023/DADOS/TS_ESCOLA.csv"

OUT_2024 = BASE_DIR.parent / "data/tmap_2024_completo.json"
OUT_HIST = BASE_DIR.parent / "data/tmap_historico_comparativo.json"

TMAP_MUNIS = [
    "ARAXA","ARAGUARI","CARMO DO PARANAIBA","CARNEIRINHO","CONCEICAO DAS ALAGOAS","FRUTAL",
    "ITUIUTABA","ITURAMA","JOAO PINHEIRO","MONTE ALEGRE DE MINAS","MONTE CARMELO","PATOS DE MINAS",
    "PATROCINIO","PRATA","SACRAMENTO","SERRA DO SALITRE","SANTA VITORIA","TAPIRA","UBERABA",
    "UBERLANDIA","UNAI","CAMPINA VERDE","CANAPOLIS","CENTRALINA","GURINHATA","CAPINOPOLIS",
    "INDIANOPOLIS","IRAI DE MINAS","NOVA PONTE","ROMARIA","ESTRELA DO SUL","CASCALHO RICO",
    "COMENDADOR GOMES","DELTA","CONQUISTA","COROMANDEL","GUIMARANIA","CRUZEIRO DA FORTALEZA",
    "ABADIA DOS DOURADOS","DOURADOQUARA","GRUPIARA","SANTA JULIANA","VERISSIMO","TIROS",
    "LAGOA FORMOSA","PRESIDENTE OLEGARIO","VAZANTE","PARACATU"
]

def normalizar(txt):
    if not isinstance(txt, str): return ""
    from unicodedata import normalize
    return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII').upper()

# --- MAPEAMENTOS OFICIAIS INEP ---
MAPA_DEPENDENCIA = {'1': 'Federal', '2': 'Estadual', '3': 'Municipal', '4': 'Privada'}
MAPA_LOCALIZACAO = {'1': 'Urbana', '2': 'Rural'}

print("🚀 INICIANDO ETL SINAPSE-BR IA (V2.2 - Correção Definitiva de Zona/Rede)")

# 1. INSE MUNICIPAL
print("\n🔹 Carregando Contexto Municipal (INSE)...")
dict_inse_muni = {}
try:
    df_mun = pd.read_excel(FILE_INSE_MUN, usecols=["NO_MUNICIPIO", "CO_UF", "MEDIA_INSE"], dtype=str)
    df_mun = df_mun[df_mun['CO_UF'] == '31']
    df_mun['Muni_Norm'] = df_mun['NO_MUNICIPIO'].apply(normalizar)
    for _, row in df_mun.iterrows():
        if row['Muni_Norm'] in TMAP_MUNIS:
            dict_inse_muni[row['Muni_Norm']] = round(float(row['MEDIA_INSE']), 2)
    print(f"   ✅ Dados socioeconômicos carregados.")
except:
    print(f"   ⚠️ Erro ao ler INSE Municípios (Pulando).")

# 2. PROCESSAMENTO 2024
print("\n🔹 Processando Escolas e Cursos 2024...")

# A. Cursos (Traz TP_LOCALIZACAO e TP_DEPENDENCIA originais)
try:
    df_cursos = pd.read_csv(FILE_CURSOS_24, sep=None, engine='python', encoding='latin-1', dtype=str)
    df_cursos['Muni_Norm'] = df_cursos['NO_MUNICIPIO'].apply(normalizar)
    df_cursos = df_cursos[(df_cursos['SG_UF'].str.upper() == 'MG') & (df_cursos['Muni_Norm'].isin(TMAP_MUNIS))]
    print(f"   ✅ Cursos carregados: {len(df_cursos)}.")
except Exception as e:
    print(f"   ❌ Erro fatal cursos: {e}")
    exit()

# B. Infraestrutura (SEM colunas de localização para não duplicar)
cols_infra = [
    'CO_ENTIDADE', 'IN_INTERNET', 'IN_LABORATORIO_INFORMATICA', 'IN_BIBLIOTECA', 'IN_SALA_LEITURA',
    'IN_ALIMENTACAO', 'IN_ACESSIBILIDADE_RAMPAS', 'IN_BANHEIRO_PNE'
]
try:
    df_infra = pd.read_csv(FILE_INFRA_24, sep=None, engine='python', encoding='latin-1', usecols=cols_infra, dtype=str)
    print(f"   ✅ Infraestrutura carregada.")
except:
    df_infra = pd.DataFrame(columns=cols_infra)

# C. INSE e SAEB
try:
    df_inse_esc = pd.read_excel(FILE_INSE_ESC, usecols=["ID_ESCOLA", "INSE_CLASSIFICACAO", "MEDIA_INSE"], dtype=str)
    df_inse_esc = df_inse_esc.rename(columns={"ID_ESCOLA": "CO_ENTIDADE"})
except:
    df_inse_esc = pd.DataFrame(columns=["CO_ENTIDADE", "INSE_CLASSIFICACAO", "MEDIA_INSE"])

try:
    df_saeb = pd.read_csv(FILE_SAEB, sep=None, engine='python', encoding='latin-1', usecols=["ID_ESCOLA", "MEDIA_EMT_LP", "MEDIA_EMT_MT"], dtype=str)
    df_saeb = df_saeb.rename(columns={"ID_ESCOLA": "CO_ENTIDADE"})
    df_saeb['Nota_SAEB'] = (pd.to_numeric(df_saeb['MEDIA_EMT_LP'], errors='coerce') + pd.to_numeric(df_saeb['MEDIA_EMT_MT'], errors='coerce')) / 2
    df_saeb = df_saeb[['CO_ENTIDADE', 'Nota_SAEB']]
except:
    df_saeb = pd.DataFrame(columns=["CO_ENTIDADE", "Nota_SAEB"])

# Merge
df_final = df_cursos.merge(df_infra, on='CO_ENTIDADE', how='left')
df_final = df_final.merge(df_inse_esc, on='CO_ENTIDADE', how='left')
df_final = df_final.merge(df_saeb, on='CO_ENTIDADE', how='left')

# Exportação
export_2024 = []
for muni_norm, grupo in df_final.groupby('Muni_Norm'):
    muni_real = grupo.iloc[0]['NO_MUNICIPIO']
    escolas_dict = {}
    
    for _, row in grupo.iterrows():
        cod = row['CO_ENTIDADE']
        if cod not in escolas_dict:
            
            # Mapeamento (Agora vai funcionar porque não há conflito de colunas)
            cod_dep = str(row.get('TP_DEPENDENCIA', '')).split('.')[0] # Remove .0 se houver
            nome_rede = MAPA_DEPENDENCIA.get(cod_dep, 'Outra')
            
            cod_loc = str(row.get('TP_LOCALIZACAO', '')).split('.')[0] # Remove .0 se houver
            nome_zona = MAPA_LOCALIZACAO.get(cod_loc, 'Não Inf.')

            escolas_dict[cod] = {
                "Nome": row['NO_ENTIDADE'],
                "Rede": nome_rede,
                "Zona": nome_zona,
                "INSE_Class": row.get('INSE_CLASSIFICACAO', 'N/A'),
                "INSE_Media": round(float(row.get('MEDIA_INSE', 0)), 2) if row.get('MEDIA_INSE') else 0,
                "SAEB": round(float(row.get('Nota_SAEB', 0)), 2) if row.get('Nota_SAEB') and row.get('Nota_SAEB') > 0 else None,
                "Infra": {
                    "Internet": row.get('IN_INTERNET') == '1',
                    "Lab_Info": row.get('IN_LABORATORIO_INFORMATICA') == '1',
                    "Acessibilidade": (row.get('IN_ACESSIBILIDADE_RAMPAS') == '1' or row.get('IN_BANHEIRO_PNE') == '1'),
                    "Alimentacao": row.get('IN_ALIMENTACAO') == '1'
                },
                "Cursos": []
            }
        
        try: mat = int(float(row['QT_MAT_CURSO_TEC']))
        except: mat = 0
        escolas_dict[cod]["Cursos"].append({"Nome": row['NO_CURSO_EDUC_PROFISSIONAL'], "Matriculas": mat})

    export_2024.append({
        "Municipio": muni_real,
        "INSE_Medio_Municipal": dict_inse_muni.get(muni_norm, None),
        "Total_Matriculas": grupo['QT_MAT_CURSO_TEC'].astype(float).sum(),
        "Escolas": list(escolas_dict.values())
    })

with open(OUT_2024, 'w', encoding='utf-8') as f:
    json.dump(export_2024, f, indent=2, ensure_ascii=False)

# 3. PROCESSAMENTO 2017 (Igual)
try:
    df_17 = pd.read_csv(FILE_CENSO_17, sep=None, engine='python', encoding='latin-1', usecols=['NO_MUNICIPIO', 'SG_UF', 'QT_MAT_PROF_TEC', 'TP_SITUACAO_FUNCIONAMENTO'])
    df_17['Muni_Norm'] = df_17['NO_MUNICIPIO'].apply(normalizar)
    df_17 = df_17[(df_17['SG_UF'].str.upper() == 'MG') & (df_17['Muni_Norm'].isin(TMAP_MUNIS)) & (df_17['TP_SITUACAO_FUNCIONAMENTO'] == 1)]
    df_17['Matriculas'] = pd.to_numeric(df_17['QT_MAT_PROF_TEC'], errors='coerce').fillna(0)
    agg_17 = df_17.groupby('NO_MUNICIPIO')['Matriculas'].sum().reset_index()
    export_hist = [{"Municipio": r['NO_MUNICIPIO'], "Ano": 2017, "Total_Matriculas": int(r['Matriculas'])} for _, r in agg_17.iterrows()]
    with open(OUT_HIST, 'w', encoding='utf-8') as f: json.dump(export_hist, f, indent=2, ensure_ascii=False)
except: pass

print(f"✅ JSONs Recriados! Verifique se 'Zona' agora aparece como Urbana/Rural.")
