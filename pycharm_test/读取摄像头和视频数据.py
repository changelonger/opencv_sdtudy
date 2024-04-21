import cv2
# 打开摄像头
cv2.namedWindow('video', cv2.NORM_HAMMING)
# 如果打开失败，不会报错
cap = cv2.VideoCapture(0)
# 如果打开视频，就加入视频的地址就可以了
# cap = cv2.VideoCapture('./MC.mp4')

# 循环读取每一帧
while True:
    # 读每一帧的数据，返回标记True读到了，False 没督导
    ret, frame = cap.read()

    # 根据ret做一个判断
    if not ret:
        # 没读到数据，直接退出
        break
    # 显示数据
    cv2.imshow('video', frame)
    key = cv2.waitKey(30)
    if key == ord('q'):
        break
# 释放资源
cap.release()
cv2.destroyAllWindows()
