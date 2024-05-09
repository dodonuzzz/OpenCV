import cv2
import os

path = r'Sinem_Baskan.jpg'

dizin = r'C:\Users\Doğukan\OneDrive\Masaüstü'

img = cv2.imread(path)

os.chdir(dizin)

print("Resmi Kaydetmeden Önce : ")
print(os.listdir(dizin))

filename = 'Sinem_Baskan.jpg'

cv2.imwrite(filename, img)

print("Resmi Kaydettikten Sonra : \n" , os.listdir(dizin))

print("Resim Kaydedildi.")
