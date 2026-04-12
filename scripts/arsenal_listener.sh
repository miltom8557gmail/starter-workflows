#!/bin/bash
# OUVINTE DO ARSENAL - AKAME FASE 4

echo "🕵️ [NEXUS]: Escutando sinais do Arsenal..."

while true; do
    # Verifica se o arquivo de comando foi criado pelo serviço do app
    if [ -f "logs/cmd_trigger.tmp" ]; then
        CMD=$(cat logs/cmd_trigger.tmp)
        echo "⚔️ [GATILHO]: Comando '$CMD' detectado!"
        
        # Executa a ação baseada no comando
        if [ "$CMD" == "open_arsenal" ]; then
            termux-notification -t "Akame Nexus" -c "Arsenal Ativo: Sistema Pronto para Combate"
            # Aqui você pode colocar qualquer script de ataque/defesa
        fi
        
        rm logs/cmd_trigger.tmp
    fi
    sleep 2
done
