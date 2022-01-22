from utils import show_image


def invert(image):
    for row in range(image.shape[0]):
        for col in range(image.shape[1]):
            for c in range(3):
                image[row][col][c] = -image[row][col][c]


if __name__ == "__main__":
    import cv2 as cv

    image = cv.imread("pics/sample_image.jpg", -1)

    invert(image)
    show_image(image)
