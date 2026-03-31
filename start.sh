#!/bin/bash
fuser -k 8081-8089/tcp > /dev/null 2>&1
echo "[🔥] SISTEMA AKAME ETERNIZADO..."
cd ~/Imperio_IA
python sentinela.py & 
echo "[🛰️] BACKUP AUTOMÁTICO ATIVO."
while true; do
    git add .
    git commit -m "[⚔️] GUARDIAO DO IMPERIO: $(date)" && git push origin main
    sleep 300
done &
