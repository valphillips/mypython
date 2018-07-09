#Record the time that a moving object enters the video

import cv2, time, pandas
from datetime import datetime


first_frame=None   #Create a null variable
status_list=[None,None] #Add the first 2 items so that the list comparison won't fail
times=[]
df=pandas.DataFrame(columns=["Start","End"])
                    
video=cv2.VideoCapture(0)

check, frame = video.read()  #My First frame is black, so read and discard
img1=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) 

#Create the base image by capturing the first frame

while True:
    
    check, frame = video.read()

    status=0  #No motion in the current frame
    
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0)   #Blur the image to smooth it, to increase accuracy in the difference calculation
                                         
    
    if first_frame is None:
        first_frame=gray                #Set the initial frame
        print("Captured first frame")
        continue                        #Continue to the beginning of loop again

    delta_frame=cv2.absdiff(first_frame,gray)   #Give an image which is the difference between first frame and current frame


    #If the difference between first frame and second frame is more than 30, assign it white value,
    #otherwise assign it black value.  255=white

    thresh_frame=cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]

    thresh_frame=cv2.dilate(thresh_frame, None, iterations=2)  #Smooth the threshold frame. Go through it twice. The more times the smoother image will be.

    #Find the contours of the threshold frame and store in a tuple (cnts). Check what the area is
    (_,cnts,_)=cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    #Keep only the contours that have an area bigger than 1000 pixels
    for contour in cnts:
        if cv2.contourArea(contour) < 10000: #100 x 100 window.  Depends on size of objects you want ot capture
            continue   #Continue to end of the loop
        status=1 #We now have movement in the frame
        (x, y, w, h)=cv2.boundingRect(contour)  #Get the co-ordinates of the contour
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3) #Draw the rectangle on the colour frame


    status_list.append(status)
    if status_list[-1]==1 and status_list[-2]==0:  #record time status changed from 0 to 1 (movement started)
        times.append(datetime.now())
    if status_list[-1]==0 and status_list[-2]==1:  #record time status changed from 1 to 0 (movement stopped)
        times.append(datetime.now())
        
    
    
    cv2.imshow("First Frame",first_frame)
    cv2.imshow("Delta Frame",delta_frame)
    cv2.imshow("Threshold Frame", thresh_frame)
    cv2.imshow("Color Frame", frame)


    key=cv2.waitKey(1)
        
    if key==ord('q'):
        if status==1:
            times.append(datetime.now())  #If there is motion while you exit the program. record end time
        break


video.release()
cv2.destroyAllWindows

print(status_list)
print(times)

for i in range(0,len(times),2):     #iterate through the 'times' list, 2 items at a time
    df=df.append({"Start":times[i],"End":times[i+1]},ignore_index=True)

                    
df.to_csv("Times.csv")  #Export the dataframe to a csv file                    
                    

