from flask import Flask, render_template_string, request, jsonify
import subprocess, os, requests

app = Flask(__name__)

# UI UNIFICADA (Estética Cyberpunk + Feed de Mídia Real)
UI_HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <style>
        :root { --neon: #ff003c; --sub: #00f2ff; --bg: #000; }
        body { background: var(--bg); color: #fff; font-family: 'Segoe UI', sans-serif; margin: 0; padding: 0; }
        .header { padding: 25px; text-align: center; border-bottom: 1px solid var(--neon); box-shadow: 0 0 15px var(--neon); }
        .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; padding: 15px; }
        .btn { 
            background: #080808; border: 1px solid #222; color: #fff; padding: 18px; border-radius: 10px; 
            font-size: 11px; text-align: center; transition: 0.2s;
        }
        .btn:active { border-color: var(--sub); box-shadow: 0 0 15px var(--sub); transform: scale(0.95); }
        .feed { padding: 10px; }
        .media-card { width: 100%; border-radius: 12px; margin-bottom: 15px; border: 1px solid #1a1a1a; overflow: hidden; }
        .media-card img { width: 100%; display: block; }
        .console { background: #000; color: #0f0; font-family: monospace; font-size: 10px; padding: 10px; height: 70px; overflow: auto; border: 1px solid #111; margin: 10px; }
    </style>
</head>
<body>
    <div class="header"><h1 style="margin:0; letter-spacing:5px; color:var(--neon)">AKAME OMNI</h1></div>
    
    <div class="grid">
        <div class="btn" onclick="act('omega')">🔥 OMEGA<br>CORE</div>
        <div class="btn" onclick="act('bunker')">🧅 BUNKER<br>TOR</div>
        <div class="btn" onclick="act('tunnel')">☁️ TUNNEL<br>GLOBAL</div>
        <div class="btn" onclick="act('sync')">🔄 SYNC<br>ARSENAL</div>
    </div>

    <div class="console" id="log">> Sistema Unificado v52 Ativo...</div>

    <div class="feed" id="feed">
        <p style="text-align:center; color:#444;">Sincronizando Mídia do Arsenal...</p>
    </div>

    <script>
        function act(c) {
            const l = document.getElementById('log');
            l.innerHTML += "<br>> Exec: " + c;
            fetch('/execute?action=' + c).then(r => r.json()).then(d => { l.innerHTML += "<br>[OK] " + d.status; });
        }
        async function loadFeed() {
            try {
                const r = await fetch('https://civitai.com/api/v1/images?limit=8&nsfw=true');
                const d = await r.json();
                document.getElementById('feed').innerHTML = d.items.map(i => `
                    <div class="media-card"><img src="${i.url.replace('width=450', 'width=1080')}" loading="lazy"></div>
                `).join('');
            } catch(e) {}
        }
        loadFeed();
    </script>
</body>
</html>
"""

@app.route('/')
def index(): return render_template_string(UI_HTML)

@app.route('/execute')
def execute():
    action = request.args.get('action')
    # Dispara os scripts de backend sem travar a UI
    subprocess.Popen(["bash", "./scripts/omni_awakening.sh"])
    return jsonify({"status": "Protocolo "+action+" em execução."})

if __name__ == '__main__':
    os.system("fuser -k 8080/tcp 2>/dev/null")
    app.run(port=8080, host='0.0.0.0', threaded=True)
