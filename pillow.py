# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 17:18:58 2019

@author: Artemis
"""

from PIL import Image

IMAGE_PATH = r'data/Lisa.jpg'
CHAR_PATH = r'output/Lisa.txt'
ASCII_CHAR = list("$%_&WM#*oahkbdpqwmZO0QLCJUYXzcvunxr\jft/\|()1{}[]?-/+@<>i!;:,\"^`'. ")

"""
Argument:
IMAGE_PATH - The path of an input image.
CHAR_PATH - The path of a .txt file(output).
ASCII_CHAR - The element of the char image.
"""                  
                  
class CharImage(object):
    """
    Represents a char image.
    """
    def __init__(self):
        pass
        
    def __read_image(self, image_path):
        """
        Reads an image.
        Takes the path of the image, and returns the object Image
        """
        try:
            image = Image.open(image_path)
        except FileNotFoundError:
            print("Check out the image path.")
        else:
            return image
        
    def __get_char(self, r, b, g, alpha=256):
        """
        Calculates the char.
        Takes the data of the image, and returns the char of every point in the image.
        """
        if alpha == 0:
            return ' '
        gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
        unit = 256 / len(ASCII_CHAR)
        return ASCII_CHAR[int(gray//unit)]
    
    def main(self, image_path):
        image = self.__read_image(image_path)
        width, height = 100, 60
        image = image.resize((width, height))
        text = ""
        for i in range(height):
            for j in range(width):
                text += self.__get_char(*image.getpixel((j, i)))
            text += '\n'
        pic_char = open(CHAR_PATH, "w")
        pic_char.write(text)
        pic_char.close()
        
if __name__ == '__main__':
    im = CharImage()
    im.main(IMAGE_PATH)