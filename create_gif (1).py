from PIL import Image
import imageio.v3 as iio
import numpy as np
import glob

def resize_image(image, target_size):
    """Resize image to target size while maintaining aspect ratio"""
    aspect_ratio = image.width / image.height
    if aspect_ratio > 1:
        # Width is larger, so scale based on width
        new_width = target_size
        new_height = int(target_size / aspect_ratio)
    else:
        # Height is larger or equal, so scale based on height
        new_height = target_size
        new_width = int(target_size * aspect_ratio)
    
    resized_image = image.resize((new_width, new_height), Image.LANCZOS)
    
    # Create a new image with the target size and paste the resized image
    new_image = Image.new("RGB", (target_size, target_size), (0, 0, 0))
    paste_x = (target_size - new_width) // 2
    paste_y = (target_size - new_height) // 2
    new_image.paste(resized_image, (paste_x, paste_y))
    
    return new_image

# Set target size for all images
TARGET_SIZE = 500  # You can adjust this value

# Collect filenames
image_extensions = ["*.png", "*.jpeg", "*.jpg"]
filenames = []
for extension in image_extensions:
    filenames.extend(glob.glob(extension))
filenames.sort()

# Load and resize images
images = []
for filename in filenames:
    image = Image.open(filename)
    resized_image = resize_image(image, TARGET_SIZE)
    images.append(resized_image)

# Create transition images
transition_images = []
for i in range(len(images) - 1):
    for alpha in np.linspace(0, 1, 10):
        blended = Image.blend(images[i], images[i+1], alpha)
        transition_images.append(np.array(blended))

# Convert original images to numpy arrays
arrayed_images = [np.array(image) for image in images]

# Combine original and transition images
final_images_with_transitions = []
for i in range(len(arrayed_images) - 1):
    final_images_with_transitions.append(arrayed_images[i])
    final_images_with_transitions.extend(transition_images[i*10:(i+1)*10])

final_images_with_transitions.append(arrayed_images[-1])

# Create GIF
iio.imwrite("output.gif", final_images_with_transitions, duration=150, loop=0)
