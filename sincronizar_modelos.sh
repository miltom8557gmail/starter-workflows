#!/bin/bash
echo "[!] ACESSANDO ARMAZENAMENTO DO ANDROID..."
# Garante que a pasta de destino existe
mkdir -p ~/Imperio_IA/models/loras

echo "[!] COLETANDO LORAS DA PASTA DOWNLOADS..."
# Copia todos os .safetensors dos Downloads do celular para o Termux
cp /sdcard/Download/*.safetensors ~/Imperio_IA/models/loras/ 2>/dev/null

echo "[!] SINCRONIZANDO DNA DA INFLUENCER COM O GITHUB..."
git add models/loras/*.safetensors
git commit -m "General OMNI: Injecao de DNA LoRA"
git push origin main -f

echo "[OK] MODELOS CARREGADOS NO CAMPO DE BATALHA!"
