from flask import Flask, request

app = Flask(__name__)
encryption_key = "05cbb41656c51dcd7df6b8bb6307bfda"
messages = []

def encrypt_text(text, key):
    # 在此处实现加密逻辑
    return encrypted_text

def decrypt_text(encrypted_text, key):
    # 在此处实现解密逻辑
    return decrypted_text

@app.route('/')
def index():
    return "Welcome to the messaging app!"

@app.route('/send_message', methods=['POST'])
def send_message():
    input_text = request.form.get("inputText")
    encrypted_text = encrypt_text(input_text, encryption_key)

    messages.append(encrypted_text)
    return "Message sent successfully."

@app.route('/receive_message', methods=['POST'])
def receive_message():
    encrypted_text = request.form.get("encryptedText")
    decrypted_text = decrypt_text(encrypted_text, encryption_key)

    messages.append(encrypted_text)
    return "Message received successfully."

if __name__ == '__main__':
    app.run()
