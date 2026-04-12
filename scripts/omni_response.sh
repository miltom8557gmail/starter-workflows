#!/bin/bash
# Coordenador de Respostas Gratuitas (Jarvis Style)

TEXTO_PROMPT="$1"

# Passa pelo Sentinela antes de tudo
./scripts/cost_sentinel.sh || exit 1

# 1. Envia para o Groq (Cérebro Rápido/Grátis) para gerar o diálogo
echo "🧠 Consultando Groq Failover..."
# (A integração da chave do Groq será feita no próximo passo de segurança)

# 2. Dispara a Geração de Imagem no Pollinations (Ilimitado/Grátis)
IMAGE_URL="https://image.pollinations.ai/prompt/$(echo $TEXTO_PROMPT | sed 's/ /%20/g')?width=1080&height=1920&nologo=true"
echo "🎨 Arte gerada: $IMAGE_URL"

# 3. Gera a Voz no Hugging Face (Se houver cota)
./scripts/voice_processor.sh "Mestre, processei sua visão. A arte está pronta."
