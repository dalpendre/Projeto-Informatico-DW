class CamMessage:
    def __init__(self, cam_key, time_key, c_location, speed ):
        self.cam_key = cam_key,
        self.time_key = time_key,
        self.c_location = c_location,
        self.speed = speed

    def __str__(self):
        return self.msg