"""
=========================================================================================
ARQUIVO:       refine_rubrica_gold.py
CAMINHO:       .../scripts_offline/refine_rubrica_gold.py
DESCRIÇÃO:     Aplica patches de correção na Rubrica SINAPSE-BR IA (Versão Eixos).
               CORREÇÃO DE BUG: Agora acessa a chave 'eixos' corretamente.
SAÍDA:         data/rubrica_sinapse_br_ia.json (Versão Gold Master)
=========================================================================================
"""

import json
import os
from pathlib import Path

# --- CONFIGURAÇÃO ---
DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
DIRETORIO_RAIZ = os.path.dirname(DIRETORIO_ATUAL)
CAMINHO_JSON = os.path.join(DIRETORIO_RAIZ, "data", "rubrica_sinapse_br_ia.json")

# --- CONTEÚDO DE MELHORIA (PATCHES) ---
# Novos exemplos robustos para os eixos criticados
MELHORIAS_EIXOS = {
    "E3": { # Metodológico
        "novos_exemplos": [
            "Monte Carmelo: Alunos utilizam 'Design Thinking' para criar novos padrões de queima na cerâmica local.",
            "Coromandel: Aplicação de 'Aprendizagem Baseada em Projetos' (PBL) para resolver a logística do leite.",
            "Patos de Minas: Uso de 'Sala de Aula Invertida' para debater genética do milho com produtores."
        ],
        "nivel_4_refinado": "Cria e valida estratégias metodológicas inéditas (ex: novos algoritmos/processos) para resolver desafios complexos do arranjo produtivo local."
    },
    "E6": { # Tecnológico
        "novos_exemplos": [
            "Uberaba (Parque Tec): Prototipagem de sensores IoT de baixo custo para monitoramento de enchentes.",
            "Iturama: Uso de Drones e IA para mapeamento de áreas de preservação permanente (APP).",
            "Campina Verde: Desenvolvimento de redes Mesh offline para levar comunicação a assentamentos."
        ],
        "nivel_4_refinado": "Atua como produtor crítico de tecnologia, desenvolvendo soluções éticas (IA/IoT) que respondem a demandas específicas do território."
    },
    "E8": { # Inclusivo
        "novos_exemplos": [
            "Araguari: Adaptação sensorial de materiais didáticos para alunos com TEA filhos de trabalhadores rurais.",
            "Prata: Criação de interfaces de voz em apps agrícolas para produtores idosos com baixa literacia.",
            "Uberlândia: Projeto de acessibilidade arquitetônica no transporte público focado na periferia."
        ],
        "nivel_4_refinado": "Desenha soluções universais (DUA) que eliminam barreiras arquitetônicas, digitais e atitudinais, garantindo equidade plena."
    }
}

def aplicar_refinamento():
    if not os.path.exists(CAMINHO_JSON):
        print(f"❌ JSON base não encontrado em: {CAMINHO_JSON}")
        return

    # 1. Carregar JSON atual
    try:
        with open(CAMINHO_JSON, 'r', encoding='utf-8') as f:
            dados = json.load(f)
    except Exception as e:
        print(f"❌ Erro ao ler JSON: {e}")
        return

    print("🛠️ Aplicando correções de excelência (Gold Master)...")

    # 2. Verificar Chave Correta
    chave_principal = 'eixos'
    if 'eixos' not in dados:
        if 'dimensoes' in dados:
            chave_principal = 'dimensoes'
            print("⚠️ Aviso: Usando chave antiga 'dimensoes'.")
        else:
            print("❌ Erro fatal: Estrutura do JSON desconhecida (nem 'eixos' nem 'dimensoes').")
            return

    # 3. Aplicar Patches
    count = 0
    for eixo in dados[chave_principal]:
        id_eixo = eixo.get('id')
        
        if id_eixo in MELHORIAS_EIXOS:
            patch = MELHORIAS_EIXOS[id_eixo]
            
            # Atualiza Exemplos (Formato Lista de Strings para compatibilidade com Eixos)
            if 'exemplos_tmap' in eixo:
                eixo['exemplos_tmap'] = patch['novos_exemplos']
            elif 'exemplos_praticos' in eixo:
                eixo['exemplos_praticos'] = patch['novos_exemplos']
            
            # Atualiza Descritor Nível 4
            # Verifica se usa 'niveis' (novo) ou 'descritores' (antigo)
            if 'niveis' in eixo:
                eixo['niveis']['4'] = patch['nivel_4_refinado']
            elif 'descritores' in eixo:
                eixo['descritores']['nivel_4'] = patch['nivel_4_refinado']
            
            print(f"   ✅ {eixo.get('nome', eixo.get('titulo'))}: Turbinado com sucesso.")
            count += 1

    # 4. Atualizar Metadados
    if 'metadados' in dados:
        dados['metadados']['status'] = "Gold Master (Auditada e Refinada)"
        dados['metadados']['ultima_atualizacao'] = "21/01/2026 - Pós-Auditoria"

    # 5. Salvar
    with open(CAMINHO_JSON, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)
    
    print(f"\n✨ Sucesso! {count} eixos foram refinados.")
    print(f"📂 Arquivo salvo: {CAMINHO_JSON}")

if __name__ == "__main__":
    aplicar_refinamento()
