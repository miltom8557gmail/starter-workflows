import os
import speech_recognition as sr

def escutar_chamado():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🔱 Akame em modo de vigia... Aguardando o Mestre.")
        while True:
            audio = r.listen(source)
            try:
                comando = r.recognize_google(audio, language='pt-BR').lower()
                if "akame acordar" in comando or "hey akame" in comando:
                    os.system("termux-open-url http://127.0.0.1:8080") # Abre o APK
                    os.system("python3 akame_brain.py --speak 'Sim, Mestre. Estou online.'")
                elif "mudar cor" in comando:
                    # Lógica para alterar o CSS do index.html via script
                    os.system("./scripts/change_ui.sh green")
            except:
                continue

if __name__ == "__main__":
    escutar_chamado()
