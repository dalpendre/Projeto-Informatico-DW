from colors import bcolors
import os
import extract
import transform
import load

def delete_files_starting_with(num_lines):
    files = os.listdir()

    # Delete files starting with num_lines characters
    for file in files:
        if file.startswith(num_lines):
            os.remove(file)

# Example usage
delete_files_starting_with("num_lines")