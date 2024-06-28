import os

def list_directory_contents(directory_path):
    # Try to open the directory
    try:
        dir_entry = os.scandir(directory_path)
    except FileNotFoundError:
        print(f"Directory '{directory_path}' not found.")
        return

    # If the directory was opened successfully, read its contents
    print(f"Contents of the directory '{directory_path}':")
    for entry in dir_entry:
        print(entry.name)

    # Close the directory
    dir_entry.close()
    print(f"Directory '{directory_path}' closed.")

if __name__ == "__main__":
    directory_path = input("Enter the directory path: ")
    list_directory_contents(directory_path)
