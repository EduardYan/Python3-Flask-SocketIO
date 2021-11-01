"""
This is the principal file for execute the server.
"""

from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
# configurating the connection for the socketio
app.config['SECRET_KEY'] = 'secret'

# getting the connection of socket
socketio = SocketIO(app)

@app.route('/')
def index():
    # retornando la plantilla para la ruta initial
    return render_template('index.html')

@socketio.on('message')
def handleMessage(msg):
    """Manage the connection with the client."""
    print(f'Message: {msg}')

    # sending the message of the client of the others clients
    send(msg, broadcast = True)


if __name__ == '__main__':
    # app.run(debug = True)
    # running the app
    socketio.run(app)
