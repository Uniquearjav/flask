var firebaseConfig = {
    apiKey: "AIzaSyCe1AX6UtCSlH_TLyBujufAOC0nHqy-dRM",
    authDomain: "horiz-aura.firebaseapp.com",
    databaseURL: "https://horiz-aura-default-rtdb.firebaseio.com",
    projectId: "horiz-aura",
    storageBucket: "horiz-aura.appspot.com",
    messagingSenderId: "195677751898",
    appId: "1:195677751898:web:2142ec5235e3117969a663",
    measurementId: "G-VHHQEREH9H"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);

const auth = firebase.auth();
const database = firebase.database();

// Login function
const login = async (email, password) => {
  try {
    const response = await auth.signInWithEmailAndPassword(email, password);
    console.log(response.user.uid);
  } catch (error) {
    console.error(error);
  }
};

// Event listener for login form submit
document.getElementById("login-form").addEventListener("submit", e => {
  e.preventDefault();
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;
  login(email, password);
});