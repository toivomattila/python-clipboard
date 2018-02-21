import socket
import pyperclip
import time
import thread
import sys

client_ip = ''

def client():
    #If client_ip is empty, wait for server to give the ip
    while not client_ip:
        time.sleep(1)
    s = socket.socket()
    port = 12345
    s.connect((client_ip, port))
    print("Listening to " + client_ip)
    while True:
        data = s.recv(65536)
        if(data != pyperclip.paste() and data != ""):
            pyperclip.copy(data)
        time.sleep(1)
    s.close

def server():
    global client_ip
    s = socket.socket()
    port = 12345
    s.bind(('', port))

    s.listen(5)
    c, addr = s.accept()
    print("Sending to " + addr[0])
    client_ip = addr[0]
    clipboard = ""
    while True:
        if(clipboard != pyperclip.paste()):
            clipboard = pyperclip.paste()
            c.send(clipboard)
        time.sleep(1)
    c.close()

if len(sys.argv) == 2:
    client_ip = sys.argv[1]
thread.start_new_thread(client, ())
server()
