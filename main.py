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

#finger movement detection function 
def movement_fingers(CMC,MCP,IP,TIP):
   if IP.x >0.5 and  MCP.x >0.5 and CMC.x >0.5 and TIP.x > 0.5 :
          print("thumb is moving to the left")
   elif IP.x ==0.5 and MCP.x == 0.5 and  CMC.x == 0.5 and TIP.x == 0.5 :
        print("thumb is in the middle ") 
   else:
          print("thumb is moving to right")

def print_result(result: HandLandmarkerResult, output_image: mp.Image, timestamp_ms: int):
#detecting hand 
    if len(result.hand_landmarks) == 0:
       print("---hand not detected---")
       return
    print("----hand detected----")

#get number of hands detected 
    total_hands = len(result.hand_landmarks)
    print(total_hands)

# get the index fingers of the hands and printing results 
    for index_hands in range(total_hands):
       print("processing hand index : " ,index_hands)

       hand_landmarks = result.hand_landmarks[index_hands]
       handedness_info = result.handedness[index_hands][0]
       hand_type = handedness_info.category_name
       confidence_score = handedness_info.score 

       print(" hand type ", hand_type)
       print("confidence score ", confidence_score)

      #handmarks of thumb 
       thumb_CMC = hand_landmarks[1]
       thumb_MCP = hand_landmarks[2]
       thumb_ip = hand_landmarks[3]  
       thumb_tip = hand_landmarks[4]

       print("thump position ")

       print(" thump tip -> x", thumb_CMC.x , "thumb tip -> y ", thumb_CMC.y, "thumb_tip -> z " ,thumb_CMC.z)
       print(" thump tip -> x", thumb_MCP.x , "thumb tip -> y ", thumb_MCP.y, "thumb_tip -> z " ,thumb_MCP.z)
       print(" thump tip -> x", thumb_ip.x , "thumb tip -> y ", thumb_ip.y, "thumb_tip -> z " ,thumb_ip.z) 
       print(" thump tip -> x", thumb_tip.x , "thumb tip -> y ", thumb_tip.y, "thumb_tip -> z " ,thumb_tip.z)

       movement_fingers(CMC=thumb_CMC,MCP=thumb_MCP,IP=thumb_ip,TIP=thumb_tip)




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

# closing everything 
cap.release()
cv2.destroyAllWindows()
landMarker.close()
