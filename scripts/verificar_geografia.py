# Arquivo: /home/neirivon/SINAPSE2.0/sinapsebr_rubrica/scripts/verificar_geografia.py
import pandas as pd
from pathlib import Path
import warnings

# Ignora avisos de Dtype para limpar o terminal
warnings.simplefilter(action='ignore', category=pd.errors.DtypeWarning)

# --- CONFIGURAÇÃO ---
BASE_DIR = Path("/home/neirivon/SINAPSE2.0/sinapsebr_rubrica/data")
# Apontando para o arquivo de 2024 que tem os dados oficiais do IBGE
FILE_CENSO = BASE_DIR / "microdados_censo_escolar_2024/dados/microdados_ed_basica_2024.csv"

# Sua lista do TMAP (incluindo a expansão institucional IFTM)
SUA_LISTA = [
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

print("🌍 VERIFICANDO CLASSIFICAÇÃO OFICIAL IBGE (FILTRO: MINAS GERAIS)...")

try:
    # 1. LER O ARQUIVO (Agora incluindo SG_UF para filtrar o estado)
    # Usamos separador ';' que é o padrão de 2024
    cols = ['NO_MUNICIPIO', 'NO_MESORREGIAO', 'NO_MICRORREGIAO', 'SG_UF']
    
    try:
        df = pd.read_csv(FILE_CENSO, sep=';', encoding='latin-1', usecols=cols)
    except:
        # Fallback se o separador for diferente
        df = pd.read_csv(FILE_CENSO, sep='|', encoding='latin-1', usecols=cols)

    # 2. APLICAR FILTROS RIGOROSOS
    # Normaliza nome
    df['Muni_Norm'] = df['NO_MUNICIPIO'].apply(normalizar)
    
    # AQUI ESTÁ A CORREÇÃO: Filtra Nome E Estado (MG)
    df_filtrado = df[
        (df['Muni_Norm'].isin(SUA_LISTA)) & 
        (df['SG_UF'] == 'MG') 
    ].drop_duplicates(subset=['Muni_Norm'])
    
    # 3. EXIBIR RESULTADOS
    print(f"\n📋 RESULTADO DA ANÁLISE ({len(df_filtrado)} municípios encontrados em MG):\n")
    print(f"{'MUNICÍPIO':<25} | {'MESORREGIÃO IBGE':<35} | {'MICRORREGIÃO'}")
    print("-" * 85)
    
    contagem_meso = {}
    
    for _, row in df_filtrado.sort_values('NO_MESORREGIAO').iterrows():
        print(f"{row['NO_MUNICIPIO']:<25} | {row['NO_MESORREGIAO']:<35} | {row['NO_MICRORREGIAO']}")
        
        meso = row['NO_MESORREGIAO']
        contagem_meso[meso] = contagem_meso.get(meso, 0) + 1

    print("\n📊 RESUMO DA SUA LISTA (VALIDAÇÃO):")
    for meso, qtd in contagem_meso.items():
        print(f"   -> {qtd} cidades pertencem a: {meso}")

    # Validação Institucional
    if "Noroeste de Minas" in contagem_meso:
        print("\n✅ NOTA METODOLÓGICA NECESSÁRIA:")
        print("   O script detectou cidades do 'Noroeste de Minas' (ex: Paracatu, Unaí).")
        print("   Isso está CORRETO para o seu TCC, pois você definiu o recorte pela rede IFTM.")
        print("   Certifique-se de incluir a nota explicativa na Metodologia.")
    
    # Validação de Erros Antigos
    if "Borborema" not in contagem_meso and "Extremo Oeste Baiano" not in contagem_meso:
        print("\n🎉 SUCESSO: Nenhuma cidade de fora de MG foi detectada!")

except Exception as e:
    print(f"❌ Erro fatal: {e}")
