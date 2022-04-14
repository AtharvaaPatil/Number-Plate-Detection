import cv2

#################################
frameWidth = 640
frameHeight = 480
nPlateCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
minArea = 500
color = (255,0,255)
#################################

cap = cv2.VideoCapture(1)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)
while True: 
    success, img = cap.read()
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # converting to greyscale
    numberPlates = nPlateCascade.detectMultiScale(imgGray,1.1,4) #(img, scale factor, minimum number of nearest neighbours)


    for (x,y,w,h) in numberPlates:
        area = w*h
        if area > minArea:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.putText(img,"Number Plate",(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
    #loop through all the bounding boxes faces that we have detected and put rectangles around it



    cv2.imshow("Result",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break