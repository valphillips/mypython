import cv2

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#img=cv2.imread("photo.jpg")
img=cv2.imread("news.jpg")
#

# Use grayscale when doing image recognition as it increases accuracy

gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)   #Will take the image and convert to grayscale


#Get the co-ordinates of the face
#
#Scalefactor of 1.05 will decrease the scale by 5% each time when it does a pass to search for a face, until it has searched whole image
#The smaller the value, the higher the accuracy                                    
#These are widely accepted values to use for image recognition

faces=face_cascade.detectMultiScale(gray_img,
scaleFactor=1.05,
minNeighbors=5)
# Can ply around with the scale if we are picking up stuff that we don't want to e.g. hand
# change scalefactor=1.1 will get rid of the hand.
# May not be able to recognise the partial face

# Draw the rectangle around the face
#
# x,y co-ordinate of top left of image, (x+w, y+h) = co-ordinate of bottom right of imager corner of image - add width to x, add height to y
# (0,255,0) = Colour of the rectangle in BGR format: Blue=0, Green=255, Red=0) - intensity of each colour
# 3 = width of the line of the rectangle

for x, y, w, h in faces:
        img=cv2.rectangle(img, (x,y), (x+w,y+h),(0,255,0),3)


print(type(faces))  #It is a numpy n-dimensional array
print(faces) #Gives you the co-ordinates of the face - upper left corner of face, width, height
# e.g. [[157  84 379 379]]   = Column 157, Row 84, Height 379 ,Width 379

#Now resize the image so that you can be sure it will fit on your screen
#
resized=cv2.resize(img,(int(img.shape[1]/3),int(img.shape[0]/3)))


#cv2.imshow("Gray",gray_img)
cv2.imshow("Color",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
