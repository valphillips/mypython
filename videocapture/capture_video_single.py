#Read frames one by one and then display in a loop as a video

import cv2, time

#time library provides some time related functions

# e.g video=cv2.VideoCapture("moviefile.mp4")

video=cv2.VideoCapture(0)
# The argument can be either 0/1/2 or name of a video file.  If you only have one
# camera it will be 0
# Above line will open the camera

#create a frame object that wil read the images from the video object
# check is a boolean
# frame is a numpy array with an image
# 3 dimensional array because it is a color image from camera

check, frame = video.read()

#print(check)
#print(frame)


gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #Convert to grayscale image

time.sleep(3)  #Wait 3 seconds)
cv2.imshow("Capturing", gray)   #show the first frame of the video


cv2.waitKey(0)  #Wait for key to be pressed to close window
video.release() #release camera
cv2.destroyAllWindows #destroy windows
