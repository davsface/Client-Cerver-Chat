# Author: Dave Huston
# Course: CS 372
# Assignment: Programming Project 4 - Client Server Chat
# Sources:
# https://www.geeksforgeeks.org/simple-chat-room-using-python/
# https://docs.python.org/3/library/socket.html
# Kurose and Ross, Computer Networking: A Top-Down Approach, 8th Edition, Pearson

import socket

def serverFunction():
    server_port = 8889  # set port
    server_host = socket.gethostname() # set host
    server_socket = socket.socket()
    server_socket.bind((server_host, server_port)) # bind server port to the port
    server_socket.listen(2) # have socket listen for 2 connection
    conn, address = server_socket.accept()

    # print connection info an prompt user
    print("Server listening on: " + str(server_host) + " on port: " +str(server_port))
    print("Connected by {addr}".format(addr = address))
    print('waiting for message. . .')
    print('Type /q to quit')

    while True:
        message = conn.recv(9999).decode() # receive message
        print(str(message))
        data = input('>')
        if data.strip() == '/q':
            break
        conn.send(data.encode())  # send data to the client

    conn.close()  # close connection

if __name__ == '__main__':
    serverFunction()