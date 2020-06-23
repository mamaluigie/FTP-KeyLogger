# FTP-KeyLogger
This is a project that I have started that will send information back to a central ftp server that is built upon the socket library in python.

This will require for you to have two computers to set up.

Design:
Server will be on the a raspberry pi.
Compatable to work on linux or windows operating system.
Multithreaded application with each of the processes are done on a separate thread.

things that it will do:
1. Capture images that are taken through the camera every 5 seconds. 
2. Log all of the text that is pressed by the user and sent every 300 characters that are pressed.
3. Take screenshots of the computer screen every 5 seconds
- All of the files that are created above are saved in the network folder in windows. I thought that this folder was a good folder to use that no one checks very often.

Things that still need to be done:

- have support for linux
- have the file be created in another location
- have that file startup everytime that person restarts the computer
