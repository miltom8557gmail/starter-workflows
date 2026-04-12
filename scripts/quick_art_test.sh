#!/bin/bash
# Teste de geração gratuita via Pollinations
PROMPT=$(echo "$1" | sed 's/ /%20/g')
echo "🎨 Gerando visualização rápida: https://image.pollinations.ai/prompt/$PROMPT?width=1080&height=1920&nologo=true"
