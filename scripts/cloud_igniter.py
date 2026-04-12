import os

def disparar_forja_nuvem(workflow_name):
    print(f"🚀 Disparando {workflow_name} no Supercomputador GitHub...")
    # Comando para acionar o GitHub Actions via CLI (usando o token que já está no seu ambiente)
    os.system(f"gh workflow run {workflow_name}")
    print("✅ Comando enviado. Acompanhe a forja pelo APK.")

if __name__ == "__main__":
    disparar_forja_nuvem("akame_forge.yml")
