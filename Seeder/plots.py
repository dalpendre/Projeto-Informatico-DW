import time
import matplotlib.pyplot as plt

import roadEvent
from roadEvent import RoadEvent

number_rows_to_insert = [10, 100, 1000, 10000, 100000]
road_event_insertion_times = []

for rows in number_rows_to_insert:
    start_time = time.time()
    for i in range(rows):
        roadEvent.main()
    end_time = time.time()
    execution_time = end_time - start_time
    road_event_insertion_times.append(execution_time)
    print("Time to insert " + str(rows) + " rows: " + str(execution_time) + " seconds")

# Plotting
plt.plot(number_rows_to_insert, road_event_insertion_times)
plt.xlabel('Number of Rows to Insert')
plt.ylabel('Time Taken (seconds)')
plt.title('Execution Time vs Number Of Rows Inserted')
plt.show()