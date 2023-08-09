const express = require('express');
const app = express();
const cors = require('cors');
const crypto = require('crypto');

app.use(cors()); // 添加CORS中间件
const encryptionKey = Buffer.from('05cbb41656c51dcd7df6b8bb6307bfda', 'hex'); // 替换为您的加密密钥
const cipher = crypto.createCipheriv('aes-128-ecb', encryptionKey, null);

const messages = [];

app.post('/send_message', (req, res) => {
  const { message } = req.body;
  const encryptedText = encryptText(message);
  messages.push(encryptedText);
  res.json({ success: true });
});

app.get('/get_messages', (req, res) => {
  const decryptedMessages = messages.map(msg => decryptText(msg));
  res.json({ messages: decryptedMessages });
});

function padText(text) {
  while (text.length % 16 !== 0) {
    text += ' ';
  }
  return text;
}

function encryptText(text) {
  const paddedText = padText(text);
  const encryptedBytes = cipher.update(paddedText, 'utf8', 'base64') + cipher.final('base64');
  return encryptedBytes;
}

function decryptText(encryptedText) {
  const decryptedBytes = cipher.update(encryptedText, 'base64', 'utf8') + cipher.final('utf8');
  return decryptedBytes.trim();
}

const port = 3000;
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
