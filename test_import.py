import detector
import mask_function.aux_functions as aux_function
from opentool import Config
import cv2

class AUTO_MASK(object):
    def __init__(self, config):
        self.detector = detector.DLIB_DETECTOR()
        self.function = aux_function
        self.config = config
    def mask(self, image):
        face_locations, bboxes = self.detector.detect_faces(image)
        print('CHECKPOINT 1')
        masked_image, mask, mask_binary, original_image = self.function.mask_image(self.detector, face_locations, image, config)
        print('CHECKPOINT 2')
        if len(masked_image) == 0:
            masked_image = image
        else:
            masked_image = mask_image[0]
        return masked_image

config = Config.fromfile('config.py')
if __name__ == '__main__':
    mask_machine = AUTO_MASK(config)
    image = cv2.imread('blankimage.jpg')
    mask_image = mask_machine.mask(image)
    cv2.imwrite('blankimage_result.jpg', mask_image)
