import os, time, socket
from flask import Flask, request, send_file

app = Flask(__name__)
log_msg = "[🛰️] AGUARDANDO COMANDO..."

@app.route('/ia/nuvem')
def nuvem():
    global log_msg
    prompt = request.args.get('prompt', '')
    log_msg = f"[☁️] DISPARANDO GITHUB: {prompt}"
    with open("ordem_nuvem.txt", "w") as f: f.write(prompt)
    os.system("git add . && git commit -m 'Comando Akame' && git push origin main &")
    return "OK"

@app.route('/status_nuvem')
def status_nuvem():
    os.system("git pull origin main > /dev/null 2>&1")
    if os.path.exists("resultado_nuvem.txt"):
        with open("resultado_nuvem.txt", "r") as f: return f.read()
    return "PROCESSANDO NA NUVEM..."

@app.route('/check')
def check(): return "OK", 200

@app.route('/logs')
def logs(): return log_msg

if __name__ == '__main__':
    for p in range(8081, 8090):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(('127.0.0.1', p)) != 0:
                print(f">>> PORTA {p} OCUPADA PELO IMPÉRIO")
                app.run(host='0.0.0.0', port=p, threaded=True)
                break
