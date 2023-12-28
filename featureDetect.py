
import cv2

# load an image
image = cv2.imread('grayPhoto.png')

# check if the image is loaded
if image is None:
    print("ERR: Image not loaded!")
else:
    # initialize the ORB detector
    orb = cv2.ORB_create()
    # detect keypoints
    keypoints = orb.detect(image, None)
    # compute descriptors
    keypoints, descriptors = orb.compute(image, keypoints)
    # draw keypoints on the image
    outputImage = cv2.drawKeypoints(image, keypoints, None, color=(0, 0, 255), flags=0)
    # save the image with keypoints
    cv2.imwrite('keypoints_image3.png', outputImage)
    print("feature detection completed successfully.")