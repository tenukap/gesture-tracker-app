import cv2
import mediapipe as mp
from mediapipe.tasks.python import vision
from callback import print_result
from display_landmarks import OutputLandmarks
import callback

frame_global = None 
cap = cv2.VideoCapture(1)
# model declariation 
model = "models/Hand Landmarker Task - Google AI Guide.task"


#model processing initializaiton
BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
HandLandmarkerResult = mp.tasks.vision.HandLandmarkerResult
VisionRunningMode = mp.tasks.vision.RunningMode

#where movement fingers funtion use to be

#where print result function used to be

#output landmarks function use to be 
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
      # test red dot (static position)
 #  cv2.circle(frame, (200, 200), 10, (0, 0, 255), -1)
   frame_timestamp_ms = int(cv2.getTickCount()/cv2.getTickFrequency() * 100)
   landMarker.detect_async(mp_image,frame_timestamp_ms)
   if callback.Latest_hand_indexs is not None:
    for index in callback.Latest_hand_indexs.values():
        OutputLandmarks(index, frame)
   cv2.imshow("Camera", frame)

   if cv2.waitKey(1) & 0xFF == ord('q'):
       break

# closing everything 
cap.release()
cv2.destroyAllWindows()
landMarker.close()
