print("Creating CAM data")
from cam import Cam
print(Cam)

num_records_to_insert = int(input("Insira o número de registos desejadas para as tabelas de sistema fonte: "))

for i in range(num_records_to_insert):
    print("Creating data - iteration " + str(i+1))

    print("Creating road event data")
    from roadEvent import RoadEvent
    print(RoadEvent)
    print("Creating Event data")
    from event import Event
    print(Event)
    print("Creating Time data")
    from timeClass import Time
    print(Time)
    print("Creating Denm data")
    from denm import Denm
    print(Denm)
    print("Creating Road data")
    from road import Road
    print(Road)
    print("Creating Segment data")
    from segment import Segment
    print(Segment)
    print("Creating Zone data")
    from zone import Zone
    print(Zone)
    print("Creating Road Sign data")
    from roadSign import RoadSign
    print(RoadSign)
    print("Creating IVIM data")
    from ivim import Ivim
    print(Ivim)

    print("\n")