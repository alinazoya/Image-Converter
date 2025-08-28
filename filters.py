from PIL import Image, ImageOps
import cv2
import numpy as np

def apply_filter(image, filter_type):
    if filter_type == 'grayscale':
        return ImageOps.grayscale(image)

    elif filter_type == 'negative':
        return ImageOps.invert(image.convert('RGB'))

    elif filter_type == 'cartoon':

        img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray, 5)
        edges = cv2.adaptiveThreshold(
            gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9
        )
        color = cv2.bilateralFilter(img, 9, 300, 300)
        cartoon = cv2.bitwise_and(color, color, mask=edges)
        return Image.fromarray(cv2.cvtColor(cartoon, cv2.COLOR_BGR2RGB))

    return image
