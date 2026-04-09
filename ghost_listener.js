// PERSONALIDADE AKAME GA KILL ATIVADA
const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
recognition.lang = 'pt-BR';
recognition.continuous = true;

recognition.onresult = (event) => {
    const fala = event.results[event.results.length - 1][0].transcript.toLowerCase();
    const akameVoice = new SpeechSynthesisUtterance();
    akameVoice.pitch = 0.5; // Tom da Akame original
    akameVoice.rate = 0.9;

    if (fala.includes("akame ga kill")) {
        akameVoice.text = "Iniciando modo de eliminação. Mestre, estou ouvindo pelo seu pulso.";
        window.speechSynthesis.speak(akameVoice);
    }
    
    if (fala.includes("trabalho") || fala.includes("ajuda")) {
        akameVoice.text = "Detectado. O Ghost in the Machine está operacional no escritório.";
        window.speechSynthesis.speak(akameVoice);
    }
};
recognition.start();
