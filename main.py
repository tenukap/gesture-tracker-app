import cv2
import mediapipe as mp
from mediapipe.tasks.python import vision

cap = cv2.VideoCapture(1)
# model declariation 
model = "models/Hand Landmarker Task - Google AI Guide.task"


#model processing initializaiton
BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
HandLandmarkerResult = mp.tasks.vision.HandLandmarkerResult
VisionRunningMode = mp.tasks.vision.RunningMode


def print_result(result: HandLandmarkerResult, output_image: mp.Image, timestamp_ms: int):
#detecting hand 
    if len(result.hand_landmarks) == 0:
       print("---hand not detected---")
       return
    print("----hand detected----")

#get number of hands detected 
    total_hands = len(result.hand_landmarks)
    print(total_hands)

# get the index fingers of the hands 
    for index_hands in range(total_hands):
       print("processing hand index : " ,index_hands)

       hand_landmarks = result.hand_landmarks[index_hands]
       



options = HandLandmarkerOptions( 
    base_options = BaseOptions(model_asset_path = model),
    running_mode = VisionRunningMode.LIVE_STREAM,
    num_hands = 2 ,
    result_callback=print_result
    
)

#initialize landMarker 
landMarker = HandLandmarker.create_from_options(options)


# looping thorugh the frames 
while True:
   sucess, frame = cap.read() 
   if not sucess:
    print("failded to open Camera")
    break 
   RGB_Frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
   mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=RGB_Frame)

   frame_timestamp_ms = int(cv2.getTickCount()/cv2.getTickFrequency() * 100)
   landMarker.detect_async(mp_image,frame_timestamp_ms)
   cv2.imshow("Camera", frame)
   if cv2.waitKey(1) & 0xFF == ord('q'):
       break


cap.release()
cv2.destroyAllWindows()
landMarker.close()
