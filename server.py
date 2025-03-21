# selenium_framework/server.py
import http.server
import socketserver
import threading
import time
from run_tests import run_tests

PORT = int(os.environ.get('PORT', 8080))

class SimpleHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Health check passed')

def start_server():
    handler = SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()

def main():
    # Start the HTTP server in a separate thread
    server_thread = threading.Thread(target=start_server)
    server_thread.daemon = True
    server_thread.start()
    
    # Give the server a moment to start
    time.sleep(2)
    
    # Run the tests
    run_tests()
    
    # Keep the main thread alive to maintain the HTTP server
    while True:
        time.sleep(60)

if __name__ == "__main__":
    import os
    main()