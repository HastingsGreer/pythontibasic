import numpy as np
import cv2
width = height = 1024

screen = np.zeros((width, height))
cv2.namedWindow("title", cv2.WINDOW_NORMAL)
cv2.resizeWindow("title", width, width)
def show():
    cv2.imshow("title", screen)
    
show()

def horiz(y):
    cv2.line(screen, (0, y), (width, y), 1)

def vert(x):
    cv2.line(screen, (x, 0), (x, height), 1)



x = 64
y = 64
slide = 0

while(True):
  for _ in range(1000):
    screen[int(y), int(x)] = 1
    
    r = np.random.random()
    if r < .33:
        #x, y = x- width / 2, y - width / 2
        
        

        x, y = np.cos(slide) * x + np.sin(slide) * y, -np.sin(slide) * x + np.cos(slide) * y
        
        #x, y = x + width / 2, y + width / 2
        x = x / 2 + width / 4
        y /= 2
    elif r < .66:
        x /= 2
        y = y / 2 + width / 2
    else:
        xt = x
        x = width / 2 + x / 2 
        y = width/2 + y / 2
  screen *= .992
  slide += .0003
  temp = cv2.waitKey(1)
  if temp == ord("q"):
    break
  show()
    
cv2.line(screen, (0, 0), (100, 100), 1)
show()