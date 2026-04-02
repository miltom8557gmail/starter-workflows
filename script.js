const firebaseConfig = {
    apiKey: "AIzaSyAs-V0-vQnI9-p-Seu_Link_Real",
    authDomain: "gen-lang-client-0399949449.firebaseapp.com",
    projectId: "gen-lang-client-0399949449",
    storageBucket: "gen-lang-client-0399949449.appspot.com",
    messagingSenderId: "157939074644",
    appId: "1:157939074644:web:757041793668e1a1489e24"
};

firebase.initializeApp(firebaseConfig);
const auth = firebase.auth();
const provider = new firebase.auth.GoogleAuthProvider();

const loginBtn = document.getElementById('login-btn');
const logoutBtn = document.getElementById('logout-btn');
const loginScreen = document.getElementById('login-screen');
const userScreen = document.getElementById('user-screen');
const welcomeMsg = document.getElementById('welcome-msg');

loginBtn.addEventListener('click', () => {
    auth.signInWithRedirect(provider);
});

auth.onAuthStateChanged((user) => {
    if (user) {
        loginScreen.style.display = 'none';
        userScreen.style.display = 'block';
        welcomeMsg.innerText = `Seraphina: "Seja bem-vindo, mestre ${user.displayName}. O Nexus é seu."`;
    } else {
        loginScreen.style.display = 'block';
        userScreen.style.display = 'none';
    }
});

logoutBtn.addEventListener('click', () => {
    auth.signOut().then(() => { location.reload(); });
});
