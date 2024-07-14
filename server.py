import http.server
import socketserver

# Specifică portul pe care vrei să rulezi serverul
PORT = 8000

# Configurarea serverului
Handler = http.server.SimpleHTTPRequestHandler

# Creează un server HTTP
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serverul rulează pe portul:", PORT)
    # Așteaptă cereri
    httpd.serve_forever()
