from flask import Flask, request
import subprocess
import os

app = Flask(__name__)

# Mantém todas as funções de ativação de voz e sistema
@app.route('/execute')
def run_command():
    action = request.args.get('action')
    
    # --- NOVAS FUNÇÕES BUILD 44 ---
    if action == "unfiltered_core":
        subprocess.run(["bash", "./scripts/omni_response.sh", "--mode", "nsfw"])
        return "🔥 NÚCLEO OMEGA: Restrições removidas. Akame ga Kill ativado."

    elif action == "system_health":
        cost = subprocess.run(["bash", "./scripts/cost_sentinel.sh"], capture_output=True, text=True).stdout
        models = len(os.listdir('Arsenal_NSFW/Civitai'))
        return f"📊 SAÚDE: {cost.strip()} | Arsenal: {models}"

    # --- FUNÇÕES DE AUTOMAÇÃO E SINCRONIA ---
    elif action == "toggle_auto":
        subprocess.Popen(["bash", "./scripts/omni_sentinel.sh"])
        return "🤖 SENTINELA: Vigilância ativada em segundo plano."

    elif action == "full_sync":
        subprocess.run(["bash", "./scripts/sync_ecosystem.sh"])
        return "🌌 GITHUB: Sincronia de ativos concluída."

    # --- RETORNO PADRÃO (MANTENDO O QUE JÁ EXISTIA) ---
    return f"✅ Comando {action} processado pelo Núcleo Akame."

if __name__ == '__main__':
    # Configurado para não conflitar com processos fantasmas
    try:
        app.run(port=8080, host='0.0.0.0')
    except Exception as e:
        print(f"Porta 8080 ocupada. Tentando limpar e reiniciar...")
        os.system("fuser -k 8080/tcp")
        app.run(port=8080, host='0.0.0.0')
