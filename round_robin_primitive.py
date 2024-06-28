def round_robin(processes, quantum):
    time = 0
    queue = processes[:]
    while queue:
        process = queue.pop(0)
        pid, burst_time = process
        if burst_time > quantum:
            print(f"Time {time}: Process {pid} running for {quantum} units")
            time += quantum
            queue.append((pid, burst_time - quantum))
        else:
            print(f"Time {time}: Process {pid} running for {burst_time} units")
            time += burst_time
            print(f"Time {time}: Process {pid} completed")

processes = [("P1", 10), ("P2", 4), ("P3", 6)]
quantum = 3
round_robin(processes, quantum)
