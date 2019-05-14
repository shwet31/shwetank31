from datetime import datetime
from difflib import get_close_matches
import glob2


files=glob2.glob("*.txt")

def fileAppend(files):
    content=""
    for i in files:
        ff=open(i,"r")
        content += (ff.read()+"\n")
        ff.close()
    now=datetime.now()
    appendedFile=open(now.strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt","w")
    appendedFile.write(content)
    appendedFile.close()

fileAppend(files)
