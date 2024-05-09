import cv2

image = cv2.imread('Sinem_Baskan.jpg')
B, G, R = cv2.split(image)
cv2.imshow('Sinem_Baskan', image)

cv2.imshow('Blue', B)
cv2.imshow('Green', G)
cv2.imshow('Red', R)
cv2.waitKey(0)
cv2.destroyAllWindows()

