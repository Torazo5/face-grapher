import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def create_color_graph(image_array, block_size):
    height, width, _ = image_array.shape
    graph = []

    for i in range(0, height, block_size):
        for j in range(0, width, block_size):
            block_color = np.mean(image_array[i:i+block_size, j:j+block_size], axis=(0, 1))
            graph.append([i, j, *block_color])

    return np.array(graph)

def plot_color_graph(color_graph, image_shape, block_size):
    plt.scatter(color_graph[:, 1], color_graph[:, 0], c=color_graph[:, 2:] / 255.0, marker='.', s=block_size**2)
    plt.axis('off')
    plt.gca().set_aspect('equal', adjustable='box')  # Ensure equal aspect ratio
    plt.xlim(0, image_shape[1])
    plt.ylim(image_shape[0], 0)  # Flip y-axis to match image orientation
    plt.show()

# Example usage
image_path = '94224_video_512x512.png'
block_size = 8

# Read the image as a NumPy array
image_array = np.array(Image.open(image_path))

# Create the color graph with each dot representing a 2x2 block
color_graph = create_color_graph(image_array, block_size)

# Plot the color graph
plot_color_graph(color_graph, image_array.shape[:2], block_size)
