import cv2 as cv 
from main import grayscale, binary_convert


image = cv.imread("pics/Desert.jpg", -1)

def show_image():
  cv.imshow("image", image)
  cv.waitKey(0)
  cv.destroyAllWindows()

grayscale(image)
show_image()

binary_convert(image, 60)
show_image()
