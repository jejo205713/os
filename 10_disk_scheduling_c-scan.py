def c_scan(start, requests, max_track):
    total_movement = 0
    current_track = start
    
    # Sort requests to simplify scan
    requests.sort()
    
    # Find the position of start in requests
    index = requests.index(start)
    
    # Forward scan from start to max_track
    for track in requests[index:]:
        total_movement += abs(track - current_track)
        current_track = track
    
    # Handle the end case (move to the end of the disk)
    total_movement += abs(max_track - current_track)
    current_track = max_track
    
    # Wrap around to the beginning of the disk (move to track 0)
    total_movement += current_track
    
    # Forward scan from 0 to the original start
    for track in requests[:index]:
        total_movement += abs(track - current_track)
        current_track = track
    
    return total_movement

# Example usage
if __name__ == "__main__":
    start = 53
    requests = [98, 183, 37, 122, 14, 124, 65, 67]
    max_track = 199
    
    total_movement = c_scan(start, requests, max_track)
    print(f"Total head movement using C-SCAN: {total_movement}")
