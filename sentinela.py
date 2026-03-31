import os, socket, json, time, requests
from flask import Flask, request, jsonify

app = Flask(__name__)
log_msg = "[🛰️] AKAME CORE: AGUARDANDO ORDEM"

@app.route('/ia/treinar_lora')
def treinar():
    global log_msg
    nome = request.args.get('nome', 'akame_model')
    log_msg = f"[🔥] DELEGANDO LORA: {nome} PARA NUVEM"
    
    # Trigger para o GitHub Actions
    with open("trigger.json", "w") as f:
        json.dump({"lora_name": nome, "timestamp": time.time()}, f)
    
    os.system("git add . && git commit -m '[⚒️] TRIGGER LORA' && git push origin main &")
    return "ORDEM ENVIADA PARA NUVEM"

@app.route('/ia/executar')
def executar():
    global log_msg
    prompt = request.args.get('prompt', '')
    log_msg = f"[⌨️] LOCAL CMD: {prompt}"
    # Executa comando local e retorna log
    os.system(f"{prompt} > last_log.txt 2>&1 &")
    return f"EXECUTANDO LOCAL: {prompt}"

@app.route('/check')
def check(): return "OK", 200

@app.route('/logs')
def logs(): 
    global log_msg
    return log_msg

if __name__ == '__main__':
    for p in range(8081, 8090):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(('127.0.0.1', p)) != 0:
                print(f"SISTEMA ONLINE NA PORTA {p}")
                app.run(host='0.0.0.0', port=p, threaded=True)
                break
