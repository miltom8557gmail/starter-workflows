#!/bin/bash
if [ "$1" == "on" ]; then
    echo "Iniciando Protocolo Bunker Onion..."
    tor & 
    sleep 2
    # Configura proxy para que todo o tráfego Akame saia pelo Tor
    export http_proxy="http://127.0.0.1:9050"
    echo "Bunker Ativo. Camada Onion estabelecida."
fi
