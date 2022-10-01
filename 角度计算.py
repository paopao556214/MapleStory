# -*- coding: utf-8 -*-
import cv2
import numpy as np

imagepath = 'E://CHN_Char/char_after_bin.jpg'
img = cv2.imread(imagepath, -1)
contours, _ = cv2.findContours(img, 2, 2)

for cnt in contours:

    # 最小外界矩形的宽度和高度
    width, height = cv2.minAreaRect(cnt)[1]

    if width* height > 100:
        # 最小的外接矩形
        rect = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(rect)  # 获取最小外接矩形的4个顶点
        box = np.int0(box)

        if 0 not in box.ravel():

            '''绘制最小外界矩形
            for i in range(4):
                cv2.line(image, tuple(box[i]), tuple(box[(i+1)%4]), 0)  # 5
            '''
            # 旋转角度
            theta = cv2.minAreaRect(cnt)[2]
            if abs(theta) <= 45:
                print('图片的旋转角度为%s.'%theta)
                angle = theta

# 仿射变换,对图片旋转angle角度
h, w = img.shape
center = (w//2, h//2)
M = cv2.getRotationMatrix2D(center, angle, 1.0)
rotated = cv2.warpAffine(img, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

# 保存旋转后的图片la
cv2.imwrite('E://CHN_Char/after_rotated.jpg', rotated)
