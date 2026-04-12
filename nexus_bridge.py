from flask import Flask, request, jsonify
import subprocess
import os
import threading

app = Flask(__name__)

# --- FUNÇÕES DE ATAQUE E SINTONIA ---
@app.route('/execute')
def run_command():
    action = request.args.get('action')
    
    if action == "unfiltered_core":
        subprocess.Popen(["bash", "./scripts/omni_response.sh", "--mode", "nsfw"])
        return jsonify({"status": "🔥 NÚCLEO OMEGA LIBERADO", "target": "Akame ga Kill"})

    elif action == "system_health":
        cost = subprocess.run(["bash", "./scripts/cost_sentinel.sh"], capture_output=True, text=True).stdout
        return jsonify({"status": "📊 SAÚDE OMNI", "data": cost.strip()})

    elif action == "tor_status":
        tor_check = os.popen("pgrep tor").read()
        return jsonify({"status": "🧅 BUNKER ONION", "active": bool(tor_check)})

    return jsonify({"status": "✅ COMANDO PROCESSADO", "action": action})

if __name__ == '__main__':
    # Autocura de portas
    os.system("fuser -k 8080/tcp 2>/dev/null")
    print("🔱 AKAME: Cérebro Central Operacional. Ouvindo APK e Termux.")
    app.run(port=8080, host='0.0.0.0', threaded=True)
