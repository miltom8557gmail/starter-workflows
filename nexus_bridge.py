from flask import Flask, request
import subprocess
import os

app = Flask(__name__)

@app.route('/execute')
def run_command():
    action = request.args.get('action')
    
    # Gatilho do Sistema NSFW (Cerebro_Sem_Filtros)
    if action == "unfiltered_core":
        # Ativa o modelo open source sem restrições
        subprocess.run(["bash", "./scripts/omni_response.sh", "--mode", "nsfw"])
        return "🔥 NÚCLEO OMEGA: Restrições removidas. Sistema Sem Filtros Ativo."

    # Monitor de Saúde e Custos (HUD do APK)
    elif action == "system_health":
        cost = subprocess.run(["bash", "./scripts/cost_sentinel.sh"], capture_output=True, text=True).stdout
        models = len(os.listdir('Arsenal_NSFW/Civitai'))
        return f"📊 SAÚDE: {cost.strip()} | Modelos Civitai: {models}"

    # Sincronia de Elite (GitHub -> HF)
    elif action == "full_sync":
        subprocess.run(["bash", "./scripts/sync_ecosystem.sh"])
        return "🌌 GITHUB: Sincronia de ativos iniciada via Nuvem."

    elif action == "toggle_auto":
        subprocess.Popen(["bash", "./scripts/omni_sentinel.sh"])
        return "🤖 AUTOMAÇÃO: Sentinela ativado em segundo plano."
    return "❌ Comando Desconhecido."

if __name__ == '__main__':
    app.run(port=8080)
