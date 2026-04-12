#!/bin/bash
# Verificador de limite gratuito para evitar gastos
CHECK_LIMIT=$(curl -s -I "https://api.tensor.art" | grep -i "x-rate-limit-remaining")

if [[ "$CHECK_LIMIT" == *"0"* ]]; then
    echo "⚠️ [SENTINELA]: Créditos Free esgotados. Bloqueando requisição para evitar custos."
    exit 1
else
    echo "✅ [SENTINELA]: Créditos disponíveis. Prosseguindo..."
fi
