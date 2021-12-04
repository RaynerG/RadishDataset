from tkinter import Tk
from tkinter.filedialog import askdirectory
from lxml import etree
import os

print("[INFO] Select label source directory")
Tk().withdraw()
sourcedir = askdirectory()
print(sourcedir)
os.chdir(sourcedir)

class0 = 0
class1 = 0

for f in os.listdir(): 
    f_name, f_ext = os.path.splitext(f)
        
    if f_ext == '.txt':
        print("[INFO] Counting labels in ", f)
        file = open(f, 'r')
        while True:
            line = file.readline()
            if not line:
                break
            if line[0] == '0':
                class0 = class0 + 1
            elif line[0] == '1':
                class1 = class1 + 1

print("[INFO] Total number class0: ", class0)
print("[INFO] Total number class1: ", class1)
print("[INFO] Finished directory, exiting")
