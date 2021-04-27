import cv2

import numpy as np
import glob
import json
import math 
from math import radians, cos, sin, asin, sqrt
import os
from scipy import ndimage
from PIL import Image, ImageEnhance
import random

path=os.getcwd()
print(path)
jpegs = sorted(glob.glob(path+"\\*.png"))
path2=path+"\\colored\\"
print(jpegs)
print('agfafgafgs')
nf=0
lent=len(jpegs)
while nf<lent:

 im=cv2.imread(jpegs[nf],0)
 basename=os.path.basename(jpegs[nf])
 # grab the image dimensions
 h = im.shape[0]
 w = im.shape[1]


 base1=np.zeros((h,w,3),np.uint8)   
    # loop over the image, pixel by pixel
 for y in range(0, h):
        for x in range(0, w):
           val=im[y,x]
          
           if val==0:
            base1[y,x]=[0,0,0]
           if val==1:
            base1[y,x]=[0,0,255]
           if val==2:
            base1[y,x]=[0,255,0]
           if val==3:
            base1[y,x]=[255,0,0]
           # base1[y,x]=[0,0,255]
# jpegs2 = sorted(glob.glob(path2+"*.png"))
# jpegs3 = sorted(glob.glob(path3+"*.png"))
# jpegs4 = sorted(glob.glob(path4+"*.png"))
 nf+=1
# im_v = cv2.imread(jpegs[0])

# i=random.sample(range(70), 5)

# lent=len(jpegs)
# z=1
# im_vs=[]
# for nf in i:
 # basename = os.path.basename(jpegs[nf])
 # basename2=basename[:-4]+".png"
 # basename=basename[:-4]+"_pre.png"
 
 # print(basename)
 # imgs = cv2.imread(jpegs[nf])
 # print(path2+basename)
 # imgs2 = cv2.imread(path2+basename2)
 # #cv2.imshow("asdsad",imgs2)
 # imgs2 = cv2.addWeighted(imgs,0.7,imgs2,0.3,0)
 # im_v = cv2.hconcat([imgs, imgs2])
 # imgs3 = cv2.imread(path3+basename)
 # imgs3 = cv2.addWeighted(imgs,0.7,imgs3,0.3,0)
 # im_v = cv2.hconcat([im_v, imgs3])
 # imgs4 = cv2.imread(path4+basename)
 # imgs4 = cv2.addWeighted(imgs,0.7,imgs4,0.3,0)
 # im_v = cv2.hconcat([im_v, imgs4])
 # im_vs.append(im_v)
# imk=im_vs[0]
# p=0
# for x in im_vs:

 # if p==0:
  # p+=1
  # continue
 # imk = cv2.vconcat([imk, x])
 if os.path.exists(path2)is False:
	  os.makedirs(path2)
 cv2.imwrite(path2+basename,base1)

