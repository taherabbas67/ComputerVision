# OpenCV headless version is installed in this playground which is suitable for servers without GUI interface.
import cv2

# load an image
image = cv2.imread('/assets/photo.png')

#check if image is loaded successfully
if image is not None:
    #convert image to grayscale
    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # saving the processed image
    cv2.imwrite('grayPhoto.png', grayImage)
    print("Image processing completed successfully.")
else:
    print("Err: Img not loaded!")