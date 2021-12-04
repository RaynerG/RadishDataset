# change pascal VOC label format to yolo format

from tkinter import Tk
from tkinter.filedialog import askdirectory
from lxml import etree
import os

print("[INFO] Select label source directory")
Tk().withdraw()
sourcedir = askdirectory()
print(sourcedir)
os.chdir(sourcedir)

print("[INFO] Select save directory")
Tk().withdraw()
savedir = askdirectory()
print(savedir)

for f in os.listdir(): 
    f_name, f_ext = os.path.splitext(f)
        
    if f_ext == '.xml':
        print("[INFO] Changing label format ", f)

        save_path = savedir + '/' + f_name + '.txt'
        handle = open(save_path,"x")

        doc = etree.parse(f)


        for elem in doc.findall('object'):
            
            descriptor = str()

            cid = elem.find('name')
            if cid.text == 'RAD1':
                descriptor += '0 '
            elif cid.text == 'RAD2':
                descriptor += '0 '
            elif cid.text == 'RAD3':
                descriptor += '1 '
            elif cid.text == 'RAD4':
                descriptor += '1 '
            
            xmin = int(elem.find('bndbox/xmin').text)
            xmax = int(elem.find('bndbox/xmax').text)
            xmid = (xmin + (xmax - xmin)/2)/1280
            xmid = round(xmid, 6)
            descriptor += str(xmid) + ' '

            ymin = int(elem.find('bndbox/ymin').text)
            ymax = int(elem.find('bndbox/ymax').text)
            ymid = (ymin + (ymax - ymin)/2 )/1280
            ymid = round(ymid, 6)
            descriptor += str(ymid) + ' '

            width = xmax/1280 - xmin/1280
            width = round(width, 6)
            descriptor += str(width) + ' '

            height = ymax/1280 - ymin/1280
            height = round(height, 6)
            descriptor += str(height) + ' '

            handle.write(descriptor + '\n')


print("[INFO] Finished directory, exiting")