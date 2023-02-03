import socket
import ssl

HOST = '127.0.2.1'  # Indirizzo IP del server
PORT = 6000  # Numero di porta su cui il server ascolta le connessioni

# Creazione del socket del client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Creazione del socket SSL/TLS
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations('C:/Users/casa/cert.pem')  # Path del certificato del server
ssl_client_socket = context.wrap_socket(client_socket, server_hostname=HOST)

# Connessione al server
ssl_client_socket.connect((HOST, PORT))

# Invio della richiesta di login al server
request = 'login'
ssl_client_socket.sendall(request.encode())

# Ricezione della risposta dal server
response = ssl_client_socket.recv(1024)
print('Ricevuto: {}'.format(response.decode()))

# Chiusura della connessione SSL/TLS con il server
ssl_client_socket.shutdown(socket.SHUT_RDWR)
ssl_client_socket.close()
