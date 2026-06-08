#!/usr/bin/env python3
import http.server, ssl, os, socket

os.chdir(os.path.dirname(os.path.abspath(__file__)))

PORT = 8443
Handler = http.server.SimpleHTTPRequestHandler

ip = socket.gethostbyname(socket.gethostname())
# Try to get the real LAN IP
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
except: pass

ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ctx.load_cert_chain('cert.pem', 'key.pem')

with http.server.HTTPServer(('', PORT), Handler) as httpd:
    httpd.socket = ctx.wrap_socket(httpd.socket, server_side=True)
    print(f"\n  SX-70 Light Meter — HTTPS Server")
    print(f"  ──────────────────────────────────")
    print(f"  On your phone, open:")
    print(f"\n  https://{ip}:{PORT}")
    print(f"\n  ⚠  Tap 'Advanced' → 'Proceed' on the security warning")
    print(f"  (self-signed cert — safe on your own network)")
    print(f"\n  Mac and phone must be on same Wi-Fi")
    print(f"  Press Ctrl+C to stop.\n")
    httpd.serve_forever()
