import os
import cv2
import videokf as vf
import time
import glob

Nonkey_Folder = "C:\\Users\\nonkeyframes" #Adress of Non-key frames folder
Key_Folder = "C:\\Users\\keyframes" #Adress of Key frames folder
VideoFile = "C:\\Users\\test.mp4" #Adress of Video file
vid = cv2.VideoCapture(VideoFile)

try: #Check Non-key folder and if it doesn't exist make folder
    if not os.path.exists(Nonkey_Folder):
        os.makedirs(Nonkey_Folder)
except OSError:
    print("Error in path")

currentframe=0
while (True):
    ret , frame = vid.read()
    if ret:
        currentframe += 1
        name  = Nonkey_Folder + "\\" + str(currentframe) + ".jpg" #Extract video to frames with "videokf" library
        cv2.imwrite(name , frame)
    else:
        try:
            vf.extract_keyframes(VideoFile, method="iframes") #Extract Key frame and save them
            break
        except:
            print("Connection refused by the server..")
            time.sleep(5)
            print("Continue...")
            continue
        break
cam.release()

#Compare Key frame and all frame to extract Non-key frame and save them
KeyFrame = [os.path.basename(x) for x in glob.glob(Key_Folder + "\\*.jpg")]
NonKeyFrame = [os.path.basename(x) for x in glob.glob(Nonkey_Folder + "\\*.jpg")]
for k in KeyFrame:
    for n in NonKeyFrame:
        if k == n:
            os.remove(Nonkey_Folder + "\\"+ n)