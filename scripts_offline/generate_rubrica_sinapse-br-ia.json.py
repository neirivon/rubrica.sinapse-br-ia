"""
=========================================================================================
ARQUIVO:       generate_rubrica_json.py
CAMINHO:       .../PROJETO_SINAPSE_BR_IA/scripts_offline/generate_rubrica_sinapse_br_ia_json.py
-----------------------------------------------------------------------------------------
PROJETO:       ECOSSISTEMA SINAPSE-BR IA (Educação Profissional e Tecnológica)
INSTITUIÇÃO:   IFTM / UFU (Pós-Graduação em Docência)
AUTOR:         Neirivon Elias Cardoso
DATA:          21/01/2026
VERSÃO:        1.0.0 (Data Generator)

DESCRIÇÃO:     
    Gera o artefato JSON oficial da "Rubrica SINAPSE-BR IA (v4)".
    Este JSON contém:
    1. Metadados do TCC.
    2. As 8 Dimensões Neuropsicopedagógicas.
    3. Os 4 Níveis de Progressão (Emergente -> Avançado).
    4. Os Exemplos Práticos Territorializados (TMAP) para cada dimensão.
    
    Este arquivo JSON servirá de entrada para o Streamlit e para o Validador LLM.
=========================================================================================
"""

import json
import os
from pathlib import Path

# --- CONFIGURAÇÃO DE CAMINHOS ---
# Define onde o JSON será salvo: na pasta 'data' na raiz do projeto
DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
DIRETORIO_RAIZ = os.path.dirname(DIRETORIO_ATUAL)
PASTA_DATA = os.path.join(DIRETORIO_RAIZ, "data")
NOME_ARQUIVO = "rubrica_sinapse_v4_tmap.json"

