import os

# Fork a child process
pid = os.fork()

if pid > 0:
    # This is the parent process
    print(f"Parent Process: PID = {os.getpid()}")
    os.wait()  # Wait for the child process to finish
elif pid == 0:
    # This is the child process
    print(f"Child Process: PID = {os.getpid()}")
    os._exit(0)  # Exit the child process
else:
    # Fork failed
    print("Fork failed")
