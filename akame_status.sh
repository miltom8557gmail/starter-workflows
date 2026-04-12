#!/bin/bash
clear
echo -e "\033[1;35m╔══════════════════════════════════════════════════════════════╗\033[0m"
echo -e "║          🔱 MONITOR DE SOBERANIA - VISÃO REAL V52 🔱         ║"
echo -e "╚══════════════════════════════════════════════════════════════╝\033[0m"

# --- 🔑 VERIFICAÇÃO DE IDENTIDADE (SSH) ---
echo -e "\n\033[1;34m[🔑] CHAVES DE ACESSO SSH:\033[0m"
if [ -f ~/.ssh/id_rsa ] || [ -f ~/.ssh/id_ed25519 ]; then
    echo -e "  ✅ Chave Privada:  \033[1;32mDETECTADA\033[0m (Pronta para GitHub/HF)"
    # Testa conexão SSH com GitHub
    ssh -T git@github.com 2>&1 | grep -q "successfully authenticated" && echo -e "  ✅ Link GitHub:    \033[1;32mESTABELECIDO\033[0m" || echo -e "  ⚠️ Link GitHub:    \033[1;33mNECESSITA AUTH\033[0m"
else
    echo -e "  ❌ Chaves SSH:     \033[1;31mNÃO ENCONTRADAS NO PADRÃO\033[0m"
fi

# --- 🧠 ECOSSISTEMA HUGGINGFACE & CIVITAI ---
echo -e "\n\033[1;34m[🧠] NÚCLEO DE MODELOS (HF/CIVITAI):\033[0m"
if command -v huggingface-cli &> /dev/null; then
    echo -e "  ✅ CLI HF:         \033[1;32mINSTALADO\033[0m"
    [ -f ~/.cache/huggingface/token ] && echo -e "  ✅ Token HF:       \033[1;32mATIVO\033[0m" || echo -e "  ⚪ Token HF:       \033[1;37mNÃO LOGADO\033[0m"
else
    echo -e "  ⚪ CLI HF:         \033[1;37mAGUARDANDO INSTALAÇÃO\033[0m"
fi

# --- 🗄️ INFRAESTRUTURA SUPABASE ---
echo -e "\n\033[1;34m[🗄️] BASE DE DADOS (SUPABASE):\033[0m"
# Busca profunda por variáveis de ambiente
ENV_FILE=$(find . -name ".env" | head -n 1)
if [ ! -z "$ENV_FILE" ] && grep -q "SUPABASE" "$ENV_FILE"; then
    echo -e "  ✅ Configuração:   \033[1;32mENCONTRADA EM $ENV_FILE\033[0m"
else
    echo -e "  ⚠️ Configuração:   \033[1;33mVARIÁVEIS NÃO MAPEADAS\033[0m"
fi

# --- 📡 STATUS DO SERVIDOR LOCAL ---
echo -e "\n\033[1;34m[📡] SERVIÇOS ATIVOS:\033[0m"
pgrep -f "nexus_bridge.py" > /dev/null && echo -e "  ✅ Nexus Bridge:  \033[1;32mRODANDO EM BACKGROUND\033[0m" || echo -e "  ❌ Nexus Bridge:  \033[1;31mPARADO\033[0m"

echo -e "\n\033[1;35m══════════════════════════════════════════════════════════════\033[0m"
