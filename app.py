from flask import Flask, render_template, redirect, url_for
from flask_socketio import SocketIO
import random
import string

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new')
def new_session():
    key = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    return redirect(url_for('collaborate', key=key))

@app.route('/<key>')
def collaborate(key):
    return render_template('collaborate.html', key=key)

@socketio.on('text_change')
def handle_text_change(data):
    key = data['key']
    text = data['text']
    socketio.emit('update_text', {'key': key, 'text': text})

if __name__ == '__main__':
    socketio.run(app)
