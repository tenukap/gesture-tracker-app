class gesture_detector:

    def __init__(self):
        self.prev_avg_x = None
        self.cooldown_frames = 0
        self.threshold = 0.04

    def Four_finger_extended(self, landmarks):
        fingers = {}
    # Thumb: compare tip with IP joint (landmarks[4] vs landmarks[3])
        fingers['thumb'] = landmarks[4].x < landmarks[3].x  # Right hand example

        # Other fingers: tip y < pip y (y is vertical, origin at top)
        fingers['index'] = landmarks[8].y < landmarks[6].y
        fingers['middle'] = landmarks[12].y < landmarks[10].y
        fingers['ring'] = landmarks[16].y < landmarks[14].y
        fingers['pinky'] = landmarks[20].y < landmarks[18].y

        return fingers

    def detect_swipe(self,landmarks):
        print("working ")
        direction = None

        avg_x = (
                landmarks[8].x + landmarks[12].x + landmarks[16].x + landmarks[20].x
            ) / 4

        if self.prev_avg_x is not None:
            dx = (avg_x - self.prev_avg_x)  # prev_avg_x is stored in your GestureDetector object
            if dx > self.threshold:
                direction = "RIGHT"
            elif dx < -self.threshold:
                    direction = "LEFT"
            self.prev_avg_x = avg_x
        else:
            self.prev_avg_x = None

        return direction
