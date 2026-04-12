from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/execute')
def run_command():
    action = request.args.get('action')
    if action == "full_sync":
        # Dispara o motor remoto LoRA
        subprocess.run(["bash", "./scripts/sync_ecosystem.sh"])
        return "🔱 Sincronia de LoRA Iniciada na Nuvem."
    elif action == "voice_test":
        # Dispara o processador de voz
        subprocess.run(["bash", "./scripts/voice_processor.sh", "Sistema Online"])
        return "🎙️ Pulso de Voz Enviado."
    elif action == "audit":
        # Executa varredura de integridade
        result = subprocess.run(["bash", "./scripts/hacker_mode.sh"], capture_output=True, text=True)
        return f"🛡️ Auditoria: {result.stdout}"
    return "Comando Inválido."

if __name__ == '__main__':
    app.run(port=8080)
