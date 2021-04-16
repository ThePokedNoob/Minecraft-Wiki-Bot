print("Preparing Bot...")

import time,os,pydirectinput,pyautogui, wikipedia

LookFor = "!wikipedia" #What word in the mc chat should the bot look for to trigger it.
timeBetweenLogCheck = 1 #How often should the bot check the chat log.
printLogInConsole = False #Should the bot print the last found chat message in console? This is used for debugging and can get quite spammy on servers

def writeChat(text):
    pydirectinput.keyDown('t')
    pydirectinput.keyUp('t')
    pyautogui.write(text)
    pydirectinput.keyDown('enter')
    pydirectinput.keyUp('enter')


print("Bot Started!")

while True:
    logfile = open(os.getenv("APPDATA")+"/.minecraft/logs/latest.log",'r')  #Opens a file with the chat log and gets the last chat message every few seconds since the bot can't directly read the minecraft chat
    lines = logfile.read().splitlines()
    last_line = lines[-1]
    last_word = last_line.split()[-1]
    if(printLogInConsole == True):
        print(last_line)
    if LookFor in last_line:
        print("Found valid player request. Now writing in chat.. (" + str(last_word) + ")") #If the bot finds the word that triggers it, it will print in the python console that it found a player triggering the bot and what message the player wants to search for
        try:
            writeChat(wikipedia.summary(last_word, sentences=2)) #Writes in chat what it found on wikipedia.
        except:
            writeChat("There was a issue searching for the term '" + str(last_word) + "'") #If there was a issue searching for the word on wikipedia, it writes this in chat
    time.sleep(timeBetweenLogCheck)
