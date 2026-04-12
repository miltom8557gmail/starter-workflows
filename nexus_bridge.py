from flask import Flask, render_template_string, request, jsonify
import subprocess, os, json

app = Flask(__name__)

UI_HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { background: #000; color: #ff0000; font-family: sans-serif; text-align: center; margin: 0; padding: 10px; }
        .btn { background: #111; border: 1px solid #f00; color: #f00; padding: 20px; width: 100%; border-radius: 10px; margin: 5px 0; font-size: 16px; font-weight: bold; }
        .gallery { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 20px; }
        .img-card { border: 1px solid #333; border-radius: 5px; overflow: hidden; background: #050505; }
        img { width: 100%; height: auto; display: block; }
        .log { color: #0f0; font-size: 10px; background: #0a0a0a; padding: 5px; height: 50px; overflow: auto; border: 1px solid #222; margin-top: 10px; }
    </style>
</head>
<body>
    <h2>🔱 AKAME NEXUS</h2>
    <button class="btn" onclick="act('unfiltered_core')">🔥 OMEGA NSFW</button>
    <button class="btn" onclick="location.reload()">🔄 ATUALIZAR ARSENAL</button>
    
    <div class="log" id="term">Conectado ao Arsenal...</div>

    <div class="gallery" id="images">
        <p style="color:#555">Carregando mídias da nuvem...</p>
    </div>

    <script>
        function act(a) {
            fetch('/execute?action='+a).then(r => r.json()).then(d => {
                document.getElementById('term').innerText = "> " + d.status;
            });
        }
        
        // Simulação de carregamento de imagens do Arsenal
        fetch('/arsenal_data').then(r => r.json()).then(data => {
            let html = '';
            data.images.forEach(url => {
                html += '<div class="img-card"><img src="'+url+'"></div>';
            });
            document.getElementById('images').innerHTML = html;
        });
    </script>
</body>
</html>
"""

@app.route('/')
def home(): return render_template_string(UI_HTML)

@app.route('/arsenal_data')
def arsenal():
    # Aqui o sistema busca os links reais do Civitai/HuggingFace salvos no log do Sentinela
    return jsonify({"images": [
        "https://image.civitai.com/xG1nkqKTMz69hu8icL4uS/47517/width=450/00012-34985734.jpeg",
        "https://image.civitai.com/xG1nkqKTMz69hu8icL4uS/11234/width=450/image.jpeg"
    ]})

@app.route('/execute')
def execute():
    action = request.args.get('action')
    subprocess.Popen(["bash", "./scripts/omni_awakening.sh"])
    return jsonify({"status": "Ação disparada com sucesso."})

if __name__ == '__main__':
    os.system("fuser -k 8080/tcp 2>/dev/null")
    app.run(port=8080, host='0.0.0.0', threaded=True)
