class CamMessage:
    def __init__(self, cam_key, time_key, segment_key, station_id, latitude, longitude, altitude, speed, heading,
                 acceleration,
                 station_type, vehicle_role, time_stamp, fuel_type, brake_pedal_engaged, gas_pedal_engaged,
                 emergency_pedal_engaged,
                 collision_warning_engaged, acc_engaged, cruise_control_engaged, speed_limiter_engaged,
                 stationary_since):
        self.cam_key = cam_key
        self.time_key = time_key
        self.segment_key = segment_key
        self.station_id = station_id
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude
        self.speed = speed
        self.heading = heading
        self.acceleration = acceleration
        self.station_type = station_type
        self.vehicle_role = vehicle_role
        self.time_stamp = time_stamp
        self.fuel_type = fuel_type
        self.brake_pedal_engaged = brake_pedal_engaged
        self.gas_pedal_engaged = gas_pedal_engaged
        self.emergency_pedal_engaged = emergency_pedal_engaged
        self.collision_warning_engaged = collision_warning_engaged
        self.acc_engaged = acc_engaged
        self.cruise_control_engaged = cruise_control_engaged
        self.speed_limiter_engaged = speed_limiter_engaged
        self.stationary_since = stationary_since

    def __getitem__(self, index):
        return self.CamKey[int(index)]

    def __str__(self):
        return "CamKey: " + str(self.cam_key)