#!/usr/bin/env python

# Code for the WeedLogger camera rig 
# Designed for use on the Raspian Raspberry Pi operating system
# Author: Gilbert Rayner, gilbertrayner99@gmail.com
# Date: September 2021

import time, datetime, threading, os
import tkinter as tk
import tkinter.font as tkFont
#from tkinter.tkk import *

from picamera import PiCamera
from time import sleep	

LOCATION_OPTIONS = [
"camden",
"greenacres"
]

CROP_OPTIONS = [
"wheat",
"canola",
"beans"
]

WEED_OPTIONS = [
"radish1",
"radish2",
"ryegrass"
]

ANGLE_OPTIONS = [
"0",
"30",
"45",
"60"
]
			
class Application:
    def __init__(self):
        self.camera = PiCamera()
        self.camera.resolution = (3200,2400)

        self.location = 'default'
        self.crop = 'default'
        self.weed = 'default'
        self.angle = 'default'
        self.img_name = 'none'

        """ SET UP SAVE PATH """
        try:
            name = os.listdir('/media/pi')[0]
            output_root = '/media/pi/' + name
        except:
            print("Storing in hard drive")
            output_root = "home/pi/Desktop"
        ts = datetime.datetime.now()
        self.output_path = output_root + '/' + ts.strftime("%Y%m%d") + ts.strftime("-%H%M")
        print(self.output_path)
        os.mkdir(self.output_path)
        f = open( (self.output_path + "/description.txt"), "a+")
        f.write( input("Enter description: ") )
        f.close()

        """ SET UP ROOT WINDOW """ 
        self.root = tk.Tk()
        self.root.title('Run WeedLogger')
        self.root.geometry("800x600")
        self.root.protocol('WM_DELETE_WINDOW',self.destructor)

        """ SET FONT """
        self.helv12 = tkFont.Font(family='Helvetica',size=12,weight=tkFont.BOLD)

        """ SET UP FRAMES IN WINDOW """
        self.control_frame = tk.Frame(self.root, bg='#c4ffd2',width=100,height=800)
        self.control_frame.pack(side=tk.RIGHT)

        self.pic_frame = tk.Frame(self.root,bg='grey',width=500,height=800)
        self.pic_frame.pack()

        """ SET UP CONTROL BUTTONS """
        btn_cap = tk.Button(self.control_frame,text='CAPTURE',command=self.take_snapshot,\
            width=10,height=7,bg='green',fg='white',font=self.helv12)
        btn_cap.pack(side=tk.TOP,padx=2,pady=2)

        btn_new = tk.Button(self.control_frame,text='NEW',command=self.set_params,\
            width=10,height=6,bg='green',fg='black',font=self.helv12)
        btn_new.pack(padx=2,pady=2)

        btn_exit = tk.Button(self.control_frame,text='EXIT',command=self.destructor,\
            width=10,height=5,bg='red',fg='black',font=self.helv12)
        btn_exit.pack(padx=2,pady=2)

        btn_pres = tk.Button(self.control_frame,text='PRE SHORT',command=self.preview_short,\
            width=10,height=5,bg='yellow',fg='black',font=self.helv12)
        btn_pres.pack(padx=2,pady=2)

        btn_prel = tk.Button(self.control_frame,text='PRE LONG',command=self.preview_long,\
            width=10,height=5,bg='yellow',fg='black',font=self.helv12)
        btn_prel.pack(padx=2,pady=2)

        """ SET UP PARAMETERS """
        self.newWindow = None
        self.set_params()


    def take_snapshot(self):
        ts = datetime.datetime.now()
        filename = "{}.jpg".format(self.img_name + ts.strftime("_%Y%m%d_%H-%M-%S"))
        last_path = os.path.join(self.output_path, filename)
        self.camera.capture(last_path)
        print("[INFO] saved " + last_path)


    def preview_short(self):
        self.camera.start_preview()
        time.sleep(2)
        self.camera.stop_preview()

    def preview_long(self):
        self.camera.start_preview()
        time.sleep(10)
        self.camera.stop_preview()

    def set_params(self):
        print("[INFO] setting up new parameters")
        self.newWindow = tk.Toplevel(self.root)
        self.newWindow.tkraise()
        self.newWindow.geometry("300x500")
        self.newWindow.title('Set parameters')

        location = 'new'
        crop = 'new'
        weed = 'new'
        angle = 'new'

        """ SET UP DROPDOWN MENUS """
        #style = tkk.Style()
        #style.configure('ParamMenuButton',font=('helvetica',12,'bold'))
        
        location = tk.StringVar(self.newWindow)
        location.set(LOCATION_OPTIONS[0])
        menu_location = tk.OptionMenu(self.newWindow,location,*LOCATION_OPTIONS)#, *[None],style='ParamMenuButton')
        menu_location.pack(side=tk.TOP,fill=tk.X,pady=10)

        crop = tk.StringVar(self.newWindow)
        crop.set(CROP_OPTIONS[0])
        menu_crop = tk.OptionMenu(self.newWindow,crop,*CROP_OPTIONS)#, *[None],style='ParamMenuButton')
        menu_crop.pack(side=tk.TOP,fill=tk.X,pady=10)

        weed = tk.StringVar(self.newWindow)
        weed.set(WEED_OPTIONS[0])
        menu_weed = tk.OptionMenu(self.newWindow,weed,*WEED_OPTIONS)#, *[None],style='ParamMenuButton')
        menu_weed.pack(side=tk.TOP,fill=tk.X,pady=10)

        angle = tk.StringVar(self.newWindow)
        angle.set(ANGLE_OPTIONS[0])
        menu_angle = tk.OptionMenu(self.newWindow,angle,*ANGLE_OPTIONS)#, *[None],style='ParamMenuButton')
        menu_angle.pack(side=tk.TOP,fill=tk.X,pady=10)

        """ SET UP CONTROL BUTTONS """
        btn_ok = tk.Button(self.newWindow, text='OKAY', 
            command=lambda: self.param_ok(location,crop,weed,angle),
            width=10,height=5,bg='green',fg='white',font=self.helv12)
        btn_ok.pack(padx=2,pady=2)

        btn_cancel = tk.Button(self.newWindow, text='CANCEL', command=self.param_cancel,
            width=10,height=5,bg='red',fg='white',font=self.helv12)
        btn_cancel.pack(padx=2,pady=2)

    def param_ok(self, location,crop,weed,angle):
        #self.location = location.get()
        #self.crop = crop.get()
        #self.weed = weed.get()
        #self.angle = angle.get()
        # TODO add updating of list order based on previous input
        self.img_name = location.get() + '_' + crop.get() + '_' + weed.get() + '_' + angle.get()
        print(self.img_name)
        self.camera.start_preview()
        sleep(5)
        self.camera.stop_preview()
        self.newWindow.destroy()

    def param_cancel(self):
        self.newWindow.destroy()

    def destructor(self):
        print("[INFO] closing")
        if(self.newWindow):
            self.newWindow.destroy()
        self.root.destroy()




def main():
    print("[INFO] starting GUI ...")
    app = Application()
    app.root.mainloop()

if __name__ == "__main__":
    main()
