class gesture_detector:

    def __init__(self):
        self.prev_avg_x = None
        self.prev_avg_y = None
        self.cooldown_frames = 0
        self.threshold = 0.05

        self.finger_threshold = 0.02

#checks if finger extended
    def is_fingers_extended(self, tip_landmarks, pip_landmarks):
        is_extended = tip_landmarks > pip_landmarks
        return is_extended
    
#detect which fingers extended
    def which_fingers_extended(self, landmarks):
        fingers = {}
        fingers['thumb'] = landmarks[4].x < landmarks[3].x  # Right hand example

        # Other fingers: tip y < pip y (y is vertical, origin at top)
        fingers['index'] = landmarks[8].y < landmarks[6].y
        fingers['middle'] = landmarks[12].y < landmarks[10].y
        fingers['ring'] = landmarks[16].y < landmarks[14].y
        fingers['pinky'] = landmarks[20].y < landmarks[18].y

        return fingers
    
    #count how many fingers extended 
    def count_fingers_extended(self,landmarks):
        fingers = self.which_fingers_extended(landmarks)
        count = sum(fingers.values())
        return count,fingers


#detect swipes
    def detect_swipe(self,landmarks):
        print("working ")
        direction = None

        avg_x = (
                landmarks[8].x + landmarks[12].x + landmarks[16].x + landmarks[20].x
            ) / 4

        if self.prev_avg_x is not None:
            dx = (avg_x - self.prev_avg_x)
            if dx > self.threshold:
                direction = "RIGHT"
            elif dx < -self.threshold:
                direction = "LEFT"
        
        self.prev_avg_x = avg_x

        return direction
