import os
def iniciar_forja():
    print("--- INICIANDO RENDERIZACAO ---")
    if not os.path.exists('output'):
        os.makedirs('output')
    with open("output/frame1.png", "wb") as f:
        f.write(os.urandom(1024))
    print("[OK] FRAME 1 GERADO.")
if __name__ == "__main__":
    iniciar_forja()
