import cv2
import numpy as np
import threading
import time
import sys
import BFS as b
import Skaliranje
from Point import Pt
import math


startPoint=0
endPoint=0
mouseClick=0
pictureHeight=0
pictureWidth=0


def disp():
	global image
	cv2.imshow("Maze_solver", image)
	cv2.waitKey(0)




image=cv2.imread("FINALNITEST.png")



gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5),cv2.BORDER_DEFAULT)
ret, thresh = cv2.threshold(blur, 100, 255,cv2.THRESH_BINARY_INV)

#rubne tocke
corners=cv2.goodFeaturesToTrack(gray, 0, 0.01, 100)
corners=np.int0(corners)
rubovi=[]



topLeftval=1000000000000
topLeft=0

bottomRightval=0
bottomRight=0

bottomLeftval=0
bottomLeft=0

topRight=0
topRightVal=1000000000000


br=0
for i in corners:
    x,y=i.ravel()
    privremeniZbroj=int(x+y)
    if(privremeniZbroj<topLeftval):
        topLeftval=privremeniZbroj
        topLeft=Pt(x,y)
    if(privremeniZbroj > bottomRightval):
        bottomRightval=privremeniZbroj
        bottomRight=Pt(x,y)
    if(int(y)<topRightVal):
        topRightVal=int(y)
        topRight=Pt(x,y)
    if(int(y)>bottomLeftval):
        bottomLeftval=int(y)
        bottomLeft=Pt(x,y)
    rubovi.append(Pt(x,y))

    #cv2.circle(image, (x,y), 6, 255,-1)
    #cv2.putText(image, str(int(y)), (x + 5, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (100, 0, 100), 2)
    br+=1


'''for p in rubovi:
    if(p.x==topLeft.x and p.y==topLeft.y):
        cv2.circle(image, (p.x, p.y), 3, 255, -1)
        cv2.putText(image, "TOP LEFT", (p.x - 20, p.y - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
    if(p.x==bottomRight.x and p.y == bottomRight.y):
        cv2.circle(image, (p.x, p.y), 3, 255, -1)
        cv2.putText(image, "BOTTOM RIGHT", (p.x - 20, p.y - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
    if (p.x == topRight.x and p.y == topRight.y):
        cv2.circle(image, (p.x, p.y), 3, 255, -1)
        cv2.putText(image, "TOP RIGHT", (p.x - 20, p.y - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
    if(p.x==bottomLeft.x and p.y==bottomLeft.y):
        cv2.circle(image, (p.x, p.y), 3, 255, -1)
        cv2.putText(image, "BOTTOM LEFT", (p.x - 20, p.y - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)'''

#distance between 2 points

distance=int(math.sqrt(pow(int(bottomRight.x)-int(bottomLeft.x),2)+pow(int(bottomRight.y)-int(bottomLeft.y),2)))
const=int(distance/100)

print("1m u px= "+str(distance)+" 1cm u px= ",str(const))
inputPoints=np.float32([[topLeft.x, topLeft.y],[bottomLeft.x, bottomLeft.y],[bottomRight.x, bottomRight.y],[topRight.x,topRight.y]])
outputPoints=np.float32([[bottomLeft.x,bottomLeft.y-distance],[bottomLeft.x, bottomLeft.y],[bottomLeft.x+distance,bottomLeft.y],[bottomLeft.x+distance, bottomLeft.y-distance]])
matrix=cv2.getPerspectiveTransform(inputPoints,outputPoints)
transformed=cv2.warpPerspective(image,matrix,(1000,1000), flags=cv2.INTER_LINEAR )
image=transformed

'''gray1=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret1,threshold1=cv2.threshold(gray,200,255,0)
size=np.size(threshold1)
skel=np.zeros(threshold1.shape, np.uint8)
element=cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))

while True:
    opened=cv2.morphologyEx(threshold1, cv2.MORPH_OPEN, element)
    temp=cv2.subtract(threshold1, opened)
    eroded=cv2.erode(threshold1, element)
    skel=cv2.bitwise_or(skel,temp)
    threshold1=eroded.copy()
    print("dela")
    if cv2.countNonZero(threshold1)==1:
        print("ulazi")
        break

#cv2.imshow(' ', transformed)'''

gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur=cv2.GaussianBlur(gray,(5,5),cv2.BORDER_DEFAULT)
ret,thresh=cv2.threshold(blur, 200, 255, cv2.THRESH_BINARY_INV)
contours, hierarchies=cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
blank=np.zeros(thresh.shape[:2], dtype='uint8')
#cv2.drawContours(image, contours, -1, (255,0,0),1)
for i in contours:
    M=cv2.moments(i)
    if M['m00']!=0:
        cx=int(M['m10']/M['m00'])
        cy=int(M['m01']/M['m00'])

        #print(image[cx,cy])
        area=cv2.contourArea(i)
        #print(area)
        if (area>7500 and area<8100):
            '''cv2.drawContours(image, [i], -1, (0,255,0),2)
            cv2.circle(image, (cx, cy), 7, (0, 0, 255), -1)
            cv2.putText(image, "pocetna", (cx - 20, cy - 20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
            '''
            startPoint=Pt(cx,cy)
        elif(area>8100 and area<9100):
            '''cv2.drawContours(image, [i], -1, (0, 255, 0), 2)
            cv2.circle(image, (cx, cy), 7, (0, 0, 255), -1)
            cv2.putText(image, "krajnja", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
            '''
            endPoint=Pt(cx, cy)
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
_,image=cv2.threshold(gray, 50,255,cv2.THRESH_BINARY)
image=cv2.cvtColor(image,cv2.COLOR_GRAY2BGR)

pictureHeight=image.shape[0]
pictureWidth = image.shape[1]
print(startPoint.x,startPoint.y)
#b.bfs(startPoint,endPoint,pictureHeight,pictureWidth, image)
t=threading.Thread(target=disp, args=())
t.start()


t.join()

image=transformed
sys.exit()


#for p in path:

#cv2.imshow("",temp)
#cv2.imshow("",image)
cv2.waitKey(0)