import cv2
import matplotlib.pyplot as plt

imgpath = "torazo3.jpg"
img = cv2.imread(imgpath, cv2.IMREAD_GRAYSCALE)  # Convert to grayscale

# Resize the image to a lower quality
new_height = 300
aspect_ratio = img.shape[1] / img.shape[0]
new_width = int(new_height * aspect_ratio)
resized_img = cv2.resize(img, (new_width, new_height))

edgesx = cv2.Sobel(resized_img, -1, dx=1, dy=0, ksize=1)
edgesy = cv2.Sobel(resized_img, -1, dx=0, dy=1, ksize=1)
edges = edgesx + edgesy

output = [edges]
titles = ['Edges']

plt.imshow(output[0], cmap='gray')
plt.title(titles[0])
plt.xticks([])
plt.yticks([])

plt.show()
