import cv2 as cv
import numpy as np

# Load the image
image_path = 'torazotext.jpg'
frame = cv.imread(image_path)

# Check if the image is loaded successfully
if frame is None:
    print("Error: Could not open or read the image.")
    exit()

#cv.imshow('Original Image', frame)

# Laplacian edge detection
laplacian = cv.Laplacian(frame, cv.CV_64F)
laplacian = np.uint8(np.abs(laplacian))
#cv.imshow('Laplacian', laplacian)

# Canny edge detection
edges = cv.Canny(frame, 150, 150)
cv.imshow('Canny', edges)

cv.waitKey(0)
cv.destroyAllWindows()
