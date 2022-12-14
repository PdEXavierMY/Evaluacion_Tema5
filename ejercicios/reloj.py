import datetime
import time
import os

def reloj_terminal():
    while(True):
        os.system('cls')
        dt = datetime.datetime.now()
        print( f"{dt.hour}:{dt.minute}:{dt.second}")
        time.sleep(1)