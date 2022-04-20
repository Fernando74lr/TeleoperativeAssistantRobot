from http.server import BaseHTTPRequestHandler, HTTPServer
import json

hostName = "localhost"
serverPort = 8081


class LocobotServer(BaseHTTPRequestHandler):
    def do_GET(self):
        # file = self.path.replace('/', '')
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({"test": "ok"}).encode('utf-8'))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), LocobotServer)
    print("Server started at http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
