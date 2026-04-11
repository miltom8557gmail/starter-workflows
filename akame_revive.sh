#!/data/data/com.termux/files/usr/bin/bash

echo "🔱 [AKAME]: Iniciando Protocolo de Ressurreição..."

# 1. Atualizar Sistema e Instalar Ferramentas Base
pkg update -y && pkg upgrade -y
pkg install git python nodejs termux-api openssh curl wget -y

# 2. Restaurar DNA (Repositório)
cd /data/data/com.termux/files/home
if [ -d "AkamePortal" ]; then
    cd AkamePortal && git pull
else
    git clone git@github.com:miltom8557gmail/starter-workflows.git AkamePortal
    cd AkamePortal
fi

# 3. Configurar Licenças Android (O "Corpo")
SDK_DIR="/data/data/com.termux/files/usr/lib/android-sdk"
mkdir -p "$SDK_DIR/licenses"
printf "8933bad161af4178b1185d1a37fbf41ea5269c55\nd56f1187405551ad0638e53f353b934b9d36e783\n24333f8a63b6825ea9c5573f435dd901d32e12e5" > "$SDK_DIR/licenses/android-sdk-license"

# 4. Reativar Permissões e Watchdog
chmod +x *.sh
termux-wake-lock

# 5. Lançar a Entidade
echo "✅ [SISTEMA]: Ressurreição Concluída. A Akame está online."
python3 akame_omni_05-04-2026_15h.py --realtime
