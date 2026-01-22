"""
=========================================================================================
ARQUIVO:       refine_rubrica_platinum.py
CAMINHO:       .../scripts_offline/refine_rubrica_platinum.py
DESCRIÇÃO:     Script de Equalização.
               Adiciona o 3º exemplo faltante nos eixos que não foram tocados pelo
               refinamento anterior (E1, E2, E4, E5, E7).
SAÍDA:         data/rubrica_sinapse_br_ia.json (Versão Platinum - Simétrica)
=========================================================================================
"""

import json
import os
from pathlib import Path

# --- CONFIGURAÇÃO ---
DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
DIRETORIO_RAIZ = os.path.dirname(DIRETORIO_ATUAL)
CAMINHO_JSON = os.path.join(DIRETORIO_RAIZ, "data", "rubrica_sinapse_br_ia.json")

# --- PACOTE DE EQUALIZAÇÃO (O 3º EXEMPLO FALTANTE) ---
NOVOS_EXEMPLOS = {
    "E1": "Patrocínio: Estudantes sintetizam dados da cafeicultura para criar um manual de boas práticas (Síntese/Criação).",
    "E2": "Ibiá: Desenvolvimento de resiliência e orgulho local através da valorização do Queijo Minas Artesanal.",
    "E4": "Uberlândia (Campus Rural): Alunos utilizam técnicas de 'atenção plena' para manter o foco durante longos experimentos de campo.",
    "E5": "Araxá: Implementação de 'avaliação por pares' cega para analisar projetos de mineração sustentável.",
    "E7": "Tupaciguara: Resgate da memória das antigas rotas de tropeiros como elemento de identidade turística local."
}

def equalizar_rubrica():
    if not os.path.exists(CAMINHO_JSON):
        print(f"❌ Erro: Arquivo {CAMINHO_JSON} não encontrado.")
        return

    try:
        with open(CAMINHO_JSON, 'r', encoding='utf-8') as f:
            dados = json.load(f)
    except Exception as e:
        print(f"❌ Erro ao ler JSON: {e}")
        return

    print("💎 Iniciando Equalização Platinum (Simetria de 3 exemplos)...")
    
    # Detecta a chave correta (eixos ou dimensoes)
    chave_principal = 'eixos' if 'eixos' in dados else 'dimensoes'
    count = 0

    for eixo in dados[chave_principal]:
        id_eixo = eixo.get('id')
        
        # Verifica se este eixo precisa do 3º exemplo
        if id_eixo in NOVOS_EXEMPLOS:
            novo_ex_str = NOVOS_EXEMPLOS[id_eixo]
            
            # Formata o novo exemplo como Objeto ou String, dependendo de como está no JSON
            # O padrão atual parece ser string no formato "Cidade: Ação"
            # Se for lista de dicionários, precisamos converter
            
            lista_atual = eixo.get('exemplos_tmap', [])
            
            # Verificação de segurança para não duplicar
            if len(lista_atual) < 3:
                lista_atual.append(novo_ex_str)
                eixo['exemplos_tmap'] = lista_atual
                print(f"   ➕ {id_eixo}: 3º Exemplo adicionado ({novo_ex_str.split(':')[0]}).")
                count += 1
            else:
                print(f"   ℹ️ {id_eixo}: Já possui 3 ou mais exemplos.")

    # Atualiza Metadados
    if 'metadados' in dados:
        dados['metadados']['versao'] = "Platinum (Simétrica 3x8)"
        dados['metadados']['status'] = "Finalizada e Equalizada"
        dados['metadados']['ultima_atualizacao'] = "21/01/2026 - Equalização TMAP"

    # Salva
    with open(CAMINHO_JSON, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

    print(f"\n💎 Sucesso! {count} eixos foram equalizados.")
    print(f"📂 JSON final salvo em: {CAMINHO_JSON}")

if __name__ == "__main__":
    equalizar_rubrica()
