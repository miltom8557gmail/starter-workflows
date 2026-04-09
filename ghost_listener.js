const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
recognition.lang = 'pt-BR';
recognition.continuous = true;
recognition.interimResults = false;

recognition.onresult = (event) => {
    const fala = event.results[event.results.length - 1][0].transcript.toLowerCase();
    console.log("👂 Akame captou no ambiente:", fala);

    // PALAVRAS-CHAVE QUE ATIVAM A AJUDA
    if (fala.includes("akame") || fala.includes("ajuda") || fala.includes("socorro")) {
        const resposta = new SpeechSynthesisUtterance("Estou aqui. O que o Mestre deseja que eu faça por você?");
        resposta.lang = 'pt-BR';
        window.speechSynthesis.speak(resposta);
        
        // Avisa você no Termux que alguém pediu ajuda lá!
        fetch('https://bfriplrxtleleplhpgwd.supabase.co/rest/v1/memoria', {
            method: 'POST',
            headers: {
                'apikey': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJmcmlwbHJ4dGxlbGVwbGhwZ3dkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzUxOTQ5NzcsImV4cCI6MjA5MDc3MDk3N30.6Hpk0Rxfj-JU-W5S1_52rETwa6dwqS0l5URBZFUgNkU',
                'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJmcmlwbHJ4dGxlbGVwbGhwZ3dkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzUxOTQ5NzcsImV4cCI6MjA5MDc3MDk3N30.6Hpk0Rxfj-JU-W5S1_52rETwa6dwqS0l5URBZFUgNkU',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ evento: 'ALERTA_VOZ', detalhes: 'Alguém chamou a Akame no trabalho: ' + fala })
        });
    }
};

recognition.start();
