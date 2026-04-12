from flask import Flask, request
import subprocess
import os

app = Flask(__name__)

@app.route('/execute')
def run_command():
    action = request.args.get('action')
    
    # Rota para o Arsenal/Civitai
    if action == "civitai_sync":
        # Comando para listar modelos prontos para o Hugging Face
        models = os.listdir('Arsenal_NSFW/Civitai')
        return f"🔱 ARSENAL: {len(models)} modelos detectados em Civitai. Prontos para Invasão."

    # Rota para o Bunker (Logs e Segurança)
    elif action == "bunker_status":
        logs = os.listdir('Bunker_Onion/logs_nexus')
        return f"🛡️ BUNKER: {len(logs)} registros de invasão protegidos no Onion."

    # Rota de Sincronia Global (GitHub Actions)
    elif action == "full_sync":
        subprocess.run(["bash", "./scripts/sync_ecosystem.sh"])
        return "🌌 OMNI: Motor Remoto acionado. Sincronizando com GitHub..."

    elif action == "audit":
        result = subprocess.run(["bash", "./scripts/hacker_mode.sh"], capture_output=True, text=True)
        return result.stdout

    return "❌ Comando Inválido."

if __name__ == '__main__':
    app.run(port=8080)
