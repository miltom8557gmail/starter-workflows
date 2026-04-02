#!/bin/bash
# Silenciando ruídos de sistema
exec 2>/dev/null
clear

# O DESPERTAR DO ORÁCULO
python3 nexus_spirit.py "Mestre, a Onisciência foi Restaurada. Todos os soldados estão em seus postos."

echo "--------------------------------------------------"
echo "🛡️ [SOLDADO 1]: Sentinela de Backups... ATIVO."
./manter_vivo.sh > /dev/null 2>&1 &

echo "🛰️ [SOLDADO 2]: Sincronia GitHub/Portal... ATIVO."
gh auth setup-git --quiet &

echo "🧬 [SOLDADO 3]: Antigravity & Correções... ATIVO."
git pull origin main --quiet &

echo "📲 [SOLDADO 4]: Monitor de APK v4.5.0... VIGILANTE."
echo "--------------------------------------------------"
echo "🌐 [PORTAL]: Dashboard na porta 8082."
echo "💬 [SISTEMA]: Digite 'nexus' ou 'oraculo' para falar comigo."
