#!/bin/bash
echo "🐍 [AKAME]: Refinando a visão da malha..."
# Varredura com detecção de sistema operacional e nomes
nmap -sn 192.168.1.0/24 --open > network_map.log
echo "📡 [MAPA]: Nomes e IPs devidamente registrados no Bunker."
termux-tts-speak "Mestre, agora eu sei exatamente quem são eles. A malha está completa."
