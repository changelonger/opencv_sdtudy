import cv2
import numpy as np

# # 1、打印像素
# i = cv2.imread('MC.jpg')  # 会自动创建窗口
# p = i[100, 100, 0]  # 注意此时i是彩色的，所以p是3个数据R G B opencv是BGR
#
# print(p)
# # 返回值 = 变量[参数]
# # 前两个变量代表行列，最后一个代表返回的通道
# # 0 B
# # 1 G
# # 2 R
# # 不加第三个参数返回3个值
#
# ii = cv2.imread('MC.jpg', cv2.IMREAD_GRAYSCALE)
# # cv2.imread('路径'，类型)
# pp = ii[100, 100]
# print(pp)
# 常用的类型有三种
# cv2.IMREAD_GRAYSCALE 灰度图
# cv2.IMREAD_COLOR  彩色图
# cv2.IMREAD_UNCHANGED 不改变


# 2、修改像素
img = cv2.imread('MC.jpg')  # 彩色
print(img.item(10, 15, 0))  # 变量.item(行，列)效果一样的,但是item必须要三个参数
img[10, 15] = 0  # 一次修改三个值
print(img[10, 15])
img.itemset((10, 15, 0), 1)  # 修改一个
print(img[10, 15])
img2 = cv2.imread('GMC.jpg', cv2.IMREAD_UNCHANGED)  # 灰度
print(img2[10, 15])
img2[10, 15] = 15
print(img2[10, 15])


