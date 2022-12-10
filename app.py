from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('text_change')
def handle_text_change(data):
    text = data['text']
    socketio.emit('update_text', {'text': text})

if __name__ == '__main__':
    socketio.run(app)
