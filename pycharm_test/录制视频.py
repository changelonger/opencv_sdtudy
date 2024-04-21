import cv2

cap = cv2.VideoCapture(0)
# *mp4v表示解包，把mp4v变成'm','p' '4','v'
fourcc = cv2.VideoWriter.fourcc(*'mp4v')
# 旧版本是_,新版本是.

# vw是视频的每一帧
vw = cv2.VideoWriter('output.mp4', fourcc, 60, (640, 480))

while cap.isOpened():
    ret, frame = cap.read()  # 读取数据
    if not ret:
        print('can not receive frame,Exit')
        break
    vw.write(frame)  # 保存 把frame以vw的形式保存
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
vw.release()
cv2.destroyAllWindows()


