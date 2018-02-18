import socket
import pyperclip
import time
import thread
import sys

#TODO
#Two-way communication?
#IP from command line

def client(host):
    print(host)
    s = socket.socket()
    port = 12345
    s.connect((host, port))
    clipboard = pyperclip.paste()
    while True:
        tmp = s.recv(1024)
        if(tmp != clipboard and tmp != ""): #tmp != pyperclip.paste()
            clipboard = tmp #remove
            print(tmp)
            pyperclip.copy(clipboard) #(tmp)
            print("updated " + clipboard)
        time.sleep(1)
    s.close

def server(client_ip):
    #client
    if client_ip:
        thread.start_new_thread(client, (client_ip,))
    s = socket.socket()
    host = socket.gethostname()
    host = '192.168.10.33'
    port = 12345
    s.bind((host, port))

    s.listen(5)
    c, addr = s.accept()
    #client
    if not client_ip:
        print("Client starting")
        thread.start_new_thread(client, (addr[0],))
        print("Client started")
    print("Server 9")
    clipboard = ""
    while True:
        if(clipboard != pyperclip.paste()):
            clipboard = pyperclip.paste()
            c.send(clipboard)
            print("sent " + clipboard)
        time.sleep(1)
    c.close()

server('')
