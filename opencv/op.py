import cv2 as cv

print("---------------hello world--------------")
scr = cv.imread("D:/picture/white.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", scr)
cv.waitKey(0)
cv2.destroyAllWindows()