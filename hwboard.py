# -*- coding:utf-8 -*-
"""
Choose the button1:Generate Pattern，press M to turn to the handwrite mode, press the mouse and move to draw the number pattern(between 0~9)
After finishing writing，press W to turn to the screenshot mode, press the mouse to choose the pattern, then press Q to quit and back to the list
Choose the button2:Refresh, to redisplay the pattern 
Choose the button3:Recognize，to recognize number(between 0~9)
"""
import numpy as np
import cv2 as cv

drawing = False  # true if mouse is pressed, event begins
mode = True  # if True, draw rectangle. Press M to toggle to curve
ix, iy = -1, -1


class Mouse():

    # mouse click event
    def __init__(self):
        self.img = np.zeros((600, 600, 3), np.uint8)

    def draw_circle(self, event, x, y, flags, param):
        global ix, iy, drawing, mode
        if event == cv.EVENT_LBUTTONDOWN:
            drawing = True
            ix, iy = x, y
        elif event == cv.EVENT_MOUSEMOVE:
            if drawing:
                if self.mode:
                    cv.rectangle(self.img, (ix, iy), (x, y), (128,0,128), -1)#普通模式轨迹颜色
                else:
                    cv.circle(self.img, (x, y), 5, (255,192,203), -1) #手写体轨迹颜色
        elif event == cv.EVENT_LBUTTONUP:
            drawing = False
            if self.mode:
                cv.rectangle(self.img, (ix, iy), (x, y), (255, 0, 0), -1)
            else:
                cv.circle(self.img, (x, y), 5, (255,192,203), -1)#手写体松开鼠标后点的颜色

    def on_mouse(self, event, x, y, flags, param):
        global img, point1, point2
        img2 = self.img.copy()
        if event == cv.EVENT_LBUTTONDOWN:  # 左键点击
            point1 = (x, y)
            cv.circle(img2, point1, 10, (255, 255, 0), 5)
            cv.imshow('Digital writing pad', img2)
        elif event == cv.EVENT_MOUSEMOVE and (flags & cv.EVENT_FLAG_LBUTTON):  # 按住左键拖曳
            cv.rectangle(img2, point1, (x, y), (255,255,0), 5)#截图框颜色
            cv.imshow('Digital writing pad', img2)
        elif event == cv.EVENT_LBUTTONUP:  # 左键释放
            point2 = (x, y)
            cv.rectangle(img2, point1, point2, (255,192,203), 5)
            cv.imshow('Digital writing pad', img2)
            min_x = min(point1[0], point2[0])
            min_y = min(point1[1], point2[1])
            width = abs(point1[0] - point2[0])
            height = abs(point1[1] - point2[1])
            cut_img = self.img[min_y:min_y + height, min_x:min_x + width]
            cv.imwrite('Num.png', cut_img)

    def create_image(self):
        self.mode = True
        cv.namedWindow('Digital writing pad')
        cv.setMouseCallback('Digital writing pad', self.draw_circle)
        while (1):
            cv.imshow('Digital writing pad', self.img)
            k = cv.waitKey(1) & 0xFF
            if k == ord('m'):
                self.mode = not mode
            elif k == 27:
                break
            elif k == ord('w'):
                cv.setMouseCallback('Digital writing pad', self.on_mouse)
            elif k == ord('q'):
                break
        cv.destroyAllWindows()


if __name__ == '__main__':
    mn = Mouse()
    mn.create_image()
