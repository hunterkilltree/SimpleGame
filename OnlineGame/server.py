import socket
from  _thread import *
import sys

server = "192.168.1.6"
port = 5555 # use this port for creating connection

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # type of connection,

try:
    s.bind((server, port))
except socket.error as e :
    str(e)


s.listen(2) # if we leave it blank, it allow unlimited to this server

print("Waiting for a connection, Server started")

def threaded_client(conn): # by using thread, this one is running on background

    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", reply)
                print("Sending: ", reply)
            conn.sendall(str.encode(reply))
        except:
            break


while True:
    conn, addr = s.accept()
    print("Connected to : ", addr)

    start_new_thread(threaded_client, (conn, ))