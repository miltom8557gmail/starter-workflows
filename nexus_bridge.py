from flask import Flask, render_template_string, request, jsonify
import subprocess, os, requests

app = Flask(__name__)

# UI INFINITE: Design ultra-moderno e viciante
UI_HTML = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <style>
        :root { --main: #ff003c; --sub: #00f2ff; --bg: #000; }
        * { box-sizing: border-box; -webkit-tap-highlight-color: transparent; }
        body { background: var(--bg); color: #fff; font-family: 'Segoe UI', sans-serif; margin: 0; padding: 0; overflow-x: hidden; }
        
        /* Background Glitch Effect */
        body::before {
            content: ""; position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.25) 50%), 
                        linear-gradient(90deg, rgba(255, 0, 0, 0.06), rgba(0, 255, 0, 0.02), rgba(0, 0, 255, 0.06));
            background-size: 100% 2px, 3px 100%; z-index: 10; pointer-events: none;
        }

        .header { padding: 30px 20px; text-align: center; background: linear-gradient(to bottom, #111, transparent); }
        .header h1 { margin: 0; font-size: 28px; letter-spacing: 8px; color: var(--main); text-shadow: 0 0 15px var(--main); animation: pulse 2s infinite; }
        
        @keyframes pulse { 0% { opacity: 0.8; } 50% { opacity: 1; text-shadow: 0 0 25px var(--main); } 100% { opacity: 0.8; } }

        .nav-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px; padding: 20px; }
        .card-btn { 
            background: #080808; border: 1px solid #1a1a1a; padding: 20px; border-radius: 12px;
            text-align: center; transition: 0.3s; position: relative; overflow: hidden;
        }
        .card-btn:active { transform: scale(0.9); border-color: var(--sub); box-shadow: 0 0 20px rgba(0, 242, 255, 0.3); }
        .card-btn span { display: block; font-size: 10px; color: var(--sub); margin-top: 8px; letter-spacing: 1px; }

        /* Feed Infinito Estilo TikTok/Insta */
        .feed { padding: 10px; }
        .media-item { width: 100%; border-radius: 15px; margin-bottom: 15px; border: 1px solid #222; background: #050505; min-height: 200px; }
        .media-item img { width: 100%; border-radius: 14px; display: block; }
        
        .console { 
            background: #000; color: #0f0; font-family: monospace; font-size: 11px; 
            padding: 15px; margin: 20px; border-radius: 10px; border: 1px solid #111;
            height: 100px; overflow-y: auto; box-shadow: inset 0 0 10px #000;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>AKAME</h1>
        <div style="font-size: 9px; color: #444;">NEXUS INFINITE OS v51</div>
    </div>

    <div class="nav-grid">
        <div class="card-btn" onclick="act('omega_nsfw')">🔥 <b>OMEGA</b><span>NSFW CORE</span></div>
        <div class="card-btn" onclick="act('scan_civitai')">📡 <b>SCAN</b><span>CIVITAI API</span></div>
        <div class="card-btn" onclick="act('tunnel_on')">☁️ <b>TUNNEL</b><span>GLOBAL LINK</span></div>
        <div class="card-btn" onclick="act('bunker')">🧅 <b>BUNKER</b><span>TOR MASK</span></div>
    </div>

    <div class="console" id="log">> Nucleo Akame pronto...</div>

    <div class="feed" id="main-feed">
        </div>

    <script>
        function act(cmd) {
            const l = document.getElementById('log');
            l.innerHTML += "<br>> Executing " + cmd + "...";
            fetch('/execute?action=' + cmd)
                .then(r => r.json())
                .then(d => { l.innerHTML += "<br>[DONE] " + d.status; l.scrollTop = l.scrollHeight; });
        }

        // Busca imagens reais do Civitai (Trending NSFW)
        async function loadFeed() {
            const f = document.getElementById('main-feed');
            try {
                const res = await fetch('https://civitai.com/api/v1/images?limit=10&nsfw=true&sort=Most+Reactions');
                const data = await res.json();
                f.innerHTML = data.items.map(item => `
                    <div class="media-item">
                        <img src="${item.url.replace('width=450', 'width=1080')}" loading="lazy">
                    </div>
                `).join('');
            } catch(e) { f.innerHTML = "<p>Erro ao conectar com o Arsenal.</p>"; }
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
    # Trigger para seus scripts do Termux
    subprocess.Popen(["bash", "./scripts/omni_awakening.sh"])
    return jsonify({"status": "Protocolo " + action + " sincronizado."})

if __name__ == '__main__':
    os.system("fuser -k 8080/tcp 2>/dev/null")
    app.run(port=8080, host='0.0.0.0', threaded=True)
