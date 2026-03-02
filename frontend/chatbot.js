async function sendMessage() {
  const input = document.getElementById("userInput").value;
  const response = await fetch("http://localhost:8080/chat", { // <-- INPUT NEEDED: Replace with Cloud Run URL
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: input })
  });
  const data = await response.json();
  document.getElementById("chatbox").innerHTML += "<p>User: " + input + "</p>";
  document.getElementById("chatbox").innerHTML += "<p>Bot: " + data.reply + "</p>";
}
