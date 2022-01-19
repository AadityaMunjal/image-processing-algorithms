from utils import show_image


def half_mirrorImage(image):
    for row in range(image.shape[0]):
        for col in range(image.shape[1]):

            if row <= image.shape[0] // 2 and col <= image.shape[1] // 2:
                pass
            else:
                if row >= image.shape[0] // 2:
                    amount = (row - image.shape[0] // 2) * 2
                    image[row][col] = image[row - amount][col]


if __name__ == "__main__":
    import cv2 as cv

    image = cv.imread("pics/Desert.jpg", -1)

    half_mirrorImage(image)
    show_image(image)
