import sys
sys.path.insert(1, '../Client')
import socket
import threading
import json
import random
import string
from TileBag import TileBag

class Server():

    def __init__(self, ip_address, port):
        self.ip_address = ip_address
        self.port = port
        self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.lobbies = {}
        self.my_socket.bind((ip_address, port))
        self.my_socket.listen()
        
        print("Server started on {}:{}".format(ip_address, port))
        threading.Thread(target=self.awaitConnections).start()

    def awaitConnections(self):
        # actively look for incoming connections
        while True:
            connection, address = self.my_socket.accept()
            data = json.loads(connection.recv(1024).decode())
            ''' 
                dict will have key type set to "host" or "client" for new connections. This determines if a new lobby is created or joined
                lobbies are stored in a list and are identified by a random string of 5 chars
            '''
            if data["type"] == "host":
                code = ''.join(random.choice(string.ascii_lowercase) for i in range(5))
                lobby = Lobby(code, connection, socket)
                self.lobbies[code] = lobby

            elif data["type"] == "client":
                # make sure the lobby exists
                if code not in self.lobbies:
                     connection.send(json.dumps({"lobby_not_found": True}).encode())
                # make sure the lobby isnt full
                elif self.lobbies[code].getPlayerCount == 0:
                    connection.send(json.dumps({"lobby_full": True}).encode())
                else:
                    self.lobbies[code].addPlayer(connection)
'''
    Create multiple lobbies with different players
'''           
class Lobby():

    def __init__(self, code, connection, socket):
        self.code = code
        self.connections = {}
        self.tileBag = TileBag()
        self.default_name = ["Player1", "Player2", "Player3", "Player4",]
        self.connections[connection] = {"name": self.default_name.pop(0)}
        # inform the client that created the lobby what the code to join is
        connection.send(json.dumps({"code": code,
                                    "name": self.connections[connection]["name"]}).encode())
        # allow this lobby to wait for incoming messages while allowing other lobbies to the same.
        threading.Thread(target=self.awaitMessage, args=(connection,)).start()
        print("Lobby {} created".format(code))
        print("{} joined the game".format(self.connections[connection]["name"]))

    '''
        Lobby exists so add a new connection to the lobby. 
        Send a default name to the new player.
        Create a thread for this connection to keep looking for incoming data
        Broadcast too all other connection in the lobby that a player has joined
    '''
    def addPlayer(self, connection):

        self.connections[connection] = {"name": self.default_name.pop(0)}
        connection.send(json.dumps({"name": self.connections[connection]["name"]}).encode())
        dataToSend = {"player_joined": self.connections[connection]["name"] + " has joined.",
                      "player_name": self.connections[connection]["name"]}  
        self.broadcast(dataToSend, connection)

        print("{} joined the game".format(self.connections[connection]["name"]))
        threading.Thread(target=self.awaitMessage, args=(connection,)).start()
    
    # broadcast a message to all other connections in this lobby except for the one who sent the message 
    def broadcast(self, data, client):

        for connection in self.connections:
            if connection != client:
                connection.send(json.dumps(data).encode())
    '''
        awaitMessage will continually look for messages from each connection in the lobby,
        when it recieves the message it should be in json which will be a dict when parsed,
        incoming messages will be broadcast to all other players and can be handled on the client side based on the keys
        eg. {"start_game": True} will be broadcast too all other players indicating to start the game 
    '''
    def awaitMessage(self, connection):

        while True:
            data = json.loads(connection.recv(1024).decode())

            if "get_tiles" in data:
                print("GettingTiles")
                tiles = []
                noOfTilesToGet = data["get_tiles"]

                while noOfTilesToGet > 0:
                    tiles.append(self.tileBag.getRandomTile())
                    noOfTilesToGet -= 1
                data = {"tiles": tiles}
                connection.send(json.dumps(data).encode())
                
            else:
                if "change_name" in data:
                    prevName = self.connections[connection]["name"]
                    self.connections[connection]["name"] = data["change_name"]
                    data = {"changed_name": data["change_name"],
                            "previous_name": prevName}
                    self.default_name.append(prevName)
                    print(prevName + " changed their name to " + self.connections[connection]["name"])
                self.broadcast(data, connection)

    def getPlayerCount(self):
        return len(default_name)


def main():
    server = Server("127.0.0.1", 8000)
    #server.my_socket.close()

if __name__ == '__main__':
    main()