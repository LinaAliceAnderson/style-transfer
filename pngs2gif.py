import os
import re
from PIL import Image

def create_gif(input_folder, output_file):
    images = []
    # Get all the PNG files in input_folder
    png_files = [file for file in os.listdir(input_folder) if file.endswith('.png')]
    # Sort the files by name
    png_files.sort(key=lambda x: int(re.findall(r'\d+', x)[0]))

    # Read each PNG file and append it to the list of images
    for png_file in png_files:
        image_path = os.path.join(input_folder, png_file)
        img = Image.open(image_path)
        images.append(img)
    
    # Save the images as a GIF file (every frame gets 250 ms of display time, loop indefinitely)
    images[0].save(output_file, save_all=True, append_images=images[1:], duration=250, loop=0)

# Usage example:
input_folder = '.'
output_file = 'output.gif'
create_gif(input_folder, output_file)
