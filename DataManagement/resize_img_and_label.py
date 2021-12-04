from PIL import  Image
import os, PIL, glob, cv2, msvcrt
from tkinter import Tk
from tkinter.filedialog import askdirectory
from lxml import etree

print("[INFO] Select image save directory")
Tk().withdraw()
imgdir = askdirectory()
print(imgdir)

print("[INFO] Select label save directory")
Tk().withdraw()
labeldir = askdirectory()
print(labeldir)

while 1:
    print("[INFO] Select source directory")
    Tk().withdraw()
    dirname = askdirectory()
    print(dirname)
    os.chdir(dirname)

    for f in os.listdir(): 
        f_name, f_ext = os.path.splitext(f)

        if f_ext=='.png' or f_ext=='.jpg':
            print("[INFO] Resizing image ", f)
            img = cv2.imread(f)
            resizeImg = cv2.resize(img, (1280, 1280))   # --> CHANGE to pixel dimension

            if f_name.endswith('_crop'):
                file_path = f_name[:-5]
                file_path = imgdir + '/' + file_path + '_resize.png'

            cv2.imwrite(file_path, resizeImg)
            img2 = cv2.imread(file_path)
            os.remove(file_path)
            new_file_path = file_path[:-3]
            new_file_path = new_file_path + 'jpg'
            cv2.imwrite(new_file_path, img2)
           
        elif f_ext == '.xml':
            print("[INFO] Resizing label ", f)
            if f_name.endswith('_crop'):
                file_path = f_name[:-5]
                file_path = labeldir + '/' + file_path + '_resize.xml'

            doc = etree.parse(f)
            size = doc.find('size/width')
            size.text = str(1280)           # --> CHANGE to pixel dimension
            size = doc.find('size/height')
            size.text = str(1280)           # --> CHANGE to pixel dimension

            for elem in doc.findall('object'):
                newxmin = elem.find('bndbox/xmin')
                xmin = int (int(newxmin.text) * (1280 / 2400) )     # --> CHANGE to pixel dimension
                newxmin.text = str(xmin)

                newxmax = elem.find('bndbox/xmax')
                xmax = int ( int(newxmax.text) * (1280 / 2400) )    # --> CHANGE to pixel dimension
                newxmax.text = str(xmax)

                newymin = elem.find('bndbox/ymin')
                ymin = int ( int(newymin.text) * (1280 / 2400) )    # --> CHANGE to pixel dimension
                newymin.text = str(ymin)

                newymax = elem.find('bndbox/ymax')
                ymax = int ( int(newymax.text) * (1280 / 2400) )    # --> CHANGE to pixel dimension
                newymax.text = str(ymax)

            doc.write(file_path)



    print("[INFO] done this dir")
    print('[INFO] Press any key to continue, ESC to stop')
    if ord(msvcrt.getch()) == 27:
        print("[INFO] Exiting program ...")
        break
