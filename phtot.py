import cv2
import os

path =  "D:/photo/"   #保存路径

def takePhoto():
    print("=============================================")
    print("=  热键(请在摄像头的窗口使用)：             =")
    print("=  x: 拍摄图片                              =")
    print("=  q: 退出                                  =")
    print("=============================================")
    print()
    # class_name = input("请输入存储目录：")
    # while os.path.exists(class_name):
    #     class_name = input("目录已存在！请输入存储目录：")
    # os.mkdir(class_name)

    index = 1
    cap = cv2.VideoCapture(0)
    width = 640
    height = 480
    w = 360
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    crop_w_start = (width - w) // 2
    crop_h_start = (height - w) // 2

    print(width, height)

    while True:
        # get a frame
        ret, frame = cap.read()
        # show a frame
        frame = frame[crop_h_start:crop_h_start + w, crop_w_start:crop_w_start + w]
        frame = cv2.flip(frame, 1, dst=None)
        cv2.imshow("capture", frame)

        input = cv2.waitKey(1) & 0xFF

        # if input == ord('z'):
        #     class_name = input("请输入存储目录：")
        #     while os.path.exists(class_name):
        #         class_name = input("目录已存在！请输入存储目录：")
        #     os.mkdir(class_name)
        if input == ord('x'):
            cv2.imwrite("%s%d.png" % (path,index),
            cv2.resize(frame, (120, 120), interpolation=cv2.INTER_AREA))
            print("%d 张图片" % (index))
            index += 1

        if input == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return index

if __name__ == '__main__':
    takePhoto()