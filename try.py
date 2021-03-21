import cv2 as cv 
from main import grayscale, binary_convert, convert_to_ascii 


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