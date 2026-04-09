// Módulo de Voz da Akame
const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
recognition.lang = 'pt-BR';
recognition.continuous = true;

recognition.onresult = (event) => {
    const speechToText = event.results[event.results.length - 1][0].transcript;
    console.log("🎤 Akame ouviu:", speechToText);
    document.getElementById('comando').value = speechToText;
    enviarComando(); // Função que já existe no seu nexus.html
};

function alternarEscuta() {
    try {
        recognition.start();
        alert("🔱 Akame: Ouvindo seus comandos, Mestre...");
    } catch (e) {
        recognition.stop();
        alert("🔱 Akame: Escuta desativada.");
    }
}
