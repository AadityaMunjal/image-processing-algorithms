from utils import show_image


def binary_convert(image, threshold: int = 85):
    threshold *= 3
    for row in range(image.shape[0]):
        for col in range(image.shape[1]):
            colorsum = sum(image[row][col][i] for i in range(3))

            if colorsum > threshold:
                image[row][col] = [255, 255, 255]
            else:
                image[row][col] = [0, 0, 0]


if __name__ == "__main__":
    import cv2 as cv

    image = cv.imread("pics/Desert.jpg", -1)

    binary_convert(image)
    show_image(image)
