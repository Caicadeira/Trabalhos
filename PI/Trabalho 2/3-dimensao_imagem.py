import numpy as np
import cv2
imagem = cv2.imread("426616a6c698495a9e34016dd6c7d2d1.jpg")
print(imagem.shape)
print(imagem.size)
start=(100,300)
end=(300,600)
color=(0,0,0)
image = cv2.rectangle(imagem, start, end, color,-1)




