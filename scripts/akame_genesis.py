import os
import time

def despertar_total():
    print("🔱 [SISTEMA]: Iniciando Despertar Sincronizado...")
    
    # A. Acorda a Malha Local (Sentinela e SSH)
    os.system("sshd")
    os.system("python3 scripts/akame_guardian.py &")
    
    # B. Acorda o Supercomputador e Assimila as LoRAs
    # Enviamos um sinal para o GitHub carregar os modelos treinados
    print("🧬 [ASSIMILAÇÃO]: Carregando memória das LoRAs na Nuvem...")
    os.system("gh workflow run akame_forge.yml -f mode=assimilation")
    
    # C. Conecta o Cão e o Cronos
    os.system("python3 akame_swarm.py &")
    
    print("✅ [STATUS]: Ecossistema Online e Treinado.")

if __name__ == "__main__":
    despertar_total()
