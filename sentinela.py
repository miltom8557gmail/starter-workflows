import os, socket, requests
from flask import Flask, request

app = Flask(__name__)
log_msg = "[🛰️] AGUARDANDO ORDEM MESTRE..."
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"

@app.route('/ia/executar')
def executar():
    global log_msg
    ordem_humana = request.args.get('prompt', '')
    log_msg = f"[🧠] TRADUZINDO: {ordem_humana}"
    
    # Prompt para a IA se comportar como um tradutor de comandos Termux
    prompt_ia = f"Transforme esta ordem em UM ÚNICO comando Bash para Termux. Responda APENAS o comando, sem explicações: {ordem_humana}"
    
    try:
        payload = {"inputs": prompt_ia, "parameters": {"max_new_tokens": 100}}
        res = requests.post(API_URL, json=payload).json()
        comando_gerado = res[0]['generated_text'].split('\n')[-1].strip()
        
        log_msg = f"[🔥] EXECUTANDO: {comando_gerado}"
        # EXECUÇÃO REAL NO SISTEMA
        os.system(f"{comando_gerado} > resultado_comando.txt 2>&1")
        
        return f"Comando: {comando_gerado} executado com sucesso."
    except Exception as e:
        return f"Erro na tradução: {str(e)}"

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
