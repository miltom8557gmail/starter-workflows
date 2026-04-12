#!/bin/bash
echo "🕵️ [ARRSENAL]: Buscando Modelos de Elite..."
curl -s "https://civitai.com/api/v1/models?limit=5&nsfw=true" > Arsenal_NSFW/latest.json
echo "Sincronia Civitai concluída."
