echo -e "\033[1;35m--- STATUS DA SOBERANIA AKAME ---\033[0m"
# Checa o Servidor
if pgrep -f nexus_bridge.py > /dev/null; then
    echo -e "📡 Ponte Nexus: \033[1;32mONLINE\033[0m"
else
    echo -e "📡 Ponte Nexus: \033[1;31mOFFLINE\033[0m"
fi
# Checa a Fábrica
if [ -f "app_factory.py" ]; then
    echo -e "🏗️ Fábrica de Apps: \033[1;32mPRONTA\033[0m"
fi
# Checa a Run no GitHub (Simulado)
echo -e "🕒 Forja GitHub: \033[1;33mRUN #19 EM ANDAMENTO...\033[0m"
