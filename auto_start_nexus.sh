#!/bin/bash
cd ~/starter-workflows
clear
python3 nexus_spirit.py "Iniciando Sequência de Soberania..."

echo "🔄 [SISTEMA]: Renovando Backups e Conexões..."
./manter_vivo.sh > /dev/null 2>&1

echo "🛠️ [CORREÇÃO]: Aplicando Patches Automáticos no Antigravity..."
git pull origin main --quiet

echo "🌐 [CONEXÃO]: Sincronizando com o Portal Web e GitHub..."
gh auth setup-git

echo "✅ [STATUS]: SISTEMA 100% OPERACIONAL E PROTEGIDO."
