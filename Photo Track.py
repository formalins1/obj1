#追踪
import cv2
import numpy as np
from PIL import Image

cap = cv2.VideoCapture(0)
#firstframe=None
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
flag = 1
while (cap.isOpened()):
    ret, frame = cap.read()
    k = cv2.waitKey(1) & 0xFF

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #gray = cv2.GaussianBlur(gray, (21, 21), 0)
    #if firstframe is None:
        #firstframe = gray
        #continue
    #frameDelta = cv2.absdiff(firstframe,gray) #差值视频
    thresh = cv2.threshold(gray, 80, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=2)

    #thresh = np.float32(thresh)
    dst = cv2.cornerHarris(thresh,2,3,0.04)
    #result is dilated for marking the corners, not important
    dst = cv2.dilate(dst,None)

    # Threshold for an optimal value, it may vary depending on the image.

    frame[dst>0.01*dst.max()]=[0,0,255]                    #点追踪

    x, y, w, h = cv2.boundingRect(thresh)
    frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)      #框追踪

    cv2.imshow("原视频输出", frame)
    cv2.imshow("Thresh", thresh)
    #cv2.imshow("frame2", frameDelta)
    cv2.imshow('dst',dst)
    #if cv2.waitKey(0) & 0xff == 27:
        #cv2.destroyAllWindows()