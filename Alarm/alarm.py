import time
import webbrowser
import os
import random

#create text file youtubeLinks.txt if it does not exist already
if os.path.isfile("youtubeLinks.txt") == False:
    print("No videos present. Creating file.")
    flags = os.O_CREAT | os.O_EXCL | os.O_WRONLY
    makeFile = os.open("youtubeLinks.txt", flags)
    with os.fdopen(fisierCreat, 'w') as fileCreate:
        fileCreate.write("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

#Read url's into variable videos
with open("youtubeLinks.txt") as f:
    videos = f.readlines()

#Get time for the alarm from user
print("Enter a time to be awoken? (Between 00:00 and 24:00) Or type 'Settings' for alarm clock settings")
wake = input("--> ")

#Get current time
currentTime = time.strftime("%H:%M")

#Check to see if current time is equal to the time you want to awake. Sleep if not equal
while currentTime != wake:
    print("The time is " + currentTime)
    currentTime = time.strftime("%H:%M")
    time.sleep(1)

#If the two times equal then pick a random video from the list 'videos' and open it in your default web browser
if currentTime == wake:
    print("It is now", currentTime, ". Wake up dummy.")
    random_youtube = random.choice(videos)
    webbrowser.open(random_youtube, new=0, autoraise=True)
