import json
import cv2

def pointsToString(annotation,width,height):
    res = ""
    # a is a single annotation
    for a in annotation:
        # change your class id here
        id = 0
        # width and height
        w = width
        h = height
        # p is list of 4 points
        p = a["points"]
        x_min = int(p[0][0] * w)
        y_min = int(p[0][1] * h)
        x_max = int(p[1][0] * w)
        y_max = int(p[2][1] * h)
        cur = str(x_min) + "," + str(y_min) + "," + str(x_max) + "," + str(y_max) + "," + str(id)
        res += cur + " "
    return res

def getwh(imagename):
    img=cv2.imread(imagename)
    sp=img.shape
    w=sp[1] # get width
    h=sp[0] # get height
    s=[w,h]
    return s

folder = 'Images'
f = open("Room Number Detection - 1009 - 2.json", "r")

for line in f:
    j = json.loads(line)
    filename = j["content"].split("___")[1]
    filename1=filename.split('_')[0]
    filename2=filename.split('_')[1]
    filename3=filename.split('_')[2]
    filename4=filename2+'_'+filename3
    filename_folder=filename1+"/"+filename2+'_'+filename3
    chs=getwh(filename4)
    width=chs[0]
    height=chs[1]
    if j["annotation"] != None and len(j["annotation"]) > 0:
        path = folder +"/" +filename_folder
        print(path + " " + pointsToString(j["annotation"],width,height))
