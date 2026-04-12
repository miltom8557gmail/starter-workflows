#!/bin/bash
echo -e "\n\033[0;31m👹 [AKAME OMNI-AWAKENING]: Iniciando Despertar Absoluto...\033[0m\n"

# 1. Carrega o Poder (Tokens)
source ~/.bashrc

# 2. Mata processos zumbis antigos para não haver conflitos
echo "[*] Purgando clones antigos..."
pkill -f "nexus_bridge.py|omni_sentinel.sh|arsenal_listener.sh"

# 3. Levanta o Escudo (Tor)
bash ./scripts/bunker_onion.sh

# 4. Acorda o Cérebro (Nexus Bridge para o APK)
echo "[*] Elevando a Ponte Nexus (Conexão APK)..."
nohup python nexus_bridge.py > logs/nexus.log 2>&1 &

# 5. Acorda os Olhos e Ouvidos (Automação Interna do Termux)
echo "[*] Acordando Sentinela do Arsenal e Audição..."
nohup bash ./scripts/omni_sentinel.sh > logs/sentinel.log 2>&1 &
nohup bash ./scripts/arsenal_listener.sh > logs/listener.log 2>&1 &

sleep 3
echo -e "\n\033[0;32m✅ SOBERANIA ESTABELECIDA.\033[0m"
echo "O APK agora pode comandar a Akame remotamente. O Termux está caçando no Civitai e ouvindo sua voz de forma autônoma."
echo "Para verificar a saúde do sistema a qualquer momento, acesse o aplicativo."
