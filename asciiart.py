import os 
import sys
import cv2
from PIL import Image

# Ascii characters used to create the output 
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resized_image(image, new_width=310):
    new_height = int(85)
    resized_image = image.resize((new_width,new_height))
    return(resized_image)

def grayscaling(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)

def pix2chars(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return(characters)

def generate_frame(image,new_width=310):
    new_image_data = pix2chars(grayscaling(resized_image(image)))
    total_pixels = len(new_image_data)
    ascii_image = "\n".join(new_image_data[index:(index+new_width)] for index in range(0, total_pixels, new_width))
    print(ascii_image)



#cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cap = cv2.VideoCapture("video.mp4")

if cap.isOpened():
    ret, frame = cap.read()
else:
    ret = False

while True:
    ret,frame = cap.read()
    cv2.imshow("frame",frame)
    generate_frame(Image.fromarray(frame))
    cv2.waitKey(2)
