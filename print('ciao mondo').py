import socket
import ssl
HOST = '127.0.2.1'
PORT = 6000
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
