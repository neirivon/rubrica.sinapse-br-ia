"""
=========================================================================================
ARQUIVO:       generate_rubrica_sinapse_br_ia.py
CAMINHO:       .../scripts_offline/generate_rubrica_sinapse_br_ia.py
DESCRIÇÃO:     Gera o JSON oficial da Rubrica SINAPSE-BR IA.
               ATENÇÃO: Estrutura estritamente alinhada aos scripts Python do Streamlit
               (04_Mapa_Fundamentacao_Teorica.py).
=========================================================================================
"""

import json
import os
from pathlib import Path

DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
DIRETORIO_RAIZ = os.path.dirname(DIRETORIO_ATUAL)
PASTA_DATA = os.path.join(DIRETORIO_RAIZ, "data")
NOME_ARQUIVO = "rubrica_sinapse_br_ia.json"

# --- ESTRUTURA OFICIAL (Alinhada aos Eixos do Script 04) ---
RUBRICA_SINAPSE = {
    "metadados": {
        "titulo": "RUBRICA SINAPSE-BR IA",
        "versao": "Final (Sincronizada com Streamlit)",
        "contexto": "EPT / IFTM / TMAP",
        "data_geracao": "21/01/2026"
    },
    "eixos": [
        {
            "id": "E1",
            "nome": "Eixo Cognitivo",
            "foco": "Taxonomia de Bloom e Complexidade do Pensamento",
            "niveis": {
                "1": "Memorização/Reprodução (Baixa Ordem)",
                "4": "Criação/Análise Crítica (Alta Ordem)"
            },
            "exemplos_tmap": [
                "Uberlândia: Alunos criam novos algoritmos baseados em dados climáticos (Criação).",
                "Ituiutaba: Estudantes analisam a composição química da água local (Análise)."
            ]
        },
        {
            "id": "E2",
            "nome": "Eixo Afetivo",
            "foco": "Engajamento, Motivação e Inteligência Emocional",
            "niveis": {
                "1": "Participação passiva ou resistente.",
                "4": "Liderança empática e engajamento profundo."
            },
            "exemplos_tmap": [
                "Nova Ponte: Alunos lideram campanhas solidárias com autonomia emocional.",
                "Conceição das Alagoas: Trabalho voluntário técnico em asilos (Empatia)."
            ]
        },
        {
            "id": "E3",
            "nome": "Eixo Metodologico",
            "foco": "Raciocínio Lógico, Resolução de Problemas e Processos",
            "niveis": {
                "1": "Execução mecânica de passos.",
                "4": "Desenvolvimento de estratégias inéditas de solução."
            },
            "exemplos_tmap": [
                "Monte Carmelo: Criação de fluxogramas para otimizar cerâmicas locais.",
                "Coromandel: Cálculo logístico complexo para transporte de leite."
            ]
        },
        {
            "id": "E4",
            "nome": "Eixo Neurofuncional",
            "foco": "Funções Executivas (Planejamento, Inibição, Memória)",
            "niveis": {
                "1": "Dependência total de regulação externa.",
                "4": "Autorregulação plena e gestão do foco."
            },
            "exemplos_tmap": [
                "Frutal: Gestão autônoma do tempo de estudo durante a safra agrícola.",
                "Sacramento: Organização de grupos de estudo sem tutela docente."
            ]
        },
        {
            "id": "E5",
            "nome": "Eixo Avaliativo",
            "foco": "Metacognição e Capacidade de Autoavaliação",
            "niveis": {
                "1": "Foco apenas na nota final.",
                "4": "Monitoramento contínuo do próprio aprendizado (Aprender a Aprender)."
            },
            "exemplos_tmap": [
                "Canápolis: Uso de diários de bordo para monitorar estratégias de erro/acerto.",
                "Patrocínio: Alunos criam seus próprios critérios de qualidade para projetos."
            ]
        },
        {
            "id": "E6",
            "nome": "Eixo Tecnologico",
            "foco": "Letramento Digital e Uso Ético de IA",
            "niveis": {
                "1": "Consumidor passivo de tecnologia.",
                "4": "Produtor crítico de soluções tecnológicas éticas."
            },
            "exemplos_tmap": [
                "Uberaba (Parque Tec): Desenvolvimento de soluções IoT para problemas urbanos.",
                "Campina Verde: Inclusão digital ativa para comunidades rurais desconectadas."
            ]
        },
        {
            "id": "E7",
            "nome": "Eixo Territorial",
            "foco": "Pertencimento, Identidade e Contexto Local (Geofilosofia)",
            "niveis": {
                "1": "Desconexão com a realidade local.",
                "4": "Intervenção transformadora no território."
            },
            "exemplos_tmap": [
                "Gurinhatã: Mapeamento histórico de comunidades tradicionais.",
                "Iturama: Projetos de memória ribeirinha e impacto ambiental local."
            ]
        },
        {
            "id": "E8",
            "nome": "Eixo Inclusivo",
            "foco": "Desenho Universal para Aprendizagem (DUA) e Acessibilidade",
            "niveis": {
                "1": "Padronização excludente.",
                "4": "Flexibilidade curricular e acessibilidade plena."
            },
            "exemplos_tmap": [
                "Araguari: Adaptação de horários e materiais para alunos trabalhadores rurais.",
                "Prata: Criação de materiais didáticos multimodais (áudio/texto) para todos."
            ]
        }
    ]
}

def gerar():
    Path(PASTA_DATA).mkdir(parents=True, exist_ok=True)
    caminho = os.path.join(PASTA_DATA, NOME_ARQUIVO)
    with open(caminho, 'w', encoding='utf-8') as f:
        json.dump(RUBRICA_SINAPSE, f, indent=4, ensure_ascii=False)
    print(f"✅ [SUCESSO] JSON Sincronizado gerado em: {caminho}")

if __name__ == "__main__":
    gerar()
