class DenmMessage:
    def __init__(self, DENMKey, Heading, TimeStamp, Latitude, Longitude, Altitude, Cause, TrafficCause,
                 AccidentSubCause, RoadworksSubCause, HumanPresenceOnTheRoadSubCause, WrongWayDrivingSubCause,
                 AdverseWeatherCondition_ExtremeWeatherConditionSubCause, AdverseWeatherCondition_AdhesionSubCause,
                 AdverseWeatherCondition_VisibilitySubCause, AdverseWeatherCondition_PrecipitationSubCause,
                 SlowVehicleSubCause, StationaryVehicleSubCause, HumanProblemSubCause,
                 EmergencyVehicleApproachingSubCause, HazardousLocation_DangerousCurveSubCause,
                 HazardousLocation_SurfaceConditionSubCause, HazardousLocation_ObstacleOnTheRoadSubCause,
                 HazardousLocation_AnimalOnTheRoadSubCause, CollisionRiskSubCause, SignalViolationSubCause,
                 RescueAndRecoveryWorkInProgressSubCause, DangerousEndOfQueueSubCause, DangerousSituationSubCause,
                 VehicleBreakdownSubCause, PostCrashSubCause):
        self.DENMKey = DENMKey
        self.Heading = Heading
        self.TimeStamp = TimeStamp
        self.Latitude = Latitude
        self.Longitude = Longitude
        self.Altitude = Altitude
        self.Cause = Cause
        self.TrafficCause = TrafficCause
        self.AccidentSubCause = AccidentSubCause
        self.RoadworksSubCause = RoadworksSubCause
        self.HumanPresenceOnTheRoadSubCause = HumanPresenceOnTheRoadSubCause
        self.WrongWayDrivingSubCause = WrongWayDrivingSubCause
        self.AdverseWeatherCondition_ExtremeWeatherConditionSubCause = AdverseWeatherCondition_ExtremeWeatherConditionSubCause
        self.AdverseWeatherCondition_AdhesionSubCause = AdverseWeatherCondition_AdhesionSubCause
        self.AdverseWeatherCondition_VisibilitySubCause = AdverseWeatherCondition_VisibilitySubCause
        self.AdverseWeatherCondition_PrecipitationSubCause = AdverseWeatherCondition_PrecipitationSubCause
        self.SlowVehicleSubCause = SlowVehicleSubCause
        self.StationaryVehicleSubCause = StationaryVehicleSubCause
        self.HumanProblemSubCause = HumanProblemSubCause
        self.EmergencyVehicleApproachingSubCause = EmergencyVehicleApproachingSubCause
        self.HazardousLocation_DangerousCurveSubCause = HazardousLocation_DangerousCurveSubCause
        self.HazardousLocation_SurfaceConditionSubCause = HazardousLocation_SurfaceConditionSubCause
        self.HazardousLocation_ObstacleOnTheRoadSubCause = HazardousLocation_ObstacleOnTheRoadSubCause
        self.HazardousLocation_AnimalOnTheRoadSubCause = HazardousLocation_AnimalOnTheRoadSubCause
        self.CollisionRiskSubCause = CollisionRiskSubCause
        self.SignalViolationSubCause = SignalViolationSubCause
        self.RescueAndRecoveryWorkInProgressSubCause = RescueAndRecoveryWorkInProgressSubCause
        self.DangerousEndOfQueueSubCause = DangerousEndOfQueueSubCause
        self.DangerousSituationSubCause = DangerousSituationSubCause
        self.VehicleBreakdownSubCause = VehicleBreakdownSubCause
        self.PostCrashSubCause = PostCrashSubCause

    def __str__(self):
        return "DENMKey: " + str(self.DENMKey) + "\nHeading: " + str(self.Heading) + "\nTimeStamp: " + str(self.TimeStamp) + "\nLatitude: " + str(self.Latitude) + "\nLongitude: " + str(self.Longitude) + "\nAltitude: " + str(self.Altitude) + "\nCause: " + str(self.Cause) + "\nTrafficCause: " + str(self.TrafficCause) + "\nAccidentSubCause: " + str(self.AccidentSubCause) + "\nRoadworksSubCause: " + str(self.RoadworksSubCause) + "\nHumanPresenceOnTheRoadSubCause: " + str(self.HumanPresenceOnTheRoadSubCause) + "\nWrongWayDrivingSubCause: " + str(self.WrongWayDrivingSubCause) + "\nAdverseWeatherCondition_ExtremeWeatherConditionSubCause: " + str(self.AdverseWeatherCondition_ExtremeWeatherConditionSubCause) + "\nAdverseWeatherCondition_AdhesionSubCause: " + str(self.AdverseWeatherCondition_AdhesionSubCause) + "\nAdverseWeatherCondition_VisibilitySubCause: " + str(self.AdverseWeatherCondition_VisibilitySubCause) + "\nAdverseWeatherCondition_PrecipitationSubCause: " + str(self.AdverseWeatherCondition_PrecipitationSubCause) + "\nSlowVehicleSubCause: " + str(self.SlowVehicleSubCause) + "\nStationaryVehicleSubCause: " + str(self.StationaryVehicleSubCause) + "\nHumanProblemSubCause: " + str(self.HumanProblemSubCause) + "\nEmergencyVehicleApproachingSubCause: " + str(self.EmergencyVehicleApproachingSubCause) + "\nHazardousLocation_DangerousCurveSubCause: " + str(self.HazardousLocation_DangerousCurveSubCause) + "\nHazardousLocation_SurfaceConditionSubCause: " + str(self.HazardousLocation_SurfaceConditionSubCause) + "\nHazardousLocation_ObstacleOnTheRoadSubCause: " + str(self.HazardousLocation_ObstacleOnTheRoadSubCause) + "\nHazardousLocation_AnimalOnTheRoadSubCause: " + str(self.HazardousLocation_AnimalOnTheRoadSubCause) + "\nCollisionRiskSubCause: "