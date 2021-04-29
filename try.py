import cv2 as cv 
from algorithms.Binary_Convert import binary_convert
from algorithms.Grayscale import grayscale
from algorithms.Convert_to_ASCII import convert_to_ascii
from algorithms.Invert import invert


image = cv.imread("pics/Desert.jpg", -1)

def show_image(img):
  cv.imshow("image", img)
  cv.waitKey(0)
  cv.destroyAllWindows()

grayscale(image)
show_image(image)

binary_convert(image, 60)
show_image(image)

image = cv.imread("pics/Chrysanthemum.jpg")

image = convert_to_ascii(image)
print(image)

invert(image)
show_image(image)