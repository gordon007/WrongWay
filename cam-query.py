import os
from pymongo import MongoClient
import subprocess
import sys
from datetime import datetime, timedelta
import time
import cv2

def main():
    
    directory = sys.argv[1]
    ip = sys.argv[2]
    cam_name = sys.argv[3]
    nowish = datetime.now() + timedelta(seconds = 28)
    endTime = datetime.now() + timedelta(minutes = 59)
    endTime = endTime + timedelta(seconds = 20)
    fps = 2
    
    client = MongoClient('localhost',27017)
    db = client['WrongWay']
    collection = db[str(cam_name + nowish.strftime("_%Y%m%d_%H"))]
    #collection = db["testCollection"]
    
    #command = "ffmpeg -i  " + ip + " -t " + str(1) + " -vf fps=10 -strftime 1 " + directory + now.strftime("_%Y%m%d_%H:%M:%S") + ".mp4"# > ~/logs/' + obj["name"] + '.txt 2>&1 &'
    #print(command)
    #process = subprocess.Popen(command.format(), shell=True)
    #exitcode = p.wait()
    #time.sleep(3)
    
    
                
                
                
                
    vidcap = cv2.VideoCapture(ip)
    success,image = vidcap.read()
    count = 0
    for x in range(0,20):
        success,image = vidcap.read()
        
    lastFrame = datetime.now()
    while success and (datetime.now() < endTime):
        now = datetime.now() + timedelta(seconds = 28)
        success,image = vidcap.read()
        if(now > (lastFrame + timedelta(seconds = 1.0/fps))):
            cv2.imwrite(directory + now.strftime("_%Y%m%d_%H:%M:%S:%f") + ".jpg", image)     # save frame as JPEG file
            print ('Read a new frame: ', success)
            count += 1
            #time.sleep(0.05)
            entry = {"cam_name":cam_name,
                "file":directory + now.strftime("_%Y%m%d_%H:%M:%S:%f") + ".jpg",
                "date":now}
            collection.insert_one(entry)
            lastFrame = now
        
    #entry = {"cam_name":cam_name,
    #         "file":directory + now.strftime("_%Y%m%d_%H:%M:%S") + ".mp4",
    #         "date":now}
    #collection.insert_one(entry)
    vidcap.release()


    nowsh = time.time()

    for f in os.listdir(directory):

        if os.stat(os.path.join(directory, f)).st_mtime < nowsh -  17000:

            if os.path.isfile(os.path.join(directory, f)):

                os.remove(os.path.join(directory, f))
                                 
if __name__ == "__main__":
    main()