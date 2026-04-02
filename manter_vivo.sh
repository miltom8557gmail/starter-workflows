#!/bin/bash
echo "🔄 [SENTINELA]: Renovando tokens e pulso de conexão..."
git fetch origin
gh auth setup-git
git commit --allow-empty -m "📡 Pulso de Manutenção: $(date)"
git push origin main
echo "✅ [STATUS]: Conexões renovadas por mais 30 dias."
