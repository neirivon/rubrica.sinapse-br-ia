# Arquivo: /home/neirivon/SINAPSE2.0/sinapsebr_rubrica/scripts/inspecionar_novos_dados.py
import pandas as pd
from pathlib import Path
import sys

# --- CONFIGURAÇÃO ---
# Caminho exato que você mostrou no terminal
BASE_DIR = Path("/home/neirivon/SINAPSE2.0/sinapsebr_rubrica//home/neirivon/SINAPSE2.0/sinapse_data_lake/microdados_censo_escolar_2024/dados")

ARQUIVOS = [
    "microdados_ed_basica_2024.csv",
    "suplemento_cursos_tecnicos_2024.csv"
]

def analisar_arquivo(caminho):
    print(f"\n{'='*80}")
    print(f"📂 ANALISANDO: {caminho.name}")
    print(f"{'='*80}")
    
    if not caminho.exists():
        print(f"❌ Erro: Arquivo não encontrado em {caminho}")
        return

    # O INEP costuma usar Latin-1 (ISO-8859-1) e separador ';'. 
    # Vamos tentar ler assim primeiro, se falhar, tentamos UTF-8.
    encodings_teste = ['latin-1', 'utf-8', 'cp1252']
    df = None
    
    for enc in encodings_teste:
        try:
            print(f"🔸 Tentando ler com encoding '{enc}' e detectar separador automático...")
            # nrows=50 para pegar só os 50 primeiros e ser rápido
            # sep=None e engine='python' detecta se é ; ou , automaticamente
            df = pd.read_csv(caminho, sep=None, engine='python', encoding=enc, nrows=50)
            print(f"✅ SUCESSO com encoding '{enc}'!")
            break
        except Exception as e:
            print(f"   Falha com {enc}: {e}")
            continue
    
    if df is None:
        print("❌ FALHA CRÍTICA: Não foi possível ler o arquivo com nenhum encoding padrão.")
        return

    # --- EXIBIÇÃO DOS RESULTADOS ---
    
    # 1. Colunas (Para caçarmos 'NU_ANO_CENSO', 'NO_MUNICIPIO', etc)
    print(f"\n📋 LISTA DE COLUNAS ({len(df.columns)} encontradas):")
    colunas_formatadas = [c.strip() for c in df.columns]
    print(colunas_formatadas)
    
    # Verificação rápida de colunas vitais para o TCC
    print("\n🕵️ VERIFICAÇÃO DE COLUNAS CHAVE:")
    chaves_procuradas = ['NU_ANO_CENSO', 'Ano', 'NO_MUNICIPIO', 'Municipio', 'CO_MUNICIPIO', 'NO_ENTIDADE', 'NO_IES']
    for chave in chaves_procuradas:
        encontrada = any(chave.upper() == c.upper() for c in colunas_formatadas)
        status = "✅ ACHOU" if encontrada else "❌ NÃO ACHOU"
        if encontrada:
            print(f"   {status}: {chave}")

    # 2. Os Dados (50 registros)
    print(f"\n👀 PREVIEW DOS DADOS (Primeiros 5 registros para não poluir, dataframe tem {len(df)}):")
    # Configura o pandas para não cortar colunas na visualização do terminal
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)
    print(df.head(5)) # Mostra 5 aqui, mas carregou 50 na memória se precisar debugar mais
    
    print("\n" + "-"*80)

# --- EXECUÇÃO ---
for arquivo in ARQUIVOS:
    caminho_completo = BASE_DIR / arquivo
    analisar_arquivo(caminho_completo)
