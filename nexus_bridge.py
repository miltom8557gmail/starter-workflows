from flask import Flask, render_template_string, request, jsonify
import subprocess, os

app = Flask(__name__)

# UI Otimizada para Celular e Smartwatch (Streaming do Arsenal)
UI_HTML = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { background: #000; color: #ff0000; font-family: 'Courier New', monospace; margin: 0; padding: 10px; text-align: center; }
        .card { border: 1px solid #333; padding: 10px; margin-bottom: 10px; border-radius: 5px; background: #050505; }
        .btn { background: #111; color: #ff0000; border: 1px solid #ff0000; padding: 12px; width: 100%; margin: 5px 0; border-radius: 5px; font-weight: bold; cursor: pointer; }
        .log-box { background: #0a0a0a; color: #00ff00; height: 120px; overflow-y: auto; text-align: left; padding: 5px; font-size: 11px; border: 1px solid #222; }
        img { max-width: 100%; border: 1px solid #444; margin-top: 10px; }
        h1 { font-size: 16px; letter-spacing: 2px; }
    </style>
</head>
<body>
    <div class="card">
        <h1>🔱 AKAME NEXUS v48</h1>
        <div id="status">● SISTEMA ONLINE</div>
    </div>
    
    <div class="card">
        <button class="btn" onclick="run('unfiltered_core')">🔥 ACTIVAR OMEGA (NSFW)</button>
        <button class="btn" onclick="run('full_sync')">🌌 SINCRONIA TOTAL</button>
        <button class="btn" onclick="run('shadow_tunnel')">☁️ ABRIR TÚNEL MUNDIAL</button>
        <button class="btn" onclick="run('tor_check')">🧅 STATUS BUNKER</button>
    </div>

    <div class="card">
        <div class="log-box" id="terminal">Aguardando comando do Mestre...</div>
    </div>

    <div id="arsenal_view"></div>

    <script>
        function run(act) {
            let log = document.getElementById('terminal');
            log.innerHTML += "<br>> " + act + "...";
            fetch('/execute?action=' + act)
                .then(r => r.json())
                .then(d => { log.innerHTML += "<br>[OK] " + d.status; });
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home(): return render_template_string(UI_HTML)

@app.route('/execute')
def execute():
    action = request.args.get('action')
    cmds = {
        "unfiltered_core": "bash ./scripts/omni_response.sh",
        "full_sync": "bash ./scripts/sync_ecosystem.sh",
        "shadow_tunnel": "bash ./scripts/shadow_tunnel.sh",
        "tor_check": "pgrep tor"
    }
    if action in cmds:
        subprocess.Popen(cmds[action].split())
        return jsonify({"status": "Processamento iniciado no Termux"})
    return jsonify({"status": "Comando inválido"})

if __name__ == '__main__':
    os.system("fuser -k 8080/tcp 2>/dev/null")
    app.run(port=8080, host='0.0.0.0', threaded=True)
