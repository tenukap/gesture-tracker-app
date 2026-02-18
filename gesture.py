# finger movement detection function


class gesture_detector:

    def __init__(self):
        self.prev_avg_x = None
        self.cooldown_frames = 0
        self.threshold = 0.04

    def Four_finger_extended(self, landmark):
        pass

    def detect_swipe(landmarks, self):
        direction = None
        if (
            landmarks[8].y < landmarks[6].y
            and landmarks[12].y < landmarks[10].y
            and landmarks[16].y < landmarks[14].y
            and landmarks[20].y < landmarks[18].y
        ):

            avg_x = (
                landmarks[8].x + landmarks[12].x + landmarks[16].x + landmarks[20].x
            ) / 4

            if self.prev_avg_ is not None:

                dx = (
                    avg_x - self.prev_avg_x
                )  # prev_avg_x is stored in your GestureDetector object
                if dx > self.threshold:
                    direction = "RIGHT"
                elif dx < -self.threshold:
                    direction = "LEFT"
            self.prev_avg_x = avg_x

        else:
            self.avg_prev_x = None

        return direction
