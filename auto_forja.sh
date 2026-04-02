#!/bin/bash
# Script de Sincronia Eterna Akame
echo "[⚔️] INICIANDO SENTINELA DE BACKUP..."

while true; do
    # Verifica se houve mudanças nos arquivos
    if [[ -n $(git status -s) ]]; then
        echo "[🛰️] MUDANÇA DETECTADA! SINCRONIZANDO COM GITHUB..."
        git add .
        git commit -m "[🚀] ATUALIZAÇÃO AUTOMÁTICA: $(date +'%d/%m/%Y %H:%M:%S')"
        git push origin main
        echo "[✅] IMPÉRIO ATUALIZADO NA NUVEM."
    fi
    sleep 30 # Verifica a cada 30 segundos
done
