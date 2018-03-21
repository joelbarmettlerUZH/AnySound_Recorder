import pyscreenshot as ImageGrab
import numpy as np
import cv2
import win32api
from PIL import Image
from pytesseract import *
from time import time
import random

class ScreenInfo:
    def __init__(self, coordinates):
        # Define the box where the screenshot shall be taken
        self._coordinates = tuple(coordinates)
        self._image = self.grabImage()
        self._text = self.imgToText(self._image)

    # Static method that returns the current cursor position
    @staticmethod
    def getCoordinates():
        return win32api.GetCursorPos()

    # Takes a new screenshot and extracts the text. Returns whether image text changed in comparison to old one
    def update(self):
        img = self.grabImage()
        txt = self.imgToText(img)
        if txt != self._text:
            self._image = img
            self._text = txt
            return True
        return False

    def getText(self):
        # Return unknown text as unknown + random ID to not overwrite old one
        if not self._text:
            self._text = "Unknown - "+str(random.randint(10000,100000))
        return self._text.replace("\n"," - ")

    # Returns Image converted to RGB in order to make it easily displayable
    def getImage(self):
        return cv2.cvtColor(self._image, cv2.COLOR_GRAY2RGB)

    # screenshot module grabs image by provided coordinates
    # Convert it to numpy grey image, scale it up and apply median blurr to make the text better readable
    def grabImage(self, resize=1.5, blurr=3):
        screenshot = ImageGrab.grab(bbox=self._coordinates)
        imageArray = np.array(screenshot)
        image = cv2.cvtColor(imageArray, cv2.COLOR_RGB2GRAY)
        image = cv2.resize(image, (0,0), fx=resize, fy=resize)
        image = cv2.medianBlur(image,blurr)
        return image

    # Call pytesseract install location and let it extract text out of image
    @staticmethod
    def imgToText(image):
        # Give the path to your tesseract.exe if installed at different location
        pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
        text = pytesseract.image_to_string(Image.fromarray(image))
        # Make sure to replace tesseracts newlines with a minus
        return text.replace("\"", " - ")

    # To pick location, hover cursor steady over the same location for 1 second
    @staticmethod
    def pickLocation(timedif=1):
        start = time()
        x1,y1 = ScreenInfo.getCoordinates()
        while(True):
            x2, y2 = ScreenInfo.getCoordinates()
            if x1 != x2 or y1 != y2:
                print(x2, y2)
                x1, y1 = x2, y2
                start = time()
                continue
            if time() - start >= timedif:
                return x1, y1


if __name__=="__main__":
    print("Chose the first Value")
    x1, y1 = ScreenInfo.pickLocation()
    print("Chose second Value")
    x2, y2 = ScreenInfo.pickLocation()
    info = ScreenInfo((x1, y1, x2, y2))
    print(info.getText())

    cv2.imshow("img", info.getImage())
    cv2.waitKey(0)
    cv2.destroyAllWindows()

