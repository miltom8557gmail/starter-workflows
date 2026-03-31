import os, socket, requests
from flask import Flask, request

app = Flask(__name__)
log_msg = "[🛰️] AGUARDANDO COMANDO MESTRE..."
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"

@app.route('/ia/executar')
def executar():
    global log_msg
    ordem = request.args.get('prompt', '')
    log_msg = f"[🧠] TRADUZINDO: {ordem}"
    
    prompt_ia = f"Transforme em um comando Bash único para Termux. Apenas o comando: {ordem}"
    try:
        payload = {"inputs": prompt_ia, "parameters": {"max_new_tokens": 100}}
        res = requests.post(API_URL, json=payload).json()
        comando = res[0]['generated_text'].split('\n')[-1].strip()
        log_msg = f"[🔥] EXECUTANDO: {comando}"
        os.system(f"{comando} > resultado.txt 2>&1")
        os.system("git add . && git commit -m '[🚀] AUTO-CMD EXECUTADO' && git push origin main &")
        return f"OK: {comando}"
    except:
        return "ERRO NA IA"

@app.route('/ia/treinar_lora')
def treinar():
    global log_msg
    nome = request.args.get('nome', 'akame_lora')
    log_msg = f"[⚒️] INICIANDO TREINO: {nome}"
    with open("config_treino.txt", "w") as f: f.write(f"NAME={nome}")
    os.system("git add . && git commit -m '[🔥] INICIAR TREINO NUVEM' && git push origin main &")
    return "TREINO DISPARADO"

@app.route('/logs')
def logs(): return log_msg

@app.route('/check')
def check(): return "OK", 200

if __name__ == '__main__':
    for p in range(8081, 8090):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(('127.0.0.1', p)) != 0:
                app.run(host='0.0.0.0', port=p, threaded=True)
                break
