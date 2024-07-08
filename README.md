# Image to GIF Animator

## Description
This Python script creates a smooth GIF animation from a series of images. It's a beginner-friendly project that demonstrates basic image processing and animation techniques using Python.

## Features
- Automatically detects and loads image files from the current directory
- Supports PNG, JPEG, and JPG image formats
- Creates smooth transitions between images
- Generates a GIF animation from the processed images

## Requirements
- Python 3.x
- Pillow (PIL Fork)
- imageio
- numpy

## Installation
1. Clone this repository:
git clone https://github.com/yourusername/image-to-gif-animator.git

2. Install the required packages:
pip install pillow imageio numpy


## Usage
1. Place your image files in the same directory as the script.
2. Run the script:
python image_to_gif.py

3. The script will generate an `output.gif` file in the same directory.

## How it Works
1. The script finds all image files in the current directory.
2. It loads these images using PIL (Python Imaging Library).
3. Transition frames are created between each pair of images.
4. Original images and transitions are combined into a sequence.
5. Finally, it generates a GIF from this sequence.

## Limitations
- Currently, the script processes all images in the directory. Be cautious with large numbers of images.
- The transition effect is a simple blend. More advanced effects could be implemented.

## Future Improvements
- Add command-line arguments for customization (e.g., output filename, transition frames)
- Implement error handling for various edge cases
- Add support for more image formats

## Contributing
This is a learning project, but contributions or suggestions are welcome! Feel free to fork the repository and submit pull requests.

## Acknowledgments
This project was created as part of my learning journey with Codedex. Special thanks to the Codedex community for their support and inspiration.
