import os
from PIL import Image
def remember_remember(image_path):
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
    relative_path = "Notebooks/content/week06/resources/code.png"  # relative path
    full_path = os.path.abspath(relative_path)  # Convert to absolute path
    print(remember_remember(full_path))