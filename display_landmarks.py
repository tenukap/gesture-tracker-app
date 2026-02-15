import cv2
 
def OutputLandmarks(Tip,frame):
    print("output function starting ")
    height,width,channels = frame.shape
    x_pixel  = int(Tip.x * width)
    y_pixel = int(Tip.y* height)
    cv2.circle(frame, (x_pixel, y_pixel), 8, (0, 0, 255), -1)

