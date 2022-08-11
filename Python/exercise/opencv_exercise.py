import cv2
import numpy as np
"""
==========================
图像读取，显示和保存
==========================
"""
def cv_show(name, img, wait_key=0):
    cv2.imshow(name, img)
    cv2.waitKey(wait_key)
    cv2.destroyAllWindows()
# img = cv2.imread('./test.png')
# cv_show('test.png', img)
# cv2.imwrite('test.png', img)
"""
==========================
颜色通道
==========================
"""
# img = cv2.imread('./test.png')
# b, g, r = cv2.split(img)
# target_img = cv2.merge((b, g, r))
# cv_show('test.png', target_img)
"""
==========================
图像融合
==========================
"""
# img1 = cv2.imread('test1.png')
# img2 = cv2.imread('test2.png')
# img = cv2.addWeighted(cv2.resize(img1, (300, 200)), 0.6, cv2.resize(img2, (300, 200)), 0.4, 0)
# cv_show('test.png', img)
"""
==========================
边界填充
==========================
"""
# img = cv2.imread('./test.png')
# 复制边缘像素
# target_img = cv2.copyMakeBorder(img, 50, 50, 50, 50, cv2.BORDER_REPLICATE)
# 反射法
# target_img = cv2.copyMakeBorder(img, 50, 50, 50, 50, cv2.BORDER_REFLECT)
# 反射法（已最边缘像素为轴）
# target_img = cv2.copyMakeBorder(img, 50, 50, 50, 50, cv2.BORDER_REFLECT_101)
# 外包装法
# target_img = cv2.copyMakeBorder(img, 50, 50, 50, 50, cv2.BORDER_WRAP)
# 常数值填充
# target_img = cv2.copyMakeBorder(img, 50, 50, 50, 50, cv2.BORDER_CONSTANT, 0)
# cv_show('test.png', target_img)
"""
==========================
阈值操作
==========================
"""
# img = cv2.imread('./test.png')
# 从0和maxval中取值，以thresh为阈值
# ret, target_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# 与上面相反
# ret, target_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
# 阈值以下的部分设为0
# ret, target_img = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
# 阈值以上的部分设为0
# ret, target_img = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)
# 阈值以上的部分设为阈值
# ret, target_img = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
# cv_show('test.png', target_img)
"""
==========================
平滑处理
==========================
"""
# img = cv2.imread('./test.png')
# 均值滤波
# target_img = cv2.blur(img, (3,3))
# 中值滤波
# target_img = cv2.medianBlur(img, 5)
# 高斯滤波
# target_img = cv2.GaussianBlur(img, (3,3), 1)
# cv_show('test.png', target_img)
"""
==========================
腐蚀与膨胀
==========================
"""
# img = cv2.imread('./test.png')
# 腐蚀
# target_img = cv2.erode(img, np.ones((3,3), np.uint8), iterations=1)
# 膨胀
# target_img = cv2.dilate(img, np.ones((3,3), np.uint8), iterations=1)
# cv_show('test.png', target_img)
"""
==========================
算子操作--提取轮廓信息
==========================
"""
# img = cv2.imread('./test.png')
# Sobel算子
# x_img = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
# x_img = cv2.convertScaleAbs(x_img)
# y_img = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
# y_img = cv2.convertScaleAbs(y_img)
# target_img = cv2.addWeighted(x_img, 0.5, y_img, 0.5, 0)
# Scharr算子
# x_img = cv2.Scharr(img, cv2.CV_64F, 1, 0)
# x_img = cv2.convertScaleAbs(x_img)
# y_img = cv2.Scharr(img, cv2.CV_64F, 0, 1)
# y_img = cv2.convertScaleAbs(y_img)
# target_img = cv2.addWeighted(x_img, 0.5, y_img, 0.5, 0)
# Laplacian算子
# target_img = cv2.Laplacian(img, cv2.CV_64F)
# target_img = cv2.convertScaleAbs(target_img)
# Canny边缘检查算法
# target_img = cv2.Canny(img, 80, 150)
# cv_show('test.png', target_img)