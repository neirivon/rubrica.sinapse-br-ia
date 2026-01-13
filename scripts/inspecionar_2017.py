# Arquivo: /home/neirivon/SINAPSE2.0/sinapsebr_rubrica/scripts/inspecionar_2017.py
import pandas as pd
from pathlib import Path

# Caminho exato que você mostrou no pwd
ARQUIVO_2017 = Path("/home/neirivon/SINAPSE2.0/sinapsebr_rubrica//home/neirivon/SINAPSE2.0/sinapse_data_lake/microdados_censo_escolar_2017/dados/microdados_ed_basica_2017.csv")

def inspecionar():
    print(f"{'='*80}")
    print(f"📂 INSPECIONANDO ARQUIVO 2017: {ARQUIVO_2017.name}")
    print(f"{'='*80}")

    if not ARQUIVO_2017.exists():
        print(f"❌ ERRO: O arquivo não está no caminho: {ARQUIVO_2017}")
        return

    # Tenta detectar separador e encoding automaticamente
    # INEP 2017 costuma ser '|' (pipe) e 'latin-1'
    try:
        print("🔸 Tentando leitura (ISO-8859-1)...")
        
        # O engine='python' com sep=None tenta adivinhar o separador
        df = pd.read_csv(ARQUIVO_2017, sep=None, engine='python', encoding='latin-1', nrows=50)
        
        print(f"✅ LEITURA BEM SUCEDIDA!")
        print(f"📊 Colunas encontradas: {len(df.columns)}")
        print("-" * 80)
        
        # 1. MOSTRAR CABEÇALHO (COLUNAS)
        print("📋 LISTA DE COLUNAS (Primeiras 50 para conferência):")
        print(df.columns[:50].tolist())
        
        # Verificação rápida de colunas importantes para TCC
        cols_upper = [c.upper() for c in df.columns]
        print("\n🕵️ BUSCA POR CHAVES:")
        for chave in ['NU_ANO_CENSO', 'NO_MUNICIPIO', 'CO_MUNICIPIO', 'QT_MAT_BAS', 'QT_MAT_PROF', 'IN_INTERNET']:
            achou = "✅ SIM" if chave in cols_upper else "❌ NÃO"
            print(f"   {achou} -> {chave}")

        # 2. MOSTRAR OS DADOS
        print("\n👀 PREVIEW DOS 50 PRIMEIROS REGISTROS:")
        # Ajuste de visualização para não cortar colunas no terminal
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', 1000)
        pd.set_option('display.max_rows', 50)
        
        print(df)

    except Exception as e:
        print(f"\n❌ FALHA NA LEITURA: {e}")
        print("Dica: Verifique se o arquivo não está corrompido ou se você tem permissão de leitura.")

if __name__ == "__main__":
    inspecionar()
