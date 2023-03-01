from flask import Flask, request
import requests

app = Flask(__name__)

backend_servers = [
    "http://backend1:8080",
    "http://backend2:8080",
    "http://backend3:8080"
]

current_server_index = 0

@app.route('/')
def handle_request():
    global current_server_index
    backend_server = backend_servers[current_server_index]
    current_server_index = (current_server_index + 1) % len(backend_servers)
    response = requests.get(backend_server + request.path)
    return response.content

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)