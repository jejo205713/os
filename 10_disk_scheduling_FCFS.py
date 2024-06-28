def fcfs(start, requests):
    total_movement = 0
    current_track = start
    
    for track in requests:
        total_movement += abs(track - current_track)
        current_track = track
    
    return total_movement

# Example usage
if __name__ == "__main__":
    start = 53
    requests = [98, 183, 37, 122, 14, 124, 65, 67]
    
    total_movement = fcfs(start, requests)
    print(f"Total head movement using FCFS: {total_movement}")
