from flask import Flask, render_template, jsonify
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/comando/<tipo>')
def executar_comando(tipo):
    scripts = {
        'akame_brain': 'python3 akame_brain.py',
        'akame_status': './akame_status.sh',
        'akame_civitai': './akame_civitai.sh',
        'lora_injector': 'python3 akame_lora_injector.py',
        'akame_terror': 'python3 akame_terror.py',
        'smoke_screen': './smoke_screen.sh'
    }
    
    cmd = scripts.get(tipo)
    if cmd:
        # Executa em background para não travar o APK
        subprocess.Popen(cmd.split())
        return jsonify({"status": f"Executando {tipo}..."})
    return jsonify({"status": "Comando não encontrado"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
