# Arquivo: /home/neirivon/SINAPSE2.0/sinapsebr_rubrica/scripts/analise_zona_tmap.py
import pandas as pd
from pathlib import Path
import sys

# --- CONFIGURAÇÃO ---
BASE_DIR = Path("/home/neirivon/SINAPSE2.0/sinapsebr_rubrica/data")
FILE_2024 = BASE_DIR / "microdados_censo_escolar_2024/dados/microdados_ed_basica_2024.csv"
FILE_2017 = BASE_DIR / "microdados_censo_escolar_2017/dados/microdados_ed_basica_2017.csv"

# Lista TMAP (Para filtrar apenas o que interessa)
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

def analisar_arquivo(ano, file_path, sep):
    print(f"\n{'='*60}")
    print(f"🔎 ANALISANDO CENSO {ano}")
    print(f"📂 Arquivo: {file_path.name}")
    
    if not file_path.exists():
        print("❌ Arquivo não encontrado.")
        return

    try:
        # Lê apenas colunas necessárias para ser rápido
        cols = ['NO_MUNICIPIO', 'SG_UF', 'TP_LOCALIZACAO', 'NO_ENTIDADE']
        
        # Engine python é mais lento mas mais robusto para detectar separadores
        df = pd.read_csv(file_path, sep=sep, encoding='latin-1', usecols=cols, engine='python')
        
        # Normaliza e Filtra
        df['Muni_Norm'] = df['NO_MUNICIPIO'].apply(normalizar)
        df_tmap = df[
            (df['SG_UF'].str.upper() == 'MG') & 
            (df['Muni_Norm'].isin(TMAP_MUNIS))
        ]
        
        print(f"📊 Escolas encontradas no TMAP: {len(df_tmap)}")
        print(f"{'-'*60}")
        print(f"{'MUNICÍPIO':<25} | {'URBANA':<10} | {'RURAL':<10} | {'% RURAL':<10}")
        print(f"{'-'*60}")
        
        # Agrupa e Conta
        stats = []
        for muni, grupo in df_tmap.groupby('NO_MUNICIPIO'):
            total = len(grupo)
            # TP_LOCALIZACAO: 1 = Urbana, 2 = Rural
            urbana = len(grupo[grupo['TP_LOCALIZACAO'] == 1])
            rural = len(grupo[grupo['TP_LOCALIZACAO'] == 2])
            
            pct_rural = (rural / total * 100) if total > 0 else 0
            
            print(f"{muni:<25} | {urbana:<10} | {rural:<10} | {pct_rural:>6.1f}%")
            stats.append({'Muni': muni, 'Rural_Pct': pct_rural})
            
        # Resumo Geral
        print(f"{'-'*60}")
        total_geral = len(df_tmap)
        rural_geral = len(df_tmap[df_tmap['TP_LOCALIZACAO'] == 2])
        pct_geral = (rural_geral / total_geral * 100) if total_geral > 0 else 0
        print(f"MÉDIA GERAL DO TMAP: {pct_geral:.1f}% das escolas estão na Zona Rural.")

    except Exception as e:
        print(f"❌ Erro ao ler arquivo: {e}")

# --- EXECUÇÃO ---
# 2024 (Geralmente separador ;)
analisar_arquivo(2024, FILE_2024, sep=None) 

# 2017 (Geralmente separador |)
analisar_arquivo(2017, FILE_2017, sep=None)
