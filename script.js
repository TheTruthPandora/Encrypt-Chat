document.addEventListener('DOMContentLoaded', function() {
  const chatbox = document.getElementById('chatbox');
  const inputText = document.getElementById('inputText');
  const sendMessageButton = document.getElementById('sendMessageButton');
  const decryptButton = document.getElementById('decryptButton');

  sendMessageButton.addEventListener('click', sendMessage);
  decryptButton.addEventListener('click', decryptMessages);

  function sendMessage() {
    const text = inputText.value;
    if (text.trim() === '') {
      return;
    }

    const formData = new FormData();
    formData.append('text', text);

    fetch('/api/send-message', {
      method: 'POST',
      body: formData
    })
    .then(response => response.json())
    .then(data => {
      if (data.status === 'success') {
        inputText.value = '';
        inputText.focus();
      }
    })
    .catch(error => {
      console.error('Error:', error);
    });
  }

  function decryptMessages() {
    fetch('/api/receive-message', {
      method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
      const decryptedText = data.decrypted_text;
      if (decryptedText) {
        const p = document.createElement('p');
        p.textContent = decryptedText;
        chatbox.appendChild(p);
      }
    })
    .catch(error => {
      console.error('Error:', error);
    });
  }
});
