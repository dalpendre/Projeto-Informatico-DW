import time
import matplotlib.pyplot as plt

import road
import roadEvent
import segment
import timeClass

#segment

number_rows_to_insert = [5, 10, 25, 50, 100, 150, 200, 250, 500, 1000, 5000, 10000]
road_event_insertion_times = []

for rows in number_rows_to_insert:
    start_time = time.time()
    for i in range(rows):
        segment.main()
    end_time = time.time()
    execution_time = end_time - start_time
    road_event_insertion_times.append(execution_time)
    print("Time to insert " + str(rows) + " rows: " + str(execution_time) + " seconds")

# Plotting
plt.plot(number_rows_to_insert, road_event_insertion_times, marker='o', linestyle='-')
plt.xlabel('Number of Rows to Insert')
plt.ylabel('Time Taken (seconds)')
plt.title('Execution Time vs Number Of Rows Inserted')
plt.savefig('segment.png')  # Save the plot as an image file
plt.show()

#road

number_rows_to_insert = [5, 10, 25, 50, 100, 150, 200, 250, 500, 1000, 5000, 10000]
road_event_insertion_times = []

for rows in number_rows_to_insert:
    start_time = time.time()
    for i in range(rows):
        road.main()
    end_time = time.time()
    execution_time = end_time - start_time
    road_event_insertion_times.append(execution_time)
    print("Time to insert " + str(rows) + " rows: " + str(execution_time) + " seconds")

# Plotting
plt.plot(number_rows_to_insert, road_event_insertion_times, marker='o', linestyle='-')
plt.xlabel('Number of Rows to Insert')
plt.ylabel('Time Taken (seconds)')
plt.title('Execution Time vs Number Of Rows Inserted')
plt.savefig('road.png')  # Save the plot as an image file
plt.show()

#road event

number_rows_to_insert = [5, 10, 25, 50, 100, 150, 200, 250, 500, 1000, 5000, 10000]
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
plt.plot(number_rows_to_insert, road_event_insertion_times, marker='o', linestyle='-')
plt.xlabel('Number of Rows to Insert')
plt.ylabel('Time Taken (seconds)')
plt.title('Execution Time vs Number Of Rows Inserted')
plt.savefig('road_event.png')  # Save the plot as an image file
plt.show()

#time

number_rows_to_insert = [5, 10, 25, 50, 100, 150, 200, 250, 500, 1000, 5000, 10000]
road_event_insertion_times = []

for rows in number_rows_to_insert:
    start_time = time.time()
    for i in range(rows):
        timeClass.main()
    end_time = time.time()
    execution_time = end_time - start_time
    road_event_insertion_times.append(execution_time)
    print("Time to insert " + str(rows) + " rows: " + str(execution_time) + " seconds")

# Plotting
plt.plot(number_rows_to_insert, road_event_insertion_times, marker='o', linestyle='-')
plt.xlabel('Number of Rows to Insert')
plt.ylabel('Time Taken (seconds)')
plt.title('Execution Time vs Number Of Rows Inserted')
plt.savefig('time.png')  # Save the plot as an image file
plt.show()