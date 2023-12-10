import cv2
import os

path="/home/pavel/Desktop/kvety/clean_flowers_v1"

#Get file names
list=os.listdir(path)
#alphabetical sorting
s_list=sorted(list,key=str.lower)

# Loop through the video frames
for a in range(len(s_list)):
    #Load frame
    frame=cv2.imread(path +'/'+s_list[a])
    #crop accordingly to camera name
    if 'arecont' in s_list[a]:
        img=frame[50:890,80:400]
    elif 'basler' in s_list[a]:
        img=frame[1200:2475,650:1500]
    elif 'route' in s_list[a]:
        img=frame[40:535,50:210]
    elif 'RSrgb' in s_list[a]:
        img=frame[270:843,75:300]
    else:
        print("Unsupported camera name")
        break
    #save image as file in folder
    cv2.imwrite(path + '/cropped/' + str(s_list[a]), img)
    print('/cropped/' + str(s_list[a]))
    cv2.waitKey(50)
