import cv2
import numpy as np
import matplotlib.pyplot as plt

imgpath = "torazo6.jpg"
img = cv2.imread(imgpath, cv2.IMREAD_GRAYSCALE)  # Convert to grayscale

# Resize the image to a lower quality
new_height = 1000
aspect_ratio = img.shape[1] / img.shape[0]
new_width = int(new_height * aspect_ratio)
resized_img = cv2.resize(img, (new_width, new_height))

# Apply Gaussian blur
blurred_img = cv2.GaussianBlur(resized_img, (5, 5), 0)  # You can adjust the kernel size (e.g., (5, 5)) and standard deviation (e.g., 0)

edgesx = cv2.Sobel(blurred_img, -1, dx=1, dy=0, ksize=1)
edgesy = cv2.Sobel(blurred_img, -1, dx=0, dy=1, ksize=1)

# Calculate the magnitude of edges using Euclidean distance
edges_magnitude = np.sqrt(edgesx**2 + edgesy**2)

# Increase sensitivity by multiplying by a constant factor (e.g., 2)
sensitive_edges = edges_magnitude * 2


plt.imshow(sensitive_edges, cmap='gray')
plt.show()
