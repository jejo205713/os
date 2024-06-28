def sjf_scheduling(processes):
    time = 0
    processes.sort(key=lambda x: x[1])  # Sort by burst time
    for pid, burst_time in processes:
        print(f"Time {time}: Process {pid} running for {burst_time} units")
        time += burst_time
        print(f"Time {time}: Process {pid} completed")

processes = [("P1", 10), ("P2", 4), ("P3", 6)]
sjf_scheduling(processes)
