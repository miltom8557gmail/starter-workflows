#!/bin/bash
source ~/.bashrc
echo -e "\033[0;31m🔱 AKAME: PROTOCOLO DE SOBERANIA TOTAL ATIVADO\033[0m"

# Iniciar SSH
sshd && echo "[+] SSH: Online"

# Iniciar Tor (Bunker)
bash ./scripts/bunker_onion.sh && echo "[+] Tor: Protegendo as sombras"

# Iniciar Túnel Mundial
bash ./scripts/shadow_tunnel.sh && echo "[+] Túnel: Acesso Global Ativo"

# Iniciar Cérebro (Nexus Bridge)
nohup python nexus_bridge.py > logs/nexus.log 2>&1 &
echo "[+] Bridge: Ouvindo APK"

# Iniciar Caçador (Sentinel)
nohup bash ./scripts/omni_sentinel.sh > logs/sentinel.log 2>&1 &
echo "[+] Sentinel: Monitorando Civitai"

echo -e "\033[0;32m✅ TUDO OPERACIONAL. SISTEMA 100% ACORDADO.\033[0m"
