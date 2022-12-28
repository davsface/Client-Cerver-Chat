# Author: Dave Huston
# Course: CS 372
# Assignment: Programming Project 4 - Client Server Chat
# Sources:
# https://www.geeksforgeeks.org/simple-chat-room-using-python/
# https://docs.python.org/3/library/socket.html
# Kurose and Ross, Computer Networking: A Top-Down Approach, 8th Edition, Pearson

import socket

def clientFunction():
    port = 8889  # set port
    host = socket.gethostname()  # set host
    client_socket = socket.socket()
    client_socket.connect((host, port))  # connect to the server

    # print connection info an prompt user
    print("Connected to: {addr} on port: {port}".format(addr=host, port = port))
    print('Type /q to quit')
    print('Enter message to send. . .')
    message = input(">")  # take input

    while True:
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response
        print(data)
        message = input(">")
        if message.strip() == '/q':
            break

    client_socket.close()  # close connection

if __name__ == '__main__':
    clientFunction()