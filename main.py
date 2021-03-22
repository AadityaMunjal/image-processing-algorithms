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

def convert_to_ascii(image, invert=False):
  import cv2 as cv
  image = cv.resize(image, (0, 0), fx=0.1, fy=0.1) 
  newImage = "\n"
  print(newImage)
  asciiChars = [" ", ".", ";", "/", "$", "#", "@"] # ascending 

  color_step_threshold = 255 // len(asciiChars)

  for col in range(image.shape[0]):
    for row in range(image.shape[1]):
      color_avg = sum(image[col][row][i] for i in range(3)) // 3

      for i in range(len(asciiChars)):
        if color_avg < color_step_threshold * i:
          if invert:
            symbol = asciiChars[-i-1]
          else:
            symbol = asciiChars[i-1]
          break
        else: 
          symbol = asciiChars[0]

      newImage += symbol
    newImage += "\n"

  return newImage