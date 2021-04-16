print("Preparing Bot...")

import time,os,pydirectinput,pyautogui, wikipedia

LookFor = "!wikipedia" #What word should the bot look for to trigger it.
timeBetweenLogCheck = 1 #How often should the bot open the logs to read the chat.
printLogInConsole = False #Should the bot print the last log message in console? This is used for debugging and can get quite spammy

def writeChat(text):
    pydirectinput.keyDown('t')
    pydirectinput.keyUp('t')
    pyautogui.write(text)
    pydirectinput.keyDown('enter')
    pydirectinput.keyUp('enter')


print("Bot Started!")

while True:
    logfile = open(os.getenv("APPDATA")+"/.minecraft/logs/latest.log",'r')
    lines = logfile.read().splitlines()
    last_line = lines[-1]
    last_word = last_line.split()[-1]
    if(printLogInConsole == True):
        print(last_line)
    if LookFor in last_line:
        print("Found valid player request. Now writing in chat.. (" + str(last_word) + ")")
        try:
            writeChat(wikipedia.summary(last_word, sentences=2))
        except:
            writeChat("There was a issue searching for the term '" + str(last_word) + "'")
    time.sleep(timeBetweenLogCheck)
