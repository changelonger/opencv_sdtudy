import cv2
# 创建新窗口,名字为window
cv2.namedWindow('window', cv2.WINDOW_AUTOSIZE)
# 重新设置窗口
cv2.resizeWindow('window', 800, 600)
#  展示名字为window的新窗口
cv2.imshow('window', 0)