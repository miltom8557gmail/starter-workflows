import os
import subprocess
from datetime import datetime

def capturar_evidencia():
    # Garante que a pasta de capturas existe
    if not os.path.exists('capturas_akame'):
        os.makedirs('capturas_akame')
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    arquivo = f"capturas_akame/EV_AKAME_{timestamp}.jpg"
    
    print(f"🔱 [VISÃO]: Iniciando escaneamento ocular...")
    
    # Comando Termux para capturar foto pela câmera traseira (id 0)
    try:
        subprocess.run(["termux-camera-photo", "-c", "0", arquivo], check=True)
        print(f"✅ [SUCESSO]: Evidência capturada: {arquivo}")
    except Exception as e:
        print(f"❌ [ERRO]: Falha sensorial: {e}")

if __name__ == "__main__":
    capturar_evidencia()
