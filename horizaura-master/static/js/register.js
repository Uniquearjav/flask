// Initialize Firebase
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
  firebase.initializeApp(firebaseConfig);
  
  // Get references to the form and inputs
  const registerForm = document.querySelector("#register-form");
  const nameInput = document.querySelector("#name");
  const emailInput = document.querySelector("#email");
  const passwordInput = document.querySelector("#password");
  
  // Handle form submission
  registerForm.addEventListener("submit", (event) => {
    event.preventDefault();
    const name = nameInput.value;
    const email = emailInput.value;
    const password = passwordInput.value;
    firebase
      .database()
      .ref("users")
      .push({
        name: name,
        email: email,
        password: password,
      });
  });
  