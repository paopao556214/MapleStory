import os
import cv2
import sys

def cameraAutoForPictures(saveDir='data/'):
    '''
    调用电脑摄像头来自动获取图片
    '''
    if not os.path.exists(saveDir):
        os.makedirs(saveDir)
    count = 1  # 图片计数索引
    cap = cv2.VideoCapture(0)
    width, height, w = 640, 480, 360
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    crop_w_start = (width - w) // 2
    crop_h_start = (height - w) // 2
    print
    'width: ', width
    print
    'height: ', height
    while True:
        ret, frame = cap.read()  # 获取相框
        frame = frame[crop_h_start:crop_h_start + w, crop_w_start:crop_w_start + w]  # 展示相框
        frame = cv2.flip(frame, 1, dst=None)  # 前置摄像头获取的画面是非镜面的，即左手会出现在画面的右侧，此处使用flip进行水平镜像处理
        cv2.imshow("capture", frame)
        action = cv2.waitKey(1) & 0xFF
        if action == ord('c'):
            saveDir = input(u"请输入新的存储目录：")
            if not os.path.exists(saveDir):
                os.makedirs(saveDir)
        elif action == ord('p'):
            cv2.imwrite("%s/%d.jpg" % (saveDir, count), cv2.resize(frame, (4752, 3168), interpolation=cv2.INTER_AREA))
            print(u"%s: %d 张图片" % (saveDir, count))
            count += 1
        if action == ord('q'):
            break
    cap.release()  # 释放摄像头
    cv2.destroyAllWindows()  # 丢弃窗口


if __name__ == '__main__':
    cameraAutoForPictures(saveDir='data/')


