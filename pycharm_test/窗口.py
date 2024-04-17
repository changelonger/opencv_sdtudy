import cv2
# ##窗口创建销毁
# 创建新窗口,名字为window
# WINDOW_AUTOSIZE不允许改窗口大小
# cv2.namedWindow('window', cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('window', cv2.WINDOW_NORMAL)
# 重新设置窗口
cv2.resizeWindow('window', 800, 600)
#  展示名字为window的新窗口
cv2.imshow('window', 0)
# 可以用cv2.waitKey()来销毁窗口 不用每次都重启
key = cv2.waitKey(0)
if key == ord('q'):
    print("销毁窗口")
    cv2.destroyAllWindows()
