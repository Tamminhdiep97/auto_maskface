import cv2
import time
import mask_module
import mask_module.opentool as opentool
config = opentool.Config.fromfile('config.py')
mask_machine = mask_module.AUTO_MASK(config)
image = cv2.imread('image_test.jpg')
while True:
    mask_image, vat = mask_machine.mask(image)
    if vat:
        cv2.imwrite('masked_image_test.jpg', mask_image)
    else:
        print('error')
    time.sleep(0.5)
