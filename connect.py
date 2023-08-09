from flask import Flask, request, jsonify
from Crypto.Cipher import AES
from base64 import b64encode, b64decode

app = Flask(__name__)
encryption_key = b'0da9055fd6030b855c20786ef5ac6a75'  # 替换为您的加密密钥
cipher = AES.new(encryption_key, AES.MODE_ECB)

messages = []

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.get_json()
    encrypted_text = encrypt_text(data['message'])
    messages.append(encrypted_text)
    return jsonify({'success': True})

@app.route('/get_messages', methods=['GET'])
def get_messages():
    decrypted_messages = [decrypt_text(msg) for msg in messages]
    return jsonify({'messages': decrypted_messages})

def pad_text(text):
    while len(text) % 16 != 0:
        text += ' '
    return text

def encrypt_text(text):
    padded_text = pad_text(text)
    encrypted_bytes = cipher.encrypt(padded_text.encode())
    encrypted_text = b64encode(encrypted_bytes).decode()
    return encrypted_text

def decrypt_text(encrypted_text):
    encrypted_bytes = b64decode(encrypted_text)
    decrypted_bytes = cipher.decrypt(encrypted_bytes)
    decrypted_text = decrypted_bytes.decode().rstrip()
    return decrypted_text

if __name__ == '__main__':
    app.run()