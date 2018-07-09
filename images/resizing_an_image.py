import cv2

img=cv2.imread("galaxy.jpg",0) #parameter 2:  1=colour, 0=grayscale, -1=colour with transparent capability

print(type(img))

print(img)
print(img.shape)#Number of values in each axis
print(img.ndim) #Number of dimensions

#resize the image to fit on screen - provide the new dimensions
resized_image=cv2.resize(img,(500,1000))
#resize and keep ratio of the image using the shape function
resized_image_ratio=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))


cv2.imshow("Galaxy",img)   #Title, image object
cv2.imshow("Galaxy resized", resized_image)
cv2.imshow("Galaxy resized ratio", resized_image_ratio)

cv2.imwrite("Galaxy_resized_ratio.jpg",resized_image_ratio)
cv2.waitKey(0)  #Functionality to close the window - 0=closes when user presses any button
               # 2000 = 2000 milliseconds

cv2.destroyAllWindows()


