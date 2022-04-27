import sys
import numpy as np
import cv2 as cv

# параметры цветового фильтра
hsv_min = np.array((2, 28, 65), np.uint8)
hsv_max = np.array((26, 238, 255), np.uint8)
def contur(fn):

    img = cv.imread(fn)

    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)  # меняем цветовую модель с BGR на HSV
    thresh = cv.inRange(hsv, hsv_min, hsv_max)  # применяем цветовой фильтр
    # ищем контуры и складируем их в переменную contours
    contours, hierarchy = cv.findContours(thresh.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # отображаем контуры поверх изображения
    cv.drawContours(img, contours, -1, (255, 0, 0), 3, cv.LINE_AA, hierarchy, 1)
    return contours

if __name__ == '__main__':
    img_base = "\\\\dc\\users\\desktop\\d.antonov\\Desktop\\img\\4.jpg"
    img1 = "\\\\dc\\users\\desktop\\d.antonov\\Desktop\\img\\1.jpg"
    img2 = "\\\\dc\\users\\desktop\\d.antonov\\Desktop\\img\\3.jpg"
    c1 = contur(img_base)
    c2 = contur(img1)
    c3 = contur(img2)

    sum = 0
    sum1= 0
    count = 0
     # выводим итоговое изображение в окно
    #cv.imshow('contours', img)  # выводим итоговое изображение в окно
    for i in range(len(c1)):
        for k in range(len(c2)):
            if cv.matchShapes(c2[k],c1[i], 1, 0.0) < 1:
                count = count + 1
                sum=sum+cv.matchShapes(c2[k],c1[i], 1, 0.0)
    sum = sum / count
    count = 0
    print(len(c1),len(c2),len(c3))
    for i in range(len(c1)):
        for k in range(len(c3)):
            if cv.matchShapes(c3[k], c1[i], 1, 0.0) < 1:
                count = count + 1
                sum1 = sum1 + cv.matchShapes(c3[k], c1[i], 1, 0.0)
    sum1 = sum1 / count
    print(sum,sum1)
    cv.waitKey()
    cv.destroyAllWindows()
