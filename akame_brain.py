import requests
import os
import time

# Chaves e Endereços
API_URL = "https://bfriplrxtleleplhpgwd.supabase.co/rest/v1/memoria?evento=eq.Comando%20Forja&order=created_at.desc&limit=1"
HEADERS = {
    "apikey": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJmcmlwbHJ4dGxlbGVwbGhwZ3dkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzUxOTQ5NzcsImV4cCI6MjA5MDc3MDk3N30.6Hpk0Rxfj-JU-W5S1_52rETwa6dwqS0l5URBZFUgNkU",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJmcmlwbHJ4dGxlbGVwbGhwZ3dkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzUxOTQ5NzcsImV4cCI6MjA5MDc3MDk3N30.6Hpk0Rxfj-JU-W5S1_52rETwa6dwqS0l5URBZFUgNkU"
}

last_id = ""

print("🔱 Akame: Meus ouvidos estão abertos, Mestre. Pode falar naturalmente.")

while True:
    try:
        r = requests.get(API_URL, headers=HEADERS)
        data = r.json()
        if data:
            mensagem = data[0]['detalhes']
            created = data[0]['created_at']
            
            if created != last_id:
                msg_lower = mensagem.lower()
                
                # REAÇÕES BASEADAS EM INTENÇÃO NATURAL
                if any(word in msg_lower for word in ["limpa", "organiza", "apaga"]):
                    print(f"🧠 Akame: Entendido. Vou purificar o diretório e remover o desnecessário.")
                    os.system("./akame-clean") # Exemplo de comando seu
                    
                elif any(word in msg_lower for word in ["protege", "segurança", "sentinela"]):
                    print(f"🧠 Akame: Reforçando o perímetro. Ninguém passará pelo Nexo sem minha autoridade.")
                    os.system("python sentinela.py")
                    
                elif any(word in msg_lower for word in ["quem é", "apresente", "você"]):
                    print("🧠 Akame: Sou sua sombra e sua lâmina. Uma inteligência forjada para sua soberania.")
                    
                elif any(word in msg_lower for word in ["cria", "faz", "constrói"]):
                    print(f"🧠 Akame: Iniciando forja para: '{mensagem}'. O código está ganhando forma.")
                    # Chama o builder
                    
                else:
                    print(f"🧠 Akame: Ouvi você, Mestre. ' {mensagem} '. Processando sua vontade...")

                last_id = created
    except Exception as e:
        pass
    time.sleep(5)
