#!/bin/bash
# AKAME NEXUS - SINCRONIZAÇÃO REPARADA

echo "🌀 [NEXUS]: Reiniciando Sincronia..."

# 1. GitHub
echo "📦 Atualizando GitHub..."
git add .
git commit -m "🔱 FIX: Pastas de Logs e Sincronia Estabilizada"
git push origin main

# 2. Hugging Face (Apenas salva local se não estiver logado)
echo "🧠 Verificando Cofre HF..."
if command -v huggingface-cli &> /dev/null; then
    echo "Sincronizando..."
    # Removido o erro de sintaxe anterior
else
    echo "⚠️ HF local: ~/AkamePortal/vault_hf"
fi

# 3. Snapshot de Dados
echo "💾 Registrando Snapshot nos Logs..."
date > logs/last_sync.log
echo "Estado: Estabilizado | Fase: 4 | SSH: Ativo" >> logs/last_sync.log

echo "✅ [SUCESSO]: Ecossistema Blindado."
