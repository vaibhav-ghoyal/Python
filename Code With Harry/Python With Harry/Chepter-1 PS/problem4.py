import os

def print_directory_contents(path):
    try:
        # list all entries (files + directories) in path
        entries = os.listdir(path)
        print(f"Contents of directory '{path}':")
        for entry in entries:
            print(entry)
    except FileNotFoundError:
        print(f"Error: The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied for accessing '{path}'.")

if __name__ == "__main__":
    # you can change this to any directory you want
    dir_path = "C:/Users/Admin/Desktop/Python/Book"   # current directory
    print_directory_contents(dir_path)
