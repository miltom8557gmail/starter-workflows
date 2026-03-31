import os, socket, requests
from flask import Flask, request

app = Flask(__name__)
log_msg = "[🛰️] AGUARDANDO COMANDO..."

# Rota do Cérebro (Mistral-7B via API Direta)
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"

@app.route('/ia/chat')
def chat():
    global log_msg
    pergunta = request.args.get('prompt', '')
    log_msg = f"[🧠] PENSANDO: {pergunta}"
    try:
        # Envia a pergunta para a nuvem do Hugging Face
        payload = {"inputs": pergunta, "parameters": {"max_new_tokens": 500}}
        response = requests.post(API_URL, json=payload).json()
        
        # Extrai o texto da resposta
        if isinstance(response, list):
            res_text = response[0].get('generated_text', 'Sem resposta.')
        else:
            res_text = str(response)

        log_msg = "[✅] RESPOSTA GERADA"
        with open("resultado_ia.txt", "w") as f: f.write(res_text)
        return res_text
    except Exception as e:
        log_msg = f"[❌] ERRO NA IA: {str(e)}"
        return str(e)

@app.route('/ia/nuvem')
def nuvem():
    global log_msg
    p = request.args.get('prompt', '')
    log_msg = f"[☁️] ENVIANDO ORDEM: {p}"
    with open("ordem_nuvem.txt", "w") as f: f.write(p)
    os.system("git add . && git commit -m 'Ordem Nuvem' && git push origin main &")
    return "OK"

@app.route('/check')
def check(): return "OK", 200

@app.route('/logs')
def logs(): return log_msg

if __name__ == '__main__':
    for p in range(8081, 8090):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(('127.0.0.1', p)) != 0:
                print(f">>> SISTEMA AKAME ONLINE NA PORTA: {p}")
                app.run(host='0.0.0.0', port=p, threaded=True)
                break
