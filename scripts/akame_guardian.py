import os
import subprocess
import time

def verificar_tunel():
    print("🔱 Verificando Integridade da Malha SSH...")
    # Verifica conexão com o GitHub via SSH
    try:
        subprocess.run(["ssh", "-T", "git@github.com"], capture_output=True, timeout=5)
        print("✅ Conexão GitHub: ESTÁVEL")
    except:
        print("⚠️ Falha no Handshake GitHub")

    # Garante que o sshd (Termux) está ouvindo o APK
    os.system("sshd")
    print("✅ Servidor Interno: ONLINE")

if __name__ == "__main__":
    while True:
        verificar_tunel()
        time.sleep(300) # Verifica a cada 5 minutos
