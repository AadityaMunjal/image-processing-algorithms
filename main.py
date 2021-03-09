def binary_convert(image, threshold: int):
  threshold *= 3
  for row in range(image.shape[0]):
    for col in range(image.shape[1]):
      colorsum = sum(image[row][col][i] for i in range(3))

      if colorsum > threshold:
        image[row][col] = [255, 255, 255]
      else:
        image[row][col] = [0, 0, 0]

def grayscale(image):
  for row in range(image.shape[0]):
    for col in range(image.shape[1]):
      avg = sum(image[row][col][i] for i in range(3)) // 3
      image[row][col] = [avg for _ in range(3)]
      