from utils import show_image
from math import gcd, sqrt


def get_size(x, y):
    lcm = x * y // gcd(x, y)
    size = (x * y) // lcm

    a = size
    curr_a = a
    while True:
        if a == int(a):
            curr_a = a
            a = sqrt(a)
        else:
            return int(curr_a)


def pixilate(image, scale=1):
    size = get_size(image.shape[0], image.shape[1]) * scale

    for row in range(0, image.shape[0], size):
        for col in range(0, image.shape[1], size):

            total_color = [0, 0, 0]

            pixels_run = 0
            for x in range(size):
                for y in range(size):
                    try:
                        current_color = image[row + x][col + y]
                        total_color = [
                            total_color[i] + current_color[i] for i in range(3)
                        ]
                        pixels_run += 1
                    except IndexError:
                        break

            # populate pixels
            average_color = [c // pixels_run for c in total_color]
            for _x in range(size):
                for _y in range(size):
                    try:
                        image[row + _x][col + _y] = average_color
                    except IndexError:
                        break


if __name__ == "__main__":
    import cv2 as cv

    image = cv.imread("pics/Desert.jpg", -1)

    pixilate(image, scale=2)
    show_image(image)
