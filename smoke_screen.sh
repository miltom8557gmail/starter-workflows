#!/bin/bash
echo -e "\e[1;31m[ALERTA]: PROTOCOLO DE FUGA ATIVADO!\e[0m"
termux-tts-speak "Mestre, fomos detectados. Iniciando cortina de fumaça. Desapareça nas sombras."

# Simulação de ataque de inundação de logs para confundir o invasor
for i in {1..50}; do
   echo "ERRO_CRÍTICO_SISTEMA_$(date +%s)_$i" >> /dev/null
done

# Escondendo a pasta AkamePortal (Torna a pasta invisível no sistema)
mv ~/AkamePortal ~/..AkamePortal_Hidden
echo "🛡️ [SISTEMA]: Arquivos movidos para o Bunker Subterrâneo."
