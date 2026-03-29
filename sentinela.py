from flask import Flask
import os
import time

app = Flask(__name__)

@app.route('/forjar', methods=['POST'])
def forjar():
    print("\n[!] ORDEM RECEBIDA! INICIANDO CICLO DE FORJA...")
    
    # Sobe os frames
    os.system("git add . && git commit -m 'Forja Disparada' && git push origin main -f")
    
    print("[...] RADAR ATIVO: Aguardando GitHub Actions...")
    # Espera o processo terminar (gh run watch já configurado com o repo default)
    os.system("gh run watch") 
    
    print("[...] BAIXANDO VÍDEO...")
    # Baixa o vídeo (Certifique-se que o nome no GitHub é 'video_final')
    os.system("gh run download --name video_final")
    
    # ALERTA DE VITÓRIA (Voz e Vibração)
    # Nota: Certifique-se de ter o app 'Termux:API' instalado na Play Store/F-Droid
    os.system("termux-vibrate -d 1000")
    os.system("termux-tts-speak 'Mestre, o vídeo da Súcubus está pronto na sua tela.'")
    
    print("[OK] ABRINDO VÍDEO...")
    # Procura qualquer arquivo mp4 na pasta e abre
    os.system("termux-open *.mp4")
    
    return "Missão Cumprida", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
