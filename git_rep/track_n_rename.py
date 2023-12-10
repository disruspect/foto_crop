import cv2
import os
import math

path="/home/pavel/Desktop/kvety/cropped/"
path2="/home/pavel/Desktop/kvety/clean_flowers_v1"

#Get file names
list=os.listdir(path2)
#alphabetical sorting
s_list=sorted(list,key=str.lower)

#L-jede se doprava
#R - jeden se doleva
#B=R
# Loop through the video frames
for a in range(len(s_list)):
    frame=cv2.imread(path2 +'/'+s_list[a])
    #RENAME PART

    print(s_list[a].split("-"))
    if 'route' in s_list[a]:
        if "noc" in s_list[a]:
            #o index dolu thisisfine
            parsed = s_list[a].split("_")
            rada = parsed[6][0]
            smer = parsed[6][1]
            strom = int(parsed[6][2] + parsed[6][3] + parsed[6][4])
            print(strom)
            new_name = rada + smer + "_" + str(math.floor(strom / 20)) + "_" + str(strom % 20)
            print(new_name)
            odruda=parsed[5]

        else:
            #o index nahoru
            parsed = s_list[a].split("_")
            rada = parsed[5][0]
            smer = parsed[5][1]
            strom = int(parsed[5][2] + parsed[5][3] + parsed[5][4])
            print(strom)
            new_name = rada + smer + "_" + str(math.floor(strom / 20)) + "_" + str(strom % 20)
            print(new_name)
            odruda=parsed[4]


    elif 'arecont' or 'basler' or 'RSrgb' in s_list[a]:
        parsed = s_list[a].split("-")
        rada=parsed[2]
        strom=parsed[3].split(".")[0]
        #print("strom",strom)
        if "b" in strom:
            smer="R"
            strom=int(strom.replace('b',''))
        else:
            smer="L"
            strom=int(strom)
        #print(type(strom))
        new_name=rada+smer+"_"+str(math.floor(strom/20))+"_"+str(strom%20)
        print("new name",new_name)

    else:
        print("Unsupported camera name")
        break

    #CROP PART
    #Load frame
    frame=cv2.imread(path2 +'/'+s_list[a])
    #crop accordingly to camera name
    if 'arecont' in s_list[a]:
        img=frame[50:890,80:400]
        cv2.imwrite(path + parsed[0]+"_"+parsed[1]+"_"+new_name+".jpg", img)
        print('/cropped/' + str(s_list[a]))
        cv2.waitKey(50)
    elif 'basler' in s_list[a]:
        img=frame[1200:2475,650:1500]
        cv2.imwrite(path + parsed[0]+"_"+parsed[1]+"_"+new_name+".jpg", img)
        print('/cropped/' + str(s_list[a]))
        cv2.waitKey(50)
    elif 'route' in s_list[a]:
        img=frame[40:535,50:210]
        cv2.imwrite(path +parsed[0]+"_"+parsed[1]+"_"+parsed[2]+"_"+parsed[3]+"_"+odruda+"_"+new_name+".jpg", img)
        print('/cropped/' + str(s_list[a]))
        cv2.waitKey(50)
    elif 'RSrgb' in s_list[a]:
        img=frame[270:843,75:300]
        cv2.imwrite(path + parsed[0]+"_"+parsed[1]+"_"+new_name+".jpg", img)
        print('/cropped/' + str(s_list[a]))
        cv2.waitKey(50)
    else:
        print("Unsupported camera name")
        break
    #save image as file in folder

