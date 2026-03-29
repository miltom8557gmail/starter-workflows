from flask import Flask
import os

app = Flask(__name__)

@app.route('/forjar', methods=['POST'])
def forjar():
    print("ORDEM RECEBIDA DO MESTRE MILTON!")
    # COMANDOS QUE O TERMUX VAI EXECUTAR
    os.system("git add .")
    os.system("git commit -m 'Forja disparada pelo App'")
    os.system("git push origin main -f")
    print("FRAMES ENVIADOS AO GITHUB!")
    return "Ordem executada", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
