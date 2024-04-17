
import cv2
# 创建窗口
cv2.namedWindow('img',cv2.WINDOW_NORMAL)
cv2.resizeWindow('img',640,480)

# 读取图片
img=cv2.imread('./beauty.jpeg')
while True:
    cv2.imshow('img',img)
    key=cv2.waitKey(0)
    if key ==ord('q'):
        break
    elif key == ord('s'):
        cv2.imwrite('./beauty2.png',img)
cv2.destroyAllWindows()