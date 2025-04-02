"""
This script extracts a hidden message from an image by analyzing black pixels in each column.
"""

import os
from PIL import Image  # Ensure `Pillow` is installed: `pip install pillow`

def remember_remember(image_path):
    """
    Extracts a hidden message from an image by detecting black pixels.

    :param image_path: Path to the image file.
    :return: Decoded message as a string.
    """
    image = Image.open(image_path).convert("L")  # Convert to grayscale
    width, height = image.size  # Get image dimensions
    decoded_message = ""

    # Iterate through the columns of the image
    for col in range(width):
        # Find the row where the pixel is black
        for row in range(height):
            pixel_value = image.getpixel((col, row))  # Get grayscale pixel value
            if pixel_value == 1:  # Black pixel
                decoded_message += chr(row)  # Convert row index to character
                break  # Move to next column

    return decoded_message

if __name__ == '__main__':
    RELATIVE_PATH = "Notebooks/content/week06/resources/code.png"  # Relative path
    FULL_PATH = os.path.abspath(RELATIVE_PATH)  # Convert to absolute path
    print(remember_remember(FULL_PATH))
