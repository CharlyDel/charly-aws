import json
from http.server import BaseHTTPRequestHandler, HTTPServer

# Définir le port sur lequel le serveur écoutera
PORT = 8080

# Définir la classe qui gère les requêtes entrantes
class RequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        # Ouvrir le fichier JSON
        with open('fichier.json', 'r') as f:
            data = json.load(f)
        
        # Extraire les informations
        id = data['id']
        nom = data['nom']
        nom_de_famille = data['nom_de_famille']
        email = data['email']
        
        # Envoyer les informations en réponse
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        message = f'ID : {id}<br>Nom : {nom}<br>Nom de famille : {nom_de_famille}<br>Email : {email}'
        self.wfile.write(bytes(message, 'utf8'))

# Lancer le serveur
if __name__ == '__main__':
    httpd = HTTPServer(('localhost', PORT), RequestHandler)
    print(f'Serveur actif sur le port {PORT}')
    httpd.serve_forever()