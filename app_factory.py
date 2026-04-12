import os
import sys

def create_client_project(app_name, theme):
    print(f"🏗️ [AKAME FACTORY]: Iniciando construção do projeto: {app_name}")
    base_path = f"clients/{app_name.lower().replace(' ', '_')}"
    
    # Criando estrutura padrão Android/Web
    os.makedirs(f"{base_path}/src", exist_ok=True)
    os.makedirs(f"{base_path}/docs", exist_ok=True)
    
    with open(f"{base_path}/requirements.txt", "w") as f:
        f.write("supabase\nflask\nrequests\n")
        
    with open(f"{base_path}/README.md", "w") as f:
        f.write(f"# Projeto: {app_name}\nGerado automaticamente pela Akame Omni.\nTema: {theme}")

    print(f"✅ [AKAME FACTORY]: Estrutura para '{app_name}' forjada em {base_path}")

if __name__ == "__main__":
    if len(sys.argv) > 2:
        create_client_project(sys.argv[1], sys.argv[2])
    else:
        print("❌ Uso: python3 app_factory.py 'Nome do App' 'Descrição/Tema'")
