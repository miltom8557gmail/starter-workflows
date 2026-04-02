import os
import subprocess

def check_status():
    print("🛰️ [ANTIGRAVITY]: Analisando integridade do Nexus...")
    # Tenta validar o gradle antes de enviar
    result = subprocess.run(["./gradlew", "help"], capture_output=True)
    if result.returncode != 0:
        print("⚠️ [ALERTA]: Erro detectado na estrutura Android. Corrigindo...")
        return False
    return True

if __name__ == "__main__":
    check_status()
