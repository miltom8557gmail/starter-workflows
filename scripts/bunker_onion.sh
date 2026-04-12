#!/bin/bash
echo "🧅 [BUNKER ONION]: Iniciando malha de anonimato Tor..."
pgrep tor || tor --RunAsDaemon 1
sleep 5
# Revela o endereço .onion da Akame (Acesso indetectável)
cat /data/data/com.termux/files/home/AkamePortal/Bunker_Onion/hostname 2>/dev/null || echo "Aguardando geração do endereço da Deep Web..."
