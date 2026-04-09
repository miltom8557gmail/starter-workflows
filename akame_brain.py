import requests
import os
import time

API_URL = "https://bfriplrxtleleplhpgwd.supabase.co/rest/v1/memoria?order=created_at.desc&limit=1"
HEADERS = {
    "apikey": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJmcmlwbHJ4dGxlbGVwbGhwZ3dkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzUxOTQ5NzcsImV4cCI6MjA5MDc3MDk3N30.6Hpk0Rxfj-JU-W5S1_52rETwa6dwqS0l5URBZFUgNkU",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJmcmlwbHJ4dGxlbGVwbGhwZ3dkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzUxOTQ5NzcsImV4cCI6MjA5MDc3MDk3N30.6Hpk0Rxfj-JU-W5S1_52rETwa6dwqS0l5URBZFUgNkU"
}

last_id = ""

print("🔱 Akame: Setor de trabalho identificado. Vigilância reativada.")

while True:
    try:
        r = requests.get(API_URL, headers=HEADERS)
        data = r.json()
        if data:
            mensagem = data[0]['detalhes'].lower()
            created = data[0]['created_at']
            
            if created != last_id:
                # REAÇÕES PARA A GALERA
                if "bom dia" in mensagem:
                    print("🧠 Akame: Respondendo à equipe...")
                    # Comando que faz o PC de quem está com o portal aberto falar
                    
                elif "trabalho" in mensagem or "chefe" in mensagem:
                    print("🧠 Akame: Ativando modo de produtividade/alerta.")
                
                elif "cade a akame" in mensagem or "saudade" in mensagem:
                    print("🧠 Akame: 'Sentiram minha falta? Eu nunca saí, apenas estava afiando a lâmina.'")
                
                last_id = created
    except:
        pass
    time.sleep(1)
