#!/bin/bash
# Verificador de limite gratuito para evitar gastos
CHECK_LIMIT=$(curl -s -I "https://api.tensor.art" | grep -i "x-rate-limit-remaining")

if [[ "$CHECK_LIMIT" == *"0"* ]]; then
    echo "⚠️ [SENTINELA]: Créditos Free esgotados. Bloqueando requisição para evitar custos."
    exit 1
else
    echo "✅ [SENTINELA]: Créditos disponíveis. Prosseguindo..."
fi

# Verificador Hugging Face
check_hf_status() {
    STATUS=$(curl -s -o /dev/null -w "%{http_code}" "https://api-inference.huggingface.co/models/AKAME_MODEL")
    if [ "$STATUS" -eq 402 ]; then
        echo "⚠️ [SENTINELA]: Hugging Face exigindo pagamento. Bloqueando acesso imediatamente."
        exit 1
    fi
}
