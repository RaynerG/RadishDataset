from tkinter import Tk
from tkinter.filedialog import askdirectory
import os

print("[INFO] Select label source directory")
Tk().withdraw()
sourcedir = askdirectory()
print(sourcedir)
os.chdir(sourcedir)

for f in os.listdir(): 
    f_name, f_ext = os.path.splitext(f)
        
    if f_ext == '.txt':
        file = open(f, 'r+')
        writethis = ""
        while True:
            line = file.readline()
            if not line:
                break
            writethis = writethis + str(int(0)) + line[1:]  # <-- changes all labels to class "0" (yolo format)
            print( writethis )
        file.seek(0)
        file.write(writethis)
        file.truncate()
        file.close()




print("[INFO] Finished directory, exiting")