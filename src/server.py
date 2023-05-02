from flask import Flask, jsonify, request
import gevent.pywsgi


# simple flask server
class Server:
    def __init__(self, port, host, commmand_handler) -> None:
        self.port = port
        self.host = host
        self.app = Flask(__name__)
        self.app.add_url_rule('/', 'index', self.index, methods=['GET'])
        self.app.add_url_rule('/execute/<name>', 'execute', commmand_handler, methods=['GET'])
        self.app_server = None
    def index(self):
        return jsonify({'info':'Simple Command 1.0 (https://github.com/officialEmmel/simple-command) - USE ONLY IN TRUSTED AND SECURED NETWORKS'})
    def run(self):
        print(f'Starting server on {self.host}:{self.port}')
        self.app_server = gevent.pywsgi.WSGIServer((self.host, self.port), self.app)
        self.app_server.serve_forever()
    def stop(self):
        if self.app_server:
            self.app_server.stop()
            self.app_server = None  
    def __del__(self):
        self.stop()