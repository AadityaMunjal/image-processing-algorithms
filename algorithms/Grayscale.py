from utils import show_image


def grayscale(image):
    for row in range(image.shape[0]):
        for col in range(image.shape[1]):
            avg = sum(image[row][col][i] for i in range(3)) // 3
            image[row][col] = [avg for _ in range(3)]


if __name__ == "__main__":
    import cv2 as cv

    image = cv.imread("pics/Desert.jpg", -1)

    grayscale(image)
    show_image(image)
