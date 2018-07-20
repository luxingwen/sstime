#!/usr/bin/python
# -*- coding: UTF-8 -*-


import tkinter
import time
from PIL import Image,ImageTk


def resize( w_box, h_box, pil_image): #参数是：要适应的窗口宽、高、Image.open后的图片
  w, h = pil_image.size #获取图像的原始大小   
  f1 = 1.0*w_box/w 
  f2 = 1.0*h_box/h    
  factor = min([f1, f2])   
  width = int(w*factor)    
  height = int(h*factor)    
  return pil_image.resize((width, height), Image.ANTIALIAS)   

main = tkinter.Tk()
main.title("甩甩日期转换")
now1 = time.time()
es = tkinter.StringVar()
entry = tkinter.Entry(main, textvariable= es)
es.set(str(round(now1)))
entry.pack()

def resetnowtime():
	global now1
	now1 = time.time()
	es.set(str(round(now1)))

def transtime():
	format_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(float(es.get())))
	e2s.set(format_time)

def strtranstime():
	ts = time.strptime(e2s.get(), "%Y-%m-%d %H:%M:%S")
	e3s.set(round(time.mktime(ts)))

b = tkinter.Button(main, text = "获取当前时间戳", command = resetnowtime)
b.pack()
e2s =  tkinter.StringVar()
e2 = tkinter.Entry(main, textvariable = e2s)
e2.pack()
b1 = tkinter.Button(main, text = "时间戳转换", command = transtime)
b1.pack()
e3s = tkinter.StringVar()
e3 = tkinter.Entry(main, textvariable = e3s)
e3.pack()
b2 = tkinter.Button(main, text = "转换时间戳", command = strtranstime)
b2.pack()
im=Image.open("bg.png")
img = resize(200,200, im)
img1=ImageTk.PhotoImage(img)
tkinter.Label(main, image = img1, width = 200, height = 200).pack()
main.mainloop()