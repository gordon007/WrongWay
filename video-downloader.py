import os
#from subprocess import callf
import subprocess
import array
import time

import json
from datetime import datetime, timedelta

def main():
    #totalRunMin = 1
    #timeBetweenStart = 4/5
    #runtimeSec = 30

    
    #now_str = now.date() 
    with open(os.path.join(os.path.expanduser('~'),'Wrong_Way/DesMoines.json')) as f:
            objects = json.load(f)
            
            startTime = datetime.now()
            thisHr = startTime
            nextHr = datetime(thisHr.year, thisHr.month, thisHr.day, thisHr.hour + 1, 0, 0)
            
            c = 0
            while True:
                checkNow = datetime.now()
                    
                for obj in objects:
                    if obj["id"] > 153001 and obj["id"] < 153005:
                        directory = os.path.join(os.path.expanduser('~'),'Wrong_Way/images/',str(obj["name"] + "/"))
                        if not os.path.exists(directory):
                            os.makedirs(directory)
                        #now = datetime.now() + timedelta(seconds = 10)
                        command = "python cam-query.py " + directory + " " + obj["ip"] + " " + obj["name"]
                        print(command)
                        processes = [subprocess.Popen(command.format(i=i), shell=True)for i in range(1l)]
                        #os.system(command)
                c = c + 1
                #nextHr = datetime(thisHr.year, thisHr.month, thisHr.day, thisHr.hour + 1, 0, 0)
                print(((nextHr - datetime.now()).total_seconds()))
                time.sleep((nextHr - datetime.now()).total_seconds())
                thisHr = nextHr
                nextHr = thisHr + timedelta(hours = 1)
                
                 
                
                
    #exitcodes = [p.wait() for p in processes]
    f.close()
if __name__ == "__main__":
    main()

