import socket
from  _thread import *
import sys


server = "192.168.1.4"
port = 5555 # use this port for creating connection

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # type of connection,

try:
    s.bind((server, port))
except socket.error as e :
    str(e)


s.listen(2) # if we leave it blank, it allow unlimited to this server
print("Waiting for a connection, Server started")

pos = [(0,0), (100, 100)]


def read_pos(str):
    str = str.split(',')
    return int(str[0]), int(str[1])

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

def threaded_client(conn, player): # by using thread, this one is running on background
    # conn.send(str.encode("Connected"))
    conn.send(str.encode(make_pos(pos[player])))
    reply = ""
    while True:
        try:
            data = read_pos(conn.recv(2048).decode())
            pos[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1 :
                    reply = pos[0]
                else:
                    reply = pos[1]

                print("Received: ", reply)
                print("Sending: ", reply)
            conn.sendall(str.encode(make_pos(reply)))
        except:
            break

    print("Connect lost")
    conn.close()

currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to : ", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1