import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import visio

cap = cv2.VideoCapture(0)

while(0):
    frame = cap.read()

    HSV = cv2.cvtColor(frame, cv2.COLOR_BAYER_BG2BGR)

    