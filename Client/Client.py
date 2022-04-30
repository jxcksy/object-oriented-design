import socket
import json

class Client():

    def __init__(self, type, ip_address, port, code=""):

        self.host_ip = ip_address
        self.host_port = port
        self.my_socket = socket.socket()
        self.my_socket.connect((ip_address, port))

        data = {"type": type,
                "code": code}
                
        self.my_socket.send(json.dumps(data).encode())

    def send_message(self, data):
        self.my_socket.send(data)
