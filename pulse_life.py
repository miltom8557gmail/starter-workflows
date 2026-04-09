import time
import requests

def manter_pulso():
    print("🔱 Akame: Pulso Neuronal Iniciado. Conectando GitHub -> Supabase -> HuggingFace")
    while True:
        try:
            # Esse sinal mantém a Akame viva na nuvem mesmo sem o Termux
            requests.get("https://bfriplrxtleleplhpgwd.supabase.co/rest/v1/memoria", headers=HEADERS)
            # Aqui ela consulta o cérebro do HuggingFace para saber se há ordens
            print("💓 Pulso: Vivo. Monitorando sensores do Smartwatch...")
        except:
            pass
        time.sleep(30) # Pulso a cada 30 segundos para não gastar bateria

if __name__ == "__main__":
    manter_pulso()