# --- CONTEÚDO DA RUBRICA (V4 + TMAP) ---
RUBRICA_SINAPSE = {
    "metadados": {
        "titulo": "RUBRICA SINAPSE-BR IA",
        "versao": "4.0 (Integrada EPT/Neuro/DUA/Território)",
        "contexto": "Educação Profissional e Tecnológica (EPT) - IFTM",
        "autor": "Neirivon Elias Cardoso",
        "orientadora": "Profa. Dra. Thays Martins Vital da Silva",
        "objetivo_geral": "Instrumento de mediação da aprendizagem, equidade territorial e inclusão."
    },
    "escala_niveis": {
        "1": {"rotulo": "Emergente", "conceito": "Reprodução/Memória. Dependência externa."},
        "2": {"rotulo": "Intermediário", "conceito": "Compreensão/Aplicação Simples. Necessita de andaimes."},
        "3": {"rotulo": "Proficiente", "conceito": "Análise/Relação. Autonomia consistente."},
        "4": {"rotulo": "Avançado", "conceito": "Criação/Metacognição. Estratégias inovadoras e complexas."}
    },
    "dimensoes": [
        {
            "id": "D1",
            "eixo": "Eixo Cognitivo",
            "titulo": "Progressão Cognitiva Educacional",
            "objetivo": "Avaliar a complexidade do pensamento (Taxonomia de Bloom/SOLO).",
            "descritores": {
                "nivel_1": "O estudante lida apenas com informações simples, memorizadas ou repetidas. Foco em lembrar/reproduzir.",
                "nivel_2": "Compreende conceitos básicos e consegue aplicá-los em situações padrão com apoio docente (Andaime).",
                "nivel_3": "Analisa criticamente, estabelece relações entre variáveis e propõe explicações próprias.",
                "nivel_4": "Elabora projetos originais (criação) utilizando dados locais e estratégias científicas complexas (Metacognição)."
            },
            "exemplos_tmap": [
                {"cidade": "Uberlândia", "atividade": "Criação de gráficos climáticos comparando dados do INMET com sensação térmica em bairros periféricos."},
                {"cidade": "Ituiutaba", "atividade": "Análise do pH do Rio Tijuco e proposta de filtros de cerâmica local para ribeirinhos."},
                {"cidade": "Patos de Minas", "atividade": "Desenvolvimento de app para roteirizar coleta de lixo durante a Fenamilho."}
            ]
        },
        {
            "id": "D2",
            "eixo": "Eixo Afetivo/Social",
            "titulo": "Perfil Socioeconômico e Contextual",
            "objetivo": "Reconhecer as condições materiais de existência como parte da avaliação.",
            "descritores": {
                "nivel_1": "Acesso restrito a recursos tecnológicos e culturais; necessita de suporte básico para permanência.",
                "nivel_2": "Participa das atividades com apoio institucional em ambientes estruturados.",
                "nivel_3": "Adapta-se a diferentes contextos de aprendizagem com autonomia relativa.",
                "nivel_4": "Propõe soluções para equidade e justiça social dentro do ambiente escolar e comunitário."
            },
            "exemplos_tmap": [
                {"cidade": "Araguari", "atividade": "Mapeamento de transporte rural da cafeicultura para propor horários flexíveis no AVA."},
                {"cidade": "Campina Verde", "atividade": "Projeto de inclusão digital via dados móveis para filhos de trabalhadores rurais."},
                {"cidade": "Uberaba", "atividade": "Estudo comparativo de acesso cultural entre o Centro e o bairro Residencial 2000."}
            ]
        },
        {
            "id": "D3",
            "eixo": "Eixo Neurofuncional",
            "titulo": "Autonomia e Autorregulação da Aprendizagem",
            "objetivo": "Avaliar funções executivas e capacidade de 'aprender a aprender'.",
            "descritores": {
                "nivel_1": "Total dependência de regulação externa (professor) para iniciar e concluir tarefas.",
                "nivel_2": "Inicia a organização pessoal (tempo/espaço) mediante orientação direta.",
                "nivel_3": "Administra tempo, metas e recursos com consistência. Identifica suas próprias dúvidas.",
                "nivel_4": "Planeja, monitora e executa estratégias autônomas de aprendizagem (Metacognição plena)."
            },
            "exemplos_tmap": [
                {"cidade": "Frutal", "atividade": "Cronogramas de estudo compartilhados conciliando safra do abacaxi e provas."},
                {"cidade": "Sacramento", "atividade": "Grupos de estudo autônomos na biblioteca municipal para recuperação de matemática."},
                {"cidade": "Canápolis", "atividade": "Uso de diários de bordo focados em 'como aprendi' e estratégias de estudo."}
            ]
        },
        {
            "id": "D4",
            "eixo": "Eixo Comunicacional",
            "titulo": "Capacidade de Comunicação e Expressão",
            "objetivo": "Avaliar a clareza e o multiletramento.",
            "descritores": {
                "nivel_1": "Vocabulário restrito, dificuldade de expressar ideias de forma linear.",
                "nivel_2": "Comunica-se com clareza em contextos familiares e gêneros textuais simples.",
                "nivel_3": "Expressa ideias com coesão, coerência e argumentos relevantes em diferentes mídias.",
                "nivel_4": "Domina a linguagem (escrita/oral/digital) com argumentação crítica e adaptação ao público."
            },
            "exemplos_tmap": [
                {"cidade": "Itapagipe", "atividade": "Podcasts resgatando histórias orais de trabalhadores de fazendas antigas."},
                {"cidade": "Prata", "atividade": "Cartas argumentativas à Câmara Municipal sobre internet rural."},
                {"cidade": "Patrocínio", "atividade": "Seminários explicando a cadeia do café para visitantes externos."}
            ]
        },
        {
            "id": "D5",
            "eixo": "Eixo Metodológico",
            "titulo": "Raciocínio Lógico e Solução de Problemas",
            "objetivo": "Avaliar o pensamento computacional e a resolução de problemas reais.",
            "descritores": {
                "nivel_1": "Executa procedimentos simples ou algorítmicos sem compreender a lógica subjacente.",
                "nivel_2": "Aplica fórmulas ou estratégias conhecidas para resolver problemas padrão com apoio.",
                "nivel_3": "Decompõe problemas contextualizados e os resolve de forma estruturada.",
                "nivel_4": "Cria estratégias inovadoras e transfere conhecimentos para resolver desafios complexos/inéditos."
            },
            "exemplos_tmap": [
                {"cidade": "Coromandel", "atividade": "Cálculo de perdas no transporte de leite em estradas de terra via Python/Planilha."},
                {"cidade": "Monte Carmelo", "atividade": "Fluxogramas para otimizar escalas em cooperativas de cerâmica."},
                {"cidade": "Tupaciguara", "atividade": "Jogos de tabuleiro simulando gestão de recursos hídricos da represa."}
            ]
        },
        {
            "id": "D6",
            "eixo": "Eixo Ético",
            "titulo": "Engajamento e Responsabilidade Social",
            "objetivo": "Avaliar a postura cidadã e colaborativa.",
            "descritores": {
                "nivel_1": "Participação passiva. Cumpre tarefas apenas por obrigação externa.",
                "nivel_2": "Contribui com o grupo quando estimulado. Demonstra empatia básica.",
                "nivel_3": "Participa com protagonismo, colabora com pares e respeita a diversidade.",
                "nivel_4": "Lidera ações transformadoras, solidárias e éticas na comunidade escolar."
            },
            "exemplos_tmap": [
                {"cidade": "Nova Ponte", "atividade": "Logística completa de campanha de agasalhos gerida por alunos."},
                {"cidade": "Conceição das Alagoas", "atividade": "Mutirão técnico para inspeção elétrica em asilos locais."},
                {"cidade": "Uberaba", "atividade": "Produção de fanzines e debates sobre racismo estrutural no bairro Abadia."}
            ]
        },
        {
            "id": "D7",
            "eixo": "Eixo Epistemológico",
            "titulo": "Relacionamento com Saberes Científicos e Culturais",
            "objetivo": "Avaliar a apropriação do conhecimento historicamente acumulado.",
            "descritores": {
                "nivel_1": "Espectador passivo de saberes escolares. Não conecta com a vida.",
                "nivel_2": "Reproduz conteúdos disciplinares, mas com pouca contextualização crítica.",
                "nivel_3": "Relaciona conhecimentos científicos a práticas vividas e fenômenos observáveis.",
                "nivel_4": "Integra criticamente saberes científicos, culturais e populares (Omnilateralidade)."
            },
            "exemplos_tmap": [
                {"cidade": "Araxá", "atividade": "Análise química da lama local vs. saberes populares de moradores antigos."},
                {"cidade": "Lagoa Formosa", "atividade": "Documentação sociológica e econômica da organização das Festas de Reis."},
                {"cidade": "Perdizes", "atividade": "Comparativo entre agricultura de precisão (drones) e manejo tradicional da batata."}
            ]
        },
        {
            "id": "D8",
            "eixo": "Eixo Territorial (CTC)",
            "titulo": "Pertencimento e Equidade Territorial",
            "objetivo": "Avaliar a conexão do saber com o território (Triângulo Mineiro) e a identidade.",
            "descritores": {
                "nivel_1": "Não reconhece ou desvaloriza sua identidade, história local e território.",
                "nivel_2": "Identifica desigualdades locais, mas de forma descritiva ou assistencialista.",
                "nivel_3": "Atua valorizando a cultura local, os arranjos produtivos e a diversidade do território.",
                "nivel_4": "Formula ações concretas para justiça territorial, ambiental e cultural (Geofilosofia aplicada)."
            },
            "exemplos_tmap": [
                {"cidade": "Gurinhatã", "atividade": "Mapeamento georreferenciado de comunidades quilombolas e rotas históricas."},
                {"cidade": "Monte Alegre de Minas", "atividade": "Organização de Feira Territorial para valorização da agricultura familiar."},
                {"cidade": "Iturama", "atividade": "Projeto de turismo pedagógico sobre memória ribeirinha e impacto da hidrelétrica."}
            ]
        }
    ],
    "referencias_teoricas": [
        "Bloom & Krathwohl (Taxonomia)",
        "Vygotsky (ZDP e Mediação)",
        "Paulo Freire (Pedagogia da Autonomia)",
        "Milton Santos (Território Usado)",
        "CAST (Desenho Universal para Aprendizagem - DUA)",
        "Ciavatta & Ramos (Ensino Médio Integrado)",
        "Gelda Costa (História Instituições Escolares)",
        "Paulo Irineu (Geofilosofia)"
    ]
}

# --- FUNÇÃO GERADORA ---
def gerar_arquivo_json():
    # Garante que a pasta 'data' existe
    Path(PASTA_DATA).mkdir(parents=True, exist_ok=True)
    
    caminho_completo = os.path.join(PASTA_DATA, NOME_ARQUIVO)
    
    try:
        with open(caminho_completo, 'w', encoding='utf-8') as f:
            json.dump(RUBRICA_SINAPSE, f, indent=4, ensure_ascii=False)
        
        print("\n" + "="*60)
        print(f"✅ SUCESSO: JSON da Rubrica SINAPSE-BR IA gerado!")
        print(f"📂 Arquivo: {NOME_ARQUIVO}")
        print(f"📍 Caminho: {caminho_completo}")
        print("="*60 + "\n")
        
    except Exception as e:
        print(f"❌ ERRO ao gerar JSON: {e}")

if __name__ == "__main__":
    gerar_arquivo_json()
