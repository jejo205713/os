def priority_scheduling(processes):
    time = 0
    processes.sort(key=lambda x: x[1])  # Sort by priority (lower number = higher priority)
    while processes:
        pid, priority, burst_time = processes.pop(0)
        print(f"Time {time}: Process {pid} with priority {priority} running for {burst_time} units")
        time += burst_time
        print(f"Time {time}: Process {pid} completed")

processes = [("P1", 2, 10), ("P2", 1, 4), ("P3", 3, 6)]
priority_scheduling(processes)
