import cv2
from PIL import Image

# Function to extract frames
def FrameCapture(path):
    # Path to video file
    vidObj = cv2.VideoCapture("videos/" + path)

    success,image = vidObj.read()
    count = 0

    while success:
        if count % 3 == 0:
            resized = cv2.resize(image, (960, 540), interpolation=cv2.INTER_AREA)
            filename = "%s_%d.jpg" % (path.split(".MOV")[0],count)
            cv2.imwrite(filename, resized)
        success, image = vidObj.read()
        count += 1

    vidObj.release()

# Driver Code
if __name__ == '__main__':
    # Calling the function
    FrameCapture("IMG_0994.MOV")