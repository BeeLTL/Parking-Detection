import cv2

# Load the mask generated by  Cvat
image = cv2.imread('frame.png')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Threshold the grayscale image
_, binary_image = cv2.threshold(gray_image, 100, 255, cv2.THRESH_BINARY)

# Display the binary image
cv2.imwrite('images/mask2.png', binary_image)