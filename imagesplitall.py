import numpy as np
import matplotlib
import os
from PIL import Image

imgsdir = "D:\\1091\\paper\\dataprocesscode\\DATA1029"
spimgdir = "D:\\1091\\paper\\dataprocesscode\\split"
 
def img_seg(dir):
    files = os.listdir(dir)
    for file in files:
        a, b = os.path.splitext(file) #a: filename(1,2,3) b:filetype(jpg)
        img = Image.open(os.path.join(dir + "\\" + file))
        width, hight = img.size
        print("*********")
        w = 640
        id = 1
        rename = "D:\\1091\\paper\\dataprocesscode\\split\\"
        #如果是垂直圖片
        if(hight>1500):
            xmin = 0 
            ymin = 0
            xmax = w
            ymax = w
            new_img = img.crop((xmin,ymin,xmax,ymax))
            new_img.save(rename + a + "_" + str(id) + b)
            id+=1
            xmin = width-w 
            ymin = 0
            xmax = width
            ymax = w
            new_img = img.crop((xmin,ymin,xmax,ymax))
            new_img.save(rename + a + "_" + str(id) + b)
            id+=1
            xmin = 0
            ymin = hight - w
            xmax = w
            ymax = hight
            new_img = img.crop((xmin,ymin,xmax,ymax))
            new_img.save(rename + a + "_" + str(id) + b)
            id+=1
            xmin = width-w
            ymin = hight-w
            xmax = width
            ymax = hight
            new_img = img.crop((xmin,ymin,xmax,ymax))
            new_img.save(rename + a + "_" + str(id) + b)
            id+=1
            print(a,b,"done")
        #如果是水平圖片
        else:
            xmin = 0 
            ymin = 0
            xmax = w
            ymax = w
            new_img = img.crop((xmin,ymin,xmax,ymax))
            new_img.save(rename + a + "_" + str(id) + b)
            id+=1
            xmin = 0
            ymin = hight - w
            xmax = w
            ymax = hight
            new_img = img.crop((xmin,ymin,xmax,ymax))
            new_img.save(rename + a + "_" + str(id) + b)
            id+=1
            xmin = width - w
            ymin = 0
            xmax = width
            ymax = w
            new_img = img.crop((xmin,ymin,xmax,ymax))
            new_img.save(rename + a + "_" + str(id) + b)
            id+=1
            xmin = width - w
            ymin = hight - w
            xmax = width
            ymax = hight 
            new_img = img.crop((xmin,ymin,xmax,ymax))
            new_img.save(rename + a + "_" + str(id) + b)
            id+=1
            print(a,b,"done")
 
 
if __name__ == '__main__':
    path = imgsdir
    img_seg(path)