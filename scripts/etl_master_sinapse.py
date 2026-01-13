# Arquivo: /home/neirivon/SINAPSE2.0/sinapsebr_rubrica/scripts/etl_master_sinapse.py
import pandas as pd
import json
import numpy as np
from pathlib import Path
import warnings

warnings.simplefilter(action='ignore', category=pd.errors.DtypeWarning)

# --- CONFIGURAÇÃO DE CAMINHOS ---
BASE_DIR = Path("/home/neirivon/SINAPSE2.0/sinapsebr_rubrica/data")

# Arquivos de Entrada (Conforme sua estrutura de pastas)
FILE_CURSOS_24 = BASE_DIR / "microdados_censo_escolar_2024/dados/suplemento_cursos_tecnicos_2024.csv"
FILE_INFRA_24  = BASE_DIR / "microdados_censo_escolar_2024/dados/microdados_ed_basica_2024.csv"
FILE_CENSO_17  = BASE_DIR / "microdados_censo_escolar_2017/dados/microdados_ed_basica_2017.csv"
FILE_INSE      = BASE_DIR / "INSE_2021/INSE_2021_escolas.xlsx"
FILE_SAEB      = BASE_DIR / "MICRODADOS_SAEB_2023/DADOS/TS_ESCOLA.csv"

# Arquivos de Saída (JSONs limpos para o Streamlit ler)
OUT_2024 = BASE_DIR.parent / "data/tmap_2024_completo.json"
OUT_HIST = BASE_DIR.parent / "data/tmap_historico_comparativo.json"

# Lista TMAP
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

print("🚀 INICIANDO ETL SINAPSE-BR IA (Processamento Definitivo)")

# ==============================================================================
# 1. PROCESSAMENTO 2024 (CURSOS + INFRA + EQUIDADE)
# ==============================================================================
print("\n🔹 Processando 2024 (Cursos + Infra + Equidade)...")

# A. Carregar Cursos (Base)
try:
    # Lê com separador automático e latin-1
    df_cursos = pd.read_csv(FILE_CURSOS_24, sep=None, engine='python', encoding='latin-1', dtype=str)
    
    df_cursos['Muni_Norm'] = df_cursos['NO_MUNICIPIO'].apply(normalizar)
    
    # CORREÇÃO DE SEGURANÇA: FILTRA MG PARA EVITAR CIDADES HOMÔNIMAS
    df_cursos = df_cursos[
        (df_cursos['SG_UF'].str.upper() == 'MG') & 
        (df_cursos['Muni_Norm'].isin(TMAP_MUNIS))
    ]
    print(f"   ✅ Cursos carregados: {len(df_cursos)} registros no TMAP/MG.")
except Exception as e:
    print(f"   ❌ Erro crítico em Cursos 2024: {e}")
    df_cursos = pd.DataFrame()

# B. Carregar INSE (Nível Socioeconômico)
try:
    df_inse = pd.read_excel(FILE_INSE, usecols=["ID_ESCOLA", "INSE_CLASSIFICACAO"], dtype=str)
    df_inse = df_inse.rename(columns={"ID_ESCOLA": "CO_ENTIDADE", "INSE_CLASSIFICACAO": "INSE"})
    print(f"   ✅ INSE carregado.")
except Exception as e:
    print(f"   ⚠️ Erro INSE (opcional): {e}")
    df_inse = pd.DataFrame(columns=["CO_ENTIDADE", "INSE"])

# C. Carregar SAEB (Qualidade/Média)
try:
    df_saeb = pd.read_csv(FILE_SAEB, sep=None, engine='python', encoding='latin-1', 
                          usecols=["ID_ESCOLA", "MEDIA_EMT_LP", "MEDIA_EMT_MT"], dtype=str)
    df_saeb = df_saeb.rename(columns={"ID_ESCOLA": "CO_ENTIDADE"})
    # Converte para numérico e calcula média
    df_saeb['MEDIA_EMT_LP'] = pd.to_numeric(df_saeb['MEDIA_EMT_LP'], errors='coerce')
    df_saeb['MEDIA_EMT_MT'] = pd.to_numeric(df_saeb['MEDIA_EMT_MT'], errors='coerce')
    df_saeb['Nota_SAEB'] = (df_saeb['MEDIA_EMT_LP'] + df_saeb['MEDIA_EMT_MT']) / 2
    df_saeb = df_saeb[['CO_ENTIDADE', 'Nota_SAEB']].dropna()
    print(f"   ✅ SAEB carregado.")
except Exception as e:
    print(f"   ⚠️ Erro SAEB (opcional): {e}")
    df_saeb = pd.DataFrame(columns=["CO_ENTIDADE", "Nota_SAEB"])

