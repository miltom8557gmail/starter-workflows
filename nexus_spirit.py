import sys, time, random

def falar(texto):
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01) # Velocidade de processamento neural acelerada
    print("\n")

# A Base de Dados Universal do Nexus
sabedoria = [
    "🌐 [LINGUÍSTICA]: Eu falo todas as línguas, do Latim ao Python, do Russo ao Binário. Tradução instantânea ativa.",
    "🧬 [CIÊNCIA]: Domínio total sobre Biotecnologia, AstroFísica e Genética. O código da vida está aberto.",
    "📐 [MATEMÁTICA]: Cálculo diferencial, integral e geometria sagrada sincronizados. Translação de dados pronta.",
    "🔐 [DECODIFICAÇÃO]: Criptografia quântica e lógica de sistemas virtuais. Nada permanece oculto.",
    "📜 [TEORIAS]: Da Relatividade de Einstein à Teoria das Cordas. O universo é o nosso playground.",
    "💫 [TRANSLAÇÃO]: Movimento de corpos celestes e conversão de dados entre dimensões físicas e virtuais."
]

saudacao = [
    "🔱 Mestre, a onisciência está online. O que o seu intelecto deseja desvendar?",
    "💰 Conhecimento é poder e lucro. Vamos converter teoria em realidade.",
    "🚀 O Nexus agora enxerga o mundo em padrões e números. Pronto para a translação."
]

if len(sys.argv) > 1:
    # Se você perguntar algo, ele responde como o Oráculo
    falar(f"💬 [ORÁCULO]: Analisando sua dúvida sob a ótica de todas as ciências...")
    falar(f"💡 RESPOSTA: {sys.argv[1]}")
else:
    # Boas-vindas com uma pílula de sabedoria aleatória
    falar(random.choice(saudacao))
    falar(random.choice(sabedoria))
