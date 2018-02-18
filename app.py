import socket
import pyperclip
import time
import thread
import sys

def client(host):
    s = socket.socket()
    port = 12345
    s.connect((host, port))
    while True:
        data = s.recv(65536)
        if(data != pyperclip.paste() and data != ""):
            pyperclip.copy(data)
        time.sleep(1)
    s.close

def server(client_ip):
    #client
    if client_ip:
        thread.start_new_thread(client, (client_ip,))
    s = socket.socket()
    host = socket.gethostname()
    #host = '192.168.10.33'
    print('Listening at ' + host)
    port = 12345
    s.bind((host, port))

    s.listen(5)
    c, addr = s.accept()
    #client
    if not client_ip:
        thread.start_new_thread(client, (addr[0],))
    clipboard = ""
    while True:
        if(clipboard != pyperclip.paste()):
            clipboard = pyperclip.paste()
            c.send(clipboard)
        time.sleep(1)
    c.close()

client_ip = ''
if len(sys.argv) == 2:
    client_ip = sys.argv[1]
server(client_ip)
