"""
=========================================================================================
ARQUIVO:       rotor_validator_local.py
CAMINHO:       .../scripts_offline/rotor_validator_local.py
-----------------------------------------------------------------------------------------
PROJETO:       ECOSSISTEMA SINAPSE-BR IA
DESCRIÇÃO:     Módulo de Auditoria Qualitativa (ROTOR V5.0).
               Realiza a análise pedagógica profunda de cada um dos 8 EIXOS.
               
OBJETIVO:      Para cada Eixo (E1-E8), entregar:
               1. Nota Mullinix (1-4)
               2. Justificativa Técnica (Por que?)
               3. AÇÃO CORRETIVA (O que mudar no texto para atingir a excelência?)
=========================================================================================
"""

import os
import json
import datetime
import requests
from pathlib import Path

# --- CONFIGURAÇÕES ---
MODELO_OLLAMA = "llama3"
DIRETORIO_RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARQUIVO_ENTRADA = os.path.join(DIRETORIO_RAIZ, "data", "rubrica_sinapse_br_ia.json")
PASTA_SAIDA = os.path.join(DIRETORIO_RAIZ, "data", "rotor_artifacts")

# --- CONTRATO DE AUDITORIA (MULLINIX - SINAPSE) ---
# Define o padrão ouro que a IA deve cobrar
CRITERIOS_EXCELENCIA = """
PADRÃO DE NOTA 4 (EXCELENTE):
1. Territorialidade: O eixo cita cidades reais do TMAP (Uberlândia, Ituiutaba, etc.) e atividades econômicas locais?
2. Neuropsicopedagogia: O eixo menciona processos mentais claros (metacognição, funções executivas)?
3. DUA: A linguagem é inclusiva e focada na superação de barreiras?
"""

def ler_rubrica(caminho):
    if not os.path.exists(caminho): return None
    with open(caminho, 'r', encoding='utf-8') as f: return json.dumps(json.load(f), ensure_ascii=False)

def auditar_qualidade(texto_rubrica):
    print(f"🧠 [IA] Iniciando Auditoria Qualitativa Propositiva ({MODELO_OLLAMA})...")
    print("⏳ [IA] Analisando cada eixo e gerando soluções de melhoria...")
    
    prompt = f"""
    ### SUA FUNÇÃO ###
    Você é o Consultor Pedagógico Sênior do projeto SINAPSE-BR IA.
    Sua tarefa é analisar criticamente o JSON da rubrica abaixo.

    ### CRITÉRIOS DE AVALIAÇÃO ###
    {CRITERIOS_EXCELENCIA}

    ### OBJETO DE ANÁLISE ###
    {texto_rubrica}

    ### FORMATO DE RESPOSTA OBRIGATÓRIO (JSON PT-BR) ###
    Analise os 8 EIXOS (E1 a E8) um por um. Responda APENAS este JSON:
    {{
        "auditoria_eixos": [
            {{
                "id": "E1 - Eixo Cognitivo",
                "nota_mullinix": (1 a 4),
                "motivo_da_nota": "Explique brevemente o ponto forte ou fraco encontrado.",
                "solucao_para_melhoria": "Se nota < 4, sugira COMO reescrever. Se nota 4, sugira como manter/expandir."
            }},
            {{
                "id": "E2 - Eixo Afetivo",
                "nota_mullinix": (1 a 4),
                "motivo_da_nota": "...",
                "solucao_para_melhoria": "..."
            }},
            {{
                "id": "E3 - Eixo Metodologico",
                "nota_mullinix": (1 a 4),
                "motivo_da_nota": "...",
                "solucao_para_melhoria": "..."
            }},
            {{
                "id": "E4 - Eixo Neurofuncional",
                "nota_mullinix": (1 a 4),
                "motivo_da_nota": "...",
                "solucao_para_melhoria": "..."
            }},
            {{
                "id": "E5 - Eixo Avaliativo",
                "nota_mullinix": (1 a 4),
                "motivo_da_nota": "...",
                "solucao_para_melhoria": "..."
            }},
            {{
                "id": "E6 - Eixo Tecnologico",
                "nota_mullinix": (1 a 4),
                "motivo_da_nota": "...",
                "solucao_para_melhoria": "..."
            }},
            {{
                "id": "E7 - Eixo Territorial",
                "nota_mullinix": (1 a 4),
                "motivo_da_nota": "...",
                "solucao_para_melhoria": "..."
            }},
            {{
                "id": "E8 - Eixo Inclusivo",
                "nota_mullinix": (1 a 4),
                "motivo_da_nota": "...",
                "solucao_para_melhoria": "..."
            }}
        ],
        "diagnostico_geral": "Texto resumo sobre a maturidade do artefato.",
        "score_total": (Soma das notas)
    }}
    """
    
    try:
        resp = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": MODELO_OLLAMA,
                "prompt": prompt,
                "stream": False,
                "format": "json",
                "options": {"temperature": 0.2} # Baixa temperatura para ser analítico
            }
        )
        return json.loads(resp.json()['response'])
    except Exception as e:
        print(f"❌ [ERRO] Falha na conexão com LLM: {e}")
        return None

def salvar(dados):
    Path(PASTA_SAIDA).mkdir(parents=True, exist_ok=True)
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    nome = f"rotor_audit_QUALITATIVA_{ts}.json"
    caminho = os.path.join(PASTA_SAIDA, nome)
    
    # Recalcula soma para garantir precisão matemática
    try:
        soma = sum(item['nota_mullinix'] for item in dados['auditoria_eixos'])
        dados['score_total'] = soma
    except: pass

    with open(caminho, 'w', encoding='utf-8') as f:
        json.dump({"meta": {"tipo": "Auditoria Qualitativa Propositiva"}, "dados": dados}, f, indent=4, ensure_ascii=False)
    return caminho

if __name__ == "__main__":
    c = ler_rubrica(ARQUIVO_ENTRADA)
    if c:
        res = auditar_qualidade(c)
        if res:
            path = salvar(res)
            print(f"✅ Auditoria Completa!")
            print(f"🏆 Score: {res.get('score_total', 0)} / 32")
            print(f"📂 Relatório com Soluções: {path}")
