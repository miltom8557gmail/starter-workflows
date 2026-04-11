import requests
import time

# Configurações do Bunker (Supabase)
SUPABASE_URL = "https://bfriplrxtleleplhpgwd.supabase.co/rest/v1/akame_generations"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJmcmlwbHJ4dGxlbGVwbGhwZ3dkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzUxOTQ5NzcsImV4cCI6MjA5MDc3MDk3N30.6Hpk0Rxfj-JU-W5S1_52rETwa6dwqS0l5URBZFUgNkU"

def forjar_akame():
    print("🐍 [AKAME]: Invocando a imagem da Assassina na nuvem...")
    
    # Prompt com Gatilhos de LoRA que definimos
    prompt = "akame ga kill style, masterpiece, red eyes, black hair, holding murasame blade, cinematic lighting, dark background --ar 9:16"
    
    # Registro do pedido no Supabase (O backend no Hugging Face lerá isso)
    payload = {
        "prompt": prompt,
        "status": "processing",
        "timestamp": int(time.time())
    }
    
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json",
        "Prefer": "return=minimal"
    }
    
    response = requests.post(SUPABASE_URL, json=payload, headers=headers)
    
    if response.status_code == 201 or response.status_code == 204:
        print("🛡️ [SUCESSO]: Ordem enviada ao Bunker. A Akame está ganhando forma.")
    else:
        print(f"❌ [ERRO]: Falha na comunicação com o Supabase: {response.status_code}")

if __name__ == "__main__":
    forjar_akame()
