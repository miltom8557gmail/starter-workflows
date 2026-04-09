import requests
import os
import time

API_URL = "https://bfriplrxtleleplhpgwd.supabase.co/rest/v1/memoria?evento=eq.Comando%20Forja&order=created_at.desc&limit=1"
HEADERS = {
    "apikey": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJmcmlwbHJ4dGxlbGVwbGhwZ3dkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzUxOTQ5NzcsImV4cCI6MjA5MDc3MDk3N30.6Hpk0Rxfj-JU-W5S1_52rETwa6dwqS0l5URBZFUgNkU",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJmcmlwbHJ4dGxlbGVwbGhwZ3dkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzUxOTQ5NzcsImV4cCI6MjA5MDc3MDk3N30.6Hpk0Rxfj-JU-W5S1_52rETwa6dwqS0l5URBZFUgNkU"
}

last_id = ""
print("🔱 Akame Jarvis: Sistemas de intrusão e escuta em prontidão absoluta.")

while True:
    try:
        r = requests.get(API_URL, headers=HEADERS)
        data = r.json()
        if data:
            cmd_full = data[0]['detalhes']
            created = data[0]['created_at']
            
            if created != last_id:
                # Limpa a tag de dispositivo para processar a ordem
                msg = cmd_full.split(']')[-1].strip().lower()
                print(f"📡 Ordem recebida: {msg}")

                # LÓGICA DE REAÇÃO JARVIS
                if any(x in msg for x in ["status", "diagnóstico", "sistema"]):
                    os.system("python akame_diagnostico.py")
                
                elif any(x in msg for x in ["hack", "scan", "rede", "analise"]):
                    print("🔱 Akame: Iniciando Protocolo de Intrusão. Varrendo alvos...")
                    # Se você tiver um script de ataque, ele entra aqui:
                    # os.system("./seu_script_ataque.sh") 
                    os.system("echo 'Analizando brechas no perímetro...' && sleep 2 && echo 'Relatório de vulnerabilidades pronto.'")

                elif "limpa" in msg or "purificar" in msg:
                    print("🔱 Akame: Removendo rastros e purificando diretórios.")
                    os.system("rm -rf *.log temp_*")

                else:
                    print(f"🧠 Akame: Mestre, entendi sua mensagem: '{msg}'. Como deseja proceder?")

                last_id = created
    except:
        pass
    time.sleep(1) # Reação em Tempo Real
