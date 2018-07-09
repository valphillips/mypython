import glob2
import cv2

filelist=glob2.glob("*.jpg")

for file in filelist:
    print("filename = %s" % file)

    img=cv2.imread(file,1) #parameter 2:  1=colour, 0=grayscale, -1=colour with transparent capability
    img_resized=cv2.resize(img,(100,100))
    cv2.imshow("Hey", img_resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_"+file, img_resized)

#cv2.imshow("Galaxy",img)   #Title, image object
#cv2.imshow("Galaxy resized", resized_image)
#cv2.imshow("Galaxy resized ratio", resized_image_ratio)

#cv2.imwrite("Galaxy_resized_ratio.jpg",resized_image_ratio)
#cv2.waitKey(0)  #Functionality to close the window - 0=closes when user presses any button
               # 2000 = 2000 milliseconds

#cv2.destroyAllWindows()


