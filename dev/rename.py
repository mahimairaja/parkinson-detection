import os

# Get current directory
curr_dir = os.getcwd()

# List of new names
healthy_names = [f"healthy_{i}.png" for i in range(1, 52)]
parkinson_names = [f"parkinson_{i}.png" for i in range(1, 52)]

# Rename files in a directory
def rename(name, name_list):
    """
    To rename files in a directory using a list of new names.
    """
    # Walk through the directory
    for root, dirs, files in os.walk(os.path.join(curr_dir, f'dataset/{name}')):
        for idx, file in enumerate(files):
            file_path = os.path.join(root, file) # Get file path
            new_name = name_list[idx]
            new_file_path = os.path.join(root, new_name)
            os.rename(file_path, new_file_path) # Rename file
            print("Renamed file:", file, "->", new_name)

if __name__ == "__main__":
    # Rename files
    rename("healthy", healthy_names)
    rename("parkinson", parkinson_names)