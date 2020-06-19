# FTP-KeyLogger (Unfinished)
This is a project that I have started that will send information back to a central ftp server.

This will require for you to have two computers to set up.

Things to complete:
I will be doing this with a raspberry pi and a linux computer.
I will be  making this compatable to work on linux or windows operating system.
I am going to attempt to make this a multithreaded application with each of the functions to be completed be done in a separate thread/process

thinsg that it will do:
1. Capture a video that will be recording. 
2. Send bytes of data back to the ftp server that will append the key pressed into a text file
  - a new folder will be created that will have the captured text file in a folder and the videos in another folder.
  - in the text file there will be multiple folders for every time the program is run. the names of the folders 
    will be the time and date of when the person started the program on their computer.
3. Send 30 second video files back to the ftp server.
  - in the videos folder each 30 second video that is created will be sent after recording for 30 seconds and deleted. 
  - the videos will be stored in a random location deep in the other persons computer for each time the compter sends 
    and deletes a screenshot.
 4. Each task will be run on a concurrent process. I am going to try to implement multiprocessing into this program.
    
    (either do this or have multiple python programs running and doing the same thing and have one python program execute all of the rest from the beginning...)
 5. Have the program be reexecuted when it is stopped from being in a running state.

rescources 

https://realpython.com/intro-to-python-threading/
https://www.tutorialspoint.com/python/python_multithreading.htm