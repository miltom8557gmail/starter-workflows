#!/bin/bash
# NEXUS AUTO-SENTINEL - Vigilância 24/7

while true; do
    # Verifica se há novos modelos no Civitai
    FILES=$(ls Arsenal_NSFW/Civitai/ | wc -l)
    
    if [ "$FILES" -gt 0 ]; then
        echo "[AUTO]: Novo material detectado no Arsenal. Iniciando Ciclo de Sincronia..."
        
        # Avisa o Supabase via voz
        ./scripts/voice_processor.sh "Mestre, novos ativos detectados. Iniciando migração automática para a nuvem."
        
        # Executa a Sincronia de Elite
        ./scripts/sync_ecosystem.sh
        
        # Move arquivos processados para o cofre de segurança para não repetir o ciclo
        mv Arsenal_NSFW/Civitai/* vault_hf/
        
        echo "[AUTO]: Ciclo concluído. Sistema em standby."
    fi
    
    # Aguarda 5 minutos antes da próxima varredura
    sleep 300
done
