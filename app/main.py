import mimetypes
import pathlib
import socket
from datetime import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
from multiprocessing import Process
from pymongo import MongoClient


class HttpHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        pr_url = urllib.parse.urlparse(self.path)
        if pr_url.path == '/':
            self.send_html_file('index.html')
        elif pr_url.path == '/message':
            self.send_html_file('message.html')
        else:
            if pathlib.Path().joinpath(pr_url.path[1:]).exists():
                self.send_static()
            else:
                self.send_html_file('error.html', 404)

    def send_html_file(self, filename, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open(filename, 'rb') as fd:
            self.wfile.write(fd.read())

    def send_static(self):
        self.send_response(200)
        mt = mimetypes.guess_type(self.path)
        if mt:
            self.send_header("Content-type", mt[0])
        else:
            self.send_header("Content-type", 'text/plain')
        self.end_headers()
        with open(f'.{self.path}', 'rb') as file:
            self.wfile.write(file.read())

    def do_POST(self):
        data = self.rfile.read(int(self.headers['Content-Length']))
        self.send_to_socket(data)
        self.send_response(302)
        self.send_header('Location', '/')
        self.end_headers()

    @staticmethod
    def send_to_socket(message):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server = '', 5000
        sock.sendto(message, server)
        sock.close()


def run_http_server(server_class=HTTPServer, handler_class=HttpHandler):
    server_address = ('', 3000)
    http = server_class(server_address, handler_class)
    try:
        http.serve_forever()
    except KeyboardInterrupt:
        http.server_close()


def run_socket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server = '', 5000
    sock.bind(server)
    client = MongoClient('mongodb://root:example@mongo:27017/')
    client.server_info()
    db = client.hw6
    try:
        while True:
            data, address = sock.recvfrom(1024)
            data_parse = urllib.parse.unquote_plus(data.decode())
            data_dict = {key: value for key, value in [el.split('=') for el in data_parse.split('&')]}
            data_dict["date"] = datetime.now().isoformat()
            db.messages.insert_one(data_dict)

    except KeyboardInterrupt:
        print(f'Destroy server')
    finally:
        sock.close()
        client.close()


if __name__ == '__main__':
    Process(target=run_http_server).start()
    Process(target=run_socket).start()
