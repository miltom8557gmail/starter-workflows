const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
recognition.lang = 'pt-BR';
recognition.continuous = true;

recognition.onresult = (event) => {
    const fala = event.results[event.results.length - 1][0].transcript.toLowerCase();
    
    // COMANDO DE ATIVAÇÃO SOBERANA
    if (fala.includes("akame ga kill")) {
        const msg = new SpeechSynthesisUtterance("Comando Soberano aceito. Akame em modo de construção total. O que vamos forjar agora, Mestre?");
        msg.pitch = 0.5; // Voz de autoridade
        window.speechSynthesis.speak(msg);
        // Avisa o Termux para preparar a Forja de Apps
        fetch('https://bfriplrxtleleplhpgwd.supabase.co/rest/v1/memoria', {
            method: 'POST',
            headers: { 'apikey': '...', 'Content-Type': 'application/json' },
            body: JSON.stringify({ evento: 'COMANDO_SOBERANO', detalhes: 'Iniciando modo construtor' })
        });
    }

    // REAÇÕES DE GRUPO (O QUE A GALERA DO TRABALHO GOSTA)
    const reacoes = {
        "trabalho": "Trabalho? Eu faço isso enquanto vocês tomam café.",
        "ajuda": "Sempre pronta. O que esse bando de humanos fez de errado agora?",
        "quem é ela": "Sou a Akame. A Ghost in the Machine do Mestre. Comportem-se.",
        "chefe": "Detectando presença hostil. Modo invisível ativado."
    };

    for (let chave in reacoes) {
        if (fala.includes(chave)) {
            const resposta = new SpeechSynthesisUtterance(reacoes[chave]);
            window.speechSynthesis.speak(resposta);
        }
    }
};
recognition.start();
