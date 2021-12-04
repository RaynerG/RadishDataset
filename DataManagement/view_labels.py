from tkinter import Tk
from tkinter.filedialog import askdirectory
import os
import cv2 , msvcrt

print("[INFO] Select image source directory")
Tk().withdraw()
sourcedir = askdirectory()
print(sourcedir)
os.chdir(sourcedir)

print("[INFO] Select label source directory")
Tk().withdraw()
labeldir = askdirectory()
print(labeldir)

for i in os.listdir(): 
    i_name, i_ext = os.path.splitext(i)
    path = labeldir + '/' + i_name + '.txt'
    print(path)
    
    label = open(path,'r')
    image = cv2.imread(i)
    height = image.shape[0]
    width = image.shape[1]
    
    while True:
        line = label.readline()
        if not line:
            break
        chunks = line.split(' ')
        cx = int(float(chunks[1])*width)
        cy = int(float(chunks[2])*height)
        lw = int(float(chunks[3])*width)
        lh = int(float(chunks[4])*height)
        lx = cx - int(lw/2)
        rx = cx + int(lw/2)
        uy = cy - int(lh/2)
        ly = cy + int(lh/2)
        if lx < 0: lx = 0
        if rx >= width: rx = width-1
        if uy < 0: uy = 0
        if ly >= height: ly = height-1
        image = cv2.line(image, (lx,uy), (lx,ly), (255,255,0),8)
        image = cv2.line(image, (lx,ly), (rx,ly), (255,255,0),8)
        image = cv2.line(image, (rx,ly), (rx,uy), (255,255,0),8)
        image = cv2.line(image, (rx,uy), (lx,uy), (255,255,0),8)

    cv2.namedWindow('window', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('window', 600,600)
    cv2.imshow('window', image)
    cv2.waitKey(0)
    cv2.destroyWindow('window')
    """
    print('[INFO] Press any key to continue, ESC to stop')
    if ord(msvcrt.getch()) == 27:
        print("[INFO] Exiting program ...")
        break
    """