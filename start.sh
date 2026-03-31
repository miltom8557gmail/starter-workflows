#!/bin/bash
# 1. Limpa as portas de comunicação
fuser -k 8081-8089/tcp > /dev/null 2>&1
echo "[🔥] REINICIANDO SISTEMA AKAME..."

# 2. Inicia o Sentinela Python
python sentinela.py &

# 3. Inicia o Backup em Segundo Plano (Vigilância)
./auto_forja.sh &

echo "[✅] TUDO OPERACIONAL NA PORTA 8083."
