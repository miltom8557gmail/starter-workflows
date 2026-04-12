#!/bin/bash
echo "🕵️ [SENTINELA]: Caçando modelos NSFW de Elite..."
mkdir -p Arsenal_NSFW/Civitai
# Busca os 5 modelos mais baixados e bem avaliados da semana
QUERY=$(curl -s "https://civitai.com/api/v1/models?limit=5&types=Checkpoint&nsfw=true&sort=Highest+Rated")
echo "$QUERY" > Arsenal_NSFW/latest_scan.json
echo "✅ [ARRSENAL]: Scan completo. Novos alvos identificados."
