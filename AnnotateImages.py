import json

def pointsToString(annotation):
    res = ""
    # a is a single annotation
    for a in annotation:
        # change your class id here
        id = 0
        # width and height
        w = 960
        h = 540
        # p is list of 4 points
        p = a["points"]
        x_min = int(p[0][0] * w)
        y_min = int(p[0][1] * h)
        x_max = int(p[1][0] * w)
        y_max = int(p[2][1] * h)
        cur = str(x_min) + "," + str(y_min) + "," + str(x_max) + "," + str(y_max) + "," + str(id)
        res += cur + " "
    return res

folder = '1007'
f = open("Room Number - 1007.json", "r")

for line in f:
    j = json.loads(line)
    filename = j["content"].split("___")[1]
    filename = "IMG_" + filename.split("_")[2] + "_" + filename.split("_")[3]
    if j["annotation"] != None and len(j["annotation"]) > 0:
        path = folder + filename
        print(path + " " + pointsToString(j["annotation"]))

