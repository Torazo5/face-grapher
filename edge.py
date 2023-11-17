from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = r"torazo3.jpg"
original_image = Image.open(image_path).convert("L")  # Convert to grayscale

# Calculate the new size while preserving the aspect ratio
original_width, original_height = original_image.size
aspect_ratio = original_width / original_height
new_height = 50  # Set the desired height
new_width = int(new_height * aspect_ratio)

# Resize the image to the new size
low_quality_image = original_image.resize((new_width, new_height))

# Convert the resized image to a NumPy array
low_quality_array = np.array(low_quality_image)

# Define the 3x3 edge detector kernel
kernel = np.array([[-1, -1, -1],
                   [-1,  9, -1],
                   [-1, -1, -1]])

# Perform convolution manually
result_image_array = np.zeros_like(low_quality_array)

for i in range(1, low_quality_array.shape[0] - 1):
    for j in range(1, low_quality_array.shape[1] - 1):
        result_image_array[i, j] = np.sum(low_quality_array[i-1:i+2, j-1:j+2] * kernel)

# Clip the values to the valid range [0, 255]
result_image_array = np.clip(result_image_array, 0, 255)

# Convert the result array back to an image
result_image = Image.fromarray(result_image_array.astype(np.uint8))

# Display the resulting edge-detected image from the low-quality input
plt.imshow(result_image, cmap='gray')
plt.title('Edge Detection Result (Low Quality)')

# Create a scatter plot with green dots for white pixels and red dots for non-white pixels
height, width = result_image_array.shape
y_coords, x_coords = np.where(result_image_array > 255 * 0.8)  # Choose a threshold for white pixels

plt.scatter(x_coords, y_coords, color='green', marker='o', s=5)  # Green dots for white pixels

# Scatter red dots for non-white pixels
y_coords, x_coords = np.where(result_image_array <= 255 * 0.8)
plt.scatter(x_coords, y_coords, color='red', marker='o', s=5)

plt.axis('off')
plt.show()
