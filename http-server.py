import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/valid-json":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            valid_json = {"message": "Hello, world!"}
            self.wfile.write(json.dumps(valid_json).encode())
        elif self.path == "/invalid-json":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            invalid_json = '{"message": "Hello, world!",}'  # Note the trailing comma
            self.wfile.write(invalid_json.encode())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"404 Not Found")


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ("", 7777)
    httpd = server_class(server_address, handler_class)
    print("Starting httpd server on port 7777...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
