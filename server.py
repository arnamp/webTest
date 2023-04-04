import http.server
import socketserver
import paho.mqtt.client as mqtt

# Start the HTTP server
handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("27.55.74.223", 8001), handler) as httpd:
    print("Serving at port 8001")
    httpd.serve_forever()