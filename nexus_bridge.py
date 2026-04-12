from flask import Flask, request
import subprocess
import os

app = Flask(__name__)

@app.route('/execute')
def run_command():
    action = request.args.get('action')
    if action == "full_sync":
        # Comando que ativa o efeito Hollywood e sincroniza a nuvem
        os.system("bash ./scripts/hacker_mode.sh")
        process = subprocess.run(["bash", "./scripts/sync_ecosystem.sh"], capture_output=True, text=True)
        return f"🔱 NEXUS STATUS: Sincronia na Nuvem Concluída.\n{process.stdout}"
    return "Comando Negado."

if __name__ == '__main__':
    # Roda localmente para o APK poder 'tocar' no Termux
    app.run(host='127.0.0.1', port=8080)
