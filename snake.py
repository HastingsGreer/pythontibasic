import numpy as np
import cv2
width = height = 128

screen = np.zeros((width, height))
cv2.namedWindow("title", cv2.WINDOW_NORMAL)
cv2.resizeWindow("title", 512, 512)
def show():
    cv2.imshow("title", screen)
    
show()

def horiz(y):
    cv2.line(screen, (0, y), (width, y), 1)

def vert(x):
    cv2.line(screen, (x, 0), (x, height), 1)

horiz(0)
horiz(height - 1)

vert(0)
vert(width - 1)

x = 64
y = 64
key = ord('d')
while(screen[y, x] == 0):
    screen[y, x] = 1
    temp = cv2.waitKey(4)
    if temp != -1:
        print(temp)
        key = temp
    x = x + (key == ord("d")) - (key == ord("a"))
    y = y + (key == ord("s")) - (key == ord("w"))
    show()
    
cv2.line(screen, (0, 0), (100, 100), 1)
show()