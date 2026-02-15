from gesture import movement_fingers
from mediapipe.tasks.python.vision import HandLandmarkerResult
import mediapipe as mp


def print_result(result: HandLandmarkerResult, output_image: mp.Image, timestamp_ms: int):
#check if frame_global == frame 
  #  if frame_global is  None:
   #     return
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

      # handmarks of index finger
       IndexFinger_MCP = hand_landmarks[5]
       IndexFinger_PIP = hand_landmarks[6]
       IndexFinger_DIP = hand_landmarks[7]
       IndexFinger_Tip = hand_landmarks[8]

       #handmarks of middle finger
       MiddleFinger_MCP = hand_landmarks[9]
       MiddleFinger_PIP = hand_landmarks[10]
       MiddleFinger_DIP = hand_landmarks[11]
       MiddleFinger_Tip = hand_landmarks[12]

       #handmarks of ring finger 
       RingFinger_MCP = hand_landmarks[13]
       RingFinger_PIP = hand_landmarks[14]
       RingFinger_DIP = hand_landmarks[15]
       RingFinger_Tip = hand_landmarks[16]

       #handmark of pinky finger 
       PinkyFinger_MCP = hand_landmarks[17]
       PinkyFinger_PIP = hand_landmarks[18]
       PinkyFinger_DIP = hand_landmarks[19]
       PinkyFinger_Tip = hand_landmarks[20]
    #    print("thump position ")

    #    print(" thump tip -> x", thumb_CMC.x , "thumb tip -> y ", thumb_CMC.y, "thumb_tip -> z " ,thumb_CMC.z)
    #    print(" thump tip -> x", thumb_MCP.x , "thumb tip -> y ", thumb_MCP.y, "thumb_tip -> z " ,thumb_MCP.z)
    #    print(" thump tip -> x", thumb_ip.x , "thumb tip -> y ", thumb_ip.y, "thumb_tip -> z " ,thumb_ip.z) 
    #    print(" thump tip -> x", thumb_tip.x , "thumb tip -> y ", thumb_tip.y, "thumb_tip -> z " ,thumb_tip.z)

       movement_fingers(CMC=thumb_CMC,MCP=thumb_MCP,IP=thumb_ip,TIP=thumb_tip)
       movement_fingers(CMC=IndexFinger_DIP, MCP=IndexFinger_MCP,IP=IndexFinger_PIP,TIP=IndexFinger_Tip)
       movement_fingers(CMC=MiddleFinger_DIP,MCP=MiddleFinger_MCP,IP=MiddleFinger_PIP,TIP=MiddleFinger_Tip)
       movement_fingers(CMC=RingFinger_DIP,MCP=RingFinger_MCP,IP=RingFinger_PIP,TIP=RingFinger_Tip)
       movement_fingers(CMC=PinkyFinger_DIP,MCP=PinkyFinger_MCP,IP=PinkyFinger_PIP,TIP=PinkyFinger_Tip)
       #OutputLandmarks(thumb_tip,frame_global)