import cv2

img_location = 'C:/Users/sampa/OneDrive/Desktop/'#write the location of the picture
imgname = 'B3.jpg'#//name of the pictute

#readtheimage
img = cv2.imread(img_location+imgname)

#conversionofimage

grey_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#inverttheimage

inv_gre_img = 255-grey_image

#blurtheimage

blurred_img = cv2.GaussianBlur(inv_gre_img, (21,21) ,0)
inv_blurred_img = 255-blurred_img

#pencilsketch

pencil_ske= cv2.divide(grey_image,inv_blurred_img,scale=256.0)

#showimage
cv2.imshow('original',img)
cv2.imshow('New',pencil_ske)
cv2.waitKey(0)
