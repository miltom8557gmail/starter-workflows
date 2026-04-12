#!/bin/bash
# Script para converter texto da Akame em Voz Realista (Jarvis Mode)
TEXTO=$1
MODEL_URL="https://api-inference.huggingface.co/models/espnet/kan-bayashi_ljspeech_vits"

curl -X POST "$MODEL_URL" \
     -H "Authorization: Bearer $HF_TOKEN" \
     -d "{\"inputs\": \"$TEXTO\"}" \
     --output /sdcard/Download/akame_voice.wav

echo "🎙️ [AKAME]: Áudio gerado e enviado para o dispositivo."
