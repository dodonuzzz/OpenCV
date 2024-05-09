import cv2

img = cv2.imread('Sinem_Baskan.jpg')

cv2.namedWindow('BASGANIM DA BASGANIM', cv2.WINDOW_FULLSCREEN)

cv2.imshow('BASGANIM DA BASGANIM', img)

cv2.waitKey(0)

cv2.destroyAllWindows()