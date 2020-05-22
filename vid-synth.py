import cv2
import os
import time
from datetime import datetime, timedelta
from shutil import copyfile
from pymongo import MongoClient
import sys


def time_in_range(start, end, x):
    """Return true if x is in the range [start, end]"""
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end

cam_name = sys.argv[1]
    
start = datetime.now() - timedelta(seconds = 5)

client = MongoClient('localhost',27017)
db = client['WrongWay']
collection = db[str(cam_name + start.strftime("_%Y%m%d_%H"))]

time.sleep(7)


#orig_directory = os.path.join(os.path.expanduser('~'),'Wrong_Way/images/'+ cam_name +'/')
directory = os.path.join(os.path.expanduser('~'),'Wrong_Way/video/')

if not os.path.exists(directory):
    os.makedirs(directory)

#pics = [img for img in os.listdir(orig_directory) if img.endswith(".jpg")]


for record in collection.find():
    # do stuff with your record
    if(time_in_range(start,start + timedelta(seconds = 10),record.get("date"))):
        copyfile(record.get("file"),directory + record.get("date").strftime("_%Y%m%d_%H:%M:%S:%f") + ".jpg")


#for pic in pics:
#    if(time_in_range(start,start + timedelta(seconds = 10),datetime.datetime(os.path.getmtime(orig_directory + pic)))):
#        copyfile(orig_directory + pic,directory + pic)


video_name = 'video.avi'

images = [img for img in os.listdir(directory) if img.endswith(".jpg")]
images.sort()
frame = cv2.imread(os.path.join(directory, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, 2, (width,height))

for image in images:
    video.write(cv2.imread(os.path.join(directory, image)))

cv2.destroyAllWindows()
video.release()

for f in os.listdir(directory):
    if os.path.isfile(os.path.join(directory, f)):
        os.remove(os.path.join(directory, f))
        
        