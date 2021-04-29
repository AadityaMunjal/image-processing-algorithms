def invert(image):
  for row in range(image.shape[0]):
    for col in range(image.shape[1]):
      for c in range(3):
        image[row][col][c] = -image[row][col][c]
        