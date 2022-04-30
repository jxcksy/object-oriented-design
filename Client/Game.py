import sys 
sys.path.insert(1, '../Frontend')
import read_dictionary
from Client import  Client
import json
import threading
import pygame
import time
from TileRack import TileRack
from Tile import Tile
from start_menu import StartMenu
from host_lobby import HostLobby
from join_lobby import JoinLobby
from inGame import inGame

class Game():
 
    def __init__(self):

        self.network = None
        self.tr = TileRack()
        self.start_menu = StartMenu()
        self.start_menu.loop()
        self.host_lobby = HostLobby()
        self.join_lobby = None
        self.timer = 30

        read_dictionary.read_dictionary("/etc/dictionaries-common/words")
        self.checkOptions()

    # Determing if the host or join screen should be shown
    def checkOptions(self):

        while True:
            status = self.start_menu.getStatus()

            if status == "Host":
                self.hostGame()
                break

            elif status == "Client":
                code = self.start_menu.getCode()
                self.joinGame()
                break

    # Display the game screen and keep checking if any changes have happened such as play a word
    # Get the starting tiles
    def startGame(self):

        threading.Thread(target=self.checkForChanges).start()
        self.game_screen = inGame()

        threading.Thread(target=self.game_screen.loop).start()
        numOftilesToGet = 7 - self.tr.getNumTiles()

        self.network.send_message(json.dumps({"get_tiles": numOftilesToGet}).encode())

    # create a client object with host as a parameter to tell the serve to create a new lobby
    # display the host screen
    def hostGame(self):

        self.network = Client("host", "127.0.0.1", 8000)
        data = json.loads(self.network.my_socket.recv(1024).decode())
        code = data["code"]
        print("Joined the lobby {} as {}".format(code, data["name"]))

        self.host_lobby.player1 = (data["name"], "player1")
        self.host_lobby.set_code(code)

        # call awaitMessage on a new thread to look for messages from the server while allowing the program to continue
        threading.Thread(target=self.awaitMessage).start()
        self.start_menu.run = False
        start = self.host_lobby.loop()
        self.host_lobby.run = False

        self.network.send_message(json.dumps({start: True}).encode())
        # Disaply the game screen 
        threading.Thread(target=self.startGame).start()

    # create a client object with client as a parameter to tell the serve to join a lobby
    # display the join screen
    def joinGame(self):

        code = self.start_menu.getCode()
        self.join_lobby = JoinLobby()

        self.network = Client("client", "127.0.0.1", 8000, code)
        data = json.loads(self.network.my_socket.recv(1024).decode())
        print("Joined the lobby {} as {}".format(code, data["name"]))

        threading.Thread(target=self.awaitMessage).start()
        self.start_menu.run = False
        self.join_lobby.loop()
        self.join_lobby.run = False

    # keep checking if the inGame screen has indicated that any changes need to be pushed to the other players
    def checkForChanges(self):

        while True:
            time.sleep(1)

            if self.game_screen.changes == True:
                pt = []

                # get all the played tiles and send them to the other players to update their board
                for tile in self.game_screen.playedTiles:
                    pt.append(((tile[0].name, tile[0].value, tile[0].image), tile[1]))

                data = {"changes":{"playedTiles": pt,
                                   "blocked": self.game_screen.blocked}}

                self.network.send_message(json.dumps(data).encode())
                # get more tiles
                numOftilesToGet = 7 - self.tr.getNumTiles()

                self.network.send_message(json.dumps({"get_tiles": numOftilesToGet}).encode())
                self.game_screen.changes = False

    # look for messages from the server
    # handle the message based on what the key is
    def awaitMessage(self):

        while True:
            data = json.loads(self.network.my_socket.recv(1024).decode())

            # messaged recieved when player joined so update the host lobby screen with their name
            if "player_joined" in data:
                players = [self.host_lobby.player1, self.host_lobby.player2, self.host_lobby.player3, self.host_lobby.player4]

                for player in players:
                    if player[0] == "":
                        if player[1] == "player1":
                            self.host_lobby.player1 = (data["player_name"], "player1")
                        elif player[1] == "player2":
                            self.host_lobby.player2 = (data["player_name"], "player2")
                        elif player[1] == "player3":
                            self.host_lobby.player3 = (data["player_name"], "player3")
                        elif player[1] == "player4":
                            self.host_lobby.player4 = (data["player_name"], "player4")
                        break

            # host has started the game so this game instance must start the game
            elif "start_game" in data:
                self.join_lobby.start = True
                threading.Thread(target=self.startGame).start()

            elif "changed_name" in data:
                print(data["previous_name"] + " has changed their name to " + data["changed_name"] )

            # server has sent new tiles to be added to the tile rack
            elif "tiles" in data:
                for tile in data["tiles"]:
                    self.tr.addTile(Tile(tile[0], tile[1], tile[2]))
                self.game_screen.updateTiles(self.tr.getAllTiles())

            # other player has sent changes so update the game board
            elif "changes" in data:
                tiles = []
                for tile in data["changes"]["playedTiles"]:
                    tiles.append((Tile(tile[0][0], tile[0][1], tile[0][2]), tile[1]))
                self.game_screen.playedTiles = tiles
                self.game_screen.blocked = data["changes"]["blocked"]

    def changeName(self, name):
        
        self.player.setName(name)
        self.network.send_message(json.dumps({"change_name": name}).encode())
        print("Changed name to " + name)
 
    def getNetwork(self):
        return self.network # returns Client() object
 
    def getTileBag(self):
        return self.tile_bag # returns TileBag() object
 
    def getTime(self):
        return self.timer # int
 
    def setTimer(self, time): # int
        if type(time) == int and time > 0:
            self.timer = time #checks if new time is valid, ie; positive integer
        else:
            print("Please enter a positve integer.")

def main():
    game = Game()

if __name__ == '__main__':
    main()