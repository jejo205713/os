def fcfs_scheduling(processes):
    time = 0
    for pid, burst_time in processes:
        print(f"Time {time}: Process {pid} running for {burst_time} units")
        time += burst_time
        print(f"Time {time}: Process {pid} completed")

processes = [("P1", 10), ("P2", 4), ("P3", 6)]
fcfs_scheduling(processes)
