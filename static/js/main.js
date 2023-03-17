const form = document.querySelector('form');
const chatHistory = document.querySelector('#chat-history');

form.addEventListener('submit', async (event) => {
  event.preventDefault();
  const input = document.querySelector('#user-message');
  const message = input.value;
  input.value = '';

  // Create a new HTML element for the user's message
  const userMessage = document.createElement('div');
  userMessage.className = 'user-message';
  userMessage.innerHTML = `
    <p>${message}</p>
  `;
  chatHistory.appendChild(userMessage);

  // Send a POST request to the server with the user's message
  const response = await fetch('/get-response', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message })
  });

  const data = await response.json();
  const botMessage = document.createElement('div');
  botMessage.className = 'bot-message';
  botMessage.innerHTML = `
    <p>${data.message}</p>
  `;
  chatHistory.appendChild(botMessage);
});
