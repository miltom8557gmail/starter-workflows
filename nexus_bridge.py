from flask import Flask, render_template_string, request, jsonify
import subprocess, os

app = Flask(__name__)

UI_HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Akame Omega</title>
    <style>
        :root { --neon: #ff003c; --bg: #050505; --accent: #00f2ff; }
        body { background: var(--bg); color: #fff; font-family: 'Segoe UI', sans-serif; margin: 0; overflow-x: hidden; }
        
        /* Cabeçalho Animado */
        .header { padding: 20px; text-align: center; border-bottom: 2px solid var(--neon); box-shadow: 0 0 15px var(--neon); }
        .header h1 { margin: 0; font-size: 22px; letter-spacing: 5px; color: var(--neon); text-shadow: 0 0 10px var(--neon); }
        
        /* Grid de Módulos */
        .container { padding: 15px; }
        .section-title { font-size: 12px; color: var(--accent); text-transform: uppercase; margin: 15px 0 5px; border-left: 3px solid var(--accent); padding-left: 10px; }
        
        .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }
        
        /* Botões Estilizados */
        .btn { 
            background: #111; border: 1px solid #333; color: #ccc; padding: 15px; border-radius: 8px; 
            font-size: 11px; font-weight: bold; transition: 0.3s; text-align: center; cursor: pointer;
            display: flex; flex-direction: column; align-items: center; justify-content: center;
        }
        .btn:active { border-color: var(--neon); color: var(--neon); transform: scale(0.95); box-shadow: 0 0 10px var(--neon); }
        .btn i { font-size: 20px; margin-bottom: 5px; }

        /* Feed de Mídia (Arsenal) */
        .media-feed { margin-top: 20px; border-radius: 10px; background: #0a0a0a; padding: 10px; }
        .media-card { margin-bottom: 15px; border-radius: 8px; overflow: hidden; border: 1px solid #222; }
        .media-card img { width: 100%; display: block; filter: brightness(0.8); transition: 0.5s; }
        .media-card img:hover { filter: brightness(1); }
        
        /* Log do Sistema */
        .console { background: #000; color: #0f0; font-family: monospace; font-size: 10px; padding: 10px; height: 80px; overflow-y: auto; border: 1px solid #111; margin-top: 10px; }
    </style>
</head>
<body>
    <div class="header">
        <h1>AKAME ΩMEGA</h1>
        <div id="clock" style="font-size: 10px; color: #555;">SISTEMA SINCRONIZADO</div>
    </div>

    <div class="container">
        <div class="section-title">🛡️ Sombra & Conexão</div>
        <div class="grid">
            <div class="btn" onclick="act('bunker_onion')">🧅 BUNKER<br>(TOR)</div>
            <div class="btn" onclick="act('shadow_tunnel')">☁️ TÚNEL<br>(GLOBAL)</div>
            <div class="btn" onclick="act('ssh_activate')">🔑 SSH<br>(REMOTO)</div>
            <div class="btn" onclick="act('status_check')">📊 STATUS<br>(GERAL)</div>
        </div>

        <div class="section-title">🔥 Forja & Arsenal (NSFW)</div>
        <div class="grid">
            <div class="btn" style="border-color: var(--neon);" onclick="act('civitai_scan')">🔞 CIVITAI<br>SCAN</div>
            <div class="btn" onclick="act('hugging_pull')">🤗 HUGGING<br>FACE</div>
            <div class="btn" onclick="act('generate_art')">🎨 GERAR<br>ARTE</div>
            <div class="btn" onclick="act('sync_media')">🔄 ATUALIZAR<br>FEED</div>
        </div>

        <div class="section-title">🖼️ Galeria do Arsenal</div>
        <div class="media-feed" id="feed">
            <div class="media-card"><img src="https://image.civitai.com/xG1nkqKTMz69hu8icL4uS/47517/width=450/00012-34985734.jpeg"></div>
            <div class="media-card"><img src="https://image.civitai.com/xG1nkqKTMz69hu8icL4uS/11234/width=450/image.jpeg"></div>
        </div>

        <div class="section-title">📡 Terminal de Saída</div>
        <div class="console" id="console">> Aguardando comando...</div>
    </div>

    <script>
        function act(command) {
            const c = document.getElementById('console');
            c.innerHTML += "<br>> Executando: " + command;
            fetch('/execute?action=' + command)
                .then(r => r.json())
                .then(d => { c.innerHTML += "<br>[OK] " + d.status; c.scrollTop = c.scrollHeight; });
        }
        
        // Relógio do Sistema
        setInterval(() => {
            const now = new Date();
            document.getElementById('clock').innerText = "VDR: " + now.getHours() + ":" + now.getMinutes() + ":" + now.getSeconds() + " | OMEGA ACTIVE";
        }, 1000);
    </script>
</body>
</html>
"""

@app.route('/')
def home(): return render_template_string(UI_HTML)

@app.route('/execute')
def execute():
    action = request.args.get('action')
    # Mapeamento para todos os seus scripts reais
    scripts = {
        "bunker_onion": "bash ./scripts/bunker_onion.sh",
        "shadow_tunnel": "bash ./scripts/shadow_tunnel.sh",
        "ssh_activate": "sshd",
        "civitai_scan": "bash ./scripts/omni_sentinel.sh",
        "status_check": "bash ./check_status.sh"
    }
    if action in scripts:
        subprocess.Popen(scripts[action].split())
        return jsonify({"status": "Protocolo "+action+" iniciado."})
    return jsonify({"status": "Ação registrada."})

if __name__ == '__main__':
    os.system("fuser -k 8080/tcp 2>/dev/null")
    app.run(port=8080, host='0.0.0.0', threaded=True)
