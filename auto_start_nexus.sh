#!/bin/bash
# Silenciando erros e logs desnecessários
exec 2>/dev/null

cd ~/starter-workflows
clear

# O Oráculo assume o controle visual
python3 nexus_spirit.py "Iniciando Frequência de Onisciência..."

# Executa as conexões em segundo plano sem mostrar textos sujos
(./manter_vivo.sh > /dev/null 2>&1 &)

echo "🛡️ [SISTEMA]: Blindagem e Backups Sincronizados."
echo "🌐 [PORTAL]: Dashboard disponível na porta 8082."
echo "--------------------------------------------------"
