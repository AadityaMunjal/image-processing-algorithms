import cv2 as cv


def show_image(img):
    cv.imshow("image", img)
    cv.waitKey(0)
    cv.destroyAllWindows()
