import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

cap = cv2.VideoCapture(0)
# model declariation 
model = "models/Hand Landmarker Task - Google AI Guide.task"

#model processing initializaiton
BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
HandLandmarkerResult = mp.tasks.vision.HandLandmarkerResult
VisionRunningMode = mp.tasks.vision.RunningMode

def print_result(result: HandLandmarkerResult, output_image: mp.Image, timestamp_ms: int):
   print('hand landmarker result: {}'.format(result))


options = HandLandmarkerOptions(
    base_options = BaseOptions(model ),
    running_mode = VisionRunningMode.LiveStream,
    result_callback=print_result
)

#initialize landMarker 
landMarker = HandLandmarker.create_from_options(options)

while(0):
    frame = cap.read()

    HSV = cv2.cvtColor(frame, cv2.COLOR_BAYER_BG2BGR)

    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data = HSV
    )


