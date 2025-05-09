# Importing the necessary libraries
import os
import shutil

# Asking for and scanning the selected path
path = input("Enter Path: ")

# Validating the path
if not os.path.isdir(path):
    print("Invalid directory. Please provide a valid path.")
    exit()

files = os.listdir(path)

# Checking the extension and organizing files
for file in files:
    file_path = os.path.join(path, file)
    
    # Skip directories
    if os.path.isdir(file_path):
        continue

    filename, extension = os.path.splitext(file)
    extension = extension[1:]  # Remove the dot from the extension

    # Handle files without an extension
    if not extension:
        extension = "No_Extension"

    destination_dir = os.path.join(path, extension)

    # Creating new directories if they don't exist
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Moving the file
    try:
        shutil.move(file_path, os.path.join(destination_dir, file))
    except Exception as e:
        print(f"Could not move file {file}: {e}")

print("Files organized successfully!")
