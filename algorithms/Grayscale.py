def grayscale(image):
  for row in range(image.shape[0]):
    for col in range(image.shape[1]):
      avg = sum(image[row][col][i] for i in range(3)) // 3
      image[row][col] = [avg for _ in range(3)]
