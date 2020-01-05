from flask import send_file, Flask
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/<path:filename>')
def serve_file(filename):
    return send_file(filename)

@app.route('/test')
def test():
    return 'test'

@socketio.on('message')
def handle_message(message):
    print('received message: %s' % message)


if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=8000, debug=True)
