import os, socket, json, time, threading
from flask import Flask, request

app = Flask(__name__)
log_msg = "[🛰️] AKAME CORE: SISTEMA BLINDADO"

def vigilante_git():
    while True:
        # Puxa os artefatos da nuvem a cada 5 min
        os.system("git pull origin main --rebase > /dev/null 2>&1")
        time.sleep(300)

threading.Thread(target=vigilante_git, daemon=True).start()

@app.route('/ia/treinar_lora')
def treinar():
    global log_msg
    nome = request.args.get('nome', 'akame_model')
    log_msg = f"[🔥] FORJA INICIADA: {nome}"
    with open("trigger.json", "w") as f:
        json.dump({"lora_name": nome, "timestamp": time.time()}, f)
    # Envio imediato para a nuvem
    os.system("git add . && git commit -m '[⚒️] TRIGGER' && git push origin main &")
    return "OK"

@app.route('/ia/verificar_artefatos')
def verificar_artefatos():
    for file in os.listdir('.'):
        if file.endswith(".safetensors"):
            return file
    return "NONE"

@app.route('/ia/download_final')
def download_final():
    global log_msg
    file = request.args.get('file')
    if file:
        log_msg = f"[✅] COLETANDO: {file}"
        # Garante que o arquivo vá para a pasta de downloads do Android
        os.system(f"mv {file} /sdcard/Download/ 2>/dev/null")
        return "OK"
    return "NONE", 404

@app.route('/check')
def check(): return "OK", 200

@app.route('/logs')
def logs(): return log_msg

if __name__ == '__main__':
    for p in range(8081, 8090):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(('127.0.0.1', p)) != 0:
                print(f"SISTEMA ONLINE NA PORTA {p}")
                app.run(host='0.0.0.0', port=p, threaded=True)
                break
