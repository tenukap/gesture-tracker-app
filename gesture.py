#finger movement detection function 

    
class gesture_detector:

       def __init__(self):
              self.prev_avg_x = None 
              self.cooldown_frames = 0
              self.threshold = 0.04

       def Four_finger_extended(self, landmark ):
              pass