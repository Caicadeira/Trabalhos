import numpy as np
import cv2
imagem = cv2.imread("426616a6c698495a9e34016dd6c7d2d1.jpg")
imagem2= cv2.imread("426616a6c698495a9e34016dd6c7d2d1.jpg")
altura, largura, cores = imagem.shape

for y in range(0, altura):
        for x in range(0, largura):
            azul, verde, vermelho = imagem2[y][x]
            imagem2[y][x] = [0, 0, 0]

retangulo_preto = imagem2[278:470 , 374:482]
imagem[278 : 278 + retangulo_preto.shape[0],374:374+retangulo_preto.shape[1]] = retangulo_preto
cv2.imwrite("batman_reino_do_amanha.jpg",imagem)
cv2.imshow("batman_reino_do_amanha.jpg",imagem)
cv2.waitKey()




