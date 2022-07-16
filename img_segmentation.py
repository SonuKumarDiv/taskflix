import cv2
import numpy as np

# Load image, create mask, and draw white circle on mask
image = cv2.imread('input.jpg')
print('lll',image)
mask = np.zeros(image.shape, dtype=np.uint8)
mask = cv2.rectangle(mask, (400, 120), (900, 1200), 500, -2)
# Mask input image with binary mask
result = cv2.bitwise_and(image, mask)
# Color background white
result[mask==0] = 255 # Optional

cv2.imshow('image', image)
cv2.imshow('mask', mask)
cv2.imshow('result', result)
cv2.waitKey()

# import cv2
# import numpy as np

# # read image
# img = cv2.imread('input.png')

# #mask it - method 1:
# # read mask as grayscale in range 0 to 255
# mask1 = cv2.imread('input.png',0)
# print(img,'lllll')
# # while True:
# #     #success, img = cap.read()
# #     if img is None:
# #         break
# result1 = img.copy()
# #result1 = img.copy()
# result1[mask1 == 0] = 0
# result1[mask1 != 0] = img[mask1 != 0]

# # mask it - method 2:
# # read mask normally, but divide by 255.0, so range is 0 to 1 as float
# mask2 = cv2.imread('input.png') / 255.0
# # mask by multiplication, clip to range 0 to 255 and make integer
# result2 = (img * mask2).clip(0, 255).astype(np.uint8)

# cv2.imshow('image', img)
# cv2.imshow('mask1', mask1)
# cv2.imshow('masked image1', result1)
# cv2.imshow('masked image2', result2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#     # save results
# cv2.imwrite('input.png1', result1)
# cv2.imwrite('input.png2', result2)
