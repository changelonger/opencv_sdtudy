import cv2
import matplotlib.pyplot as plt
a = cv2.imread('./beauty.jpeg')
plt.imshow(a)
plt.show()  # 显示图像
cv2.waitKey(0)  # 等待按键
# matplotlib显示的图像颜色和真是的图像不一样
# 因为opencv的默认通道不是RBG，是BGR
# 所以opencv读进来的图片不要用matplotlib展示
# 用opencv自己自带的就可以了
# cv2.imshow('beauty', a)
# cv2.waitKey(0)