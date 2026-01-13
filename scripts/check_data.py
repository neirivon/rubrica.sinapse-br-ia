# Arquivo: /home/neirivon/SINAPSE2.0/sinapsebr_rubrica/scripts/check_data.py
import pandas as pd
from pathlib import Path
import sys

# --- CONFIGURAÇÃO DE CAMINHOS ---
# Ajuste este nível (.parent) até encontrar a raiz correta
THIS = Path(__file__).resolve()
PROJECT_ROOT = THIS.parent.parent # Supõe que check_data.py está em scripts/
DATA_DIR = PROJECT_ROOT / "data"

print(f"🔍 INICIANDO BATERIA DE TESTES DE INTEGRIDADE")
print(f"📂 Diretório de Dados esperado: {DATA_DIR}\n")

# --- LISTA DE ARQUIVOS ESPERADOS ---
FILES_TO_CHECK = [
    "Relatorio_IPES_Escolas.csv",
    "Sistec_Cursos_Tecnicos_ativos_120922.csv",
    "microdados_censo_escolar_2024/dados/suplemento_cursos_tecnicos_2024.csv"
]

def read_csv_preview(filepath):
    """Tenta ler o CSV e retorna sucesso, colunas e erro (se houver)"""
    if not filepath.exists():
        return False, None, "Arquivo não encontrado (File Not Found)"
    
    for enc in ["utf-8", "latin-1", "cp1252", "ISO-8859-1"]:
        try:
            df = pd.read_csv(filepath, sep=None, engine="python", dtype=str, encoding=enc, nrows=5)
            return True, df.columns.tolist(), None
        except Exception:
            continue
            
    return False, None, "Falha na leitura (Erro de Encoding ou Formato)"

# --- EXECUÇÃO DOS TESTES ---
all_passed = True

for filename in FILES_TO_CHECK:
    full_path = DATA_DIR / filename
    print(f"🔸 Testando: {filename}...")
    
    success, columns, error = read_csv_preview(full_path)
    
    if success:
        print(f"   ✅ LEITURA OK.")
        print(f"   📋 Colunas detectadas ({len(columns)}): {columns[:5]} ...") # Mostra as 5 primeiras
        
        # Teste específico para colunas críticas
        colunas_str = " ".join(columns).lower()
        if "ano" in colunas_str:
            print("   ✅ Coluna 'Ano' (ou similar) ENCONTRADA.")
        else:
            print("   ⚠️ ALERTA: Coluna 'Ano' NÃO encontrada neste arquivo.")
            
        if "munic" in colunas_str:
            print("   ✅ Coluna 'Município' (ou similar) ENCONTRADA.")
        else:
            print("   ❌ ERRO CRÍTICO: Nenhuma coluna de Município identificada.")
            
    else:
        print(f"   ❌ FALHA: {error}")
        print(f"   Caminho tentado: {full_path}")
        all_passed = False
    
    print("-" * 40)

# --- RESUMO FINAL ---
print("\n" + "="*40)
if all_passed:
    print("🎉 SUCESSO: Todos os arquivos foram lidos.")
    print("Nota: Verifique os alertas acima se a coluna 'Ano' realmente existe onde deveria.")
else:
    print("🚫 ERROS ENCONTRADOS: Verifique os caminhos ou nomes dos arquivos acima.")
    print("DICA: Se o erro for 'File Not Found', ajuste a variável PROJECT_ROOT na linha 9.")
print("="*40)
