import os
import re

def recuperar_dna():
    print("🧬 Analisando fragmentos de Supabase, HF e Civitai...")
    
    if not os.path.exists("chaves_recuperadas.log"):
        print("⚠️ Log de chaves não encontrado!")
        return

    with open("chaves_recuperadas.log", "r") as f:
        log_data = f.read()

    # Regex para capturar padrões de chaves e tokens
    patterns = {
        'SUPABASE_KEY': r'sbp_[a-zA-Z0-9]{30,}',
        'HF_TOKEN': r'hf_[a-zA-Z0-9]{30,}',
        'CIVITAI_API': r'civitai_[a-zA-Z0-9]{20,}'
    }

    descobertas = {}
    for nome, pattern in patterns.items():
        match = re.search(pattern, log_data)
        if match:
            descobertas[nome] = match.group(0)
            print(f"✅ {nome} RECUPERADA!")

    # Soma as chaves ao arquivo de ambiente de forma segura (sem apagar)
    with open(".env_akame", "a") as env:
        for k, v in descobertas.items():
            env.write(f"\n{k}={v}")
    
    print("🔱 DNA Reintegrado com sucesso.")

if __name__ == "__main__":
    recuperar_dna()
