print("Preparing Bot...")

import time,os,pydirectinput,pyautogui, wikipediaapi

LookFor = "!wikipedia" #What word should the bot look for to trigger it.
timeBetweenLogCheck = 1 #How often should the bot open the logs to read the chat.
printLogInConsole = False #Should the bot print the last log message in console? This is used for debugging and can get quite spammy
wikiLanguage = "en" #Change the searching language (If language does not exist it should say a internal issue occured.)


wiki = wikipediaapi.Wikipedia(wikiLanguage)
    
def writeChat(text):
    pydirectinput.keyDown('t')
    pydirectinput.keyUp('t')
    pyautogui.write(text)
    pydirectinput.keyDown('enter')
    pydirectinput.keyUp('enter')


print("Bot Started!")

while True:
    try:
        logfile = open(os.getenv("APPDATA")+"/.minecraft/logs/latest.log",'r')
        lines = logfile.read().splitlines()
        last_line = lines[-1].lower()
        searchFor = (str(last_line.partition(LookFor + " ")[2]))
        if(printLogInConsole == True):
            print(last_line)
        if LookFor in last_line:
            print("Found valid player request. Now writing in chat.. (" + str(searchFor) + ")")
            page = wiki.page(searchFor)
            if (page.exists() == True):
                writeChat(page.summary)
            else:
                writeChat("A wikipedia page with that name does not exist!")


        time.sleep(timeBetweenLogCheck)
    except:
        writeChat("An internal issue occured. This same message may appear over and over again..")
        print("An internal issue occured. You might want to inspect the issue. Problems could be: Language name does not exist, a important piece of code was removed, etc..")
