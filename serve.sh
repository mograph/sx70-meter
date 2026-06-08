#!/bin/bash
# Find your local IP
IP=$(ipconfig getifaddr en0 2>/dev/null || ipconfig getifaddr en1 2>/dev/null || echo "127.0.0.1")
PORT=8080
echo ""
echo "  SX-70 Light Meter"
echo "  ─────────────────────────────────"
echo "  Open on your phone:"
echo ""
echo "  http://$IP:$PORT"
echo ""
echo "  (Mac and phone must be on the same Wi-Fi)"
echo "  Press Ctrl+C to stop."
echo ""
cd "$(dirname "$0")"
python3 -m http.server $PORT
