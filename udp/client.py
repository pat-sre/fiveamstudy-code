from socket import socket, AF_INET, SOCK_DGRAM

server_name = 'hostname'
server_port = '12000'

client_socket = socket(AF_INET, SOCK_DGRAM)
message = input('input message:')

