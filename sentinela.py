from flask import Flask
import os
import subprocess

app = Flask(__name__)

@app.route('/forjar', methods=['POST'])
def forjar():
    print("\n[!] ORDEM RECEBIDA: INICIANDO CONSTRUÇÃO S-RANK!")
    
    # 1. Gatilho no GitHub
    os.system("git add . && git commit -m 'Comando: Gerar Influencer' && git push origin main -f")
    
    # 2. O OLHO DE HÓRUS: Monitorando Logs ao Vivo
    print("[...] CONECTANDO AO SERVIDOR DE RENDERIZAÇÃO...")
    # Pega o ID da última execução
    run_id = subprocess.getoutput("gh run list --limit 1 --json databaseId --jq '.[0].databaseId'")
    
    print(f"[📡] LOGS EM TEMPO REAL (ID: {run_id}):")
    # Este comando faz o Termux mostrar o que acontece no GitHub AGORA
    os.system(f"gh run watch {run_id} && gh run view {run_id} --log")
    
    # 3. Resgate Final
    print("\n[OK] RENDERIZAÇÃO CONCLUÍDA! BAIXANDO VÍDEO...")
    os.system("gh run download --name video_final")
    
    # Alerta de Hardware
    os.system("termux-vibrate -d 1500")
    os.system("termux-tts-speak 'Mestre, a influencer foi forjada e o vídeo está pronto.'")
    
    # 4. Projeção
    os.system("termux-open *.mp4")
    
    return "Sucesso", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