# D. Carregar Infraestrutura (Microdados 2024)
try:
    cols_infra = ['CO_ENTIDADE', 'IN_INTERNET', 'IN_LABORATORIO_INFORMATICA', 'IN_BIBLIOTECA', 'TP_LOCALIZACAO']
    df_infra = pd.read_csv(FILE_INFRA_24, sep=None, engine='python', encoding='latin-1', usecols=cols_infra, dtype=str)
    print(f"   ✅ Infraestrutura carregada.")
except Exception as e:
    print(f"   ❌ Erro Infra 2024: {e}")
    df_infra = pd.DataFrame(columns=cols_infra)

# --- MERGE FINAL 2024 ---
if not df_cursos.empty:
    # Junta tudo na base de cursos usando o Código da Escola
    df_final_24 = df_cursos.merge(df_infra, on='CO_ENTIDADE', how='left')
    df_final_24 = df_final_24.merge(df_inse, on='CO_ENTIDADE', how='left')
    df_final_24 = df_final_24.merge(df_saeb, on='CO_ENTIDADE', how='left')

    # Estrutura o JSON hierárquico: Município -> Escolas -> Cursos
    export_2024 = []
    for muni, grupo in df_final_24.groupby('NO_MUNICIPIO'):
        escolas_dict = {}
        
        for _, row in grupo.iterrows():
            cod_esc = row['CO_ENTIDADE']
            nome_esc = row['NO_ENTIDADE']
            
            if cod_esc not in escolas_dict:
                escolas_dict[cod_esc] = {
                    "Nome": nome_esc,
                    "Zona": "Urbana" if row.get('TP_LOCALIZACAO') == '1' else "Rural",
                    "INSE": row.get('INSE', 'N/A'),
                    "SAEB": round(float(row.get('Nota_SAEB', 0)), 2) if row.get('Nota_SAEB') and row.get('Nota_SAEB') > 0 else None,
                    "Infra": {
                        "Internet": row.get('IN_INTERNET') == '1',
                        "Lab_Info": row.get('IN_LABORATORIO_INFORMATICA') == '1'
                    },
                    "Cursos": []
                }
            
            # Adiciona curso
            try: q_mat = int(float(row['QT_MAT_CURSO_TEC']))
            except: q_mat = 0
            
            escolas_dict[cod_esc]["Cursos"].append({
                "Curso": row['NO_CURSO_EDUC_PROFISSIONAL'],
                "Matriculas": q_mat
            })
            
        export_2024.append({
            "Municipio": muni,
            "Total_Matriculas": grupo['QT_MAT_CURSO_TEC'].astype(float).sum(),
            "Escolas": list(escolas_dict.values())
        })

    # Salvar JSON 2024
    with open(OUT_2024, 'w', encoding='utf-8') as f:
        json.dump(export_2024, f, indent=2, ensure_ascii=False)
    print(f"   💾 Salvo: tmap_2024_completo.json ({len(export_2024)} municípios)")

# ==============================================================================
# 2. PROCESSAMENTO 2017 (HISTÓRICO)
# ==============================================================================
print("\n🔹 Processando Histórico 2017 (Comparativo)...")
try:
    # O Raio-X mostrou separador '|' ou ';'. O engine 'python' com sep=None detecta sozinho.
    cols_17 = ['NO_MUNICIPIO', 'SG_UF', 'QT_MAT_PROF_TEC', 'TP_SITUACAO_FUNCIONAMENTO']
    df_17 = pd.read_csv(FILE_CENSO_17, sep=None, engine='python', encoding='latin-1', usecols=cols_17)
    
    df_17['Muni_Norm'] = df_17['NO_MUNICIPIO'].apply(normalizar)
    
    # CORREÇÃO DE SEGURANÇA: FILTRA MG
    df_17 = df_17[
        (df_17['SG_UF'].str.upper() == 'MG') & 
        (df_17['Muni_Norm'].isin(TMAP_MUNIS)) &
        (df_17['TP_SITUACAO_FUNCIONAMENTO'] == 1)
    ]
    
    # Agrega por Município
    df_17['Matriculas_17'] = pd.to_numeric(df_17['QT_MAT_PROF_TEC'], errors='coerce').fillna(0)
    agregado_17 = df_17.groupby('NO_MUNICIPIO')['Matriculas_17'].sum().reset_index()
    
    export_hist = []
    for _, row in agregado_17.iterrows():
        export_hist.append({
            "Municipio": row['NO_MUNICIPIO'],
            "Ano": 2017,
            "Total_Matriculas": int(row['Matriculas_17'])
        })
        
    # Salva JSON Histórico
    with open(OUT_HIST, 'w', encoding='utf-8') as f:
        json.dump(export_hist, f, indent=2, ensure_ascii=False)
    print(f"   💾 Salvo: tmap_historico_comparativo.json")

except Exception as e:
    print(f"   ❌ Erro ao processar 2017: {e}")

print("\n✅ ETL CONCLUÍDO! Arquivos JSON gerados na pasta 'data/'.")
