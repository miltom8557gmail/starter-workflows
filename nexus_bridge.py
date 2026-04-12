from flask import Flask, render_template, jsonify
import subprocess, os

app = Flask(__name__)

# Banco de dados de comandos (A SOMA)
COMMANDS = {
    'akame_brain': 'python3 scripts/akame_brain.py',
    'akame_status': './akame_status.sh',
    'akame_swarm': 'python3 akame_swarm.py',
    'bunker_on': './scripts/bunker_control.sh on',
    'voice_start': 'python3 scripts/akame_listener.py',
    'omega_auto': 'python3 scripts/omega_forge.py'
}

@app.route('/')
def index(): return render_template('index.html')

@app.route('/comando/<tipo>')
def exec_cmd(tipo):
    cmd = COMMANDS.get(tipo)
    if cmd:
        subprocess.Popen(cmd.split())
        return jsonify({"status": "Ativado", "alvo": tipo})
    return jsonify({"status": "Erro"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
