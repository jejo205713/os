import os

def dir_search(dp):
    # Try to open the directory
    try:
        dir_entry = os.scandir(dp)
    except FileNotFoundError:
        print(f"Directory '{dp}' not found.")
        return

    # If the directory was opened successfully, read its contents
    print(f"Contents of the directory '{dp}':")
    for entry in dir_entry:
        print(entry.name)

    # Close the directory
    dir_entry.close()
    print(f"Directory '{dp}' closed.")

if __name__ == "__main__":
    dp = input("Enter the directory path: ")
    dir_search(dp)
