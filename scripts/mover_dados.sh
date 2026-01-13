#!/bin/bash

# ==============================================================================
# SCRIPT DE MIGRAÇÃO DE DADOS (Versão pasta /scripts)
# ==============================================================================

# 1. Configuração Inteligente de Caminhos
# Descobre onde este script está salvo
DIR_SCRIPT="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Define a Raiz do Projeto (Um nível acima de /scripts)
RAIZ_PROJETO="$(dirname "$DIR_SCRIPT")"

# Define o Destino (Data Lake) - Ficará ao lado da pasta do projeto (SINAPSE2.0/sinapse_data_lake)
CAMINHO_DESTINO_ABS="$(dirname "$RAIZ_PROJETO")/sinapse_data_lake"

echo "--------------------------------------------------------"
echo "🔄 INICIANDO MIGRAÇÃO DE DADOS (Modo Seguro)"
echo "📍 Script em:     $DIR_SCRIPT"
echo "🏠 Raiz Projeto:  $RAIZ_PROJETO"
echo "🎯 Destino Lake:  $CAMINHO_DESTINO_ABS"
echo "--------------------------------------------------------"

# 2. Criar a pasta externa se não existir
if [ ! -d "$CAMINHO_DESTINO_ABS" ]; then
    echo "🔨 Criando pasta externa..."
    mkdir -p "$CAMINHO_DESTINO_ABS"
fi

# 3. Lista das pastas PESADAS para mover 
# (Caminhos relativos à raiz do projeto)
PASTAS_PARA_MOVER=(
    "data/microdados_censo_escolar_2017"
    "data/microdados_censo_escolar_2024"
    "data/MICRODADOS_SAEB_2023"
)

# 4. Loop de Movimentação e Atualização
for pasta_relativa in "${PASTAS_PARA_MOVER[@]}"; do
    
    # Caminho completo atual da pasta
    caminho_origem_completo="$RAIZ_PROJETO/$pasta_relativa"
    nome_pasta=$(basename "$pasta_relativa")
    
    if [ -d "$caminho_origem_completo" ]; then
        echo ""
        echo "📦 Processando: $nome_pasta"
        
        # A. Mover a pasta
        echo "   -> Movendo para o Data Lake..."
        if [ -d "$CAMINHO_DESTINO_ABS/$nome_pasta" ]; then
            echo "   ⚠️  Aviso: Pasta já existe no destino. Atualizando arquivos..."
            cp -r "$caminho_origem_completo/"* "$CAMINHO_DESTINO_ABS/$nome_pasta/"
            rm -rf "$caminho_origem_completo"
        else
            mv "$caminho_origem_completo" "$CAMINHO_DESTINO_ABS/"
        fi

        # B. Encontrar arquivos que citam essa pasta e atualizar o caminho
        # Agora busca em toda a raiz do projeto, excluindo .git e a própria pasta scripts (se quiser proteger o script)
        echo "   -> Atualizando referências nos scripts..."
        
        arquivos_afetados=$(grep -rRl "$pasta_relativa" "$RAIZ_PROJETO" --exclude-dir=.git --exclude-dir=sinapse_data_lake --exclude="mover_dados.sh")
        
        if [ -z "$arquivos_afetados" ]; then
            echo "   ℹ️  Nenhum script precisou ser alterado."
        else
            for arquivo in $arquivos_afetados; do
                echo "      ✏️  Alterando: $arquivo"
                # Substitui o caminho relativo pelo caminho ABSOLUTO novo
                sed -i "s|$pasta_relativa|$CAMINHO_DESTINO_ABS/$nome_pasta|g" "$arquivo"
            done
        fi
        
    else
        echo "💨 Pasta não encontrada na origem (já movida?): $pasta_relativa"
    fi
done

echo ""
echo "--------------------------------------------------------"
echo "✅ CONCLUÍDO!"
echo "Os dados pesados saíram de $RAIZ_PROJETO"
echo "E agora vivem em $CAMINHO_DESTINO_ABS"
echo "--------------------------------------------------------"
