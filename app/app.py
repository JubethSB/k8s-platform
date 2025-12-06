from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def hello():
    html = f"""
    <h3>Hello Jubeth! Cloud Native App v1.0</h3>
    <b>Hostname:</b> {socket.gethostname()}<br/>
    <b>Status:</b> Running on Kubernetes! 🚀
    """
    return html

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)