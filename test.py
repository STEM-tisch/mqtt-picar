import cv2
#import matplotlib.p as plt
import logging

def show_img(image):
    cv2.imshow("Image", image)

def open_img(path):
    
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

def main():
    fname = ""
    fname = input("Please enter file name: ")
    fname = fname + ".jpg"
    print ("File name {}".format(fname))
    open_img(fname)
    show_img(fname)

if __name__ =="__main__":
    main()

