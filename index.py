from flask import Flask, request, jsonify

app = Flask(__name__)

encryption_key = "05cbb41656c51dcd7df6b8bb6307bfda"
messages = []

@app.route('/api/send-message', methods=['POST'])
def send_message():
    input_text = request.form['text']
    encrypted_text = encrypt_text(input_text, encryption_key)

    # 模拟发送消息到服务器
    simulate_server_send(encrypted_text)

    return jsonify({'status': 'success'})

@app.route('/api/receive-message', methods=['POST'])
def receive_message():
    encrypted_text = request.form['text']
    decrypted_text = decrypt_text(encrypted_text, encryption_key)

    return jsonify({'decrypted_text': decrypted_text})

def simulate_server_send(encrypted_text):
    messages.append(encrypted_text)

    # 这里可以将消息发送给另一方，例如通过WebSocket或HTTP请求

def encrypt_text(text, key):
    # 实现加密逻辑，可以使用您选择的加密算法

def decrypt_text(encrypted_text, key):
    # 实现解密逻辑，可以使用您选择的解密算法

if __name__ == '__main__':
    app.run()
