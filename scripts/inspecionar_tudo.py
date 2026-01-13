# Arquivo: /home/neirivon/SINAPSE2.0/sinapsebr_rubrica/scripts/inspecionar_tudo.py
import os
import pandas as pd
from pathlib import Path
import warnings

# Suprime avisos do Excel/Pandas para limpar o output
warnings.simplefilter(action='ignore', category=UserWarning)

# --- CONFIGURAÇÃO ---
# Ajuste para a raiz onde estão as pastas INSE_2021, microdados, etc.
# Baseado no seu ls -lha, parece estar em data/
BASE_DIR = Path("/home/neirivon/SINAPSE2.0/sinapsebr_rubrica/data")
OUTPUT_FILE = BASE_DIR.parent / "RAIO_X_DADOS_COMPLETO.txt"

# Lista de arquivos prioritários para inspecionar (para não varrer lixo)
# Adicionei os principais que vi na sua árvore
TARGET_FILES = [
    "INSE_2021_escolas.xlsx",
    "INSE_2021_municipios.xlsx",
    "microdados_ed_basica_2017.csv",
    "microdados_ed_basica_2024.csv",
    "suplemento_cursos_tecnicos_2024.csv",
    "TS_ESCOLA.csv",           # SAEB - Foco na Escola
    "TS_ALUNO_34EM.csv",       # SAEB - Foco no Ensino Médio (onde está a EPT)
    "Sistec_Cursos_Tecnicos_ativos_120922.csv"
]

def formatar_preview(df, filename):
    """Gera uma string formatada com info do DataFrame."""
    buffer = []
    buffer.append("="*80)
    buffer.append(f"📂 ARQUIVO: {filename}")
    buffer.append("="*80)
    buffer.append(f"📏 Dimensões Carregadas: {df.shape[0]} linhas x {df.shape[1]} colunas")
    buffer.append("-" * 40)
    buffer.append("📋 COLUNAS (Cabeçalho):")
    buffer.append(", ".join(df.columns.tolist()))
    buffer.append("-" * 40)
    buffer.append("👀 AMOSTRA (50 primeiras linhas):")
    
    # Converte para string tabulada bonita
    buffer.append(df.head(50).to_string(index=False))
    buffer.append("\n\n")
    return "\n".join(buffer)

def processar_arquivo(caminho):
    print(f"   Processando: {caminho.name}...")
    
    try:
        # --- LÓGICA PARA EXCEL ---
        if caminho.suffix == '.xlsx':
            # Lê a primeira aba
            df = pd.read_excel(caminho, nrows=50)
            return formatar_preview(df, caminho.name)

        # --- LÓGICA PARA CSV ---
        elif caminho.suffix == '.csv':
            # Tenta diferentes encodings e separadores comuns no governo BR
            encodings = ['latin-1', 'utf-8', 'cp1252']
            separators = [';', '|', ',', '\t']
            
            for enc in encodings:
                for sep in separators:
                    try:
                        # Tenta ler apenas 55 linhas para testar (50 dados + header)
                        df = pd.read_csv(
                            caminho, 
                            encoding=enc, 
                            sep=sep, 
                            nrows=50, 
                            engine='python',
                            dtype=str # Lê tudo como texto para não dar erro de conversão agora
                        )
                        
                        # Validação simples: se leu tudo em 1 coluna, o separador está errado
                        if len(df.columns) > 1:
                            print(f"      ✅ Sucesso com {enc} e separador '{sep}'")
                            return formatar_preview(df, caminho.name)
                            
                    except Exception:
                        continue
            
            return f"❌ ERRO: Não foi possível ler {caminho.name} com os padrões testados.\n\n"

    except Exception as e:
        return f"❌ ERRO CRÍTICO em {caminho.name}: {str(e)}\n\n"
    
    return f"⚠️ ALERTA: Leitura falhou silenciosamente para {caminho.name}\n\n"

# --- EXECUÇÃO ---
print(f"🚀 INICIANDO RAIO-X DOS DADOS")
print(f"📂 Diretório Base: {BASE_DIR}")

conteudo_final = []

# Caminha recursivamente por todas as pastas
arquivos_encontrados = 0
for root, dirs, files in os.walk(BASE_DIR):
    for file in files:
        if file in TARGET_FILES:
            caminho_completo = Path(root) / file
            relatorio = processar_arquivo(caminho_completo)
            conteudo_final.append(relatorio)
            arquivos_encontrados += 1

# Salva o relatório
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(f"RELATÓRIO DE INSPEÇÃO DE DADOS - SINAPSE BR IA\n")
    f.write(f"Gerado automaticamente. Arquivos analisados: {arquivos_encontrados}\n\n")
    f.write("\n".join(conteudo_final))

print(f"\n✅ CONCLUÍDO! Relatório salvo em:")
print(f"📄 {OUTPUT_FILE}")
print("Abra este arquivo para ver os cabeçalhos e dados de 2017, 2024, SAEB e INSE.")
