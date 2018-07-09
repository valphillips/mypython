#Read frames one by one and then display in a loop as a video

import cv2, time

#time library provides some time related functions

# e.g video=cv2.VideoCapture("moviefile.mp4")

video=cv2.VideoCapture(0)

a=0

#In a loop, read frame from camera and display as video
while True:
    a=a+1     #Add each time you loop to see how many frames you are capturing
    check, frame = video.read()

    #print(check)
    print(frame)


    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #Convert to grayscale image

    cv2.imshow("Capturing", gray)   #show the first frame of the video

    key=cv2.waitKey(1)  #Wait for 1 miliseconds 

    if key==ord('q'):
        break
    #If a 'q' is entered, it will break the while loop
    
print(a)

video.release() #release camera
cv2.destroyAllWindows #destroy windows


