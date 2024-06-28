import numpy as np

def is_safe_state(available, max_claim, allocated):
    num_processes, num_resources = allocated.shape

    # Calculate need matrix
    need = max_claim - allocated

    # Initialize finish array
    finish = np.zeros(num_processes, dtype=bool)

    # Available resources at the beginning
    work = available.copy()

    # Check if a process can run safely
    while True:
        found = False
        for i in range(num_processes):
            if not finish[i] and np.all(need[i] <= work):
                work += allocated[i]
                finish[i] = True
                found = True
                break

        if not found:
            break

    return np.all(finish)

# Example usage
if __name__ == "__main__":
    # Example data
    available = np.array([3, 3, 2])
    max_claim = np.array([
        [7, 5, 3],
        [3, 2, 2],
        [9, 0, 2],
        [2, 2, 2],
        [4, 3, 3]
    ])
    allocated = np.array([
        [0, 1, 0],
        [2, 0, 0],
        [3, 0, 2],
        [2, 1, 1],
        [0, 0, 2]
    ])

    if is_safe_state(available, max_claim, allocated):
        print("The system is in a safe state.")
    else:
        print("The system is in an unsafe state.")
