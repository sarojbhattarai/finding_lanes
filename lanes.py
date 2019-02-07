import cv2
import numpy as np

image = cv2.imread('test_image.jpg')
# imread will read image from our file and return the multi-dimentional numpy array containing 
# the relative intensity of each pixel in the image

lane_image = np.copy(image)
def canny(image):
	gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)
	blur = cv2.GaussianBlur(gray, (5,5), 0)
	canny = cv2.Canny(blur, 50, 150)
	return canny
	
canny = canny(lane_image)
 
# to render the image we use imshow

cv2.imshow('result',canny)
cv2.waitKey(0)