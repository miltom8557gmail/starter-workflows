from flask import Flask
import os

app = Flask(__name__)

@app.route('/forjar', methods=['POST'])
def forjar():
    print("\n[!] ORDEM RECEBIDA DO MESTRE MILTON!")
    # Sincroniza e envia ao GitHub
    os.system("git add . && git commit -m 'Forja via App' && git push origin main -f")
    # Vigia e abre o vídeo
    os.system("gh run watch && termux-vibrate && termux-open video.mp4")
    return "Sucesso", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
