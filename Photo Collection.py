#主
from __future__ import print_function
import numpy as np
from PIL import Image
import csv,os,cv2
import pandas as pd

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

flag = 1
while (cap.isOpened()):

    ret, frame = cap.read()
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("Gray", gray)

    cv2.imshow("原视频输出", frame)

    k = cv2.waitKey(1) & 0xFF
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("灰度视频输出", gray)
    """
    threshold = 80
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    im = gray.point(table, '1')
    cv2.imshow("二值化视频输出", im)
    """
    if k == ord('s'):
        cv2.imwrite('1.jpg', gray)
        im = Image.open("1.jpg")
        threshold = 80
        table = []
        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)
        im = im.point(table, '1')
        im.save('3.jpg')
        aaa = cv2.imread("3.jpg")
        a = aaa.shape
        print('photo format:')
        print(a)
        im.show()
        aaa = cv2.resize(aaa,(28, 28),interpolation=cv2.INTER_CUBIC)
        cv2.imwrite('2.jpg', aaa)
        tyx = Image.open("2.jpg")
        zjc = []
        zjc.append(0)
        yj = 1
        for i in range(28):
            for j in range(28):
                b = tyx.getpixel((j,i))
                cc = (b[0]+b[1]+b[2])//3
                cc = 255 - cc
                if yj < 112:
                    zjc.append(0)
                elif yj > 672:
                    zjc.append(0)
                else:
                    zjc.append(cc)
                yj = yj+1
        with open('run.csv', 'w', newline='') as t_file:
            csv_writer = csv.writer(t_file)
            csv_writer.writerow(zjc)

    elif k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

