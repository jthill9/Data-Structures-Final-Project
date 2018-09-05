#!/usr/bin/env python3

import http.server
import socketserver

PORT = 9555

Handler = http.server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(("", PORT), Handler)

print("serving at port", PORT)
httpd.serve_forever()
