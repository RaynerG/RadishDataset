from tkinter import Tk
from tkinter.filedialog import askdirectory
import os
import cv2 , msvcrt, random, shutil

print("[INFO] Select source directory")
Tk().withdraw()
sourcedir = askdirectory()
print(sourcedir)
os.chdir(sourcedir)

list = os.listdir()
num_files = len(list)

num_instances = num_files/2
if (num_instances / num_instances) != 1: 
    print("[INFO] Incorrect number of files in dir, exiting")
    exit(1)

# print(list)
count = 0
new_list = []
for i in list: 
    i_name, i_ext = os.path.splitext(i)
    if i_ext == '.jpg':
        new_list.append(i_name)
    if i_ext == '.txt':
        in_file = open(i,"r")
        num = len(in_file.readlines())
        count = count + num

random.shuffle(new_list)

print("[INFO] Number of instances in dir is %d" %count )

while True:
    size = input("[INFO] Enter number of instances desired in train dir: ")
    if int(size) > 0.6*count:
        print("[INFO] proportion greater than 60% of dataset chosen, try again")
    else: break

print("[INFO] Select image destination directory")
Tk().withdraw()
dest = askdirectory()
print(dest)
print("[INFO] Creating train, validate and test dirs in chosen dir")


imtraindir = dest + '/train'
os.mkdir(imtraindir)
imvaldir = dest + '/valid'
os.mkdir(imvaldir)
imtestdir = dest + '/test'
os.mkdir(imtestdir)

print("[INFO] Select label destination directory")
Tk().withdraw()
ldest = askdirectory()
print(ldest)
print("[INFO] Creating train, validate and test dirs in chosen dir")


lbltraindir = ldest + '/train'
os.mkdir(lbltraindir)
lblvaldir = ldest + '/valid'
os.mkdir(lblvaldir)
lbltestdir = ldest + '/test'
os.mkdir(lbltestdir)

n = 0
for i in range(len(new_list)):
    if i%5 <= 2:
        in_file = open(sourcedir + '/' + new_list[i] + '.txt',"r")
        n = n + len(in_file.readlines())
        shutil.copyfile(sourcedir + '/' + new_list[i] + '.txt', lbltraindir + '/' + str(i).zfill(3) + '.txt')
        shutil.copyfile(sourcedir + '/' + new_list[i] + '.jpg', imtraindir + '/' + str(i).zfill(3) + '.jpg')
    elif i%5 == 3:
        shutil.copyfile(sourcedir + '/' + new_list[i] + '.txt', lblvaldir + '/' + str(i).zfill(3) + '.txt')
        shutil.copyfile(sourcedir + '/' + new_list[i] + '.jpg', imvaldir + '/' + str(i).zfill(3) + '.jpg')
    elif i%5 == 4:
        shutil.copyfile(sourcedir + '/' + new_list[i] + '.txt', lbltestdir + '/' + str(i).zfill(3) + '.txt')
        shutil.copyfile(sourcedir + '/' + new_list[i] + '.jpg', imtestdir + '/' + str(i).zfill(3) + '.jpg')
    if n > int(size): break

print("[INFO] Program finished, exiting")