#!/bin/bash
# Mata processos antigos
fuser -k 8081-8089/tcp > /dev/null 2>&1
echo "[🔥] INICIANDO SISTEMA AKAME..."
cd ~/Imperio_IA
# Inicia o servidor Python
python sentinela.py & 
# Inicia o Sentinela de Backup Automático (A cada 5 min)
echo "[🛰️] BACKUP AUTOMÁTICO ATIVADO EM SEGUNDO PLANO."
while true; do
    git add .
    git commit -m "Auto-Sinc Akame" && git push origin main
    sleep 300
done &
